#!/usr/bin/env python3
"""Generate the wiki's two sequence pages from one curated data file.

    config/castle-sequences.tsv           one row per sequence: a castle count, with or
                                          without an OEIS entry, or an OEIS entry the wiki cites
    config/castle-sequence-families.tsv   the catalog's sections: title, label, page, intro, note

The two pages are views of the same rows, so neither is ever hand-edited:

    wiki/pages/castle-sequence-catalog.md   the rows with a family, by family
    wiki/pages/oeis-index.md                  the rows with an A-number, by A-number, with the
                                              pages that cite each one

Run it after any edit to the data files or any page edit that adds or removes an A-number:

    python3 bin/generate-sequence-pages.py                 rewrite the pages whose body changed
    python3 bin/generate-sequence-pages.py --check         exit 1 if a committed page is stale
    python3 bin/generate-sequence-pages.py --fetch-names   fill empty oeis_name cells from oeis.org

Row columns (tab-separated; a cell never holds a tab or a newline):

    id          unique key
    family      a family id from the families file; empty for an OEIS entry that is not a
                castle count of its own (it then appears in the index only)
    page        the wiki page that proves or discusses the row (slug), optional
    counts      what the row counts, in markdown
    axis        the grading variable and its first value, e.g. `w = 1…`, optional
    terms       first terms, in markdown
    formula     generating function, recurrence or closed form
    growth      growth constant
    anum        the OEIS entry the row equals, or empty
    anum_index  where the row sits in that entry: an index such as `w − 2`, read as A(w − 2), or
                an expression in a(…), such as `a(w + 1) − 1`
    note        the rest of the OEIS cell, in markdown
    oeis_name   the entry's OEIS name, stored; --fetch-names fills empty cells
    group       count, metallic, plastic or supporting: the index section of the entry
    status      `proved` when `page` proves the identity, else empty

Family columns: id, title, label (a short noun phrase that prefixes the rows' descriptions in the
index), page, intro, note. In intro and note, `\\n` starts a new paragraph. An A-number cited on a
page but without a row is listed in the index under "Not yet annotated". Stdlib only.
"""
import json
import re
import sys
import time
import urllib.request
from datetime import date
from pathlib import Path

WIKI_ROOT = Path(__file__).resolve().parent.parent
PAGES_DIR = WIKI_ROOT / "wiki" / "pages"
ROWS_FILE = WIKI_ROOT / "config" / "castle-sequences.tsv"
FAMILIES_FILE = WIKI_ROOT / "config" / "castle-sequence-families.tsv"
INDEX_SLUG = "oeis-index"
CATALOG_SLUG = "castle-sequence-catalog"
GENERATED = {INDEX_SLUG, CATALOG_SLUG}
SCRIPT = "bin/generate-sequence-pages.py"

ROW_COLS = ["id", "family", "page", "counts", "axis", "terms", "formula", "growth", "anum",
            "anum_index", "note", "oeis_name", "group", "status"]
FAMILY_COLS = ["id", "title", "label", "page", "intro", "note"]
ANUM_RE = re.compile(r"\bA\d{6}\b")
GROUPS = [
    ("count", "Castle count interpretations",
     "Sequences whose terms count castles, towers, strips or skylines on the wiki, at "
     "the offset stated in each row."),
    ("metallic", "Continued fractions and the metallic ladder",
     "The [[metallic-means](pages/metallic-means.md)] `δ_a` family, its companion and "
     "trace sequences, and the OEIS convergent tables for `√(a²+4)`."),
    ("plastic", "Plastic-number neighborhood",
     "The sequences behind [[plastic-number](pages/plastic-number.md)] ψ."),
    ("supporting", "Supporting sequences",
     "Cross-references, ambient polyomino and tournament counts, and OEIS entries that "
     "appear as neighbors or components of a castle result."),
]
GROUP_KEYS = [g[0] for g in GROUPS]


# ---------------------------------------------------------------- reading and validation

