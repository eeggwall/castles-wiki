---
title: "A bijection between bargraphs and Dyck paths (Deutsch-Elizalde, 2017)"
category: Sources
summary: Deutsch and Elizalde map Dyck paths to bargraphs by reading the heights of a path's steps and turning each maximal run of c equal heights into floor(c/2) columns. The map does not preserve size; it sends semilength to semiperimeter minus peaks, so bargraphs with sp − pk = m are counted by the Catalan number C_m. Its recursive description (Prop. 3.5) sends uPd to the bargraph raised one row and inserts a height-1 column between concatenated factors of height at least 2, and Thm. 3.2(g) gives returns = height-1 columns + 1. On the castle side this carries the prime factorization of Dyck paths to the wiki's prime castles - prime Dyck paths of height at least 2 are exactly the castles with no height-1 column - and the one-peak column of the paper's Table 2 is the convex castles by semiperimeter, A001519.
tags: [paper, source, bargraph, dyck-path, bijection, catalan, peaks, semiperimeter, prime-castle, free-monoid, oeis]
sources: [deutsch-elizalde-2017-bargraphs-dyck-paths]
created: 2026-10-02
updated: 2026-10-02
---

# A bijection between bargraphs and Dyck paths (Deutsch-Elizalde, 2017)

**Source:** `raw/deutsch-elizalde-2017-bargraphs-dyck-paths.pdf` (text layer at `raw/deutsch-elizalde-2017-bargraphs-dyck-paths.txt`, extracted with `pdftotext -layout`; the PDF is git-ignored, the text is tracked). arXiv:1705.05984v1 [math.CO], 17 May 2017.[^1]
**Authors:** Emeric Deutsch (NYU Tandon), Sergi Elizalde (Dartmouth).[^1]
**Date ingested:** 2026-10-02
**Type:** paper (PDF, 7 pp.)

## Summary

A bargraph is a lattice path with steps `U`, `H`, `D` from the origin back to the `x`-axis, strictly above it in between, with no `UD` or `DU`; read by the heights of its `H` steps it is a composition.[^2] That is the castle ([[castle-polyomino](pages/castle-polyomino.md)]). Its semiperimeter `sp = #U + #H` is the castle's width plus blocks ([[castle-perimeter](pages/castle-perimeter.md)]), and a peak of a bargraph is an occurrence of `U H^ℓ D`, a plateau higher than both its neighbours.[^3]

The bijection `φ` goes from Dyck paths to bargraphs. Give each step of a Dyck path the height of its highest point, and turn each maximal run of `c` equal heights `h` into `⌊c/2⌋` columns of height `h`.[^4] The paper's example is the height sequence `1111123333222233332221111221`, which gives the castle `(1,1,3,3,2,2,3,3,2,1,1,2)`. The map does not preserve size. Instead the semilength of the path is the bargraph's semiperimeter minus its peaks (Thm. 3.2(a)), so the bargraphs with `sp − pk = m` are counted by the Catalan number `C_m` (Cor. 3.3). Section 4 proves the same count from the peak-and-semiperimeter generating function.[^5]

Section 3 also tracks returns, height, initial and final runs, and sums of peak and valley heights through `φ` (Thm. 3.2), and gives a recursive description of the map (Prop. 3.5). Elevating a path raises its bargraph by one row, `φ(uPd) = UBD`. Concatenating two paths concatenates their bargraphs, with a single height-1 column inserted between them when both have height at least 2.[^6] A Dyck path's returns to the axis are one more than its bargraph's height-1 columns, except at height 1 (Thm. 3.2(g)).[^7]

## Key Takeaways

