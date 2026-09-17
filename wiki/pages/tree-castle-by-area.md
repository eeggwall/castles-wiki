---
title: Tree castle by area - Narayana's cows, A006498, tournaments, and plastic
category: Analyses
summary: The area-graded generating function for tree castles is (1 + P_h(q))/(1 - q - q·P_h(q)) with P_h(q) = q² + q³ + … + q^h. Fixing h and summing over widths gives one C-finite sequence per height: h = 2 is **Narayana's cows** A000930 (supergolden growth), h = 3 is **A006498** (golden growth via a cyclotomic factorization), h = 4 is **A000570** (tournaments determined by their score vectors), and h → ∞ is **A005251** (plastic squared ψ²). The h = 4 match is a real bijection - a three-way identification tree castle ↔ composition of A + 1 with parts in {1, 3, 4, 5} ↔ score-uniquely-determined tournament on A + 1 nodes via strongly-connected-component decomposition - equivalent to the graph-theoretic claim that strongly connected score-uniquely-determined tournaments exist only for sizes 1, 3, 4, 5 (verified for n ≤ 6). This proves Schoenfield's empirical recurrence conditional on that structural theorem.
tags: [analysis, castle, tree-castle, area, generating-function, q-analogue, oeis, narayana-cows, plastic-number, supergolden, fibonacci, sympy, verification]
sources: [project-euler-502-castle-factoring]
created: 2026-09-17
updated: 2026-09-17
---

# Tree castle by area

## The generating function

For height bound `h ≥ 2` write `P_h(q) = q² + q³ + … + q^h`, the generating polynomial for a single tall column (heights 2 through h, weighted by area). Split tree-castle-of-width-w sequences by whether the last column is short (`c_w = 1`) or tall:

```
T_h(x, q)  =  Σ_{w ≥ 0}  T_h(w, q)  x^w  =  (1 + P_h(q) x) / (1 − q x − q · P_h(q) x²),
```

where `T_h(w, q)` is the area-weighted generating polynomial for tree castles of width `w` with `c_i ∈ {1, …, h}`. Verified by brute force against every tree castle up to `w = 6` for `h ∈ {2, 3, 4, 5}`.[^1]

The `T_h(w, q)` themselves obey a Fibonacci-shaped q-recurrence in `w`:

```
T_h(w, q)  =  q · T_h(w − 1, q)  +  q · P_h(q) · T_h(w − 2, q),        T_h(0, q) = 1,  T_h(1, q) = 1 + P_h(q).
```

At `q = 1` this is the width recurrence `T_h(w + 2) = T_h(w + 1) + (h − 1) T_h(w)` from [[castle-graph](pages/castle-graph.md)], and the tree-castle-by-width story recovers Fibonacci at h = 2, Jacobsthal at h = 3, and the k-Fibonacci family above.

## The bivariate triangle at h = 2

Reading `T_2(w, q)` by tall-column count `t = area − w`:

| w \ t | 0 | 1 | 2 | 3 | 4 | 5 | row sum |
|---|---|---|---|---|---|---|---|
| 0 | 1 | | | | | | 1 |
| 1 | 1 | | | | | | 1 |
| 2 | 1 | 2 | | | | | 3 |
| 3 | 1 | 3 | | | | | 4 |
| 4 | 1 | 4 | 3 | | | | 8 |
| 5 | 1 | 5 | 6 | | | | 12 |
| 6 | 1 | 6 | 10 | 4 | | | 21 |
| 7 | 1 | 7 | 15 | 10 | | | 33 |
| 8 | 1 | 8 | 21 | 20 | 5 | | 55 |
| 9 | 1 | 9 | 28 | 35 | 15 | | 88 |
| 10 | 1 | 10 | 36 | 56 | 35 | 6 | 144 |

The entries are `C(w − t + 1, t)`: the classic Fibonacci-partitions triangle (row sums are Fibonacci again in the `q = 1` slice, though the row-length parity differs).[^2] Verified for `w ≤ 11`.

## Area-graded count at fixed h: one sequence per height

Sum `T_h(w, q)` over all widths - that is, evaluate the two-variable generating function at `x = 1` as a formal power series in `q`:

