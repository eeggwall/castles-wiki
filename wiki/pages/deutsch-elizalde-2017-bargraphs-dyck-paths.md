---
title: "A bijection between bargraphs and Dyck paths (Deutsch-Elizalde, 2017)"
category: Sources
summary: Deutsch and Elizalde map Dyck paths to bargraphs by giving each step the height of its highest point and turning each maximal run of c equal heights into floor(c/2) columns. The map sends semilength to semiperimeter minus peaks (Thm. 3.2(a)), so the bargraphs with sp − pk = m are counted by the Catalan number C_m (Cor. 3.3), and returns to the number of height-1 columns plus one at height at least 2 (Thm. 3.2(g)). Its recursive description (Prop. 3.5) sends uPd to the bargraph raised one row and inserts a height-1 column between concatenated factors of height at least 2. On the castle side, the prime Dyck paths of height at least 2 correspond to the castles with no height-1 column, the primes of the wiki's castle monoid, and the one-peak column of Table 2 is the convex castles by semiperimeter, A001519(sp − 1).
tags: [paper, source, bargraph, dyck-path, bijection, catalan, peaks, semiperimeter, prime-castle, free-monoid, oeis]
sources: [deutsch-elizalde-2017-bargraphs-dyck-paths]
created: 2026-10-02
updated: 2026-10-16
---

# A bijection between bargraphs and Dyck paths (Deutsch-Elizalde, 2017)

**Source:** `raw/deutsch-elizalde-2017-bargraphs-dyck-paths.pdf` (text layer at `raw/deutsch-elizalde-2017-bargraphs-dyck-paths.txt`, extracted with `pdftotext -layout`; the PDF is git-ignored, the text is tracked). arXiv:1705.05984v1 [math.CO], 17 May 2017.[^1]
**Authors:** Emeric Deutsch (NYU Tandon), Sergi Elizalde (Dartmouth).[^1]
**Date ingested:** 2026-10-02
**Type:** paper (PDF, 7 pp.)

## Summary

A bargraph is a lattice path with steps `U = (0, 1)`, `H = (1, 0)` and `D = (0, −1)` from the origin back to the `x`-axis, strictly above it in between, with no factor `UD` or `DU`; read by the heights of its `H` steps it is a composition.[^2] So a bargraph is a castle ([[castle-polyomino](pages/castle-polyomino.md)]). Its semiperimeter `sp = #U + #H` is the castle's width plus its number of blocks ([[castle-perimeter](pages/castle-perimeter.md)]), and a peak of a bargraph is a factor `U H^ℓ D`, a plateau higher than both its neighbors.[^3]

The bijection `φ` goes from Dyck paths to bargraphs. Give each step of a Dyck path the height of its highest point, and turn each maximal run of `c` equal heights `h` into `⌊c/2⌋` columns of height `h`.[^4] The paper's example is the height sequence `1111123333222233332221111221`, which gives the castle `(1, 1, 3, 3, 2, 2, 3, 3, 2, 1, 1, 2)`. The map does not preserve size: the semilength of the path is the bargraph's semiperimeter minus its peaks, `sl(P) = sp(B) − pk(B)` (Thm. 3.2(a)), so the bargraphs with `sp − pk = m` are counted by the Catalan number `C_m` (Cor. 3.3). Section 4 proves the same count from the generating function by peaks and semiperimeter.[^5]

Theorem 3.2 also tracks returns, height, the initial and final runs, and the sums of peak and valley heights. Proposition 3.5 describes `φ` recursively. Elevating a path raises its bargraph by one row, `φ(uPd) = UBD`, where `B = φ(P)`. Concatenating two paths concatenates their bargraphs, with a single height-1 column inserted between them when both have height at least 2.[^6] The returns of a Dyck path to the axis number one more than the height-1 columns of its bargraph, except at height 1 (Thm. 3.2(g)).[^7]

## Key Takeaways

