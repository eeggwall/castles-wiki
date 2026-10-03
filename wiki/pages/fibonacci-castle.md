---
title: Fibonacci castle
category: Concepts
summary: A Fibonacci castle is a castle of exact height 2 with no two adjacent height-2 columns (equivalently no 2×2 square; the tree castles of exact height 2). There are F_{w+2} − 1 of width w, from the transfer matrix [[1,1],[1,0]], growing like (φ²/√5)φ^w, so they are a golden width growth castle carrying log₂φ ≈ 0.694 bits per column (the golden mean shift). Counting them two ways gives Σ F_j = F_{w+2} − 1 and F_{a+b} = F_a F_{b+1} + F_{a−1} F_b, and weighting the columns by F_{w+1}, …, F_2 ranks them by Zeckendorf representation, a bijection onto 1, …, F_{w+2} − 1 in lexicographic order. A Fibonacci castle with m height-2 columns has m + 1 blocks, so the even-block count is (F_{w+2} − P_F(w))/2 with a parity term P_F of period 6 (1, 0, −1, −1, 0, 1), against a parity term of size 2^{w/2} for all castles of exact height 2. Neighbours - ridge castles of exact height 2 (swap 1 and 2, F_{w+2}), castles of exact height 2 by area (F_{n+1} − 1, a bijection onto Fibonacci castles of width n − 1), and prime castles.
tags: [concept, castle, castle-type, fibonacci, golden-ratio, transfer-matrix, zeckendorf, parity, blocks, golden-mean-shift, entropy, tree-castle, ridge-castle]
sources: [deutsch-elizalde-2017-bargraphs-dyck-paths]
created: 2026-10-03
updated: 2026-10-03
---

# Fibonacci castle

## Definition

A castle is a skyline `(c_1, …, c_w)` of columns standing on a full bottom row, built from blocks (maximal horizontal runs of cells in one row), with maximum height exactly `h`; PE 502 counts those with an even number of blocks.[^pe] As a lattice path it is a bargraph, and read by its column heights it is a composition ([[castle-polyomino](pages/castle-polyomino.md)]).[^bar]

A **Fibonacci castle** is a castle of exact height 2 in which no two adjacent columns both have height 2.

- **Equivalent forms.** No 2×2 square of cells, so a Fibonacci castle is a tree castle of exact height 2 ([[castle-graph](pages/castle-graph.md)]). Its second row is a set of isolated cells.
- **Construction rule.** Choose a nonempty set of column positions in `{1, …, w}` with no two adjacent, and raise exactly those columns to height 2.
- **Example.** `(2, 1, 2, 1, 1, 2)` is a Fibonacci castle of width 6. `(1, 2, 2, 1, 1, 1)` has exact height 2 but is not one: columns 2 and 3 form a 2×2 square.
- **Width 4.** The seven Fibonacci castles of width 4, in lexicographic order: `(1,1,1,2)`, `(1,1,2,1)`, `(1,2,1,1)`, `(1,2,1,2)`, `(2,1,1,1)`, `(2,1,1,2)`, `(2,1,2,1)`.

## Counting by width

Remove the bottom row. What is left is the second row, a string of 0s and 1s with no two adjacent 1s. There are `F_{n+2}` such strings of length `n` (`F_1 = F_2 = 1`): a string starts with 0 followed by any string of length `n − 1`, or with `1, 0` followed by any string of length `n − 2`, and the counts at `n = 0, 1` are `1, 2`. Every such string except the all-zero one is the second row of a Fibonacci castle; the all-zero string gives the flat row, which does not reach height 2. So

```
#{Fibonacci castles of width w}  =  F_{w+2} − 1.
```

The strings with no two adjacent 1s are the Zeckendorf subsets of `{1, …, n}` (subsets with no two consecutive elements), whose number `F_{n+2}` is classical.[^chu]

| `w` | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| castles of exact height 2, `2^w − 1` | 1 | 3 | 7 | 15 | 31 | 63 | 127 | 255 | 511 | 1023 | 2047 | 4095 |
| Fibonacci castles, `F_{w+2} − 1` | 1 | 2 | 4 | 7 | 12 | 20 | 33 | 54 | 88 | 143 | 232 | 376 |

