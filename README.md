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

## What this is (and how to use it)

This is **not a wiki you read and edit by hand.** It is a knowledge base that an LLM builds
and maintains for you, following [Andrej Karpathy's LLM Wiki
pattern](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f): instead of
re-deriving answers from raw documents every time (RAG), you accumulate a structured,
interlinked set of markdown pages that gets richer with every source you feed it and every
question you ask.

The wiki is driven entirely by the **[`wiki-skills`](https://github.com/kfchou/wiki-skills)**
Claude Code plugin — a set of skills (`wiki-init`, `wiki-ingest`, `wiki-query`, `wiki-lint`,
`wiki-audit`, `wiki-update`, `wiki-merge`) that do the reading, writing, linking, citing, and
fact-checking. **You talk to the wiki through those skills, not by editing files.** The rest
of this README is about getting the plugin installed, pointed at this clone, and running your
first ingest and query.

## Mission

More than recording the solution, the wiki follows **every thread through the solution
methods — and the failed ones — outward into the broader polyomino and combinatorics
literature**, to surface research topics, connections to other branches of mathematics, and
concrete, accessible problems for seminars and external collaborators. Each concept page is
written as a thread to follow; each ingested source is an entry point into a neighboring
domain. See [`wiki/overview.md`](wiki/overview.md) for the current synthesis and
[`TODO.md`](TODO.md) for open research threads and pending work.

## Quick start (fresh clone → asking questions)

You need [Claude Code](https://claude.ai/code) and, for the wiki's helper scripts,
[`uv`](https://docs.astral.sh/uv/) (it also supplies Python 3 if you don't have it). Then:

### 1. Install the `wiki-skills` plugin

In Claude Code, from **any** directory:

```
/plugin marketplace add kfchou/wiki-skills
/plugin install wiki-skills@wiki-skills
```

This gives you the `wiki-*` skills. (To remove later:
`/plugin uninstall wiki-skills@wiki-skills` then `/plugin marketplace remove wiki-skills`.)

### 2. Re-arm the pre-commit hooks

`core.hooksPath` is repo-local config and does **not** survive a clone — re-run it once so the
commit-time gates (contradiction flag + structural lint) fire:

```bash
git config core.hooksPath bin/hooks
```

The hook runs `bin/check-contradictions.py`, `bin/lint-mechanical.py --staged`, and
`bin/generate-oeis-index.py --check` via `uv run` before every commit. (Override an intentional commit with `git commit --no-verify`.)

### 3. Wire up the MCP servers

`.mcp.json` configures two MCP servers that `wiki-ingest` uses. Both are launched via `npx`,
so the PDF reader works out of the box; only the MediaWiki server needs a one-line edit to
point at your (external, un-committed) credentials file. See the [MCP
servers](#mcp-servers) section below. *(This step is only needed if you'll ingest MediaWiki
pages or PDFs; plain URLs / files / notes work without it.)*

### 4. Use it

Open Claude Code **in this repo** (`cd` into the clone first — the skills find the wiki via
[`SCHEMA.md`](SCHEMA.md)). Now you can:

- **Ask a question** — invoke `wiki-query` (or just ask; the skill reads the wiki pages, never
  answers from memory, and offers to file a good answer back as a new page):
  > What's the connection between castle-counting and transfer matrices?

- **Feed it a source** — invoke `wiki-ingest` with a paper, URL, file, transcript, or note. It
  surfaces the key takeaways and asks what to emphasize *before* writing, then creates/updates
  pages (one ingest may touch 10–15 of them) and runs a backlink audit to wire in
  cross-references:
  > Ingest https://oeis.org/A… into the wiki

- **Health-check it** — run `wiki-lint` every 5–10 ingests to catch contradictions, orphans,
  broken links, and coverage gaps; `wiki-audit <page>` fact-checks a single page's footnotes
  against their sources.

The skills **suggest** a commit after each operation and commit on your confirmation — they
never auto-commit, and the git history *is* the operation log (see Conventions).

> **Starting a wiki from scratch, elsewhere?** Run `wiki-init` in an empty repo to bootstrap
> the same structure (it copies the `bin/` scripts, installs the hook, and writes a fresh
> `SCHEMA.md`). This clone is already initialized — you don't run `wiki-init` here.

## MCP servers

`wiki-ingest` reaches sources through two [MCP](https://modelcontextprotocol.io/) servers,
both declared in [`.mcp.json`](.mcp.json) at the repo root. Claude Code launches them
automatically when you open the repo.

| Server | Package | What the wiki uses it for |
|---|---|---|
| `mediawiki-mcp-server` | [`@professional-wiki/mediawiki-mcp-server`](https://www.npmjs.com/package/@professional-wiki/mediawiki-mcp-server) | Read (and, with credentials, edit) MediaWiki pages — the wikitext sources under `raw/` originate here, on charlesreid1.com |
| `pdf-reader` | [`@sylphx/pdf-reader-mcp`](https://www.npmjs.com/package/@sylphx/pdf-reader-mcp) | Read and search PDFs so `wiki-ingest` can pull their knowledge into the wiki |

**`pdf-reader` works with zero setup.** `.mcp.json` invokes it via `npx -y
@sylphx/pdf-reader-mcp`, so nothing is committed and no machine-specific paths are involved
— you just need `node` (≥ 22.13) and `npm` on `PATH`. First launch downloads the package;
subsequent launches use the npx cache.

**`mediawiki-mcp-server` needs one edit** — the `CONFIG` env var must point at an external,
un-committed credentials JSON (MediaWiki API URL + OAuth/bot credentials). Create your own
and update the path in `.mcp.json`. See the [server's
docs](https://github.com/ProfessionalWiki/mediawiki-mcp-server) for the config shape. The
package itself is launched via `npx`, same as pdf-reader — no install step required.

The current wiring:

```jsonc
{
  "mcpServers": {
    "mediawiki-mcp-server": {
      "type": "stdio",
      "command": "npx",
      "args": ["-y", "@professional-wiki/mediawiki-mcp-server"],
      "env": { "CONFIG": "/absolute/path/to/mediawiki-mcp/config.json" }  // ← your external, un-committed credentials file
    },
    "pdf-reader": {
      "type": "stdio",
      "command": "npx",
      "args": ["-y", "@sylphx/pdf-reader-mcp"]
    }
  }
}
```

You don't need either server to *ask questions* of the existing wiki or to ingest plain URLs,
files, and notes — they matter when you're ingesting MediaWiki pages or PDFs.

## Layout

```
SCHEMA.md          conventions + how the wiki tools locate this wiki (do not move/delete)
IDEAS.md           project and seminar ideas, organized by Department
TODO.md            OEIS submissions (human action), ingestion queue, housekeeping
config/            link-style rules (markdown: [[slug](pages/slug.md)]) + oeis-annotations.tsv
bin/               stdlib helper scripts + the pre-commit hook (see Quick start)
raw/               immutable source documents (wikitext, notes, cached refs) — never edited
assets/            scratch images / PDFs for ingest (git-ignored; not needed to use the wiki)
wiki/
  index.md         GENERATED catalog (git-ignored) — never hand-edit; run bin/generate-index.py
  overview.md      evolving synthesis across all sources
  pages/           all wiki pages, flat, slug-named (no subdirectories)
    oeis-index.md  GENERATED A-number directory (committed) — run bin/generate-oeis-index.py
```

Pages are grouped by `category` frontmatter into **Sources** (ingested documents),
**Concepts**, **Analyses**, and **Reference** (script-generated lookup pages). Currently ~56 pages (26 Sources, 27 Concepts, 3 Analyses).

## Conventions

These are enforced by the skills and the pre-commit gates; [`SCHEMA.md`](SCHEMA.md) is the
authoritative spec.

- **`raw/` is immutable** — every citation's `L…` line-numbers point into these files, so
  they are never modified after ingest. They are text (small, diffable) and tracked.
- **Cross-references** use the markdown link style `[[slug](pages/slug.md)]`; citation
  targets follow [`config/link-style.md`](config/link-style.md). Every claim that isn't common
  knowledge carries a footnote citing a source (a `raw/` file with a locator, or a URL).
- **`wiki/index.md` is generated**, not hand-written — set page frontmatter (`category`,
  `summary`, `created`) and run `python3 bin/generate-index.py`. It is git-ignored, so
  regenerate it before reading after a fresh clone.
- **`wiki/pages/oeis-index.md` is generated** too — `bin/generate-oeis-index.py` scans every
  page for OEIS A-numbers and lists the citing pages with mention counts; the role annotations
  it merges in live in `config/oeis-annotations.tsv`. It is committed (other pages link to it),
  and the pre-commit hook blocks a commit that leaves it stale. The hand-curated novelty
  catalogue is a normal page, `castle-sequence-catalogue`.
- **The git history is the operation log.** Each operation is one commit with a `Wiki-Op:`
  trailer (`init`, `ingest`, `update`, …); render the human log with
  `python3 bin/render-log.py`.
- **Verify before citing.** Numeric and algorithmic claims are re-checked by execution during
  ingest; the wiki records what was confirmed.
