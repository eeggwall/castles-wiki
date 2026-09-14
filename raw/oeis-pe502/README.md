# PE 502 "castles" — OEIS mining workspace

Interlinking occupation: take the Project Euler 502 "castle" object (a real, third-party
combinatorial object) and find the existing A-numbers whose integers its counts reproduce.
Full framing lives in the parent `plan-pe-502.md`; this directory holds the code, the
verified numbers, and the writeups that came out of the first mining pass.

## The object (one paragraph)

A **castle** of width `w`, height exactly `h` is a column-height profile `c_1..c_w` in
`{1..h}` with `max(c) = h`. A block is a maximal horizontal run, so

    #blocks = c_1 + sum_{i>=2} max(0, c_i - c_{i-1}).

Rule 3 (gap between neighbouring same-row blocks) is automatic in the run decomposition;
Rule 6 (even block count) is the parity filter. The even-parity count is

    F(w,h)  = (h^w - (h-1)^w - P(h-1,w) + P(h-2,w)) / 2,
    P(k,L)  = sum over towers c_1..c_L in 0..k of (-1)^#blocks.

## Files

### Code
- **`castle.py`** — the verified computation module. Exposes `F`, `F_odd`, `F_any`,
  `p_signed`, `brute`, `convex_any`, `block_poly`, `blocks_of`, `is_unimodal`.
  Self-test reproduces all four known PE values and brute-forces `w,h <= 5`.
- **`tower.py`** — the tower (heap) block-count module for tier 2: `narayana`,
  `tower_block_counts`, `T_formula`. Self-test verifies the Narayana-polynomial g.f.
  against brute force.
- **`tabulate.py`** — prints every vein's tables (run it to re-derive the numbers).
- **`vein9_area.py`** — re-indexes castles by area (total cells) for vein 9; prints
  each area-sequence ready to paste into OEIS search.
- **`vein9b_concave.py`** — vein 9b, the concave counterparts: valley, strict-valley,
  and non-convex castles by area and by (w, h).
- **`oeis_search.py`** — OEIS search helper (`search(terms) -> list of matches`).
- **`search_all.py`** — runs every castle-derived sequence through OEIS and prints matches.

### Data
- **`tables.json`** — 50-term tabulations: `F_row` (h=3,4,5), `F_odd_row` (h=3,4,5),
  `F_col` (w=3,4,5); index starts at 1. Values are exact big integers.
- **`terms_50.txt`** — the same tables, human-readable, one sequence per block with offset.

### Writeups
- **`SUBMISSION-NOTES.md`** — shared execution guide for all drafts: field map, signature
  format, scope rule, mechanical-vs-human split. Read before executing any draft.
- **`mine-notes.md`** — the first-pass findings: every vein, matched vs new, with the
  offset-correct A-numbers and the linear recurrences. Start here.
- **`binomial-vandermonde-identity.md`** — why `convex(w,h) = C(2h+w-3, w-1)` (the
  up/down decomposition + generalized Vandermonde), and why it is binomial, not Catalan.
- **`oeis-xref-draft.md`** — draft cross-reference comment for A038505/A038503 (the
  height-2 castle interpretation). **Draft only**; OEIS requires human authorship.
- **`new-sequence-F3.md`** — draft submission package for the new sequence `F(w,3)`
  (even-block castles of height 3): name, 50 terms, recurrence, g.f., program, crossrefs.
- **`crosslink-avenues.md`** — the full cross-link submission menu (tier 1/2/3), including
  the second-pass tower/heap = Narayana-polynomial finding.
- **`vein9-area.md`** — vein 9 writeup: castles indexed by area (total cells). Main
  finding is `conv(n) = A001523(n)` (weakly unimodal compositions) plus four new
  parity-refined sequences whose sum recovers A001523.
- **`vein9b-concave.md`** — vein 9b writeup: the concave counterparts. Three new
  xref matches (A332578 valley, A115981 non-convex, A332669 not-valley), one new
  base sequence (strict-valley), and six new parity-refined variants.
- **`xrefs/`** — one draft per cross-link (tier 1: `oeis-xref-draft.md` covers
  A038505/A038503; tier 2 here): `A005408-tower.md`, `A005891-tower.md`,
  `A063490-tower.md`, `A160747-tower.md`, `A001263-tower.md`; plus `A001523-castle.md`
  from vein 9 and `A332578-castle.md`, `A115981-castle.md` from vein 9b.

