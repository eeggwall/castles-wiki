#!/usr/bin/env python3
"""Rhetorical-filler scan for the wiki (see DESLOP.md, "Detection").

Two modes:
  python bin/slop-scan.py --rank      pre-filter patterns per 1000 prose words, one line per
                                      page, highest first (orders a deslop batch; not a verdict)
  python bin/slop-scan.py --regress   exit 1 if any retired phrase appears anywhere in
                                      wiki/overview.md or wiki/pages/*.md
  python bin/slop-scan.py --regress --staged
                                      the same, on the staged blobs (pre-commit gate)

Reading is the method; the rank patterns only order the queue and flag defined terms too.
The retired list holds phrases already cut once. Add a phrase when a deslop commit removes
it. Defined terms ("veins", "ladder", "hear" on the Kac pages) never go on either list.
Stdlib only.
"""
import re
import subprocess
import sys
from pathlib import Path

WIKI_ROOT = Path(__file__).resolve().parent.parent
WIKI_DIR = WIKI_ROOT / "wiki"

# Retired phrases: matched case-insensitively after stripping * and _ emphasis and
# collapsing whitespace.
RETIRED = [
    "smallest such castle a chorus can sing",
    "musical and not mechanical",
    "one object at every scale",
    "the exercise was the seminar",
    "seen at ten scales at once",
    "loudest note, different sandcastle",
    "build it and trust it",
    "but is it secure?",
    "the room leaves with",
    "the exercise was never abstract",
    "what does the bit buy",
    "what is the even-block bit?",
    "in disguise",
    "made physical",
    "castle analogue of a prng",
    "description-tier ladder for languages",
    "is a promiscuous word",
    "every method here is a lens",
    "knows which end of the castle is which",
    "asymptotically equivalent iff their transfer-matrix eigenvalue sequences agree",
    "every growth constant the wiki has catalogued is a topological entropy",
    "an order is a clock",
    "a thread to pull",
    "rates measure the rule",
    "robustness runs opposite",
    "knows where a castle's mass sits",
    "wants to be prime-heavy",
    "does not yet know it is d minor",
    "worth naming as coincidences",
    "feynman's party trick",
    "recent celebrities",
    "whose length set the size of the compact disc",
    "the same castle as the url",
    "complete invariant modulo cyclic shift",
    "fixes energy at the area-squared scale",
    "spectral phase transition",
    "from ten numbers",
    "pe502-nomography",
    "/users/creid/tmp",
    "pending ingest",
    "not yet added",
    "when its content lands",
    "sketched approach",
    "wearing a castle",
    "target energy",
    "outward research wing",
    "one-blackboard",
    "coined ourselves",
    "more interesting problem",
    "every chapter the wiki needs",
    "doing the real work",
    "genuine sign homomorphism",
    "meta-triad",
    "central win",
    "parent plan hoped",
    "hoped-for",
    "closes the circle",
    "the quotable",
    "first genuine outward",
    "wider web of combinatorics",
    "heart of the wiki",
    "the real win",
    "plan hoped for",
    "a thread being walked",
    "open half of the thread",
    "to great effect",
    "richest external connection",
    "most ubiquitous",
    "the castle points toward",
    "genuinely new formula",
    "textbook case",
    "that is the whole method",
    "rare and valuable",
    "the real power",
    "automaticity is automatic",
    "the honest boundary",
    "the beauty is that",
    "resident of the wall",
    "crossroads of several",
    "sits right at that ceiling",
    "matured into a tool",
    "does all the work",
    "lasting content",
    "the ceiling the grammar prunes",
    "cashes that promise",
    "the plastic surprise",
    "the price of periodicity",
    "aside for the observant",
    "immediate and pretty",
    "not by staring",
    "real-number mirror",
    "the real content",
    "honest way to test",
    "a castle count after all",
    "this is where axis 8 lives",
    "the definitive treatment",
    "at industrial scale",
    "in one breath",
    "welds the two sides",
    "one road up the same mountain",
    "cheap certificate",
    "that single sentence is the page",
    "the magic case",
    "the constraint is the whole difference",
    "natural generating-function home",
    "bedrock example",
    "earn a page here",
    "working as intended",
    "structurally-informative",
    "integer skeleton",
    "cold open",
    "looks like nothing",
    "made writing this page unavoidable",
    "motzkin-flavoured",
    "snippet in search of a purpose",
    "no exception, ever",
    "field loses information",
    "stops being bookkeeping",
    "castle-land",
    "q-analog hinge",
    "methodological bedrock",
    "the natural next-chapter home",
]
RETIRED_RE = [
    (r"\barcs?\b", "planning-file 'arc' vocabulary"),
    (r"\bthe item's\b", "planning-file 'item' vocabulary"),
    (r"(?-i:\bIDEAS\b)", "planning-file reference"),
    (r"\|\s*(days|weeks|months)\s*\|", "effort column"),
]

