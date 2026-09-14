# PE 502 castles — OEIS mining notes (first pass)

Computation: `castle.py` (verified against all four known values and brute force for w,h <= 5).

## The canonical object

A castle of width `w`, height exactly `h` is a column-height profile
`c_1..c_w in {1..h}` with `max(c) = h`.  Blocks are maximal runs, so

    #blocks = c_1 + sum_{i>=2} max(0, c_i - c_{i-1})

Rule 3 (gap between neighbouring same-row blocks) is automatic in this model.
Rule 6 (even block count) is the parity filter.  All results below follow from
this and the signed-tower count

    P(k,L) = sum_{c_1..c_L in 0..k} (-1)^#blocks,
    F(w,h)  = (h^w - (h-1)^w - P(h-1,w) + P(h-2,w)) / 2.

## Vein 1 — the signed count  [CORRECTION to plan]

The plan states `P(1,L) = A009545(L+1)`.  **This is wrong.**  A009545 is the
*imaginary* part of `(1+i)^n` ("Expansion of e.g.f. sin(x) exp(x)"):
`0,1,2,2,0,-4,-8,-8,0,16,...`.  `P(1,L)` is the *real* part.

    P(1,L) = Re((1+i)^{L+1}) = A146559(L+1)        (A146559 = (1-x)/(1-2x+2x^2))
    A009545(n) = Im((1+i)^n)                        (the companion, not P)

Concretely: `P(1,L) = 0,-2,-4,-4,0,8,16,16,0,-32,...`
and `A146559 = 1,1,0,-2,-4,-4,0,8,16,16,0,-32,...`, so `P(1,L)=A146559(L+1)`.

The general `P(k,·)` family is C-finite of order `k+1`:
    P(1): x^2 - 2x + 2                      (eigenvalues 1 +/- i)
    P(2): x^3 - 3x^2 + 4x - 4               (= (x-2)(x^2-x+2))
    P(3): x^4 - 4x^3 + 8x^2 - 8x + 8
    P(4): x^5 - 5x^4 + 12x^3 - 20x^2 + 16x - 16
    P(5): x^6 - 6x^5 + 18x^4 - 32x^3 + 48x^2 - 32x + 32
    (constant term = (-1)^{k-1} 2^k; leading coeff -(k+1))

## Vein 2 — any parity = difference of powers  [trivial but clean]

`h^w - (h-1)^w` (castles of height exactly h, ignoring Rule 6):
    h=2 -> A000225  (2^w - 1, Mersenne)
    h=3 -> A001047  (3^w - 2^w)
    h=4 -> A005061  (4^w - 3^w)
    h=5 -> A005060  (5^w - 4^w)
    h=6 -> A005062  (6^w - 5^w)
All offset 0 (a(0)=0); our terms are a(1),a(2),....  The castle gives each a
combinatorial interpretation it currently may lack, but this is the "trivial"
vein (immediate from the tower decomposition).

## Vein 3 — the even-parity count F(w,h)  [one real match, rest new]

**Height 2 is a genuine, non-obvious match:**

    F(w,2)   = A038505(w+1) = sum_k C(w+1, 2+4k)      (even blocks)
    odd(w,2) = A038503(w+1) - 1 = sum_{k>=1} C(w+1, 4k)  (odd blocks)
    total    = A000225(w) = 2^w - 1

A038505 = "sum of every 4th entry of row n, starting at binomial(n,2)";
A038503 = "… starting at n choose 0".  These are two of the four order-4
"hyperbolic" sequences {A038503, A038504, A038505, A000749}.  The height-2
castle count decomposes the Mersenne number 2^w-1 by block-count parity into
two of them.  This resolves the plan's flagged trap ("F(w,2) starts triangular
then diverges") — the truth is A038505, not A000217.

