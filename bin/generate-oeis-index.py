#!/usr/bin/env python3
"""Generate wiki/pages/oeis-index.md — the directory of every OEIS A-number cited on the wiki.

The directory is a mechanical artifact: for each A-number it lists which pages cite it and
how often. That goes stale on every edit, so it is never hand-edited. Regenerate it after
any page edit that adds or removes an A-number:

    python3 bin/generate-oeis-index.py              rewrite the page if its body changed
    python3 bin/generate-oeis-index.py --check      exit 1 if the committed page is stale
    python3 bin/generate-oeis-index.py --fetch-names   fill empty `name` cells from oeis.org

The curated half — each A-number's role group, OEIS name, and one-line castle role — lives
in config/oeis-annotations.tsv (tab-separated: anum, group, name, role). An A-number cited
on the wiki but absent from that file is still listed, under "Not yet annotated", so a new
citation surfaces automatically; add a row to the TSV to move it into its group. The
hand-curated novelty catalogue is a separate page, castle-sequence-catalogue, and is not
touched here. Stdlib only.
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
ANNOTATIONS = WIKI_ROOT / "config" / "oeis-annotations.tsv"
SLUG = "oeis-index"
OUTPUT = PAGES_DIR / f"{SLUG}.md"
CREATED = "2026-09-17"

ANUM_RE = re.compile(r"\bA\d{6}\b")
GROUPS = [
    ("count", "Castle count interpretations",
     "Sequences the wiki claims as counts of a castle-native object. These are the "
     "interlinking targets: candidates for an OEIS comment or formula that reads the "
     "sequence as a castle count."),
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


def split_doc(text):
    """Return (frontmatter_lines, body) — body is everything after the closing `---`."""
    if not text.startswith("---"):
        return None, text
    lines = text.splitlines()
    end = next((i for i in range(1, len(lines)) if lines[i].strip() == "---"), None)
    if end is None:
        return None, text
    return lines[1:end], "\n".join(lines[end + 1:])


def read_annotations():
    rows = {}
    if not ANNOTATIONS.exists():
        return rows
    lines = ANNOTATIONS.read_text(encoding="utf-8").splitlines()
    for line in lines[1:]:
        if not line.strip():
            continue
        cells = line.split("\t")
        cells += [""] * (4 - len(cells))
        anum, group, name, role = (c.strip() for c in cells[:4])
        if group not in GROUP_KEYS:
            sys.exit(f"{ANNOTATIONS.name}: {anum} has unknown group {group!r} "
                     f"(expected one of {', '.join(GROUP_KEYS)})")
        rows[anum] = {"group": group, "name": name, "role": role}
    return rows


def write_annotations(rows):
    out = ["anum\tgroup\tname\trole"]
    for anum in sorted(rows):
        r = rows[anum]
        out.append(f"{anum}\t{r['group']}\t{r['name']}\t{r['role']}")
    ANNOTATIONS.write_text("\n".join(out) + "\n", encoding="utf-8")


def scan_pages():
    """Return {anum: {slug: count}} over page bodies, excluding the directory itself."""
    cites = {}
    for path in sorted(PAGES_DIR.glob("*.md")):
        if path.name.startswith("audit-") or path.stem == SLUG:
            continue
        _, body = split_doc(path.read_text(encoding="utf-8"))
        for anum in ANUM_RE.findall(body):
            cites.setdefault(anum, {}).setdefault(path.stem, 0)
            cites[anum][path.stem] += 1
    return cites


def fetch_name(anum):
    url = f"https://oeis.org/search?q=id:{anum}&fmt=json"
    req = urllib.request.Request(url, headers={"User-Agent": "castles-wiki/generate-oeis-index"})
    with urllib.request.urlopen(req, timeout=20) as resp:
        data = json.loads(resp.read().decode("utf-8"))
    time.sleep(1.5)  # be polite: oeis.org returns 403 on rapid-fire requests
    results = data if isinstance(data, list) else data.get("results") or []
    for entry in results:
        if entry.get("number") == int(anum[1:]):
            return entry.get("name", "").strip()
    return ""


def cell(text):
    """Escape a table cell: pipes would otherwise split the row."""
    return text.replace("|", "\\|")


def pages_cell(counts):
    ordered = sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))
    return ", ".join(f"[[{slug}](pages/{slug}.md)] ({n})" for slug, n in ordered)


def render_body(cites, ann):
    n_pages = len({slug for counts in cites.values() for slug in counts})
    by_group = {k: [] for k in GROUP_KEYS}
    unannotated = []
    for anum in sorted(cites):
        if anum in ann:
            by_group[ann[anum]["group"]].append(anum)
        else:
            unannotated.append(anum)

    out = []
    out.append("")
    out.append("<!-- Generated by bin/generate-oeis-index.py from config/oeis-annotations.tsv "
               "and the wiki pages. Do not edit by hand: edit the TSV or the citing page and "
               "rerun the script. -->")
    out.append("")
    out.append("# Online Encyclopedia of Integer Sequences (OEIS) index")
    out.append("")
    out.append(f"Every OEIS A-number cited on this wiki ({len(cites)} sequences across {n_pages} "
               "citing pages) and where it appears. Use it to find where an A-number is "
               "discussed, or to spot a sequence that has accumulated several wiki appearances, "
               "a signal that its cross-reference is worth submitting. A-numbers link to OEIS. "
               "\"Pages\" lists the wiki pages that mention the number, most mentions first, "
               "with the mention count in parentheses; the primary discussion is generally the "
               "page with the highest count.")
    out.append("")
    out.append("This page is the mechanical half of the wiki's sequence directory and is "
               "regenerated by script. The hand-curated half, the castle-native catalogue "
               "with a novelty status for every castle-counting sequence, is "
               "[[castle-sequence-catalogue](pages/castle-sequence-catalogue.md)]. The "
               "method for identifying and verifying an OEIS match is on "
               "[[oeis-cross-referencing](pages/oeis-cross-referencing.md)].")
    out.append("")
    out.append("## Counts by role")
    out.append("")
    for key, title, blurb in GROUPS:
        out.append(f"- **{title}** ({len(by_group[key])}) - {blurb}")
    if unannotated:
        out.append(f"- **Not yet annotated** ({len(unannotated)}) - cited on the wiki but "
                   "without a row in `config/oeis-annotations.tsv`.")
    out.append("")
    out.append("## Directory")
    for key, title, _ in GROUPS:
        anums = by_group[key]
        if not anums:
            continue
        out.append("")
        out.append(f"### {title}")
        out.append("")
        out.append("| A-number | Name | Castle role | Pages |")
        out.append("|---|---|---|---|")
        for anum in anums:
            a = ann[anum]
            out.append(f"| [{anum}](https://oeis.org/{anum}) | {cell(a['name'])} | "
                       f"{cell(a['role'])} | {pages_cell(cites[anum])} |")
    if unannotated:
        out.append("")
        out.append("### Not yet annotated")
        out.append("")
        out.append("Add a row to `config/oeis-annotations.tsv` (group, OEIS name, castle role) "
                   "to move an entry into its group above.")
        out.append("")
        out.append("| A-number | Pages |")
        out.append("|---|---|")
        for anum in unannotated:
            out.append(f"| [{anum}](https://oeis.org/{anum}) | {pages_cell(cites[anum])} |")
    out.append("")
    out.append("## Related Concepts")
    out.append("")
    out.append("- [[castle-sequence-catalogue](pages/castle-sequence-catalogue.md)] - the "
               "curated catalogue: every castle-counting sequence with its novelty status "
               "and the submission priority list.")
    out.append("- [[oeis-cross-referencing](pages/oeis-cross-referencing.md)] - the method: "
               "verify against OEIS data with offsets, distinguish interlinking from "
               "generation, honor the human-authorship rule.")
    out.append("- [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] - the source workspace "
               "where the first mining passes were carried out.")
    return "\n".join(out) + "\n"


def frontmatter(n_seq, updated):
    return "\n".join([
        "---",
        "title: OEIS index",
        "category: Reference",
        f"summary: Script-generated directory of every OEIS A-number cited on the wiki "
        f"({n_seq} sequences), grouped by role, with the citing pages and mention counts. "
        f"Regenerate with bin/generate-oeis-index.py; roles live in config/oeis-annotations.tsv.",
        "tags: [reference, oeis, index, directory, cross-reference, generated]",
        "sources: [oeis-mining-pe502]",
        f"created: {CREATED}",
        f"updated: {updated}",
        "---",
    ]) + "\n"


def main(argv):
    check = "--check" in argv
    fetch = "--fetch-names" in argv
    ann = read_annotations()
    cites = scan_pages()

    if fetch:
        for anum in sorted(cites):
            if anum in ann and not ann[anum]["name"]:
                try:
                    ann[anum]["name"] = fetch_name(anum)
                    print(f"fetched {anum}: {ann[anum]['name'][:70]}")
                except Exception as exc:  # network is best-effort here
                    print(f"warning: could not fetch {anum}: {exc}", file=sys.stderr)
        write_annotations(ann)

    for anum in sorted(set(ann) - set(cites)):
        print(f"note: {anum} is annotated but no longer cited on any page", file=sys.stderr)

    body = render_body(cites, ann)
    old_fm, old_body = (None, "")
    if OUTPUT.exists():
        old_fm, old_body = split_doc(OUTPUT.read_text(encoding="utf-8"))
    unchanged = old_body.rstrip("\n") == body.rstrip("\n")

    if check:
        if unchanged:
            return 0
        rel = OUTPUT.relative_to(WIKI_ROOT)
        print(
            "\n"
            "COMMIT BLOCKED: the generated OEIS index is out of date.\n"
            "\n"
            f"  {rel} is built by script from the OEIS A-numbers cited on the wiki pages.\n"
            "  Your staged changes add, remove, or re-cite an A-number, so the index no longer\n"
            "  matches the pages. Do not edit the index by hand.\n"
            "\n"
            "  To fix, from the repo root, regenerate the index and re-stage it:\n"
            "\n"
            f"      python3 bin/generate-oeis-index.py && git add {rel}\n"
            "\n"
            "  then run your git commit again.\n"
            "\n"
            "  A new A-number with no row in config/oeis-annotations.tsv will appear under\n"
            "  \"Not yet annotated\"; add a row (group, OEIS name, castle role) to file it.\n",
            file=sys.stderr,
        )
        return 1

    updated = date.today().isoformat()
    if unchanged and old_fm:
        for line in old_fm:
            if line.startswith("updated:"):
                updated = line.split(":", 1)[1].strip()
    OUTPUT.write_text(frontmatter(len(cites), updated) + body, encoding="utf-8")
    n_un = sum(1 for a in cites if a not in ann)
    print(f"wrote {OUTPUT.relative_to(WIKI_ROOT)} ({len(cites)} A-numbers, {n_un} unannotated)"
          + ("" if unchanged else ", body changed"))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