# Rank pre-filter: retired list plus common filler shapes. Hits include false positives.
RANK_RE = [re.escape(p) for p in RETIRED] + [r for r, _ in RETIRED_RE] + [
    r"\bthe point is\b", r"\bfor free\b", r"\bhonest", r"\bthe room\b", r"\baudience\b",
    r"\bis the \w+ of\b", r"\blens\b", r"\bprecisely\b", r"\bsecretly\b", r"\bhidden\b",
    r"\bmagic", r"\bbeautiful", r"\belegan", r"\bremarkabl", r"\bstriking", r"\bsurpris",
    r"\bprofound", r"\bdeep\b", r"\bmoral\b", r"\blesson\b", r"\bslogan", r"\bpunchline",
    r"\bin one line\b", r"\bat once\b", r"\bnot just\b", r"\bnot merely\b", r"\bexactly why\b",
    r"\bthat is why\b", r"\breally\b", r"\bsimply\b", r"\bof course\b", r"\bwear(s|ing)\b",
    r"\bknows\b", r"\bwants\b", r"\bthe trick\b", r"\btwist\b", r"\bheart of\b",
    r"\bkey insight\b", r"\bworth\b", r"\bstory\b", r"\bon the board\b", r"\bblackboard\b",
    r"\bnot \w+ but\b", r"\w\?(\s|$)",
]


def scanned(path):
    return path == "wiki/overview.md" or (
        path.startswith("wiki/pages/") and path.endswith(".md")
        and not Path(path).name.startswith("audit-") and Path(path).name != "oeis-index.md")


def pages():
    """Yield (repo-relative path, text) from the working tree."""
    paths = [WIKI_DIR / "overview.md", *sorted((WIKI_DIR / "pages").glob("*.md"))]
    for path in paths:
        rel = str(path.relative_to(WIKI_ROOT))
        if scanned(rel):
            yield rel, path.read_text()


def staged_pages():
    """Yield (repo-relative path, text) from the git index, so the gate sees what is committed."""
    git = ["git", "-C", str(WIKI_ROOT)]
    listing = subprocess.run([*git, "ls-files", "-s", "wiki"], capture_output=True, text=True,
                             check=True).stdout
    for line in listing.splitlines():
        meta, path = line.split("\t", 1)
        if scanned(path):
            blob = meta.split()[1]
            yield path, subprocess.run([*git, "cat-file", "blob", blob], capture_output=True,
                                       text=True, check=True).stdout


def normalize(text):
    return re.sub(r"\s+", " ", re.sub(r"[*_]", "", text)).lower()


def prose(text):
    """Drop fenced code blocks, frontmatter and footnote definitions (quotes of sources)."""
    text = re.sub(r"^---\n.*?\n---\n", "", text, count=1, flags=re.S)
    text = re.sub(r"^```.*?^```", "", text, flags=re.S | re.M)
    return "\n".join(l for l in text.splitlines() if not l.startswith("[^"))


def regress(source, rerun):
    hits = []
    for path, text in source:
        for n, line in enumerate(text.splitlines(), 1):
            flat = normalize(line)
            found = [f'"{p}"' for p in RETIRED if p in flat]
            found += [why for r, why in RETIRED_RE if re.search(r, line, re.I)]
            for f in found:
                hits.append(f"  {path}:{n}: {f}")
    if not hits:
        print("slop-scan --regress: 0 hits")
        return 0
    print(f"slop-scan --regress: {len(hits)} retired phrase(s) back in the wiki:\n", file=sys.stderr)
    print("\n".join(hits), file=sys.stderr)
    print("\nRewrite each line without the phrase (DESLOP.md, 'Rules for the rewrite'), re-stage,"
          f" then re-run:\n  {rerun}", file=sys.stderr)
    return 1


def rank():
    rows = []
    for path, text in pages():
        body = prose(text)
        words = len(body.split()) or 1
        flat = normalize(body)
        count = sum(len(re.findall(r, flat, re.I)) for r in RANK_RE)
        rows.append((1000 * count / words, Path(path).stem, words))
    for score, slug, words in sorted(rows, reverse=True):
        print(f"{score:5.1f}  {slug}  ({words} words)")
    return 0


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else ""
    if mode == "--regress":
        if "--staged" in sys.argv:
            sys.exit(regress(staged_pages(), "uv run bin/slop-scan.py --regress --staged"))
        sys.exit(regress(pages(), "uv run bin/slop-scan.py --regress"))
    if mode == "--rank":
        sys.exit(rank())
    print(__doc__, file=sys.stderr)
    sys.exit(2)