def read_tsv(path, cols):
    lines = path.read_text(encoding="utf-8").splitlines()
    if lines[0].split("\t") != cols:
        sys.exit(f"{path.name}: the header must be {' '.join(cols)}")
    out = []
    for n, line in enumerate(lines[1:], start=2):
        if not line.strip():
            continue
        cells = line.split("\t")
        if len(cells) != len(cols):
            sys.exit(f"{path.name}:{n}: {len(cells)} cells, expected {len(cols)}")
        out.append({c: v.strip() for c, v in zip(cols, cells)})
    return out


def write_rows(rows):
    out = ["\t".join(ROW_COLS)]
    out += ["\t".join(r[c] for c in ROW_COLS) for r in rows]
    ROWS_FILE.write_text("\n".join(out) + "\n", encoding="utf-8")


def load():
    families = read_tsv(FAMILIES_FILE, FAMILY_COLS)
    rows = read_tsv(ROWS_FILE, ROW_COLS)
    fam_ids = {f["id"] for f in families}
    seen, entry = set(), {}
    for r in rows:
        where = f"{ROWS_FILE.name}: row {r['id']!r}"
        if not r["id"] or r["id"] in seen:
            sys.exit(f"{where}: missing or duplicate id")
        seen.add(r["id"])
        if r["family"] and r["family"] not in fam_ids:
            sys.exit(f"{where}: unknown family {r['family']!r}")
        if not r["family"] and not r["anum"]:
            sys.exit(f"{where}: a row needs a family, an A-number, or both")
        if r["anum"]:
            if not re.fullmatch(r"A\d{6}", r["anum"]):
                sys.exit(f"{where}: bad A-number {r['anum']!r}")
            if r["group"] not in GROUP_KEYS:
                sys.exit(f"{where}: group must be one of {', '.join(GROUP_KEYS)}")
            e = entry.setdefault(r["anum"], {"group": r["group"], "name": r["oeis_name"]})
            if e["group"] != r["group"]:
                sys.exit(f"{where}: {r['anum']} is in group {e['group']!r} on another row")
            if r["oeis_name"] and e["name"] and r["oeis_name"] != e["name"]:
                sys.exit(f"{where}: {r['anum']} has a different oeis_name on another row")
            e["name"] = e["name"] or r["oeis_name"]
        elif r["anum_index"] or r["group"] or r["oeis_name"]:
            sys.exit(f"{where}: anum_index, group and oeis_name need an A-number")
        if r["status"] not in ("", "proved"):
            sys.exit(f"{where}: status must be empty or 'proved'")
        if r["status"] == "proved" and not r["page"]:
            sys.exit(f"{where}: a proved row names the page that proves it")
        if r["page"] and not (PAGES_DIR / f"{r['page']}.md").exists():
            sys.exit(f"{where}: no page {r['page']!r}")
    for f in families:
        if f["page"] and not (PAGES_DIR / f"{f['page']}.md").exists():
            sys.exit(f"{FAMILIES_FILE.name}: family {f['id']!r}: no page {f['page']!r}")
    return families, rows, entry


def split_doc(text):
    """Return (frontmatter_lines, body); body is everything after the closing `---`."""
    if not text.startswith("---"):
        return None, text
    lines = text.splitlines()
    end = next((i for i in range(1, len(lines)) if lines[i].strip() == "---"), None)
    if end is None:
        return None, text
    return lines[1:end], "\n".join(lines[end + 1:])


def scan_pages():
    """Return {anum: {slug: count}} over the page bodies, the generated pages excluded."""
    cites = {}
    for path in sorted(PAGES_DIR.glob("*.md")):
        if path.name.startswith("audit-") or path.stem in GENERATED:
            continue
        _, body = split_doc(path.read_text(encoding="utf-8"))
        for anum in ANUM_RE.findall(body):
            cites.setdefault(anum, {}).setdefault(path.stem, 0)
            cites[anum][path.stem] += 1
    return cites


def fetch_name(anum):
    url = f"https://oeis.org/search?q=id:{anum}&fmt=json"
    req = urllib.request.Request(url, headers={"User-Agent": "castles-wiki/generate-sequence-pages"})
    with urllib.request.urlopen(req, timeout=20) as resp:
        data = json.loads(resp.read().decode("utf-8"))
    time.sleep(1.5)  # be polite: oeis.org returns 403 on rapid-fire requests
    results = data if isinstance(data, list) else data.get("results") or []
    for e in results:
        if e.get("number") == int(anum[1:]):
            return e.get("name", "").strip()
    return ""