- **Prime Dyck paths and prime castles.** Dyck paths form a free monoid under concatenation, and its primes, in Gessel and Li's sense,[^8] are the paths `uPd` that return to the axis only at the end; the number of prime factors of a path is its number of returns. By Prop. 3.5(i), a prime `uPd` with `P` nonempty maps to the bargraph `φ(P)` raised one row, which has no height-1 column. Conversely, a castle `C` with no height-1 column is a castle `B` raised one row, and `C = φ(u φ^{−1}(B) d)`. So `φ` maps the prime Dyck paths of height at least 2 one-to-one onto the castles with no height-1 column, the primes of [[prime-castles](pages/prime-castles.md)]. By Thm. 3.2(g), a path of height at least 2 with `r` prime factors maps to a castle with `r − 1` height-1 columns, whose padded form `(1, C, 1)` has `r` prime factors in the monoid of [[prime-castles](pages/prime-castles.md)]. Both statements are derived here from Prop. 3.5 and Thm. 3.2(g), and checked on every Dyck path of semilength at most 11.[^9]
- **Area is not carried.** `φ` sends semilength to `sp − pk`, so it matches the two factorizations but not the area grading that the prime-castle counts use.[^5]
- **A Catalan count of castles.** The castles with semiperimeter minus bargraph peaks equal to `m` number `C_m`: `1, 2, 5, 14, 42, 132, 429` for `m = 1, …, 7`.[^9] The table of castles by semiperimeter and peaks is `A271940`, "the number of bargraphs of semiperimeter n having k peaks".[^10]
- **The one-peak column is the convex castles.** A castle has exactly one bargraph peak exactly when its skyline is unimodal: a skyline that falls and later rises has a peak on each side of the low point, and in a unimodal skyline every plateau other than the top one has a higher neighbor. So the first column of the paper's Table 2, `1, 2, 5, 13, 34, 89, 233, 610, …` for `sp = 2, …, 9`, is the convex castles by semiperimeter, `A001519(sp − 1)` ([[convex-castle](pages/convex-castle.md)], [[castle-perimeter](pages/castle-perimeter.md)]).[^9][^10]
- **"Peak" has two meanings on the wiki.** Here a peak is `U H^ℓ D`, a plateau higher than both its neighbors. On [[castle-foata-transform](pages/castle-foata-transform.md)] a peak is a maximal run of columns of height at least 2. The castle `(2, 3, 2)` has one of each; the castle `(3, 2, 3)` has two bargraph peaks and one run of columns of height at least 2. [[castle-notation](pages/castle-notation.md)] records both.

## Entities & Concepts

- [[prime-castles](pages/prime-castles.md)] - the free monoid of castles, whose primes `φ` matches with the prime Dyck paths of height at least 2.
- [[castle-polyomino](pages/castle-polyomino.md)] - the castles, which are the bargraphs.
- [[castle-perimeter](pages/castle-perimeter.md)] - the semiperimeter `w + #blocks`.
- [[dyck-words](pages/dyck-words.md)], [[catalan-numbers](pages/catalan-numbers.md)] - the Dyck paths and the count `C_m`.
- [[convex-castle](pages/convex-castle.md)] - the castles with one bargraph peak.
- [[castle-foata-transform](pages/castle-foata-transform.md)] - the other meaning of "peak".

## Relation to Other Wiki Pages

- [[deutsch-elizalde-2016-bargraphs-cornerless-motzkin](pages/deutsch-elizalde-2016-bargraphs-cornerless-motzkin.md)] - the same authors' bijection to cornerless Motzkin paths (reference [7] of this paper), which sends paths with `#U + #H = n − 1` to bargraphs of semiperimeter `n`. Its one-row deletion at `h = 1` removes the bottom row of a castle with no height-1 column, the inverse of the raising in Prop. 3.5(i).
- [[prime-castles](pages/prime-castles.md)] - the prime castles, the image of the prime Dyck paths of height at least 2.
- [[castle-perimeter](pages/castle-perimeter.md)] - `A082582`, the castles by semiperimeter, the row sums of `A271940`, and `A271942`, the castles by semiperimeter and width.

## Footnotes

