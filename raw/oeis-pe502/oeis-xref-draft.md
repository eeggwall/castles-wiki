# OEIS cross-reference draft — height-2 PE 502 castles -> A038505 / A038503

Status: SUBMITTED to OEIS as "Chaz Reid" on 2026-09-18. The draft below is retained as the pre-submission record; the final wording differs as noted below.
OEIS forbids AI-authored submissions; treat everything below as a checked,
correct starting point, not as final text.
Execution notes (field map, signature format, scope): see SUBMISSION-NOTES.md.

**Changes made at submission (2026-09-18):**
- A038503 comment reworded to "height at most 2" (folds the all-height-1 castle in directly; drops the draft's "1 more than … height 2" framing).
- FORMULA uses the A000225 decomposition, not the direct F(w,2)/odd(w,2) form:
  - A038503: `a(n) = A000225(n-1) - A038505(n) + 1 for n >= 1` and `a(n) = A038505(n) + A146559(n)`.
  - A038505: `a(n) = A000225(n-1) - A038503(n) + 1 for n >= 1`.
- A038505 gained the `Project Euler, Problem 502: Counting Castles` link; both Cf. lists gained A000225, and A038503's also gained A146559.
- A146559 itself was also updated with `a(n) = A038503(n) - A038505(n)` (Chaz Reid, Sep 18 2026).
- Final comment text is quoted verbatim on the wiki page `oeis-height2-hyperbolic-castles.md`.

---

## 0. Verified identities (offsets nailed)

All four sequences are offset 0 (the second offset figure, "0,4" / "0,5" / "0,3"
/ "0,5", is the 1-based position of the first term with absolute value > 1 and is
auto-maintained — do not touch it).

- A038505(n) = Sum_k binomial(n, 2+4k) = Sum_k binomial(n, 4k+2).
  Data: 0, 0, 1, 3, 6, 10, 16, 28, ...  (a(0) = a(1) = 0).
- A038503(n) = Sum_k binomial(n, 4k).
  Data: 1, 1, 1, 1, 2, 6, 16, 36, ...  (a(0) = a(1) = 1).

Castle facts (already proven in mine-notes.md):

- A castle of width w, height exactly 2 is a subset of columns reaching height 2
  (equivalently a binary string of length w, 1 = column of height 2), with at
  least one such column.  The bottom row is one block; the number of blocks is
  **1 + r**, where r = number of runs of height-2 columns.
- #strings of length w with exactly r runs of 1's = binomial(w+1, 2r).
- Even block count  <=>  1 + r even  <=>  r odd  <=>  2r = 2 mod 4, so
  **F(w,2) = A038505(w+1)**, where F(w,2) is the Project Euler 502 count
  (even number of blocks).
- Odd block count  <=>  r even.  Excluding r = 0 (no height-2 column: the single
  block of length w, height 1, one block), so
  **odd(w,2) = A038503(w+1) - 1 = Sum_{k>=1} binomial(w+1, 4k)**.
- Total height-2 castles (any parity) = 2^w - 1 = **A000225(w)**, and
  A038505(n) + A038503(n) - 1 = A000225(n-1) for n >= 1.

Offset statements (exact):

- A038505:  a(n) = F(n-1, 2) for n >= 2, with a(0) = a(1) = 0.
  Check: a(2)=1=F(1,2), a(3)=3=F(2,2), a(4)=6=F(3,2), a(5)=10=F(4,2).
- A038503:  a(n) = odd(n-1, 2) + 1 for n >= 2, with a(0) = a(1) = 1.
  Check: a(2)=1=0+1, a(3)=1=0+1, a(4)=2=1+1, a(5)=6=5+1.

---

## 1. What is already there (do NOT duplicate)

A038505 (offset 0, "Sum of every 4th entry of row n, starting at binomial(n,2)"):
- Comments: trace/subtrace of binary strings over Z_2/GF(2); binomial transform
  of (0,1,1,0,...) (Barry 2003); M^n matrix interpretation (Adamson 2009); the
  order-4 hyperbolic difference analog (Shevelev 2017).
- Formulas already include "a(n) = Sum_{k=0..n} binomial(n, 2+4*k)" and the g.f.,
  recurrence 4,-6,4, and closed forms.  Do NOT re-add the bare binomial sum.
- Xref: "Cf. A000749, A009116, A009545, A038503, A038504."  (A000225 is missing.)

A038503 (offset 0, "Sum of every 4th entry of row n, starting at n choose 0"):
- Comments: trace/subtrace; M^n; generalized compositions (Janjic 2010); the
  hyperbolic family (Shevelev 2017).
- Formulas already include "a(n) = Sum_{k=0..floor(n/4)} binomial(n, 4k)" and
  g.f., e.g.f., hypergeom.  Do NOT re-add the bare binomial sum.
- Xref: "Cf. A024493, A024494, A024495, A038505, A038504, A000749." +
  "Row sums of A098173."  (A000225 is missing.)

A038504 (offset 0, starts at C(n,1)) and A000749 (offset 0, starts at C(n,3)):
- Both already cross-reference the whole family {A038503, A038504, A038505,
  A000749}.  No comment change needed for them.  A000225 is not in their xrefs
  either (optional to add).

So the castle comment is a NEW geometric interpretation (distinct from the
existing trace/subtrace and matrix comments), and the only genuinely missing
cross-reference is **A000225** (the total, 2^w - 1).

---

## 2. A038505 — draft additions

### Comment (append to COMMENTS, after the Shevelev line)

> a(n) is also the number of castles of width n-1 and height 2 with an even
> number of blocks (Project Euler Problem 502), for n >= 2.  Here a castle is a
> stack of unit blocks on a grid, snapped to the grid, whose bottom row is a
> single block of length w, whose higher blocks have height 1 and rest on the
> blocks below without overhang, whose maximum height is 2, and in which two
> neighboring blocks of the same row are separated by a gap.  Such a castle is
> determined by the columns that reach height 2; if these form r runs, the
> number of blocks is 1 + r, so an even number of blocks means r is odd.

### Formula (append to FORMULA)

> a(n) = F(n-1, 2) for n >= 2, where F(w, 2) is the number of castles of width w
> and height exactly 2 with an even number of blocks (Project Euler Problem 502);
> a(0) = a(1) = 0.

Optional second formula (decomposition; keeps the cross-reference substantive):

> a(n) = A000225(n-1) - A038503(n) + 1 for n >= 1.

---

## 3. A038503 — draft additions

### Comment (append to COMMENTS, after the Shevelev line)

> a(n) is 1 more than the number of castles of width n-1 and height 2 with an
> odd number of blocks (Project Euler Problem 502), for n >= 2; the extra 1 is
> the all-height-1 castle, a single block of length w, which has height 1, not
> 2.  Here a castle is a stack of unit blocks on a grid, snapped to the grid,
> whose bottom row is a single block of length w, whose higher blocks have
> height 1 and rest on the blocks below without overhang, whose maximum height
> is 2, and in which two neighboring blocks of the same row are separated by a
> gap.  If the columns reaching height 2 form r runs, the number of blocks is
> 1 + r, so an odd number of blocks means r is even, and the r = 0 term
> binomial(n, 0) = 1 of a(n) = Sum_k binomial(n, 4*k) is the extra 1.

### Formula (append to FORMULA)

> a(n) = odd(n-1, 2) + 1 for n >= 2, where odd(w, 2) is the number of castles of
> width w and height exactly 2 with an odd number of blocks (Project Euler
> Problem 502); a(0) = a(1) = 1.

Optional second formula (decomposition):

> a(n) = A000225(n-1) - A038505(n) + 1 for n >= 1.

---

## 4. Cross-reference note

Add **A000225** to the Cf. list of both sequences (it is the total number of
height-2 castles, 2^w - 1).  The family {A038503, A038504, A038505, A000749} is
already mutually cross-referenced everywhere; no change needed for A038504 and
A000749.

Use these exact Cf. lines (A000225 inserted first; the rest is the current entry's
existing list, unchanged):

- A038505:
  `Cf. A000225 (total number of castles of width n-1 and height 2, 2^(n-1) - 1), A000749, A009116, A009545, A038503, A038504.`
- A038503:
  `Cf. A000225 (total number of castles of width n-1 and height 2, 2^(n-1) - 1), A024493, A024494, A024495, A038505, A038504, A000749.`

---

## 5. Things to verify / decide before submitting (flags)

1. **Own wording + attribution.** OEIS requires human authorship. Rework the
   sentences into your own words. Sign each comment/formula line
   ` - _Firstname Lastname_, Mon D YYYY` — replace the placeholder
   `_Charles Reid_, Sep 05 2026` with the actual OEIS account name and the actual
   submission date.  Do not submit the text verbatim as AI output.

2. **"Project Euler Problem 502" phrasing.** OEIS links PE problems as
   `Project Euler, <a href="https://projecteuler.net/problem=502">Problem 502: Counting castles</a>`
   (compare A030101's link to Problem 463).  Consider also adding that Link line
   to each sequence so the reference is clickable; then the comment can just say
   "Project Euler Problem 502".  Confirm the exact problem title ("Counting
   castles") on projecteuler.net before adding a link.

3. **Notation in comments.** The Style Sheet prefers plain English in COMMENTS;
   the `Sum_k binomial(n, 4*k)` / `binomial(w+1, 2*r)` fragments above are
   OEIS-style ASCII (not TeX) and are fine, but if the editor flags them, move
   the identities to the FORMULA section and keep the comments purely verbal.
   Avoid `\binom`, `\sum`, `$...$`, and Mathematica.

4. **Formula-summation style.** The entries already use `Sum_{k=0..n}
   binomial(n, 2+4*k)`; match that (underscore braces) in the FORMULA section if
   you add the explicit sum there.  In the draft I wrote `Sum_k ...` only inside
   the A038503 *comment*; restate it in house style if you move it.

5. **Crossref syntax.** "Cf. A000225, ..." comma-separated, ends with a period,
   one A-number each, leading A-numbers roughly ascending.  Use exactly the lines in
   section 4; do not add a trailing period inside the parenthetical before the comma.

6. **Offsets.** Do not change the offset fields (0,4) / (0,5).  The claim
   "a(n) = F(n-1, 2) for n >= 2" is consistent with offset 0 because a(0) = a(1)
   = 0 (widths -1 and 0 have no castles); state the n >= 2 / a(0)=a(1)=0 part
   explicitly so the editor can see the shift is right.

7. **Whether to also add A000225 to A038504 / A000749.** Not required (both
   already sit in the family cluster).  Optional for completeness; A000749's
   xref list is long and the total-count link is cleaner on A038505/A038503.