# ---------------------------------------------------------------- rendering helpers

def cell(text):
    """Escape a table cell: a bare pipe would split the row."""
    return text.replace("|", "\\|")


def link(slug):
    return f"[[{slug}](pages/{slug}.md)]"


def alink(anum):
    return f"[{anum}](https://oeis.org/{anum})"


def paragraphs(text):
    return [p.strip() for p in text.split("\\n") if p.strip()]


def relation(r):
    """The row's place in its entry, as an expression: A094706(w−2), or A038503(w + 1) − 1."""
    idx = r["anum_index"]
    if not idx:
        return ""
    if "a(" in idx:
        return re.sub(r"\ba\(", f"{r['anum']}(", idx)
    return f"{r['anum']}({idx})"


def oeis_cell(r):
    note = r["note"]
    if not r["anum"]:
        return "-" + (" " + note if note else "")
    out = alink(r["anum"])
    rel = relation(r)
    if rel:
        if note.startswith("(`= "):
            return f"{out} (`= {rel} {note[2:]}"
        if note.startswith("("):
            return f"{out} (`= {rel}`; {note[1:]}"
        out += f" (`= {rel}`)"
    if note:
        out += note if note[0] in ",;" else " " + note
    return out


def role(r, label):
    """One line for the index: the family label, what the row counts, and its relation."""
    text = r["counts"]
    if label and label.lower() not in text.lower():
        text = f"{label}, {text}"
    rel = relation(r)
    return f"{text}: `{rel}`" if rel else text


# ---------------------------------------------------------------- the catalog