- **Dyck-path primes become the wiki's prime castles.** Dyck paths form a free monoid under concatenation, and its primes in the sense of Gessel and Li are the paths `uPd` that return to the axis only at the end. A path's returns are its prime factors. By Prop. 3.5(i), a prime `uPd` with `P` nonempty maps to a bargraph raised one row, which has no height-1 column. By Thm. 3.2(g), a path of height at least 2 with `r` prime factors maps to a castle with `r − 1` height-1 columns. So `φ` sends the prime Dyck paths of height at least 2 onto the castles with no height-1 column, and the factor count of a path equals the factor count of its castle on [[prime-castles](pages/prime-castles.md)] (height-1 columns plus one). Own reasoning from Prop. 3.5 and Thm. 3.2(g), checked on every Dyck path of semilength up to 11.[^8]
- **The castle's area is not carried.** Since `φ` sends semilength to `sp − pk`, it matches the factorizations but not the area grading the prime-castle counts use.[^5]
- **A new Catalan reading of castles.** Castles with semiperimeter minus peaks equal to `m` number `C_m`: `1, 2, 5, 14, 42, 132` for `m = 1..6` (checked by brute force over castles).[^8] The table of castles by semiperimeter and peaks is OEIS A271940.[^9]
- **The one-peak column is the convex castles.** A castle with exactly one peak in the paper's sense is unimodal, so the first column of the paper's Table 2, `1, 2, 5, 13, 34, 89, 233, 610, …` for `sp = 2..9`, is the convex castles by semiperimeter, A001519 on [[convex-castle](pages/convex-castle.md)] and [[castle-perimeter](pages/castle-perimeter.md)]. Own reading, checked by brute force.[^8]
- **"Peak" collides.** Here a peak is `U H^ℓ D`, a local-maximum plateau. On [[castle-foata-transform](pages/castle-foata-transform.md)] a peak is a maximal run of columns of height at least 2. The castle `(2, 3, 2)` has one of each, but `(3, 2, 3)` has two bargraph peaks and one Foata peak. Recorded on [[castle-notation](pages/castle-notation.md)].

## Entities & Concepts

- [[prime-castles](pages/prime-castles.md)] - the free monoid whose factorization `φ` carries from Dyck paths.
- [[castle-polyomino](pages/castle-polyomino.md)] - castles are bargraphs.
- [[castle-perimeter](pages/castle-perimeter.md)] - semiperimeter `= w + #blocks`.
- [[dyck-words](pages/dyck-words.md)], [[catalan-numbers](pages/catalan-numbers.md)] - the Dyck side and the count `C_m`.
- [[convex-castle](pages/convex-castle.md)] - the one-peak castles.
- [[castle-foata-transform](pages/castle-foata-transform.md)] - the other meaning of "peak".

## Relation to Other Wiki Pages

- [[deutsch-elizalde-2016-bargraphs-cornerless-motzkin](pages/deutsch-elizalde-2016-bargraphs-cornerless-motzkin.md)] - the same authors' earlier bijection to cornerless Motzkin paths (reference [7] of this paper), which keeps semiperimeter up to a shift of one. Its least-column-height bijection at `h = 1` is the row-raising map, the same raising as Prop. 3.5(i) here.
- [[prime-castles](pages/prime-castles.md)] - the prime castles are the image of the prime Dyck paths of height at least 2.
- [[castle-perimeter](pages/castle-perimeter.md)] - A082582 (castles by semiperimeter) and A271942 (by semiperimeter and width) are the row sums and another refinement of the same objects as A271940 here.

## Footnotes

