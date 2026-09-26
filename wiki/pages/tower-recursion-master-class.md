---
title: Tower recursion master class
category: Concepts
summary: The two ideas that solve the castle count — towers are independent (T(k,L) = (k+1)^L) and parity is a sign ((T±P)/2 splits even/odd) — taught end-to-end to the F(w,h) formula.
tags: [concept, castle, towers, parity, sign, pedagogy, dyck, teaching]
sources: [project-euler-502-solution, project-euler-502-representations, project-euler-502-castle-factoring, project-euler-502-observations]
created: 2026-09-14
updated: 2026-09-26
---

# Tower recursion master class

## The two ideas

The whole castle count — all the way to the closed form for `F(w,h)` — reduces to **two ideas**, each worth understanding on its own:

1. **Towers are independent.** A tower is nothing but its column heights, and every height is chosen independently — sibling sub-blocks never interact. This one fact turns the unsigned count into the trivial product `T(k,L) = (k+1)^L`.

2. **Parity is a sign.** Weight each block by −1; the signed count `P` then separates towers by block parity through the `(T ± P)/2` projector — exactly how a permutation's sign separates even from odd permutations.

Everything else is assembly. Learn these two, and the formula is the last five minutes.

## Idea 1 — Towers: T(k,L) = (k+1)^L

A **castle** is a full-width bottom block with a **tower** stacked on it. A tower of height ≤ *k* above a length-*L* block is fully described by its **column heights** `c_1…c_L`, where `c_i ∈ {0,…,k}` is how many blocks sit above the base in column *i* (the [[castle-representations](pages/castle-representations.md)] integer-tuple form). The `U`/`R`/`D` word is recovered invertibly from the heights, so heights and towers are the same object.[^1]

**The aha — independence.** Here is the fact the whole problem hangs on: the `c_i` are **independent**. No-overhang and the same-row gap rule are automatic consequences of reading a tower as a stack of maximal runs, so there is no constraint coupling one column's height to the next. Two sibling sub-blocks in the same row generate towers that never interact — "the single fact that makes the problem tractable, and it took years to see."[^2] Consequently:

```
T(k,L) = (k+1)^L      — L columns, each independently choosing one of k+1 heights.
```

**The precise proof — binary strings.** To make the independence airtight, peel the tower's bottom row off. Which columns carry a block in that row form a length-*L* **binary string** (1 = block, 0 = gap), and each **maximal run of 1s** is one sub-block; the no-adjacency rule is exactly "the runs are maximal."[^3] Above each sub-block of length *l* sits an *independent* tower of height ≤ *k*−1. So, counting over all binary strings *b*:[^4]

```
T(k,L) = ∑_b  ∏_{runs of length l in b} T(k−1, l)
       = ∑_b  ∏_{runs} k^l              (induction: T(k−1,l) = k^l)
       = ∑_b  k^{ones(b)} = ∑_{j=0}^{L} C(L,j) k^j = (1+k)^L.
```

Two readings of the same result: the product form (columns are independent) *is* the sub-block independence; the binary-string sum *proves* it by induction on the height. With `k = h−1` this gives the corollary `T(h−1,w) = h^w`, the number of towers of height ≤ *h*−1.[^4]

## Idea 2 — Parity signs: the even-block rule as a sign

The hard constraint is "an even number of blocks," and the trick is to encode it as a **sign**: weight each block by −1, i.e. each `D` step (one `D` completes one block). This is the castle analogue of the permutation sign `sgn(σ) = (−1)^{n−c}`:[^5]

```
s(C) = (−1)^{blocks(C)}.
```

Now define the **signed count** `P(k,L) = ∑_towers s(tower)`. Just as `(1 ± sgn)/2` projects a permutation onto its even/odd class, `(T ± P)/2` projects towers onto their parity class:[^6]

```
(T + P)/2 = even-block towers      (T − P)/2 = odd-block towers
```

with `T = T(k,L)` the unsigned total. The signed tower has a generating function one minus-sign away from the unsigned one — the peak `U V D` adds one block on top of `V`, so it flips the sign of everything inside:[^7]

```
P_k = 1 + x·P_k − (P_{k−1} − 1)(1 + x·P_k)      (P_0 = 1/(1−x))
```

which is the recursion behind `P` (its `num_k/den_k` form and C-finite recurrences are on [[castle-counting-formula](pages/castle-counting-formula.md)] and [[signed-tower-count](pages/signed-tower-count.md)]). The point for the master class is *why* `P` is the right object: it is the sign homomorphism, and the `(T ± P)/2` identity is the whole parity trick.

## The even and odd approaches

A full castle is `U (tower) D`, so its block count is the tower's plus one (the bottom block): **even total blocks ⟺ odd tower blocks**.[^8] So the even-block castles are the odd-block towers, and vice versa:

```
F(w,h)              = [ h^w − (h−1)^w − P(h−1,w) + P(h−2,w) ] / 2      (even blocks)
odd-block castles   = [ h^w − (h−1)^w + P(h−1,w) − P(h−2,w) ] / 2      (odd blocks)
```

The two differ only in the sign of the `P` terms, and they sum to the unsigned total `h^w − (h−1)^w` — the `P` terms cancel, which is the "almost the entire difficulty" observation: drop the parity clause and the answer is just `h^w − (h−1)^w`.[^9] The `h^w − (h−1)^w` subtracts off towers of height ≤ *h*−2, forcing height *exactly* *h*; the `−P(h−1,w) + P(h−2,w)` does the same subtraction at the signed level.

The master-class takeaway is that the technique is **symmetric**: the same sign machinery hands you the even count *and* the odd count for the price of one. Project Euler 502 (PE 502) asks for the even half; the odd half is free.

## Worked example: F(4,2) = 10