The `−1` is the exact-height condition, the `h = 2` case of the `(h − 1)^w` in `h^w − (h − 1)^w`. The fraction of castles of exact height 2 that are Fibonacci castles falls like `(φ/2)^w`.[^exec]

**Transfer matrix.** A column of height `a` may be followed by one of height `b` unless `a = b = 2`. With states `(1, 2)` the transfer matrix is `[[1, 1], [1, 0]]`, and by induction its `n`-th power is `[[F_{n+1}, F_n], [F_n, F_{n−1}]]` for `n ≥ 1`. A skyline of width `n` takes `n − 1` steps from any state to any state, so the number of strings is `𝟙ᵀ [[1,1],[1,0]]^{n−1} 𝟙 = F_n + 2F_{n−1} + F_{n−2} = F_{n+2}`. Taking determinants of the powers gives Cassini's identity `F_{n+1}F_{n−1} − F_n² = (−1)^n`. The same matrix is the first entry of [[reachable-field-census](pages/reachable-field-census.md)].

**Growth.** The eigenvalues are `φ = (1 + √5)/2` and `−1/φ`, and Binet's formula gives

```
F_{w+2} − 1  ~  (φ²/√5) · φ^w,      φ²/√5 ≈ 1.170820,
```

so the Fibonacci castles are a golden width growth castle ([[castle-classification-growth](pages/castle-classification-growth.md)], [[metallic-means](pages/metallic-means.md)]).[^exec]

**Information per column.** All castles of exact height 2 carry `log₂(2^w − 1)/w → 1` bit per column, and Fibonacci castles carry `log₂ φ ≈ 0.694242` bits, so the rule costs about 0.306 bits per column ([[castle-entropy](pages/castle-entropy.md)]). The two-sided version of the second rows, the 0/1 sequences with no two consecutive 1s, is the **golden mean shift** of symbolic dynamics, a shift of finite type whose entropy is `log φ`.[^shift]

## Fibonacci identities from Fibonacci castles

Counting Fibonacci castles, or their second rows, in two ways gives the classical identities. Second rows of length `n` number `F_{n+2}`, and it is convenient to count one (empty) second row of length `−1`, consistent with `F_1 = 1`.

- **`Σ_{j=1}^{w} F_j = F_{w+2} − 1`.** Sort the Fibonacci castles of width `w` by the position `j` of the last height-2 column. Columns after `j` have height 1; for `j ≥ 2` column `j − 1` has height 1 and columns `1, …, j − 2` carry any second row of length `j − 2`, giving `F_j` castles; `j = 1` gives one castle, `F_1`.
- **`F_{a+b} = F_a F_{b+1} + F_{a−1} F_b`.** There are `F_{a+b}` second rows of length `a + b − 2`. Look at position `a − 1`: if it is 0, the row splits into independent rows of lengths `a − 2` and `b − 1`, giving `F_a F_{b+1}`; if it is 1, both neighbours are 0 and the rest splits into rows of lengths `a − 3` and `b − 2`, giving `F_{a−1} F_b`. This covers `a ≥ 2`, `b ≥ 1`; at `a = 1` the identity reads `F_{b+1} = F_{b+1}`. This is Benjamin and Quinn's tiling identity `f_{a+b} = f_a f_b + f_{a−1} f_{b−1}` in the shift `f_n = F_{n+1}`.[^bq]
- **Shallow diagonals of Pascal's triangle.** There are `C(w − m + 1, m)` second rows of length `w` with exactly `m` ones (delete the position after each of the first `m − 1` chosen ones to get an unrestricted choice of `m` among `w − m + 1`), so `F_{w+2} = Σ_m C(w − m + 1, m)`. Benjamin and Quinn's form is `f_n = Σ_{p + 2q = n} C(p + q, q)`.[^bq] The same triangle, read as tree castles by tall-column count, is on [[tree-castle-by-area](pages/tree-castle-by-area.md)].

