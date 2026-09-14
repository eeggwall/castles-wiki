# Castles Wiki

An LLM-maintained research wiki on **Project Euler 502** — the "castle" polyomino-counting
problem — and its connections to the wider world of combinatorics.

The problem: a **castle** is a configuration of stacked integer-length, unit-height *blocks*
on a *w*×*h* grid (no overhangs, grid-snapped, ≥1-unit gaps between same-row blocks, a
full-width bottom row, maximum height exactly *h*). PE 502 asks for `F(w,h)`, the number of
castles with an **even** number of blocks. This wiki treats the even-block count as a special
case of the general object: **`A(w,h)`** counts *all* castles (either parity), `F` its
even-block restriction; the odd count is `A − F` (deliberately unnamed — `G` is reserved for
generating functions).

## Mission

More than recording the solution, the wiki follows **every thread through the solution
methods — and the failed ones — outward into the broader polyomino and combinatorics
literature**, to surface research topics, connections to other branches of mathematics, and
concrete, accessible problems for seminars and external collaborators. Each concept page is
written as a thread to follow; each ingested source is an entry point into a neighboring
domain. See `wiki/overview.md` for the current synthesis and `TODO.md` for open research
threads and pending work.

## Layout

```
SCHEMA.md          conventions + how the wiki tools locate this wiki (do not move/delete)
TODO.md            open research threads, OEIS submissions, ingestion queue
config/            link-style rules (markdown: [[slug](pages/slug.md)])
bin/               stdlib helper scripts + the pre-commit hook (see below)
raw/               immutable source documents (wikitext, notes, cached refs) — never edited
assets/            downloaded images / PDFs (git-ignored; re-fetchable, see below)
wiki/
  index.md         GENERATED catalog (git-ignored) — never hand-edit; run bin/generate-index.py
  overview.md      evolving synthesis across all sources
  pages/           all wiki pages, flat, slug-named (no subdirectories)
```

Pages are grouped by `category` frontmatter into **Sources** (ingested documents),
**Concepts**, and **Analyses**. Currently ~56 pages (26 Sources, 27 Concepts, 3 Analyses).

## Conventions

- **`raw/` is immutable** — every citation's `L…` line-numbers point into these files, so
  they are never modified after ingest. They are text (small, diffable) and tracked.
- **Cross-references** use the markdown link style `[[slug](pages/slug.md)]`; citation
  targets follow `config/link-style.md`. Every claim that isn't common knowledge carries a
  footnote citing a source (a `raw/` file with a locator, or a URL).
- **`wiki/index.md` is generated**, not hand-written — set page frontmatter (`category`,
  `summary`, `created`) and run `python3 bin/generate-index.py`. It is git-ignored.
- **The git history is the operation log.** Each operation is one commit with a `Wiki-Op:`
  trailer (`init`, `ingest`, `update`, …); render the human log with
  `python3 bin/render-log.py`.
- **Verify before citing.** Numeric and algorithmic claims are re-checked by execution during
  ingest; the wiki records what was confirmed.

## Setup (after a fresh clone)

1. **Pre-commit hooks.** `core.hooksPath` is repo-local config and does *not* survive a
   clone — re-run it once so the pre-commit gates (contradiction flag + structural lint) fire:
   ```
   git config core.hooksPath bin/hooks
   ```
   The hook runs `bin/check-contradictions.py` and `bin/lint-mechanical.py --staged` via
   `uv run`, so an interpreter is guaranteed. (Install `uv` if you don't have it, or edit the
   hook to use `python3`.)
2. **MCP config.** `.mcp.json` wires up the MediaWiki and PDF-reader MCP servers used to
   ingest sources. Its paths are **machine-specific absolute paths** (`/Users/charles/…`) and
   its MediaWiki credentials live in an external file, not in the repo — adjust the paths for
   your machine.
3. **PDFs.** The reference papers under `assets/*.pdf` are **git-ignored** (binaries don't
   diff and bloat the repo). They are cited by the wiki and can be re-fetched from
   charlesreid1.com (each source page names its origin). Other binary types are ignored too;
   see `.gitignore`.

## Working with the wiki

The wiki is maintained with the `wiki-skills` toolkit (init / ingest / lint / audit / merge /
query / update). Typical loop: add a source to `raw/` (or ingest a URL/file directly), write
or update the flat pages under `wiki/pages/`, regenerate the index, and commit — the
pre-commit gates keep every committed page structurally valid and contradiction-free.
