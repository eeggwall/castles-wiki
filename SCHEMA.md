# Wiki Schema

## Identity
- **Path:** /Users/charles/castles/castles-wiki
- **Domain:** Research notes on Project Euler 502 — the "castle" polyomino-counting problem — to organize research seminars, involve external collaborators, surface research topics and overlaps, and investigate connections to other branches of mathematics (especially combinatorics and polyominoes).
- **Source types:** Papers, URLs / web pages, Code / scripts, Notes / transcripts
- **Created:** 2026-09-13

## Page Frontmatter
Every wiki page must start with:
---
title: <page title>
category: <one of the Index Categories below>
summary: <one-line description — becomes this page's index entry>
tags: [tag1, tag2]
sources: [source-slug1]
created: YYYY-MM-DD
updated: YYYY-MM-DD
---

`category` and `summary` drive index generation (see **Index Generation** below);
`category` must match one of the wiki's Index Categories. `created` is set once when the
page is first written and never changes; `updated` bumps on every edit.

## Cross-References
- **link_style:** markdown
- **link_style_rules:** config/link-style.md
- See `config/link-style.md` for the exact emit and parse rules. Every wiki skill
  reads that file to decide how to write new cross-references and how to scan
  existing ones.

## Concept Identity

The slug **is** the concept's identity — there is no separate id. A concept is the
page at `wiki/pages/<slug>.md`; everything that links to it uses `[[slug]]`. This only
works if the link graph is trustworthy, so two rules hold everywhere links are written:

1. **Links are verified, never invented.** Before writing any `[[slug]]`, the slug must
   resolve to an existing `wiki/pages/<slug>.md` **or** to a page being created in the
   same operation. List the existing page set first (`ls wiki/pages/`); never emit a
   link to a slug you have not confirmed. A `[[slug]]` that resolves to nothing is a
   hallucinated link — the failure this discipline exists to prevent.

2. **Homonyms get qualified slugs.** When a new concept collides with an existing slug
   for a *different* sense, qualify both with a discriminator rather than overloading
   one page:
   - `mercury-planet` / `mercury-element` / `mercury-mythology`
   - `transformer-ml` / `transformer-electrical`

   Pick the narrowest discriminator that disambiguates. `wiki-lint` warns when slugs
   sharing a base token look like an unintended collision.

Consolidating two pages that turn out to be the same concept (merge), or separating one
overloaded page into qualified pages (split), is the job of the `wiki-merge` skill.

## Citations

Cite every non-common-knowledge factual claim. "Common knowledge" = uncontroversial,
undergraduate-level facts in this wiki's domain. Granularity is paragraph or claim,
never per-sentence. If you cannot produce a citation in one of the forms below,
find one, weaken the claim, or drop it.

Format: Markdown footnotes. Two citation kinds, three valid targets.
The slug-target form below follows the `link_style` declared above; the examples
shown here use that style.

**Quote citation** (preferred):
```
The model uses 8 attention heads.[^1]

[^1]: [[attention-is-all-you-need](pages/attention-is-all-you-need.md)] §3.2.2 L142-143 — "We employ h = 8 parallel attention layers"
```

**Synthesis citation** (when no single quote captures the claim):
```
The architecture is fundamentally an encoder-decoder with attention.[^2]

[^2]: [[attention-is-all-you-need](pages/attention-is-all-you-need.md)] §3.2-3.4 [synthesis] L138-202 — encoder, decoder, and
      attention sections together describe the full multi-head architecture
```

`L142-143` / `L138-202` are line ranges in the raw source file. For a quote they mark
the lines the quote is taken from; for a synthesis they mark the block being summarized.

Three rules for every footnote:

