# Cross-link submission menu (PE 502 castles -> existing A-numbers)

Ranked list of existing-A-number cross-links, each with the interpretation and what to
add.  Every identity below is verified against the OEIS data (offsets included) or against
brute force.  These are the *interlinking* actions; the *generation* actions (new sequences)
are listed separately at the bottom.

---

## Tier 1 — isolated entries, cleanest interpretations (submit first)

### 1. A038505 — "sum of every 4th entry, starting at binomial(n,2)"
- **Interpretation:** a(n) = number of castles (PE 502) of width n−1 and height exactly 2
  with an even number of blocks, for n ≥ 2.
- **Add:** Comment (see `oeis-xref-draft.md`), Formula `a(n) = F(n−1,2)`, and
  `Cf. A000225` (total, currently missing).
- **Value:** high — sparse "sum every 4th entry" entry, genuinely new geometric reading.

### 2. A038503 — "sum of every 4th entry, starting at n choose 0"
- **Interpretation:** a(n) = 1 + (number of castles of width n−1 and height 2 with an odd
  number of blocks); the +1 is the all-height-1 castle (height 1, not 2).
- **Add:** Comment, Formula `a(n) = odd(n−1,2) + 1`, `Cf. A000225`.
- **Value:** high — same family, complementary half.

### 3. A146559 — "expansion of (1−x)/(1−2x+2x²)" = Re((1+i)^n)
- **Interpretation:** a(n) = P(1, n−1) = the signed tower count (sum of (−1)^#blocks over
  height-≤1 towers of width n−1); i.e. the real part of (1+i)^n is a signed castle count.
- **Add:** Comment, plus a genuinely new Formula linking it to the hyperbolic family:
  `a(n) = A038503(n) − A038505(n)` (verified: Re((1+i)^n) = Σ_{j≡0} − Σ_{j≡2} binomial).
- **Value:** high — ties the "signed count" vein (plan vein 1) to the height-2 win.

---

## Tier 2 — the tower/heap = Narayana-polynomial finding (new, geometric)

A **tower** of width w is column heights `c_1..c_w >= 0` (no full-bottom-row, no max-height,
no parity).  Blocks are maximal horizontal runs, `#blocks = c_1 + sum max(0, c_i − c_{i−1})`.
This is Viennot's "heap of pieces": stack unit-height segments on w columns, each segment
resting on the one below, segments in the same row separated by a gap.

**Result (verified for w = 1..7 against brute force):**

    T(w,b) = # towers of width w with exactly b blocks
           = sum_{k=1..w} Narayana(w,k) * C(b + w − k, w − 1)        (Narayana-polynomial g.f.)
    g.f.   = (Narayana_w(x)) / (1 − x)^w,   Narayana_w(x) = sum_k Narayana(w,k) x^{k−1}.

Narayana(w,k) = (1/w) C(w,k) C(w,k−1) = **A001263**.  Concretely the rows hit:

| width w | T(w,b) for b = 0,1,2,3,… | OEIS |
|---|---|---|
| 2 | 1, 3, 5, 7, 9, 11, … | A005408 (odd numbers) |
| 3 | 1, 6, 16, 31, 51, 76, … | A005891 (centered pentagonal) |
| 4 | 1, 10, 40, 105, 219, 396, … | A063490 |
| 5 | 1, 15, 85, 295, 771, 1681, … | A160747 |
| 6 | 1, 21, 161, 721, 2331, 6083, … | **new** |
| 7 | 1, 28, 280, 1582, 6244, 19348, … | **new** |

Cross-link actions:
- **4. A005408, A005891, A063490, A160747** — add the heap/tower interpretation:
  "a(n) is also the number of towers (heaps of unit-height segments) on w columns with n
  blocks" (w = 2,3,4,5 respectively), plus the Narayana-polynomial formula.
- **5. A001263 (Narayana)** — add a Formula: the tower block-count generating function has
  the Narayana polynomial as its numerator, i.e. T(w,b) = Σ_k N(w,k) C(b+w−k, w−1).

This is the Catalan/Narayana connection the plan's vein 4 wanted — it lives in the *tower*
block-count (vein 6/7), not the convex count (which is binomial).

---

## Tier 3 — trivial but legitimate (the "any parity" vein)

### 6. A000225, A001047, A005061, A005060, A005062, …
- **Interpretation:** h^w − (h−1)^w = number of castles of width w and height exactly h
  (any number of blocks), i.e. the total before the parity filter.
- **Add:** one Comment each ("also the number of castles of width w, height h").
- **Value:** low-moderate — immediate from the tower decomposition, but still a real,
  previously-unstated interpretation; good filler submissions.

### 7. A001523 — stacks / weakly unimodal compositions of n
- **Interpretation:** a(n) = number of convex (unimodal) castles of area n, for n ≥ 1.
  A convex castle of area n is literally a weakly unimodal composition of n, which is
  this entry's own definition — so the identification is definitional, not new theory.
- **Add:** one Comment plus a `Cf. A038505, A038503, A146559` xref.
  Draft in `xrefs/A001523-castle.md`.
- **Value:** low — A001523 is dense (stacks, unimodal compositions, plane partitions
  containing a 1); the PE 502 reading is a real synonym but does not need another.

### 8. A332578 — compositions of n with unimodal negation (valley-shaped castles)
- **Interpretation:** a(n) = number of valley-shaped castles of area n, for n ≥ 1
  (mirror of A001523).  Draft in `xrefs/A332578-castle.md`.
- **Value:** low — dense entry; the PE 502 wording is a synonym in its already-
  documented "negation-unimodal" cluster.

### 9. A115981 — compositions of n not viewable as stacks (non-convex castles)
- **Interpretation:** a(n) = number of non-convex castles of area n, for n ≥ 1
  (complement of A001523; the entry already gives the formula
  `A011782(n) − A001523(n)`).  Draft in `xrefs/A115981-castle.md`.
- **Value:** low — same tier as A001523/A332578.

---

## Generation material (separate from interlinking)

- **`F(w,h)` even-parity, h ≥ 3** — new (C-finite; `F(w,3)` drafted in `new-sequence-F3.md`).
- **`F_odd(w,h)` h ≥ 3** — new.
- **`P(k,L)` signed towers, k ≥ 2** — new C-finite family (P(2,·): 1,3,9,19,33,59,… order 3;
  P(4,·): 1,5,25,85,225,541,… order 5), generalizing A146559.
- **`T(w,b)` tower block-count, w ≥ 6** — new rows of the Narayana-polynomial triangle.
- **castles by area, parity-refined** (vein 9, see `vein9-area.md`): four new sequences,
  even/odd/cev/cod, satisfying `even + odd = 2^(n-1)` and `cev + cod = A001523(n)`.
  The `cev + cod = A001523` relation is the quotable one: a parity refinement of a
  foundational sequence.
- **strict-valley castles by area** (vein 9b, see `vein9b-concave.md`): castles with a
  true interior dip. `0,0,0,0,1,3,8,17,34,60,107,175,285,445,691,...` — new, no OEIS
  match on 15 terms.
- **concave castles by area, parity-refined** (vein 9b): six new sequences —
  `valley_even/odd`, `nc_even/odd`, `sv_even/odd` — the first two pairs are parity
  refinements of A332578 and A115981 respectively (the quotable relations).

## Suggested submission order

A038505 → A038503 → A146559 (tier 1, highest value, isolated), then the tower/heap
interpretations (tier 2), then the difference-of-powers fillers plus A001523 (tier 3).
New contributors are throttled to a few open drafts, so lead with tier 1.