Towers of height ≤ 1 above a length-4 block are column heights `c ∈ {0,1}⁴`: `T(1,4) = 2⁴ = 16`. One of the 16 is the empty tower `(0,0,0,0)`, so **15 towers have height exactly 1** (`= 2⁴ − 1⁴`). Their signed count is `P(1,4) − P(0,4)`, and `P(0,4) = 1` (the empty tower has no blocks) while `P(1,4) = Re((1+i)⁵) = −4`, so the signed total is `−4 − 1 = −5`. Then:

```
(T − P)/2 = (15 − (−5))/2 = 10 = odd-block towers  = even-block castles F(4,2)
(T + P)/2 = (15 + (−5))/2 =  5 = even-block towers = odd-block castles
```

`10 + 5 = 15 = 2⁴ − 1⁴`, and `F(4,2) = 10` matches the known checkpoint (with `F(13,10)` and `F(10,13)` reproduced on [[castle-counting-formula](pages/castle-counting-formula.md)]).

## Appearances in Sources

- [[project-euler-502-solution](pages/project-euler-502-solution.md)] — the binary-string bijection and the `T(k,L)=(k+1)^L` induction.
- [[project-euler-502-representations](pages/project-euler-502-representations.md)] — the unsigned/signed generating functions and the `F(w,h)` formula.
- [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] — the column-height product form and the sign-homomorphism reading of `P`.
- [[project-euler-502-observations](pages/project-euler-502-observations.md)] — the sibling-independence crux and the "parity is almost the whole difficulty" point.

## Related Concepts

- [[castle-counting-formula](pages/castle-counting-formula.md)] — the reference derivation this page teaches.
- [[castle-sign](pages/castle-sign.md)] — the sign `s(C) = (−1)^{blocks}` and the `(T±P)/2` projector in full.
- [[parity-via-roots-of-unity](pages/parity-via-roots-of-unity.md)] — the sign generalized to block count mod m via m-th roots of unity.
- [[binary-string-bijection](pages/binary-string-bijection.md)] — the bijection that makes Idea 1 rigorous.
- [[generalized-dyck-grammar](pages/generalized-dyck-grammar.md)] — the grammar the two generating functions are read off.
- [[signed-tower-count](pages/signed-tower-count.md)] — the C-finite `P(k,L)` family.
- [[tower-parity-sectors](pages/tower-parity-sectors.md)] — the deep-analysis sibling: the sign homomorphism becomes a block diagonalization of the recursion into `(+1)` / `(−1)` sectors.
- [[tower-word-continued-fraction](pages/tower-word-continued-fraction.md)] — the analytical explanation of `T(k,L) = (k+1)^L`: it is the collapse of the Motzkin J-fraction under the no-UD / no-DU run constraint.
- [[castle-foata-transform](pages/castle-foata-transform.md)] — the permutation-analogy version of the "peak / tower atom" idea: peaks are maximal positive runs, records are their leftmost positive columns.
- [[castle-fibers-char-2-walkthrough](pages/castle-fibers-char-2-walkthrough.md)] - the companion seminar on the algebra side: one castle recurrence read through its fibers mod each prime.
- [[hardin-identity-seminar](pages/hardin-identity-seminar.md)] - the seminar on the signed tower count's even sector.


## Footnotes

[^1]: [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] §"A column-height factorization" L72-89 — "each c_i ranges independently over {0, …, k}, and the tower word is recovered by [the invertible procedure] ... T(k,L) = (k+1)^L."
[^2]: [[project-euler-502-observations](pages/project-euler-502-observations.md)] §"Sub-block independence" L5 — "Two sibling blocks in the same row generate towers that never interact ... This is the single fact that makes the problem tractable, and it took years to see."
[^3]: [[project-euler-502-solution](pages/project-euler-502-solution.md)] §"The binary-string bijection" L14-19 — "Configurations within a block of length L ... biject with binary strings of length L: map each string to the configuration whose sub-blocks are its maximal runs of 1s ... 2^L ... r maximal runs of 1s ... r sub-blocks."
[^4]: [[project-euler-502-solution](pages/project-euler-502-solution.md)] §"T(k, L) = (k+1)^L" L23-37 — "a length-L binary string ... plus, for each maximal run of length l, an independent tower of height ≤ k-1 ... T(k, L) = ∑_b ∏_{runs} T(k-1, l) = ∑_b k^{ones(b)} = (1 + k)^L. Corollary ... T(h-1, w) = h^w."
[^5]: [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] §"The sign of a castle" L92-101 — "sgn(σ) = (-1)^{n - c} ... Each block is an excursion atom (a U ... D pair), and each D move completes one block. Weight each block by -1 and define s(C) = (-1)^{blocks(C)}."
[^6]: [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] §"The sign of a castle" L116-123 — "(T + P)/2 = even-block castles, (T - P)/2 = odd-block castles ... exactly the (1 ± sgn)/2 trick."
[^7]: [[project-euler-502-representations](pages/project-euler-502-representations.md)] §"Signed count" L316-329 — "The even-block rule is the hard constraint, and it enters as a sign. Weight each block, that is each D, by -1 ... one minus sign on the peak ... P_k = 1 + x P_k - (P_{k-1} - 1)(1 + x P_k)".
[^8]: [[project-euler-502-representations](pages/project-euler-502-representations.md)] §"The main formula" L350 — "The full castle is U (tower) D, so its block count is the tower's block count plus one for the bottom block. Even total blocks means an odd number of blocks in the tower."
[^9]: [[project-euler-502-observations](pages/project-euler-502-observations.md)] §"The \"even number of blocks\" clause is almost the entire difficulty" L17 — "Without it, the answer is just h^w - (h-1)^w: all castles of height at most h minus those of height at most h-1."