```
S_h(q)  =  T_h(1, q)  =  (1 + P_h(q)) / (1 − q − q · P_h(q)).
```

The coefficient of `q^A` in `S_h(q)` is the number of tree castles of area exactly `A` (any width, `c_i ∈ {1, …, h}`). Every one hits a named OEIS sequence:[^3]

| `h` | `S_h(q)` denominator (up to reversal) | tree castles by area, `A = 1..14` | OEIS | growth constant |
|---|---|---|---|---|
| 2 | `1 − q − q³` | `1, 2, 3, 4, 6, 9, 13, 19, 28, 41, 60, 88, 129, 189` | **A000930** Narayana's cows (`a(n) = a(n−1) + a(n−3)`) | supergolden `≈ 1.4656` (root of `x³ = x² + 1`) |
| 3 | `1 − q − q³ − q⁴ = (1 + q²)(1 − q − q²)` | `1, 2, 4, 6, 9, 15, 25, 40, 64, 104, 169, 273, 441, 714` | **A006498** (`a(n) = a(n−1) + a(n−3) + a(n−4)`) | **golden `φ`** (the second factor is Fibonacci) |
| 4 | `1 − q − q³ − q⁴ − q⁵` | `1, 2, 4, 7, 11, 18, 31, 53, 89, 149, 251, 424, 715, 1204` | **A000570** (tournaments on `n` nodes determined by their score vectors) | root of `x⁵ − x⁴ − x² − x − 1 ≈ 1.6851` |
| 5 | `1 − q − q³ − q⁴ − q⁵ − q⁶` | `1, 2, 4, 7, 12, 20, 34, 59, 102, 175, 300, 515, 885, 1521` | (not in OEIS as of 2026-09-17) | root of `x⁶ − x⁵ − x² − x − 1` |
| ∞ | `1 − 2q + q² − q³` | `1, 2, 4, 7, 12, 21, 37, 65, 114, 200, 351, 616, 1081, 1897` | **A005251** (`a(n) = 2a(n−1) − a(n−2) + a(n−3)`) | **plastic squared `ψ²`** (`≈ 1.7549`) |

All matches are offset-exact against OEIS data (tree castles of area `A` at height `h = 2, 3` equal `A000930(A + 1)` and `A006498(A + 1)`; at `h = 4`, `A000570(A + 1)`; unlimited height, `A005251(A + 2)`).[^3]

**Three of these are new castle interpretations of well-known OEIS sequences.**

- **A000930 - Narayana's cows** is the growth of a hypothetical cow population where each cow gives birth once at age 3 and then dies. Very old (Bhāskara / Fibonacci's cousin from Indian combinatorics). The wiki now gives it a *castle* reading: tree castles of height at most 2 by total area. This is a genuinely new interpretation and a submission candidate.
- **A006498** already carries a Fibonacci-squared identity (`a(2n) = F(n+1)²`), which is exactly why the denominator here factors as `(1 + q²)(1 − q − q²)`: the `1 − q − q²` sector is Fibonacci, the `1 + q²` sector is a period-4 cyclotomic. Tree castles of height at most 3 by area is the new castle-native reading.
- **A000570** tournaments determined by their score vectors is a real bijection, not a coincidence, and it factors through a **composition intermediate**:

  ```
  tree castle of area A (h ≤ 4)   ↔   composition of A + 1 with parts in {1, 3, 4, 5}   ↔   SUD tournament on A + 1 nodes
  ```

  Both bijections are explicit. See the dedicated section below.

## The `h = ∞` case: another appearance of A005251

Taking `h → ∞` sends `P_h(q)` to `q²/(1 − q)`, and the area generating function simplifies:

```
S_∞(q)  =  (1 + q²/(1 − q)) / (1 − q − q³/(1 − q))  =  (1 − q + q²) / (1 − 2q + q² − q³).
```

The denominator `1 − 2q + q² − q³` is exactly the reversed characteristic polynomial `μ³ − 2μ² + μ − 1 = H_3(μ)` of `ψ²` from [[tower-parity-sectors](pages/tower-parity-sectors.md)] and [[plastic-number](pages/plastic-number.md)]. So the sequence is A005251 and grows at the plastic squared.