def render_catalog(families, rows):
    by_family = {f["id"]: [r for r in rows if r["family"] == f["id"]] for f in families}
    labels = {f["id"]: f["label"] for f in families}
    n_rows = sum(len(v) for v in by_family.values())
    out = ["", f"<!-- Generated by {SCRIPT} from config/castle-sequences.tsv and "
               "config/castle-sequence-families.tsv. Do not edit by hand: edit the data files "
               "and rerun the script. -->", ""]
    out += ["# Castle sequence catalog", "", "## What this is", ""]
    out.append("This page catalogs the sequences that castles produce, organized by the castle "
               "object each one counts rather than by OEIS A-number. Each row gives first terms, a "
               "recurrence or generating function (g.f.), its growth constant, and the entry of the "
               "On-Line Encyclopedia of Integer Sequences (OEIS) it equals, at the stated offset; "
               "\"-\" means no entry is listed.[^1]")
    out.append("")
    out.append(f"This page and {link(INDEX_SLUG)} are generated by `{SCRIPT}` from one data file, "
               "`config/castle-sequences.tsv`: this page shows its rows by family, and the index "
               "shows its A-numbers with the pages that cite them. "
               f"{link('oeis-cross-referencing')} describes the checks a match must pass, "
               f"{link('oeis-mining-pe502')} collects the castle counts matched to OEIS entries, and "
               f"{link('oeis-height2-hyperbolic-castles')} proves the height-2 rows.")
    out.append("")
    out.append(f"The symbols are those of {link('castle-notation')}: `A^e(w, h)` and `A^o(w, h)` "
               "count the castles of width `w` and height `h` with an even and an odd number of "
               "blocks. A skyline on `{1, …, h}` need not reach height `h`, so a count of skylines "
               "on `{1, …, h}` is a count of castles of every height up to `h`.")
    out += ["", "## OEIS entries proved on other pages", ""]
    out.append("These identities are stated and proved on the pages cited; the section *Catalog* "
               "gives the terms of most of them.")
    out.append("")
    proved = {}
    for r in rows:
        if r["status"] == "proved" and r["anum"]:
            proved.setdefault(r["page"], []).append(r)
    for page, rs in proved.items():
        items = [f"{alink(r['anum'])}, {role(r, labels.get(r['family'], ''))}" for r in rs]
        out.append(f"- {link(page)}: " + "; ".join(items) + ".")
    out += ["", "## Catalog"]
    for f in families:
        rs = by_family[f["id"]]
        if not rs:
            continue
        out += ["", f"### {f['title']}", ""]
        for p in paragraphs(f["intro"]):
            out += [p, ""]
        cols = [("object", "counts"), ("from", "axis"), ("first terms", "terms"),
                ("g.f. / formula", "formula"), ("growth", "growth")]
        cols = [(h, k) for h, k in cols if k == "counts" or any(r[k] for r in rs)]
        out.append("| " + " | ".join(h for h, _ in cols) + " | OEIS |")
        out.append("|" + "---|" * (len(cols) + 1))
        for r in rs:
            out.append("| " + " | ".join(cell(r[k]) for _, k in cols) + f" | {cell(oeis_cell(r))} |")
        for p in paragraphs(f["note"]):
            out += ["", p]
    out += ["", "## Related Concepts", ""]
    out += [
        f"- {link(INDEX_SLUG)} - the same data by A-number, with the pages that cite each entry.",
        f"- {link('oeis-cross-referencing')} - the checks a match must pass: the offset, and agreement beyond a short prefix.",
        f"- {link('oeis-height2-hyperbolic-castles')} - the height-2 rows `A038505` and `A038503`.",
        f"- {link('hyperbolic-sequence-family')} - the four sums of every fourth binomial coefficient, `A038503`, `A038504`, `A038505`, `A000749`.",
        f"- {link('metallic-means')} / {link('pell-numbers')} / {link('plastic-number')} - the metallic means, the Pell numbers and the plastic number, the growth constants of several rows.",
        f"- {link('castle-graph')} - the tree castles and tree skylines by width (`A001045`, `A006130`, `A006131`).",
        f"- {link('castle-eigenvalue-oeis-crosswalk')} - the convergents of castle eigenvalues against the OEIS, `|P(k, 4)| = A352116(k+1)`, and the Jacobi-Perron expansion of `2ψ²`.",
        f"- {link('hardin-word-identity')} - the Hardin sequences `A202882`, `A203094`, `A203184` and the proof of their recurrences.",
        f"- {link('new-sequence-fw3')} - the row `A^e(·, 3)`.",
        f"- {link('castles-of-height-h-by-area')} - castles by area with bounded height and the n-nacci numbers.",
        f"- {link('tower-spacing-castles')} - the tower-spacing skylines and Hardin's running-minimum arrays.",
        f"- {link('proper-castle-projection')} - the even-block ridge castles.",
        f"- {link('reachable-field-census')} - the strip Perron roots and the fields they reach.",
        f"- {link('odd-castles-and-block-tables')} - the odd-block rows, the parity splits by area, and the tables by blocks and peaks.",
        f"- {link('a005251-bijection')} - the bijection between the readings of `A005251`.",
        f"- {link('oeis-mining-seminar')} - a seminar that takes one row through the method.",
        f"- {link('motzkin-castles')} - the Motzkin rows: cornerless Motzkin paths, the parity split of `M_{{w−1}}`, the Motzkin paths of bounded height, and the rows by semi-perimeter.",
        f"- {link('zig-zag-castles')} - the zig-zag strips and castles, the zig-zag paths of the OEIS and the balanced strings.",
        f"- {link('oeis-mining-pe502')} - the castle counts matched to OEIS entries, among them the difference-of-powers, height-2, signed tower, convex and area rows.",
    ]
    out += ["", "## Footnotes", ""]
    out.append("[^1]: Verified by execution (Python 3.11 with SymPy, 2026-10-16 and 2026-10-22; Python 3.10, "
               "2026-10-27, for the rows checked by `bin/python/zig_zag_castles.py` and "
               "`bin/python/sequence_catalog_rows.py`, run logs beside them): every row with "
               "listed terms recomputed by enumeration, transfer matrix or dynamic program at the "
               "ranges stated under each table; every cited A-number fetched from oeis.org and "
               "compared with the computed terms at the stated offset.")
    return "\n".join(out) + "\n", n_rows


