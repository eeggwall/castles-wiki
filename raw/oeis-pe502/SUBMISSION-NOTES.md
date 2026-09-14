# OEIS submission execution notes (shared)

These notes apply to every draft in this directory (`oeis-xref-draft.md`,
`new-sequence-F3.md`, and `xrefs/*.md`).  Read this before executing any draft, so the
mechanical parts are unambiguous.

## 1. Field map (OEIS "contribute/edit" form)

The web form has labeled boxes.  A draft's headings map to them as follows:

| Draft heading        | Form field        | Internal code |
|----------------------|-------------------|---------------|
| Name                 | Name              | `%N`          |
| Data & offset        | Data, Offset      | `%D`, `%O`    |
| Comment              | Comments          | `%C`          |
| Formula              | Formula           | `%F`          |
| Crossrefs (Cf.)      | Crossrefs         | `%Y`          |
| Program              | Program (LANGUAGE) | `%p`          |
| Links                | Links             | `%H`          |
| Keywords             | Keywords          | `%K`          |

## 2. Scope rule (do this or nothing)

Every draft is a **change to one existing sequence** (or, for `new-sequence-F3.md`, one new
sequence).  Unless the draft explicitly says otherwise:

- ADD the quoted Comment and/or Formula text only.
- DO NOT modify: Name, Data, Offset, Keywords, Links, or any existing comment/formula/xref.

## 3. Signature / attribution (required on every added line)

- Every comment/formula line you add MUST be signed by a human author, OEIS style:
      `- _Firstname Lastname_, Mon D YYYY`      (no leading zero on the day)
  Example from OEIS: `- _N. J. A. Sloane_, Jul 15 2000`.
- In the drafts, the literal `_Charles Reid_, Sep 05 2026` is a PLACEHOLDER.  Replace it
  with the actual OEIS account name and the actual submission date.  Do not paste it
  verbatim without checking the account name and date.

## 4. Mechanical vs human (division of labor)

- A tool may: run the verification scripts, check offsets against the live entries, format
  data.  It may NOT author the prose.
- Only a human may: rewrite the draft prose in their own words, sign it, and submit.  OEIS
  forbids AI-authored text (`oeis-submission-process.md`, "AI policy").

## 5. Notation rules

- Plain ASCII only.  No TeX, no Mathematica.  Use `Sum_{k=1..n}`, `C(n,k)` (or
  `binomial(n,k)`), `x^2`.
- Reference A-numbers as `A000225`, never `A 000225`.

## 6. Verification scripts (all `python3`)

- Castle quantities: `pe502/castle.py` (self-test) and `pe502/tabulate.py`.
- Tower quantities (tier 2): `pe502/tower.py` (self-test).
- OEIS search: `pe502/oeis_search.py`.

## 7. Definitions used across the drafts

- **Castle** (PE 502): column heights c_1..c_w in {1..h} with max = h; blocks = maximal
  horizontal runs; see `castle.py`.
- **Tower** (tier 2): column heights c_1..c_w >= 0 (no full-bottom, no max-height, no
  parity); blocks = maximal runs = c_1 + Sum_{i=2..w} max(0, c_i - c_{i-1}); see `tower.py`.
  The tier-2 drafts restate this definition self-containedly in each Comment.