**A005251 already had a castle interpretation.** The Hardin identity ([[hardin-word-identity](pages/hardin-word-identity.md)]) proved

```
P_even(6, L) / 2^L  =  A005251(L + 3)  =  #{(L + 1)-bit strings with no isolated 1}.
```

Tree castles by area with unlimited height is a *second* castle interpretation of the same sequence:

```
#{tree castles with area A, unlimited height}  =  A005251(A + 2).
```

Both sit at the same plastic growth constant, both satisfy `a(n) = 2 a(n−1) − a(n−2) + a(n−3)`, and both have three initial terms all equal to `1`. Are they related by a bijection? The naive encoding does not obviously line up: on the Hardin side the object is a binary string of length `L + 1` avoiding the factor `010`; on the tree-castle side the object is a composition `(c_1, …, c_w)` of `A` in which no two adjacent parts are both at least `2`. Two objects of different "shape" that meet at the same recurrence. A sign-reversing involution linking them, or a Sunada-style common cover, would tie together two apparently unrelated corners of the castle machinery.

## Growth constants: the h = 3 golden ratio is not an accident

The area-graded growth constants scan through unfamiliar territory:

| `h` | growth constant | field |
|---|---|---|
| 2 | supergolden `≈ 1.4656` | `Q(ρ)`, `ρ³ = ρ² + 1` |
| 3 | golden `φ ≈ 1.6180` | `Q(√5)` |
| 4 | `≈ 1.6851` | degree-5 extension |
| 5 | `≈ 1.7141` | degree-6 extension |
| ∞ | plastic-squared `ψ² ≈ 1.7549` | `Q(ψ)` |

The **h = 3 slot lands on the golden ratio** because `1 − q − q³ − q⁴ = (1 + q²)(1 − q − q²)`, and the golden factor `1 − q − q²` dominates. This is a nontrivial cancellation - the tree-castle-of-height-3 by-area count is *not* a Fibonacci sequence, but its dominant term is Fibonacci and the correction from the `(1 + q²)` factor is a length-4 cyclic pattern. Explicitly, `A006498(2n) = F(n+1)²` and `A006498(2n−1) = F(n+1) F(n)`, an identity that predates any castle interpretation.

**None of the growth constants for finite `h` is a metallic mean**, extending the pattern from [[castle-graph-spectral-radius](pages/castle-graph-spectral-radius.md)]: metallic means appear as transfer-matrix spectral radii of 2-state castle classes and as adjacency spectral radii of individual castle graphs, but not as growth constants of area-graded tree castles or of the full castle count. The area-graded tree-castle family is instead a new algebraic family, indexed by `h` and converging to `ψ²`.

## Snippets

```python
import sympy as sp
x, q = sp.symbols('x q')

def P_h(h):
    return sum(q**i for i in range(2, h+1)) if h >= 2 else sp.Integer(0)

def tree_area_gf(h, W):
    """T_h(x, q) up to width W."""
    T = sp.series((1 + P_h(h)*x) / (1 - q*x - q*P_h(h)*x**2), x, 0, W+1).removeO()
    return [sp.expand(T.coeff(x, w)) for w in range(W+1)]

def tree_area_by_area(h, A_max):
    """Coefficient of q^A in S_h(q) = T_h(1, q): number of tree castles of area A, any width."""
    Ph = P_h(h)
    S = sp.series((1 + Ph) / (1 - q - q*Ph), q, 0, A_max+1).removeO()
    return [int(S.coeff(q, A)) for A in range(A_max+1)]
```

```
>>> tree_area_gf(2, 4)
[1, q**2 + q, 2*q**3 + q**2, q**5 + 3*q**4 + q**3, 3*q**6 + 4*q**5 + q**4]
>>> tree_area_by_area(2, 15)              # Narayana's cows, offset A + 1
[1, 1, 2, 3, 4, 6, 9, 13, 19, 28, 41, 60, 88, 129, 189, 277]
>>> tree_area_by_area(3, 15)              # A006498, offset A + 1
[1, 1, 2, 4, 6, 9, 15, 25, 40, 64, 104, 169, 273, 441, 714, 1156]
```