[^1]: [[deutsch-elizalde-2017-bargraphs-dyck-paths](pages/deutsch-elizalde-2017-bargraphs-dyck-paths.md)] title block L1-6 - "A bijection between bargraphs and Dyck paths", "Emeric Deutsch∗ Sergi Elizalde†", "arXiv:1705.05984v1 [math.CO] 17 May 2017".
[^2]: [[deutsch-elizalde-2017-bargraphs-dyck-paths](pages/deutsch-elizalde-2017-bargraphs-dyck-paths.md)] §1 L25-30 - "A bargraph is a lattice path with steps U = (0, 1), H = (1, 0) and D = (0, −1) that starts at the origin and ends on the x-axis, stays strictly above the x-axis everywhere except at the endpoints, and has no pair of consecutive steps of the form U D or DU"; "bargraph as a composition".
[^3]: [[deutsch-elizalde-2017-bargraphs-dyck-paths](pages/deutsch-elizalde-2017-bargraphs-dyck-paths.md)] §1 L39-40, §3 L119 - "The semiperimeter of a bargraph B is defined as the number of U steps plus the number of H steps, and denoted by sp(B)"; "A peak (resp. valley) in a bargraph is an occurrence of U H ℓ D (resp. DH ℓ U ) for some ℓ ≥ 1."
[^4]: [[deutsch-elizalde-2017-bargraphs-dyck-paths](pages/deutsch-elizalde-2017-bargraphs-dyck-paths.md)] §2 L67-74 - "define the height of each step of P as the y-coordinate of its highest point ... turn each maximal block of c consecutive letters h into ⌊ 2c ⌋ columns of height h"; "height sequence 1111123333222233332221111221, and thus its corresponding bargraph has column heights 113322332112."
[^5]: [[deutsch-elizalde-2017-bargraphs-dyck-paths](pages/deutsch-elizalde-2017-bargraphs-dyck-paths.md)] §1 L58-60, §3 L155, L219-220, §4 L272-291 [synthesis] - the bijection does not preserve "size"; Thm. 3.2(a) "sl(P) = sp(B) − pk(B)"; Cor. 3.3 "|{B ∈ B : sp(B) − pk(B) = m}| = Cm"; the generating-function proof of Cor. 3.3.
[^6]: [[deutsch-elizalde-2017-bargraphs-dyck-paths](pages/deutsch-elizalde-2017-bargraphs-dyck-paths.md)] §3 L236-245 - "the path U BD is the bargraph whose height sequence is obtained by adding one to each entry of the height sequence of B"; "B ◦ B′ denotes the concatenation of B and B′ viewed as height sequences. Let 1 denote the bargraph consisting of one column of height 1"; Prop. 3.5 "(i) φ(uP d) = U BD", "(ii) φ(P P′) = B ◦ 1 ◦ B′ if height(P) ≥ 2 and height(P′) ≥ 2, B ◦ B′ otherwise."
[^7]: [[deutsch-elizalde-2017-bargraphs-dyck-paths](pages/deutsch-elizalde-2017-bargraphs-dyck-paths.md)] §3 L123-124, L167 - "#H1 (B) the number of H steps of B at height 1 (equivalently, number of columns of B of height 1)"; "(g) ret(P) = #H1 (B) + 1 (unless P and B have height 1, in which case ret(P) = #H1 (B))."
[^8]: https://cs.uwaterloo.ca/journals/JIS/VOL16/Gessel/gessel6.pdf p.3 - "if M is a free monoid, then there exists a subset P of M such that every element of M has a unique factorization as a product of elements of P. We call P the set of primes of M."
[^9]: Verified by execution (Python 3.11, 2026-10-16): `φ` implemented from its definition and applied to every Dyck path of semilength at most 11; it is injective, satisfies `sl(P) = sp − pk`, reproduces the paper's example, and at height at least 2 gives returns `=` height-1 columns `+ 1`, with one return exactly when the castle has no height-1 column. Over all castles of semiperimeter at most 12, enumerated directly, the counts by semiperimeter and bargraph peaks equal every entry of Table 2 (L248-259), the castles with `sp − pk = m` number `1, 2, 5, 14, 42, 132, 429` for `m ≤ 7`, and those with one bargraph peak number `1, 2, 5, 13, 34, 89, 233, 610, 1597, 4181, 10946` for `sp = 2, …, 12`.
[^10]: [[deutsch-elizalde-2017-bargraphs-dyck-paths](pages/deutsch-elizalde-2017-bargraphs-dyck-paths.md)] §3 L231-234, L248-262 - "Table 2 displays the number of bargraphs with a given semiperimeter (up to 12) and a given number of peaks. Corollary 3.3 states that the diagonal sums of this table (which is the triangular sequence [9, A271940]) are the Catalan numbers", and Table 2 itself; https://oeis.org/A271940 and https://oeis.org/A001519 (read 2026-10-16) - "Triangle read by rows: T(n,k) is the number of bargraphs of semiperimeter n having k peaks (n >= 2, k >= 1)" and "a(n) = 3*a(n-1) - a(n-2) for n >= 2, with a(0) = a(1) = 1".