Proof of the identity: height-2 castles have blocks = 1 + (#runs of top cells),
and the number of width-w binary strings with exactly r runs of 1's is
C(w+1, 2r).  Even blocks <=> r odd <=> j = 2r ≡ 2 (mod 4).

**h >= 3 is apparently NEW** (no OEIS match), C-finite in w:
    F(w,3): order 6,  (x-3)(x-2)(x^2-x+2)(x^2-2x+2)
    F(w,4): order 9,  (x-4)(x-3) * P(3,·) * P(2,·)  [no cancellation]
    F(w,5): order 11
The `F(w,2)` case is order 4 (the hyperbolic recurrence); `F(w,3)` loses one
order because P(2,·) has x-2 as a factor, shared with 2^w.

**Columns (fixed w, varying h) are quasi-polynomials:** `F(w,h)` is annihilated
by `(x^2-1)^w`, i.e. `F(w,h) = P(h) + (-1)^h Q(h)` with P,Q polynomials of
degree < w.  (Observed: F(3,h) order 6, F(4,h) order 8, F(5,h) order 10.)

## Vein 4 — convex castles: binomial, NOT Catalan  [fork resolved]

A castle is convex iff its height profile is unimodal.  Verified:

    * every convex castle of height h has EXACTLY h blocks
      (#blocks = c_1 + sum of positive rises = peak = h for unimodal).
    * conversely #blocks >= h with equality iff convex, so convex castles
      are exactly the minimum-block castles.

Therefore the convex count (any parity) is binomial, not Catalan/Narayana:

    convex(w,h) = C(2h + w - 3, w - 1)
      h=2 -> C(w+1,2) = A000217 (triangular)
      h=3 -> C(w+3,4) = A000332 (pentatope, shifted)
      (generally a diagonal of A007318)

and the even-parity convex count = convex(w,h) if h even, else 0 (since every
convex castle has h blocks).  The "delightful Catalan find" of the plan's vein 4
does **not** materialise: the natural w/h parameterisation gives binomials.  A
Catalan/Narayana bridge would require an extra constraint the castle does not
impose (e.g. the ballot condition on the front boundary), so it is not free.

## Vein 7 — block-count distribution

Height-<=1 towers (binary strings), b = #runs of 1s:  count = C(w+1, 2b)
  = A034839 ("every other entry of each row of Pascal's triangle").
Height-2 castles, blocks = 1 + r:  count = C(w+1, 2r) (same binomial family).
For h >= 2 the full distribution is a new 2D table (no OEIS match); its first
(minimum) column is the convex count C(2h+w-3,w-1).

## Vein 8 — the odd-count complement

`odd(w,2) = A038503(w+1) - 1` (above).  For h >= 3 the odd rows are new:
`odd(w,3)` order 5, `odd(w,4)` order 9, `odd(w,5)` order 11.  No OEIS match.

## Vein 9 — castles by area (see `vein9-area.md`, `vein9_area.py`)

Re-indexing castles by area n = total cells (instead of by (w,h)) gives one clean
match and four new sequences:

* **conv(n) = A001523(n)** for n >= 1 (verified for n = 1..18).  A convex (unimodal)
  castle of area n is literally a weakly unimodal composition of n, which is A001523's
  own definition.  A001523 is dense; the PE 502 reading is a real synonym, not a
  novel formula.
* **all(n) = 2^(n-1)** (any composition of n is a castle shape; trivial).
* **even/odd/cev/cod by area** — four new sequences, none in OEIS on 18 terms.  The
  best relation to record on submission is `cev(n) + cod(n) = A001523(n)` — a parity
  refinement of a foundational sequence.
* Plan's guesses (A001168 convex polyominoes, A005435 column-convex by perimeter) are
  numerically far off; castles-by-area sit in the "stacks of boards" class, not the
  general polyomino class.

## Vein 9b — concave castles by area (see `vein9b-concave.md`, `vein9b_concave.py`)

The natural "concave" counterparts to convex castles, three readings:

* **valley(n) = A332578(n)** — valley-shaped castles = compositions of n whose
  negation is unimodal.  Mirror of A001523.
* **nonconv(n) = A115981(n)** — non-convex castles (has an interior dip) =
  "compositions not viewable as stacks" = A011782(n) − A001523(n).
* **strict_valley(n)** — castles with a true interior dip (valley AND not unimodal).
  **NEW sequence** (0,0,0,0,1,3,8,17,34,60,107,175,285,445,691,...).

The 6 parity-refined variants (`valley_even/odd`, `nc_even/odd`, `sv_even/odd`) are
all new; the first two pairs are parity splits of A332578 and A115981 respectively.

The (w, h) view is boring: `valley(w,h) = convex(w,h) = C(2h+w−3, w−1)`, same
binomial (different sets), so no new (w,h) OEIS matches drop out — but the exact
equinumeracy of valley and convex castles under a mirror is a candidate bijection
worth writing up.

## Summary of matches vs new

| Object | OEIS | Status |
|---|---|---|
| P(1,L) signed towers | A146559(L+1) | match (corrects plan's A009545) |
| P(1,L) imaginary companion | A009545 | match |
| any-parity height h | A000225, A001047, A005061, A005060, A005062 | match (trivial) |
| F(w,2) even castles h=2 | A038505(w+1) | match (real) |
| odd(w,2) odd castles h=2 | A038503(w+1)-1 | match (real) |
| convex(w,h) any parity | binomial C(2h+w-3,w-1) | match (binomial) |
| block dist h<=1 | A034839 | match (binomial) |
| convex castles by area | A001523(n) | match (real; dense entry) |
| all castles by area | A000079(n-1) | match (trivial) |
| valley castles by area | A332578(n) | match (real; dense entry) |
| non-convex castles by area | A115981(n) | match (= A011782 − A001523) |
| F(w,h), h>=3 (rows) | — | NEW (C-finite) |
| F(w,h), w>=3 (columns) | — | NEW (quasi-poly, (x^2-1)^w) |
| odd(w,h), h>=3 | — | NEW |
| block dist h>=2 | — | NEW |
| even/odd/cev/cod castles by area | — | NEW (cev+cod = A001523) |
| strict-valley castles by area | — | NEW (true interior dip) |
| parity splits of valley/nonconv/sv by area | — | NEW (6 sequences) |

## Method notes (interlinking discipline)

* Every accepted match above was checked against the actual OEIS data with
  offsets, not just the first few terms.  The plan's own "A009545" was caught
  this way (real vs imaginary).
* The false positives seen during search (A325842, A325668 "sqrt(5) difference
  sequences"; decimal-expansion/Collatz hits on short block distributions) were
  rejected — no reason behind them.
* The single highest-value new-interpretation targets are **A038505** and
  **A038503**: the height-2 castle is a clean, novel combinatorial
  interpretation for two of the four order-4 hyperbolic sequences.  Both are
  relatively isolated ("sum of every 4th entry"), so a cross-reference note is
  well-placed there.