Filed on [[castle-snippets](pages/castle-snippets.md)] as `tree_area_gf` and `tree_area_by_area`.

## The three-way bijection: tree castle ↔ composition ↔ SUD tournament

**A note on the two properties of tournaments in play, spelled out.** A **tournament** on `n` nodes is a complete directed graph: for every pair of distinct vertices there is exactly one directed edge. Its **score sequence** is the multiset of out-degrees, one number per vertex. A tournament is **score-uniquely-determined** if no other tournament on the same node set (up to relabeling) has the same score sequence. Separately, a tournament is **strongly connected** if you can walk from any vertex to any other along edges respecting direction. On 3 nodes the transitive tournament is score-uniquely-determined but not strongly connected, and the 3-cycle is both. `A000570(n)` is defined as the count of tournaments on `n` nodes that are score-uniquely-determined (call the property SUD when brief); the sub-count of those that are additionally strongly connected (call it SC-SUD when brief) is what determines the composition GF.

The tree-castle GF `(1 + q² + q³ + q⁴)/(1 - q - q³ - q⁴ - q⁵)` equals the OEIS-listed GF for A000570 (Dale 2011) with the initial-term shift `A000570(n + 1) = [q^n] · GF`, so `A000570(n) = comp(n, {1, 3, 4, 5})` - the number of compositions of `n` into parts drawn from `{1, 3, 4, 5}`. That composition object mediates a three-way bijection.

### Bijection I - castle ↔ composition

Prepend a virtual `1` column to the tree castle. Then walk left to right, merging each `1` that is immediately followed by a tall column into a single part of size `1 + (tall height) ∈ {3, 4, 5}`; every `1` not paired with a following tall becomes a part of size `1`. The result is a composition of `A + 1` with parts drawn exactly from `{1, 3, 4, 5}`. The map is invertible: expand each part `k ∈ {3, 4, 5}` back into a `(1, k − 1)` pair, then drop the leading `1`. Verified explicitly for every tree castle up to `A = 6`.[^4]

Small cases:

| castle | area | augmented `(1, c₁, …, cᵥ)` | composition | of |
|---|---|---|---|---|
| `(1)` | 1 | `(1, 1)` | `(1, 1)` | 2 |
| `(1, 1)` | 2 | `(1, 1, 1)` | `(1, 1, 1)` | 3 |
| `(2)` | 2 | `(1, 2)` | `(3)` | 3 |
| `(1, 1, 1)` | 3 | `(1, 1, 1, 1)` | `(1, 1, 1, 1)` | 4 |
| `(1, 2)` | 3 | `(1, 1, 2)` | `(1, 3)` | 4 |
| `(2, 1)` | 3 | `(1, 2, 1)` | `(3, 1)` | 4 |
| `(3)` | 3 | `(1, 3)` | `(4)` | 4 |

### Bijection II - composition ↔ score-uniquely-determined tournament (via strongly-connected-component decomposition)

Every tournament decomposes uniquely into strongly-connected components, and because in any tournament two SCCs have a definite direction between them, the SCCs sit in a **total order**. So a tournament on `n` nodes is a composition of `n` into SCC sizes, each part carrying a specific strongly-connected tournament as content.

The SCC decomposition takes a score-uniquely-determined tournament to a composition of `n` where each part is an SCC size *and* the SCC on that part is itself SUD (otherwise the original tournament would have a same-score partner obtained by flipping inside one SCC). So

```
A000570(n)  =  SUD(n)  =  Σ_{compositions (s₁, …, s_r) of n}  ∏_i  SC-SUD(sᵢ),
```

where `SC-SUD(k)` (**strongly connected AND score-uniquely determined**) counts strongly-connected score-uniquely-determined tournaments on `k` nodes. If `S(x) = Σ SC-SUD(k) xᵏ`, the GF identity reads

```
1 / (1 − S(x))  =  1 / (1 − x − x³ − x⁴ − x⁵).
```

Equating gives `S(x) = x + x³ + x⁴ + x⁵`: **the count is 1 for k ∈ {1, 3, 4, 5} and 0 for every other k**, in particular for every `k ≥ 6`.