def catalog_frontmatter(n_rows, n_fam, updated):
    return "\n".join([
        "---",
        "title: Castle sequence catalog",
        "category: Reference",
        f"summary: Script-generated catalog of the castle-counting sequences on the wiki "
        f"({n_rows} rows in {n_fam} families), by the object each one counts: first terms, "
        "recurrence or generating function, growth constant, and the OEIS entry it equals at the "
        "stated offset, or none. Built with oeis-index from one data file, "
        "config/castle-sequences.tsv, by bin/generate-sequence-pages.py.",
        "tags: [reference, oeis, castle, sequence, catalog, generated]",
        "sources: [oeis-encyclopedia]",
        "created: 2026-09-17",
        f"updated: {updated}",
        "---",
    ]) + "\n"


# ---------------------------------------------------------------- the index

def pages_cell(counts):
    if not counts:
        return "-"
    ordered = sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))
    return ", ".join(f"{link(slug)} ({n})" for slug, n in ordered)


def render_index(families, rows, entry, cites):
    labels = {f["id"]: f["label"] for f in families}
    anums = sorted(set(entry) | set(cites))
    n_pages = len({slug for counts in cites.values() for slug in counts})
    by_group = {k: [] for k in GROUP_KEYS}
    unannotated = []
    for a in anums:
        (by_group[entry[a]["group"]] if a in entry else unannotated).append(a)
    roles = {}
    for r in rows:
        if r["anum"]:
            roles.setdefault(r["anum"], []).append(role(r, labels.get(r["family"], "")))

    out = ["", f"<!-- Generated by {SCRIPT} from config/castle-sequences.tsv and the wiki pages. "
               "Do not edit by hand: edit the data file or the citing page and rerun the script. -->", ""]
    out += ["# Online Encyclopedia of Integer Sequences (OEIS) index", ""]
    out.append(f"Every OEIS A-number cited on this wiki or listed in its sequence data ({len(anums)} "
               f"sequences, cited on {n_pages} pages) and where it appears. Use it to find where an "
               "A-number is discussed. A-numbers link to OEIS. \"Pages\" lists the wiki pages that "
               "mention the number, most mentions first, with the mention count in parentheses; the "
               "primary discussion is generally the page with the highest count.")
    out.append("")
    out.append(f"This page and {link(CATALOG_SLUG)} are generated by `{SCRIPT}` from one data file, "
               "`config/castle-sequences.tsv`. The castle role of each entry is built from the rows "
               "that name it; the catalog shows the same rows by family, with their terms. The "
               f"method for identifying and verifying an OEIS match is on {link('oeis-cross-referencing')}.")
    out += ["", "## Counts by role", ""]
    for key, title, blurb in GROUPS:
        out.append(f"- **{title}** ({len(by_group[key])}) - {blurb}")
    if unannotated:
        out.append(f"- **Not yet annotated** ({len(unannotated)}) - cited on the wiki but without a "
                   "row in `config/castle-sequences.tsv`.")
    out += ["", "## Directory"]
    for key, title, _ in GROUPS:
        if not by_group[key]:
            continue
        out += ["", f"### {title}", "", "| A-number | Name | Castle role | Pages |", "|---|---|---|---|"]
        for a in by_group[key]:
            out.append(f"| {alink(a)} | {cell(entry[a]['name'])} | {cell('; '.join(roles[a]))} | "
                       f"{pages_cell(cites.get(a, {}))} |")
    if unannotated:
        out += ["", "### Not yet annotated", "",
                "Add a row to `config/castle-sequences.tsv` (the A-number, its group and what it "
                "counts) to move an entry into its group above.", "", "| A-number | Pages |", "|---|---|"]
        for a in unannotated:
            out.append(f"| {alink(a)} | {pages_cell(cites[a])} |")
    out += ["", "## Related Concepts", ""]
    out += [
        f"- {link(CATALOG_SLUG)} - the same data by family: every castle-counting sequence with its terms and OEIS entry.",
        f"- {link('oeis-cross-referencing')} - the method: check a match against OEIS data at the stated offset, and do not count a short prefix as a match.",
        f"- {link('oeis-mining-pe502')} - the castle counts matched to OEIS entries, with their offsets.",
        f"- {link('oeis-encyclopedia')} - the encyclopedia itself: A-numbers, data lines and offsets.",
    ]
    return "\n".join(out) + "\n", len(anums)


