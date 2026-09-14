# The binomial connection: convex castles and a generalized Vandermonde identity

This resolves plan vein 4 (the "binomial vs Catalan/Narayana" fork) and gives the
*reason* behind the binomial count.  The short answer: **the convex-castle count is a
binomial coefficient, and it is a binomial because the two halves of a convex castle
(its ascending front and its descending back) are chosen independently — there is no
ballot / non-crossing condition to push it into Catalan territory.**

Everything below is verified numerically (see `castle.py`; the up/down decomposition and
the Vandermonde identity were each checked against brute force for `w,h <= 7`).

---

## 1. Convex ⟺ unimodal ⟺ exactly `h` blocks

A castle is *convex* (both row- and column-convex) precisely when its height profile
`c_1..c_w` is unimodal (non-decreasing then non-increasing): the columns reaching level
`r` form the interval `{i : c_i >= r}`, and that set is an interval for every `r` iff the
profile is unimodal.

For **any** profile, `#blocks = c_1 + sum_{i>=2} max(0, c_i - c_{i-1})` (each column
contributes the number of runs it *starts*).  The sum of positive rises telescopes to the
running maximum, so

    #blocks >= max(c) = h,   with equality  iff  the profile is unimodal.

Hence **a convex castle of height h has exactly h blocks**, and convex castles are exactly
the minimum-block castles of height h.  (In particular the even-parity convex count is
`C(2h+w-3, w-1)` when `h` is even and `0` when `h` is odd — every convex castle has h
blocks.)

So counting convex castles of width `w`, height exactly `h` = counting unimodal sequences
in `{1..h}^w` with maximum `h`.

## 2. The up/down decomposition

Fix `p` = the leftmost column of height `h` (the first peak).  A unimodal profile splits
at `p` into two independent pieces:

* **Front (ascending):** `c_1 <= c_2 <= ... <= c_{p-1} <= h-1`, a non-decreasing sequence
  of length `p-1` with values in `{1..h-1}`.  Number of these is

      C((p-1) + (h-1) - 1,  p-1)  =  C(p + h - 3, p - 1)  =  C((h-2) + (p-1), p-1).

* **Back (descending):** `c_p = h >= c_{p+1} >= ... >= c_w`, a non-increasing sequence of
  length `w-p` with values in `{1..h}`.  Reversing it, this is a non-decreasing sequence,
  so its count is

      C((w-p) + h - 1, w-p)  =  C(w-p + h - 1, w-p)  =  C((h-1) + (w-p), w-p).

These are independent choices (any front pairs with any back), so

    convex(w,h)  =  sum_{p=1}^{w}  C((h-2) + (p-1), p-1) · C((h-1) + (w-p), w-p).

Note the *off-by-one in the two upper parameters*: `h-2` for the front (its entries live in
`{1..h-1}`, one value short of the peak) and `h-1` for the back (its entries live in
`{1..h}`, and the peak belongs to the back).  That asymmetry is the whole story.

**Worked example, `w = 4, h = 2`:** fronts are all-`1` (one choice each), and the back is a
non-increasing `{1,2}`-sequence of length `4-p`.  `p=1,2,3,4` give `4,3,2,1` backs, total
`4+3+2+1 = 10 = C(5,3) = C(2h+w-3, w-1)`.  (This is why convex castles of height 2 are the
triangular numbers `C(w+1,2)`.)

## 3. The generalized Vandermonde identity closes the sum

Substitute `a = p-1` (ranging `0..w-1`) and `n = w-1`:

    convex(w,h) = sum_{a=0}^{n} C((h-2)+a, a) · C((h-1)+(n-a), n-a).

This is the generalized Vandermonde convolution

    sum_{k=0}^{n} C(r+k, k) · C(s+n-k, n-k)  =  C(r+s+n+1, n),

with `r = h-2`, `s = h-1`, `n = w-1`.  (Proof: `sum_k C(r+k,k) x^k = (1-x)^{-(r+1)}`, so
the product of the two generating functions is `(1-x)^{-(r+s+2)}`, whose coefficient of
`x^n` is `C(r+s+n+1, n)`.)

Therefore

    convex(w,h) = C((h-2)+(h-1)+(w-1)+1, w-1)  =  C(2h + w - 3, w - 1).      ∎

## 4. Why binomial and not Catalan

The two halves are **independent**: the front is any non-decreasing sequence, the back any
non-increasing sequence, and they are combined by an ordinary product (then summed by
Vandermonde).  A binomial is exactly what a product of two monotone-piece counts gives.

Catalan / Narayana counts arise when a **non-crossing or ballot constraint couples the two
halves** — e.g. a Dyck path's ascending and descending segments must jointly stay above the
diagonal.  The castle's Rule 3 (gap between neighbouring same-row blocks) imposes no such
coupling: in the run decomposition it is automatic, so it neither constrains the front nor
ties the front to the back.

So the plan's hoped-for "delightful Catalan find" does not exist for the natural `(w,h)`
parameterisation; a Catalan/Narayana object would require grafting on an extra condition
(ballot, fixed peak/area, non-crossing) that the castle definition does not contain.

## 5. The same binomial theme elsewhere in the castle object

The binomial character is not isolated to convex castles — it runs through the whole object:

* **Height-2 block distribution.** A height-2 castle has `blocks = 1 + r` where `r` = number
  of runs of top cells; there are `C(w+1, 2r)` width-`w` binary strings with `r` runs of
  `1`s.  Splitting by the parity of `r` (equivalently `2r mod 4`) is exactly the split of
  row `w+1` of Pascal's triangle into its "2 mod 4" and "0 mod 4" parts:

      F(w,2)   (even blocks) = C(w+1,2) + C(w+1,6) + ... = A038505(w+1),
      odd(w,2) (odd  blocks) = C(w+1,4) + C(w+1,8) + ... = A038503(w+1) - 1.

* **Height-<=1 towers.** The block-count distribution over binary strings of length `w`
  is `C(w+1, 2b)` for `b` blocks = `A034839` ("every other entry of each row of Pascal's
  triangle").

* **Any-parity count.** `h^w - (h-1)^w` = the binomial-difference family `A000225`,
  `A001047`, `A005061`, `A005060`, `A005062`, ... (these come from summing tower counts over
  heights by inclusion–exclusion, another binomial mechanism).

No Catalan/Narayana/Motzkin number has yet surfaced in any of the natural `(w,h)`- or
`(w,blocks)`-parameterised castle counts.  The gap rule, the even-parity rule, and the
convex restriction all turn out to be *binomial* constraints.