[^1]: [[deutsch-elizalde-2017-bargraphs-dyck-paths](pages/deutsch-elizalde-2017-bargraphs-dyck-paths.md)] title block L1-6 - "A bijection between bargraphs and Dyck paths", "Emeric Deutsch∗ Sergi Elizalde†", "arXiv:1705.05984v1 [math.CO] 17 May 2017".
[^2]: [[deutsch-elizalde-2017-bargraphs-dyck-paths](pages/deutsch-elizalde-2017-bargraphs-dyck-paths.md)] §1 L25-30 - "A bargraph is a lattice path with steps U = (0, 1), H = (1, 0) and D = (0, −1) that starts at the origin and ends on the x-axis, stays strictly above the x-axis everywhere except at the endpoints, and has no pair of consecutive steps of the form U D or DU"; "thus interpreting the bargraph as a composition".
[^3]: [[deutsch-elizalde-2017-bargraphs-dyck-paths](pages/deutsch-elizalde-2017-bargraphs-dyck-paths.md)] §1 L39-40, §3 L119 - "The semiperimeter of a bargraph B is defined as the number of U steps plus the number of H steps"; "A peak (resp. valley) in a bargraph is an occurrence of U H ℓ D (resp. DH ℓ U ) for some ℓ ≥ 1."
[^4]: [[deutsch-elizalde-2017-bargraphs-dyck-paths](pages/deutsch-elizalde-2017-bargraphs-dyck-paths.md)] §2 L67-74 - "define the height of each step of P as the y-coordinate of its highest point ... turn each maximal block of c consecutive letters h into ⌊ 2c ⌋ columns of height h"; "height sequence 1111123333222233332221111221, and thus its corresponding bargraph has column heights 113322332112."
[^5]: [[deutsch-elizalde-2017-bargraphs-dyck-paths](pages/deutsch-elizalde-2017-bargraphs-dyck-paths.md)] §1 L58-60, §3 L155, L219-220, §4 L272-291 [synthesis] - the bijection "does not preserve 'size'"; Thm. 3.2(a) "sl(P) = sp(B) − pk(B)"; Cor. 3.3 "|{B ∈ B : sp(B) − pk(B) = m}| = Cm"; the generating-function proof via `G(t, z)` and `H(t, 1)`.
[^6]: [[deutsch-elizalde-2017-bargraphs-dyck-paths](pages/deutsch-elizalde-2017-bargraphs-dyck-paths.md)] §3 L236-245 - "the path U BD is the bargraph whose height sequence is obtained by adding one to each entry of the height sequence of B"; "B ◦ B ′ denotes the concatenation of B and B ′ viewed as height sequences. Let 1 denote the bargraph consisting of one column of height 1"; Prop. 3.5 "(i) φ(uP d) = U BD", "(ii) φ(P P ′ ) = B ◦ 1 ◦ B′ if height(P ) ≥ 2 and height(P ′ ) ≥ 2, B ◦ B′ otherwise."
[^7]: [[deutsch-elizalde-2017-bargraphs-dyck-paths](pages/deutsch-elizalde-2017-bargraphs-dyck-paths.md)] §3 L123-124, L167 - "#H1 (B) the number of H steps of B at height 1 (equivalently, number of columns of B of height 1)"; "(g) ret(P ) = #H1 (B) + 1 (unless P and B have height 1, in which case ret(P ) = #H1 (B))."
[^8]: Verified by execution (Python 3, 2026-10-02): `φ` implemented from the definition and applied to every Dyck path of semilength `≤ 11`. It is injective, satisfies `sl(P) = sp − pk` and `φ(uPd) = ` the raised bargraph, sends every path with one return and semilength `≥ 2` to a castle with no height-1 column and every such castle back to a one-return path, and gives returns `=` height-1 columns `+ 1` at height `≥ 2`. Over all castles enumerated by semiperimeter, those with `sp − pk = m` number `1, 2, 5, 14, 42, 132` for `m = 1..6`, and those with one bargraph peak number `1, 2, 5, 13, 34, 89, 233, 610` for `sp = 2..9`. The free-monoid sense of "prime" is Gessel and Li's: https://cs.uwaterloo.ca/journals/JIS/VOL16/Gessel/gessel6.pdf p.3 - "if M is a free monoid, then there exists a subset P of M such that every element of M has a unique factorization as a product of elements of P. We call P the set of primes of M."
[^9]: [[deutsch-elizalde-2017-bargraphs-dyck-paths](pages/deutsch-elizalde-2017-bargraphs-dyck-paths.md)] §3 L231-234 - "Table 2 displays the number of bargraphs with a given semiperimeter (up to 12) and a given number of peaks. Corollary 3.3 states that the diagonal sums of this table (which is the triangular sequence [9, A271940]) are the Catalan numbers."