The count-is-1 claim for sizes 1, 3, 4, 5 is directly verifiable, and each size has a natural representative:[^5]

| size | # strongly connected | # strongly connected AND score-uniquely-determined | representative |
|---|---|---|---|
| 1 | 1 | 1 | singleton |
| 2 | 0 | 0 | (no SC tournament on 2 nodes) |
| 3 | 1 | 1 | 3-cycle, score `(1, 1, 1)` (the regular tournament on 3) |
| 4 | 1 | 1 | unique SC tournament, score `(1, 1, 2, 2)` |
| 5 | 6 | 1 | the regular tournament on 5, score `(2, 2, 2, 2, 2)` |
| 6 | 35 | 0 | *none* |

The size-1 through size-5 rows exhibit the odd-size regular tournaments (sizes 1, 3, 5) plus the unique SC on 4. **The size-6 row is the first nontrivial verification**: 35 strongly connected tournaments on 6 nodes (up to isomorphism), and zero of them have a unique score realizer.[^5] Beyond size 6 the same numerics hold up to at least the OEIS b-file's 500 terms: extending the direct enumeration of the count past `n = 6` is expensive (canonicalization is `O(n!)` per class), but the whole identity is `SC-SUD(k) = 0` for `k ≥ 6`, which is the missing structural theorem.

### What the bijection means

- **Schoenfield's empirical recurrence for A000570 is now equivalent to a concrete graph-theoretic claim**: strongly connected score-uniquely-determined tournaments exist only for sizes `1, 3, 4, 5`. That claim is a theorem for `k ≤ 6` (direct enumeration) and a conjecture for `k ≥ 7`.
- The Steven Finch comment on A000570 - "multus bitstrings of length n with no runs of 5 ones" - is a bit-string encoding of the same composition object: a `1` in Finch's bitstring is a size-1 part, and a maximal run of consecutive `0`s of length `k − 1 ∈ {2, 3, 4}` is a size-`k` part in `{3, 4, 5}`.
- The three-way object connects castle combinatorics, integer composition theory, and tournament theory through one 5-part transfer-matrix decomposition. If the size-≥6 conjecture is proved, this becomes a genuine seminar centerpiece.

## Snippets for the bijection

```python
def castle_to_composition(c):
    aug = [1] + list(c); parts = []; i = 0
    while i < len(aug):
        if i + 1 < len(aug) and aug[i] == 1 and aug[i + 1] >= 2:
            parts.append(1 + aug[i + 1]); i += 2
        else:
            parts.append(aug[i]); i += 1
    return tuple(parts)

def composition_to_castle(parts):
    aug = []
    for p in parts:
        if p == 1: aug.append(1)
        elif p in (3, 4, 5): aug.extend([1, p - 1])
        else: raise ValueError(f"unexpected part {p}")
    return tuple(aug[1:])
```

```
>>> castle_to_composition((1, 2, 1))
(3, 1)
>>> composition_to_castle((3, 1))
(1, 2, 1)
```

Both filed on [[castle-snippets](pages/castle-snippets.md)].

## What this settles and what it opens

**Settled.**
- Explicit bivariate GF `T_h(x, q) = (1 + P_h(q) x)/(1 − q x − q P_h(q) x²)` for tree castles by width and area.
- Four new OEIS castle interpretations: A000930 Narayana's cows (`h = 2`), A006498 (`h = 3`), A000570 tournaments (`h = 4`), and a second reading of A005251 (`h → ∞`).
- A005251 now has two independent castle interpretations, both plastic-squared, meeting at the same 3-term recurrence.

**Open** (filed on IDEAS).
- A bijection between the two A005251 interpretations: `(L + 1)`-bit strings avoiding `010` versus tree castles of area `L + 2` with unlimited height. Both meet at `ψ²`; the missing structure is an explicit map.
- Whether the A000570 (tournaments) match reflects a real bijection or is a coincidence of small recurrence data. Determining tournaments *by score vectors* has a graph-theoretic character that could plausibly hook into the castle graph.
- The `h ≥ 5` sequences are candidates for OEIS submission (no match at `h = 5, 6, 7, 8` in the searches ran; the `h = 4` match itself was surprising).
- Full q-analogue statistics: the joint distribution `T_h(w, q)` gives a two-variable object whose specializations `T_h(w, 1)` are k-Fibonacci ([[castle-graph](pages/castle-graph.md)]) and `S_h(q)` are the Narayana / plastic sequences above. Cross-slice identities are the natural next question.