def index_frontmatter(n_seq, updated):
    return "\n".join([
        "---",
        "title: OEIS index",
        "category: Reference",
        f"summary: Script-generated directory of every OEIS A-number cited on the wiki or listed in "
        f"its sequence data ({n_seq} sequences), grouped by role, with the castle role built from "
        "the data rows and the citing pages with mention counts. Built with "
        "castle-sequence-catalog from one data file, config/castle-sequences.tsv, by "
        "bin/generate-sequence-pages.py.",
        "tags: [reference, oeis, index, directory, cross-reference, generated]",
        "sources: [oeis-encyclopedia]",
        "created: 2026-09-17",
        f"updated: {updated}",
        "---",
    ]) + "\n"


# ---------------------------------------------------------------- main

def emit(slug, body, frontmatter_fn, check):
    """Write the page if its body changed; in check mode, report staleness instead."""
    path = PAGES_DIR / f"{slug}.md"
    old_fm, old_body = (None, "")
    if path.exists():
        old_fm, old_body = split_doc(path.read_text(encoding="utf-8"))
    unchanged = old_body.rstrip("\n") == body.rstrip("\n")
    if check:
        return unchanged
    updated = date.today().isoformat()
    if unchanged and old_fm:
        for line in old_fm:
            if line.startswith("updated:"):
                updated = line.split(":", 1)[1].strip()
    path.write_text(frontmatter_fn(updated) + body, encoding="utf-8")
    print(f"wrote {path.relative_to(WIKI_ROOT)}" + ("" if unchanged else ", body changed"))
    return True


def main(argv):
    check = "--check" in argv
    families, rows, entry = load()
    if "--fetch-names" in argv:
        for a in sorted(entry):
            if entry[a]["name"]:
                continue
            try:
                entry[a]["name"] = fetch_name(a)
                print(f"fetched {a}: {entry[a]['name'][:70]}")
            except Exception as exc:  # network is best-effort here
                print(f"warning: could not fetch {a}: {exc}", file=sys.stderr)
        for r in rows:
            if r["anum"]:
                r["oeis_name"] = entry[r["anum"]]["name"]
        write_rows(rows)
    cites = scan_pages()
    for a in sorted(set(entry) - set(cites)):
        print(f"note: {a} is in the data but not cited on any page", file=sys.stderr)

    cat_body, n_rows = render_catalog(families, rows)
    idx_body, n_seq = render_index(families, rows, entry, cites)
    n_fam = len({r["family"] for r in rows if r["family"]})
    ok_cat = emit(CATALOG_SLUG, cat_body, lambda u: catalog_frontmatter(n_rows, n_fam, u), check)
    ok_idx = emit(INDEX_SLUG, idx_body, lambda u: index_frontmatter(n_seq, u), check)
    if check and not (ok_cat and ok_idx):
        stale = [s for s, ok in ((CATALOG_SLUG, ok_cat), (INDEX_SLUG, ok_idx)) if not ok]
        print(
            "\n"
            "COMMIT BLOCKED: a generated sequence page is out of date: " + ", ".join(stale) + ".\n"
            "\n"
            "  wiki/pages/castle-sequence-catalog.md and wiki/pages/oeis-index.md are built by script\n"
            "  from config/castle-sequences.tsv, config/castle-sequence-families.tsv and the A-numbers\n"
            "  cited on the wiki pages. Do not edit them by hand.\n"
            "\n"
            "  To fix, from the repo root, regenerate and re-stage:\n"
            "\n"
            f"      python3 {SCRIPT} && git add wiki/pages/castle-sequence-catalog.md wiki/pages/oeis-index.md\n"
            "\n"
            "  then run your git commit again. A new A-number with no row in config/castle-sequences.tsv\n"
            "  appears in the index under \"Not yet annotated\"; add a row to file it.\n",
            file=sys.stderr,
        )
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