1. **The cited target is one of three forms:**
   - A slug reference to a source-type wiki page, written in the wiki's
     `link_style` (preferred for sources you've ingested via `wiki-ingest`)
   - `raw/<file>` or `assets/<file>` — a path to a local file (for drive-by
     citations where a synthesis page isn't worth creating)
   - `<URL>` — a live URL, tweet, or ephemeral source (no local copy required)

   Never cite entity, concept, or analysis pages — those are syntheses, not sources.

2. **A locator is present.** Always a semantic locator: `§<section>`, `p.<n>`,
   `[HH:MM:SS]` for transcripts, URL anchor for web, or `(YYYY-MM-DD)` for dated posts.

   **Plus a line-range when the source is text-addressable.** If the resolved raw
   file is markdown, plaintext, code, or cached HTML, append a line-range token after
   the semantic locator:

   - `L<start>-<end>` — a range, e.g. `L142-145`
   - `L<n>` — a single line, e.g. `L142`
   - `L142-145,L201-203` — disjoint ranges

   The line range refers to lines in the **raw source file** resolved from the target
   (`[[slug]]` → its `**Source:**` raw path; or a direct `raw/<file>`/`assets/<file>`).
   `raw/` is immutable, so these line numbers are stable references.

   A line-range is **required** for text-addressable sources and applies to BOTH
   citation kinds — a `[synthesis]` footnote marks the block it summarizes with `L…`
   just as a quote marks the lines it quotes. **Exempt** (semantic locator only, no
   `L…`): PDFs, transcripts, and live URLs with no local cached copy.

3. **Either a verbatim quote, or the `[synthesis]` tag plus a description** of
   what the cited range supports. No third option.

**Drive-by citation examples:**
```
[^3]: raw/scaling-laws.pdf p.7 — "loss scales as a power law in compute"
[^4]: https://twitter.com/user/status/123 (2026-04-15) — "<tweet text>"
```

## Cross-Model Review

`wiki-audit strong` runs a second-opinion pass with a different-provider model and
stamps the audited page with an optional `review:` frontmatter block:
```
review:
  model: codex          # gemini | claude-sonnet
  provider: openai      # google | anthropic
  date: YYYY-MM-DD
  status: clean         # or: disputed
  findings: 2           # present only when status: disputed
```
- `status: clean` — the reviewer surfaced no disagreement with the normal audit.
- `status: disputed` — the reviewer flagged overreach or a contradiction the normal
  audit missed; `findings:` carries the count. The detail lives in the (local-only)
  audit report.
- `provider: anthropic` (the `claude-sonnet` fallback) means no different-provider CLI
  was available, so the check is same-provider and weaker.

This block is optional and is added only by `wiki-audit strong`. Pages never need it to
be valid.

## Contradiction Check

`wiki-ingest` runs a cheap contradiction check on the pages each ingest touches, before it
commits. It is a **gate, not an annotation**: every page that lands in git is clean.

- **Scope — touched neighbors only.** The check compares the pages an ingest wrote or
  edited against (a) themselves and (b) the pages that ingest already read (the entity /
  concept pages it updated and the neighbor pages from its backlink audit). It does NOT
  re-read the whole wiki — a conflict with a distant, untouched page is left to the
  periodic `wiki-lint` sweep.
- **Blocking vs. soft.** A **blocking** contradiction is a real factual conflict on the same
  entity under the same scope — incompatible dates, counts, names, or mutually-exclusive
  claims. A **soft** tension (differing emphasis, values within plausible version /
  measurement variance, claims that hold under different scope) is not a conflict.
- **The transient blocker flag.** When a blocking contradiction is found, a single line is
  written to the affected page's frontmatter and the ingest stops before committing:
  ```yaml
  contradiction-check: failed — <one-line reason naming the counterpart [[slug]] or "internal">
  ```
  The machine-readable token is the literal `contradiction-check: failed`. It exists ONLY
  while the conflict is unresolved; resolving the conflict **removes the line**. A committed
  page never carries it — there is no `passed` stamp, no severity history, nothing. Absence
  of the flag is the only "clean" state.
- **Soft tensions are surfaced, not recorded** — mentioned in the ingest summary so you can
  act if you wish, but never persisted and never blocking.

This flag is also what the **Pre-commit Gate** below scans staged files for.

## Pre-commit Gate

On a git wiki, `bin/hooks/pre-commit` (installed by `wiki-init` via
`git config core.hooksPath bin/hooks`) runs **three** deterministic gates before every commit —
no LLM:

1. **`bin/check-contradictions.py`** — scans the **staged** content of `wiki/pages/*.md`,
   frontmatter only, and **blocks the commit** if any page still carries a
   `contradiction-check: failed` flag. Backstop to the skill-level hold in `wiki-ingest`
   step 7b; on a healthy wiki it never fires. Resolve the contradiction and remove the
   `contradiction-check:` line, then re-stage.
2. **`bin/lint-mechanical.py --staged`** — scans the staged pages for **structural**
   problems and **blocks the commit** on any: missing required frontmatter, a broken
   `[[link]]`, or a slug collision (a bare slug clashing with a qualified one). Fix the page
   and re-stage.
3. **`bin/generate-oeis-index.py --check`** — **blocks the commit** if the generated
   `wiki/pages/oeis-index.md` no longer matches the pages it is derived from (an A-number was
   added, removed, or re-cited). Run `python3 bin/generate-oeis-index.py` and re-stage.

- **Fresh clone:** `core.hooksPath` is repo-local config and is not cloned — re-run
  `git config core.hooksPath bin/hooks` once after cloning.
- **Override** an intentional commit with `git commit --no-verify`.

## Operation Log & Commit Convention
Operations: init, ingest, query, update, lint, audit, merge, split

**Git wiki — the git history is the operation log.** After an operation, the skill
suggests a commit message and commits on your confirmation (skills never auto-commit).
Render the human log on demand with `python bin/render-log.py`.

The suggested subject line follows the repo's commit convention:
1. **Detect an existing convention first** — scan recent `git log` and any `.gitmessage`,
   commitlint config, or `CONTRIBUTING.md`. If the repo already has a subject style,
   follow it.
2. **Default to Conventional Commits** when none is found, choosing the type by operation:

   | Operation        | Type                                  |
   |------------------|---------------------------------------|
   | init             | `chore`                               |
   | ingest           | `docs`                                |
   | update           | `docs`                                |
   | query (saved)    | `docs`                                |
   | lint             | `fix` if fixes applied, else `chore`  |
   | audit            | `fix` if fixes applied, else `chore`  |
   | merge / split    | `refactor`                            |

**Always append a `Wiki-Op:` trailer**, whatever the subject style — it is what
`render-log.py` keys on, decoupling the log from the subject convention. Which pages
changed is read from the commit diff, so no `Pages:` trailer is needed.
```
docs: summarize Attention Is All You Need

Wiki-Op: ingest
```

**Non-git wiki — fallback to `wiki/log.md`.** Append one entry per operation:
`## [YYYY-MM-DD] <operation> | <title>`.

## Index Generation
`wiki/index.md` is a generated, gitignored artifact — never hand-edit it. It is rebuilt
from page frontmatter by `bin/generate-index.py`:
- Run `python bin/generate-index.py` (or `python3`) **before reading the index**, and
  **after** any operation that adds, removes, renames, or re-categorizes a page.
- The generator groups pages by their `category` frontmatter, in the order categories are
  listed under **Index Categories** below; within a category it lists pages newest-first
  by `created`. Each entry is `- [[slug]] — summary _(created)_`.
- Pages whose filename matches `audit-*.md` are excluded (gitignored local-only
  artifacts). A page with an unrecognized or missing `category` lands in an
  `Uncategorized` section.

## Generated Pages
`wiki/pages/oeis-index.md` (category `Reference`) is generated by `bin/generate-oeis-index.py`
and committed, because other pages link to it. Never hand-edit it. It scans every page body
for OEIS A-numbers and lists, per number, the citing pages with mention counts. The curated
fields — role group, OEIS name, one-line castle role — live in `config/oeis-annotations.tsv`;
an A-number cited on the wiki but missing from that file is listed under "Not yet annotated"
until a row is added. Rerun the script after any edit that adds or removes an A-number; the
pre-commit gate's `--check` mode blocks a commit that leaves it stale. `--fetch-names` fills
empty `name` cells from oeis.org. The hand-curated novelty catalogue is a normal page,
`castle-sequence-catalogue`, and is not generated.

## Index Categories
Sources
Entities
Concepts
Analyses
Reference

`Reference` holds lookup pages (directories, indexes) that are generated by script from the
rest of the wiki rather than written; see **Generated Pages** below.

## Conventions
- raw/ is immutable — skills never modify it
- operation log: git wikis record each op as a commit (see Operation Log & Commit Convention) and render it with bin/render-log.py; non-git wikis append to log.md (append-only, never rewritten)
- index.md is GENERATED by bin/generate-index.py and is gitignored — never hand-edit it; set page frontmatter (category, summary) and regenerate instead
- wiki/pages/oeis-index.md is GENERATED by bin/generate-oeis-index.py and committed — never hand-edit it; edit config/oeis-annotations.tsv or the citing page and regenerate (see Generated Pages)
- All pages live flat in wiki/pages/ — no subdirectories
- overview.md reflects the current synthesis across all sources
- Cross-reference and citation slug-targets follow `config/link-style.md` —
  every skill reads it before writing or scanning links
- contradiction check: ingest gates on blocking contradictions in touched pages via a transient `contradiction-check: failed` flag, removed before commit — committed pages are always clean (see Contradiction Check)
- pre-commit gate: git wikis run bin/hooks/pre-commit (via core.hooksPath) → bin/check-contradictions.py (blocks any commit staging a page that still carries the flag), bin/lint-mechanical.py --staged (structural checks), and bin/generate-oeis-index.py --check (stale generated directory) (see Pre-commit Gate); re-run `git config core.hooksPath bin/hooks` after a fresh clone