## Zeckendorf ranks

Zeckendorf's theorem: every positive integer is, in exactly one way, a sum of Fibonacci numbers `F_k` (`k ≥ 2`) with no two consecutive indices.[^chu] A Fibonacci castle has the same shape: a nonempty set of positions with no two adjacent.

**Ranking.** Give column `i` of a Fibonacci castle of width `w` the weight `F_{w+2−i}`, so the weights run `F_{w+1}, F_w, …, F_2` from left to right, and let the rank of the castle be the sum of the weights of its height-2 columns. Then:

- the rank is a bijection from the Fibonacci castles of width `w` onto `{1, 2, …, F_{w+2} − 1}`;
- the height-2 columns of a castle are exactly the terms of the Zeckendorf representation of its rank;
- ranks increase in the lexicographic order of the skylines.

Adjacent columns carry consecutive indices `w + 2 − i`, which run over `2, …, w + 1`, so a Fibonacci castle is a nonempty set of pairwise non-consecutive indices in `{2, …, w + 1}`. The largest sum is `F_{w+1} + F_{w−1} + ⋯ = F_{w+2} − 1`, the sums are distinct by uniqueness, and every integer up to `F_{w+2} − 1` has a representation with largest index at most `w + 1`. Castles with `c_1 = 1` have rank at most `F_w + F_{w−2} + ⋯ = F_{w+1} − 1` and castles with `c_1 = 2` have rank at least `F_{w+1}`, and the same comparison works column by column, which gives the order.[^exec]

**Unranking** is the greedy algorithm: for `i = 1, …, w`, set `c_i = 2` and subtract `F_{w+2−i}` when it does not exceed what is left of the rank, and `c_i = 1` otherwise. Both directions take `O(w)` additions. At width 4 the weights are `5, 3, 2, 1`, and the seven castles listed above have ranks `1, …, 7` in that order; for example `(1, 2, 1, 2)` has rank `3 + 1 = 4`.

## Blocks and the even-block count

**A Fibonacci castle with `m` height-2 columns has `m + 1` blocks**: the bottom row is one block, and the second-row cells are pairwise non-adjacent, so each is a block of length 1. So it has an even number of blocks exactly when `m` is odd, and PE 502's question for Fibonacci castles is a question about counting by `m`.

| `w` | `m = 0` | 1 | 2 | 3 | 4 | 5 | sum `F_{w+2}` | alternating sum `P_F(w)` |
|---|---|---|---|---|---|---|---|---|
| 1 | 1 | 1 | | | | | 2 | 0 |
| 2 | 1 | 2 | | | | | 3 | −1 |
| 3 | 1 | 3 | 1 | | | | 5 | −1 |
| 4 | 1 | 4 | 3 | | | | 8 | 0 |
| 5 | 1 | 5 | 6 | 1 | | | 13 | 1 |
| 6 | 1 | 6 | 10 | 4 | | | 21 | 1 |
| 7 | 1 | 7 | 15 | 10 | 1 | | 34 | 0 |
| 8 | 1 | 8 | 21 | 20 | 5 | | 55 | −1 |
| 9 | 1 | 9 | 28 | 35 | 15 | 1 | 89 | −1 |
| 10 | 1 | 10 | 36 | 56 | 35 | 6 | 144 | 0 |

The entries are `C(w − m + 1, m)`; the column `m = 0` is the all-zero second row, which is not a castle.

**The signed count.** `P_F(w) = Σ_m (−1)^m C(w − m + 1, m)` is the signed count of second rows of length `w`, each weighted by `(−1)^{number of ones}`. A second row is empty, a single 1, a 0 followed by a second row, or `1, 0` followed by a second row, so with `x` marking length and `y` marking ones the generating function is

```
Σ_{w,m} C(w − m + 1, m) x^w y^m  =  (1 + xy) / (1 − x − x² y).
```