## Results at a glance

| Object | OEIS | Status |
|---|---|---|
| `P(1,L)` signed towers | `A146559(L+1)` | match — **corrects plan's A009545** (that's the imaginary part) |
| `Im((1+i)^n)` companion | `A009545` | match |
| any-parity, height h | `A000225, A001047, A005061, A005060, A005062` | match (trivial) |
| `F(w,2)` even castles h=2 | `A038505(w+1) = Σₖ C(w+1, 2+4k)` | match (the real win) |
| `odd(w,2)` odd castles h=2 | `A038503(w+1) − 1 = Σ_{k≥1} C(w+1, 4k)` | match (the real win) |
| `convex(w,h)` any parity | binomial `C(2h+w−3, w−1)` | match (binomial, not Catalan) |
| block dist h≤1 | `A034839` | match (binomial) |
| convex castles by area | `A001523(n)` | match (weakly unimodal compositions; dense entry) |
| valley castles by area | `A332578(n)` | match (negation-unimodal compositions) |
| non-convex castles by area | `A115981(n)` | match (= `A011782 − A001523`) |
| all castles by area | `A000079(n−1) = 2^(n−1)` | match (trivial: compositions) |
| `F(w,h)`, h≥3 (rows) | — | **NEW** (C-finite; `F(w,3)` order 6) |
| `F(w,h)`, w≥3 (columns) | — | **NEW** (quasi-poly, `(x²−1)^w`) |
| `odd(w,h)`, h≥3 | — | **NEW** |
| block dist h≥2 | — | **NEW** |
| castles by area, parity-refined | — | **NEW** (`cev+cod = A001523(n)`) |
| strict-valley by area | — | **NEW** (castles with a true interior dip) |
| concave castles by area, parity-refined | — | **NEW** (6 sequences, parity splits of A332578 / A115981) |

## Key facts worth remembering

- **Height 2 is the order-4 "hyperbolic" family.** `F(w,2) = A038505(w+1)`,
  `odd(w,2) = A038503(w+1) − 1`, total `2^w − 1 = A000225(w)`. The castle gives
  `{A038503, A038505}` (and by symmetry `A038504`, `A000749`) a geometric reading.
- **Convex ⟺ unimodal ⟺ exactly `h` blocks.** `#blocks ≥ h` with equality iff unimodal,
  so convex castles are the minimum-block castles, counted by `C(2h+w−3, w−1)`.
- **No Catalan anywhere in the natural parameterisations.** The castle's constraints
  (gap, parity, convexity) are all *binomial* constraints; there is no ballot /
  non-crossing condition (see `binomial-vandermonde-identity.md` §4).
- **But the *tower* block-count has a Narayana-polynomial generating function.** The number of towers (heaps of
  unit-height segments) of width w with b blocks is
  `T(w,b) = Σₖ Narayana(w,k)·C(b+w−k, w−1)`; its g.f. is the Narayana polynomial over
  `(1−x)^w`. Rows w=2,3,4,5 are A005408, A005891, A063490, A160747; w≥6 is new. This is
  the Catalan/Narayana thread the plan hoped for, living in vein 6/7 (not the convex count).

## Status / next steps

Done: computation + verification, tabulations, binomial proof, cross-ref draft, the
tower/Narayana-polynomial finding, the cross-link menu, plan bug-fixes. Remaining (human action):

1. **Submit cross-links** per `crosslink-avenues.md` — lead with the tier-1 trio
   A038505 / A038503 / A146559 (reword `oeis-xref-draft.md` in own words; add the
   `Cf. A000225` link).
2. **Submit a new sequence.** `F(w,3)` is the cleanest candidate:
   `0, 0, 3, 21, 89, 307, 977, 3031, 9321, 28479, 86505, 261615, …`
   (width `w`, height exactly 3, even number of blocks), 6th-order recurrence
   `(x−3)(x−2)(x²−x+2)(x²−2x+2)`. Needs a name, definition, formula, program, b-file.

Note the repo-wide `oeis-submission-process.md` for the submission mechanics and the
OEIS AI policy (human authorship required; new contributors throttled to a few drafts).