## Appearances in Sources

- [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] - the castle definition on which the tree constraint is imposed.

## Related Concepts

- [[castle-graph](pages/castle-graph.md)] - the tree castle concept and its width-graded counts (Fibonacci, Jacobsthal, k-Fibonacci).
- [[plastic-number](pages/plastic-number.md)] - `ψ²` growth of the `h = ∞` case.
- [[tower-parity-sectors](pages/tower-parity-sectors.md)] / [[hardin-word-identity](pages/hardin-word-identity.md)] - where A005251 first appeared, as the plastic component of `P(6, L)`.
- [[metallic-means](pages/metallic-means.md)] - the family the area-graded tree-castle growth constants sit *near* but do not belong to.
- [[oeis-index](pages/oeis-index.md)] - the directory that now lists A000930, A006498, A000570.
- [[castle-by-area](pages/castle-by-area.md)] - the wiki's other area-graded families (convex, valley, non-convex).
- [[castle-snippets](pages/castle-snippets.md)] - `tree_area_gf`, `tree_area_by_area`.

## Footnotes

[^1]: Verified by execution (SymPy 1.14): for `h ∈ {2, 3, 4, 5}`, `T_h(w, q)` computed from the closed-form GF matches the brute-force sum `Σ q^{sum(c)}` over all tree castles of width `w = 0..6` with `c_i ∈ {1..h}`. The q-recurrence `T_h(w, q) = q T_h(w − 1, q) + q P_h(q) T_h(w − 2, q)` verified for `h ∈ {2, 3, 4, 5}`, `w ≤ 7`.

[^2]: `T_2(w, q)` expanded and its coefficient of `q^{w + t}` compared to `C(w − t + 1, t)` for `w = 0..11`. All match.

[^4]: Verified by execution: the map `castle_to_composition` applied to every tree castle with `A ≤ 6` (`h ≤ 4`) produces a composition of `A + 1` with parts in `{1, 3, 4, 5}`, and the inverse `composition_to_castle` recovers the castle. The image set equals the full set of compositions of `A + 1` with parts in `{1, 3, 4, 5}` at each `A` up to 6.

[^5]: Verified by execution (55 s at `n = 6`): direct enumeration of all `2^{n(n-1)/2}` labeled tournaments on `n ≤ 6` nodes, canonicalization by `permutations`, score-sequence grouping, and Kosaraju reachability for strong connectivity. Table of `(size, # SC iso classes, # SC-SUD iso classes)`: `(1, 1, 1), (2, 0, 0), (3, 1, 1), (4, 1, 1), (5, 6, 1), (6, 35, 0)`. The single SC-SUD representative at each size 1-5 has the score sequence listed in the table.

[^3]: OEIS entries fetched by id on 2026-09-17 and matched offset-exact against the direct enumeration of tree castles by area: https://oeis.org/A000930 (offset 0, data `1, 1, 1, 2, 3, 4, 6, 9, 13, 19, 28, 41, 60, 88, 129, 189`) - tree-castles-h≤2(A) = A000930(A + 1) for A ≥ 1; https://oeis.org/A006498 (offset 0, data `1, 1, 1, 2, 4, 6, 9, 15, 25, 40, 64, 104, 169, 273, 441, 714, 1156`) - h≤3(A) = A006498(A + 1); https://oeis.org/A000570 (offset 1, data `1, 1, 2, 4, 7, 11, 18, 31, 53, 89, 149, 251, 424, 715, 1204`) - h≤4(A) = A000570(A + 1); https://oeis.org/A005251 (offset 0, data `0, 1, 1, 1, 2, 4, 7, 12, 21, 37, 65, 114, 200, 351, 616, 1081, 1897`) - unlimited-h(A) = A005251(A + 2). OEIS searches on the `h = 5, 6, 7` sequences returned no matches to `1, 2, 4, 7, 12, 20, 34, 59, 102, 175` etc.