At `y = 1` this is `Σ F_{n+2} x^n`. At `y = −1` it is `(1 − x)/(1 − x + x²) = (1 − x²)/(1 + x³)`, so `P_F(w)` has period 6, with `P_F(0), …, P_F(5) = 1, 0, −1, −1, 0, 1`. The period comes from the roots of `1 − x + x²`, the primitive sixth roots of unity.[^exec]

**Even and odd.** Even-block castles have `m` odd, so

```
even-block Fibonacci castles  =  (F_{w+2} − P_F(w)) / 2,
odd-block Fibonacci castles   =  (F_{w+2} + P_F(w)) / 2 − 1,
```

the `−1` again removing the all-zero row. Their difference `1 − P_F(w)` takes only the values 0, 1, 2: the two are equal exactly when `w ≡ 0` or `5 (mod 6)`, and otherwise the even-block castles are ahead by 1 or 2.[^exec]

| `w` | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| even-block Fibonacci castles | 1 | 2 | 3 | 4 | 6 | 10 | 17 | 28 | 45 | 72 | 116 | 188 |
| odd-block Fibonacci castles | 0 | 0 | 1 | 3 | 6 | 10 | 16 | 26 | 43 | 71 | 116 | 188 |
| `F(w, 2)`, all castles of exact height 2 | 1 | 3 | 6 | 10 | 16 | 28 | 56 | 120 | 256 | 528 | 1056 | 2080 |

**Against all castles of exact height 2.** Both counts are half the total plus a parity term. For all castles of exact height 2 the parity term is `1 − Re((1 + i)^{w+1})` ([[signed-tower-count](pages/signed-tower-count.md)]), so `F(w, 2) = (2^w − Re((1 + i)^{w+1}))/2`, with `F(4, 2) = 10` as in the problem statement;[^pe-f42] that parity term grows like `2^{w/2}`. For Fibonacci castles it stays between −1 and 1.[^exec]

**In Zeckendorf terms.** By the ranking, the number of height-2 columns of a Fibonacci castle is the number of terms in the Zeckendorf representation of its rank. So among `1, 2, …, F_{w+2} − 1`, the integers with an odd number of Zeckendorf terms outnumber those with an even number by `1 − P_F(w)`.[^exec]

## Neighbouring families

- **Ridge castles of exact height 2.** The ridge rule forbids two adjacent columns of height 1 at `h = 2` ([[castle-classification-shape](pages/castle-classification-shape.md)] Axis 2, [[metallic-strip-realizability](pages/metallic-strip-realizability.md)]). Exchanging heights 1 and 2 maps them onto the Fibonacci castles plus the all-1 row, so there are `F_{w+2}` of them for `w ≥ 2`. The exchange does not preserve blocks: `(2, 2)` has two and `(1, 1)` one. At exact height `h` the ridge castles grow like the metallic mean `δ_{h−1}`; Fibonacci castles have no such extension, since the tree castles of exact height `h ≥ 3` grow at the non-metallic `(1 + √(4h − 3))/2` ([[castle-graph](pages/castle-graph.md)]).
- **Castles of exact height 2 by area.** A castle of exact height 2 with `n` cells is a composition of `n` into 1s and 2s with at least one 2, a tiling of a strip of `n` cells by squares and dominoes that uses a domino. There are `F_{n+1} − 1` of them (Benjamin and Quinn's `f_n = F_{n+1}`, minus the all-square tiling), and `C(n − m, m)` have `m` columns of height 2 and width `n − m`.[^bq] Mark each of the `n − 1` internal cell boundaries with 1 if it lies inside a domino and 0 otherwise: two dominoes never cover adjacent boundaries, so this is a bijection onto the Fibonacci castles of width `n − 1`, preserving the number of height-2 columns but not blocks (a castle of exact height 2 has one block plus one per maximal run of height-2 columns). See [[exact-height-castle-by-area](pages/exact-height-castle-by-area.md)] and [[n-nacci-disambiguation](pages/n-nacci-disambiguation.md)].[^exec]
- **Fibonacci castles by area** grow at the supergolden constant `≈ 1.4656`, not at `φ` ([[tree-castle-by-area](pages/tree-castle-by-area.md)]).
- **Prime castles**, the castles with no height-1 column, number `F_{n−1}` by area with the height unrestricted ([[prime-castles](pages/prime-castles.md)]).

## Computation

The checks behind the footnotes:

```python
from itertools import product
from math import comb
F = [0, 1]
for _ in range(80): F.append(F[-1] + F[-2])
def blocks(c): return c[0] + sum(max(0, c[i] - c[i-1]) for i in range(1, len(c)))
def fib_castle(c): return max(c) == 2 and all(not (c[i] == 2 == c[i+1]) for i in range(len(c) - 1))
def P_F(w): return sum((-1)**m * comb(w - m + 1, m) for m in range(w + 1))
for w in range(1, 15):
    G = sorted(c for c in product((1, 2), repeat=w) if fib_castle(c))
    assert len(G) == F[w+2] - 1
    assert all(blocks(c) == c.count(2) + 1 for c in G)
    even = sum(1 for c in G if blocks(c) % 2 == 0)
    assert even == (F[w+2] - P_F(w)) // 2 and len(G) - even == (F[w+2] + P_F(w)) // 2 - 1
    weights = [F[w+2-i] for i in range(1, w + 1)]
    assert [sum(x for x, c_i in zip(weights, c) if c_i == 2) for c in G] == list(range(1, F[w+2]))
    allc = [c for c in product((1, 2), repeat=w) if 2 in c]
    assert sum(1 for c in allc if blocks(c) % 2 == 0) == (2**w - round(((1 + 1j)**(w + 1)).real)) // 2
print([P_F(w) for w in range(12)])   # 1, 0, -1, -1, 0, 1, 1, 0, -1, -1, 0, 1
```

## Related Concepts

- [[castle-classification-shape](pages/castle-classification-shape.md)] - the shape catalogue, where the Fibonacci castle sits beside the ridge castles (Axis 2).
- [[castle-notation](pages/castle-notation.md)] - the Fibonacci castle entry and `P_F`.
- [[castle-graph](pages/castle-graph.md)], [[tree-castle-by-area](pages/tree-castle-by-area.md)] - tree castles, of which Fibonacci castles are the exact-height-2 case.
- [[castle-classification-growth](pages/castle-classification-growth.md)], [[metallic-means](pages/metallic-means.md)] - the golden width growth class.
- [[metallic-strip-realizability](pages/metallic-strip-realizability.md)] - the ridge rule and its metallic ladder.
- [[n-nacci-disambiguation](pages/n-nacci-disambiguation.md)] - every Fibonacci appearance on the wiki, with this family in Fibonacci section 1.
- [[exact-height-castle-by-area](pages/exact-height-castle-by-area.md)] - castles of exact height 2 by area, the area-side twin.
- [[signed-tower-count](pages/signed-tower-count.md)] - the parity term for all castles, `Re((1 + i)^{w+1})`.
- [[castle-entropy](pages/castle-entropy.md)] - `log₂ φ` among the entropy rates of castle families.
- [[kitamasa](pages/kitamasa.md)], [[aocp-generating-functions](pages/aocp-generating-functions.md)] - the Fibonacci recurrence and its generating function as worked examples.

## Footnotes

[^pe]: https://projecteuler.net/problem=502 (Project Euler, Problem 502 "Counting Castles", fetched 2026-10-03) - rules "The bottom row is occupied by a block of length w.", "The maximum achieved height of the entire castle is exactly h.", "The castle is made from an even number of blocks."; a block is a rectangle of height 1 and integer length [synthesis of the opening definition].
[^bar]: [[deutsch-elizalde-2017-bargraphs-dyck-paths](pages/deutsch-elizalde-2017-bargraphs-dyck-paths.md)] §1 L25-30 - "A bargraph is a lattice path with steps U = (0, 1), H = (1, 0) and D = (0, −1) that starts at the origin and ends on the x-axis, stays strictly above the x-axis everywhere except at the endpoints, and has no pair of consecutive steps of the form U D or DU"; "thus interpreting the bargraph as a composition".
[^chu]: https://cs.uwaterloo.ca/journals/JIS/VOL22/Chu2/chu9.pdf (H. V. Chu, J. Integer Sequences 22 (2019), Article 19.6.5) p.1 Abstract - "A finite set is said to be Zeckendorf if it does not contain two consecutive natural numbers. Let E_n be the number of Zeckendorf subsets of {1, 2, . . . , n}. It is well-known that E_n = F_n+2."; p.2 §1 - "In 1972, Zeckendorf proved that every positive integer can be uniquely written as a sum of non-consecutive Fibonacci numbers [11]", where [11] is E. Zeckendorf, "Représentation des nombres naturels par une somme de nombres de Fibonacci ou de nombres de Lucas", Bull. Soc. Roy. Sci. Liège 41 (1972), 179-182 (not read).
[^shift]: http://www-igm.univ-mlv.fr/~perrin/Recherche/HandbookAutomata/FichiersJB/symbolicdynamics.pdf (M.-P. Béal, J. Berstel, S. Eilers, D. Perrin, "Symbolic dynamics", handbook chapter) p.3 Example 2.1 - "The shift X(W) is composed of the sequences without two consecutive b's. It is a shift of finite type, called the golden mean shift."; p.6 Example 2.4 - "As a classical result, h(X) = log λ where λ = (1 + √5)/2 is the golden mean."; p.2 - "We follow the notation of the book of Doug Lind and Brian Marcus [19]", with [19] D. A. Lind and B. H. Marcus, An introduction to symbolic dynamics and coding, Cambridge University Press, 1995 (not read).
[^bq]: https://www.fq.math.ca/Papers1/43-4/paper43-4-6.pdf (P. G. Anderson, review of A. T. Benjamin and J. J. Quinn, Proofs that Really Count: The Art of Combinatorial Proof, MAA 2003, in Fibonacci Quarterly 43(4)) p.326 - "there are f_n ways to tile an n × 1 board (an 'n-board') with squares and rectangles (f_n = F_n+1, a more convenient Fibonacci sequence for this point of view)"; "fa+b = fafb + fa−1fb−1"; "an n-board can be tiled using p squares and q dominoes C(p+q, p) different ways". The book itself was not read.
[^pe-f42]: https://projecteuler.net/problem=502 (fetched 2026-10-03) [synthesis] - the problem lists `F(4,2) = 10` among its example values.
[^exec]: Verified by execution (Python 3, SymPy, 2026-10-03), by brute force over all skylines: for `w ≤ 14`, the Fibonacci castles number `F_{w+2} − 1`, each has `m + 1` blocks, `C(w − m + 1, m)` second rows have `m` ones, the even- and odd-block counts match the formulas, the Zeckendorf rank lists them in lexicographic order onto `1, …, F_{w+2} − 1`, and `F(w, 2) = (2^w − Re((1+i)^{w+1}))/2` over all castles of exact height 2; for `w ≤ 15`, odd-term minus even-term Zeckendorf counts on `1, …, F_{w+2} − 1` equal `1 − P_F(w)`; `P_F(w)` for `w = 0..17` repeats `1, 0, −1, −1, 0, 1`; the bivariate GF matches `C(w − m + 1, m)` through `x^7` and `(1 − x)/(1 − x + x²) = (1 − x²)/(1 + x³)` symbolically; `(F_{52} − 1)/φ^{50} = 1.17082039` against `φ²/√5 = 1.17082039`, and `(F_{w+2} − 1)/(2^w − 1)` divided by `(φ/2)^w` approaches the same constant; `Σ_{j ≤ w} F_j = F_{w+2} − 1`, `F_{a+b} = F_aF_{b+1} + F_{a−1}F_b` and Cassini's identity hold for all indices below 30-40 tested; for `n ≤ 16`, castles of exact height 2 with `n` cells number `F_{n+1} − 1`, `C(n − m, m)` of them have `m` height-2 columns, the domino-boundary map is a bijection onto Fibonacci castles of width `n − 1` preserving that number, and their blocks are one plus the number of maximal runs of height-2 columns.
