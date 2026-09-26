---
title: Bounded-height castles by area - the n-nacci family
category: Analyses
summary: All castles (not just tree castles) with column heights in {1, …, h}, graded by total area A, are counted by the h-step Fibonacci (n-nacci) numbers, GF 1/(1 − x − x² − ⋯ − x^h). A castle bounded by height h is a composition of A into parts {1, …, h}, and compositions into {1..h} are the n-nacci numbers. The growth constant marches up the n-nacci constants: h = 2 is Fibonacci A000045 (φ ≈ 1.618), h = 3 is tribonacci A000073 (t ≈ 1.8393), h = 4 is tetranacci A000078, h = 5 is pentanacci A001591, tending to 2 as h → ∞. This is the castle's first tribonacci interpretation, and a new, denser sibling of the tree-castle-by-area family, whose 2×2-block ban instead produces the term-skipping cubics (supergolden, plastic).
tags: [analysis, castle, area, generating-function, oeis, fibonacci, tribonacci, tetranacci, n-nacci, composition, growth-constant]
sources: [project-euler-502-castle-factoring, salem-1963-algebraic-numbers-fourier-analysis]
created: 2026-09-17
updated: 2026-09-25
---

# Bounded-height castles by area

## The result

Grade **all** castles - the full skyline family, no tree or convexity restriction - by two knobs: a height bound `h` (every column `c_i ∈ {1, …, h}`) and total area `A = Σ c_i`. The count is the **`h`-step Fibonacci number** ("n-nacci"):

```
#{castles of area A, column heights ≤ h}  =  #{compositions of A into parts {1, …, h}},
```

with ordinary generating function[^1]

```
Σ_A (count) x^A  =  1 / (1 − x − x² − ⋯ − x^h)  −  1        (the −1 drops the empty A = 0 term).
```

The identity is immediate and needs no transfer matrix: **a castle skyline `(c_1, …, c_w)` is literally a composition of its area** ([[castle-representations](pages/castle-representations.md)]), Rule 3 is automatic for area-graded *all*-castles (the same observation that gives the `2^{n−1}` baseline on [[castle-by-area](pages/castle-by-area.md)]), and "column height `≤ h`" is exactly "every part `≤ h`". Compositions of `A` into parts `{1, …, h}` satisfy the `h`-term recurrence `a(A) = a(A−1) + a(A−2) + ⋯ + a(A−h)` - the defining n-nacci recurrence - because the last part is one of `1, …, h`.

## The ladder

| `h` | area sequence, `A = 1..12` | denominator | growth constant | Online Encyclopedia of Integer Sequences (OEIS) |
|---|---|---|---|---|
| 2 | `1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233` | `1 − x − x²` | `φ ≈ 1.6180` | **A000045** Fibonacci, `= A000045(A+1)` |
| **3** | `1, 2, 4, 7, 13, 24, 44, 81, 149, 274, 504, 927` | `1 − x − x² − x³` | **`t ≈ 1.8393`** (root of `x³ = x² + x + 1`) | **A000073** tribonacci, `= A000073(A+2)` |
| 4 | `1, 2, 4, 8, 15, 29, 56, 108, 208, 401, 773, 1490` | `1 − x − x² − x³ − x⁴` | `≈ 1.9276` (root of `x⁴ = x³+x²+x+1`) | **A000078** tetranacci, `= A000078(A+3)` |
| 5 | `1, 2, 4, 8, 16, 31, 61, 120, 236, 464, 912, 1793` | `1 − x − ⋯ − x⁵` | `≈ 1.9659` | **A001591** pentanacci, `= A001591(A+4)` |
| ∞ | `1, 2, 4, 8, 16, 32, 64, …` | `(1 − x)/(1 − 2x)` | `2` | `2^{A−1}`, **A011782** ([[castle-by-area](pages/castle-by-area.md)] baseline) |

Every n-nacci constant is a Pisot number ([[pisot-number](pages/pisot-number.md)]). Checked for `h = 2..12`, the other roots have modulus `0.618, 0.737, 0.818, …, 0.980`, creeping toward 1 as the constant approaches 2. So this castle ladder is a sequence in Salem's class S converging to `2`, one of the integer limit points his Chapter II exercise constructs from the other side (`z^n(z − 2) − 1`, roots `2.414, 2.206, 2.107, …` decreasing to 2; the first is the silver ratio).[^salem2] The n-nacci constants increase monotonically from `φ` to their limit `2` (the `h → ∞` row is the wiki's `2^{A−1}` all-castles baseline, recovered as the unbounded-height case). OEIS offsets verified against the OEIS generating functions (2026-09-17): A000073 has GF `x²/(1−x−x²−x³)`, A000078 has GF `x³/(1−x−x²−x³−x⁴)`, so the area-`A` count is `A000073(A+2)` and `A000078(A+3)` respectively.[^2]

## Why this is not the tree-castle-by-area family

The obvious neighbor is [[tree-castle-by-area](pages/tree-castle-by-area.md)], which grades **tree** castles (no 2×2 filled block, i.e. no two adjacent columns both `≥ 2`) by area at fixed height. That family produces a completely different, sparser set of sequences - and crucially, the *term-skipping* cubics, not the n-nacci ones:

| `h` | this page (all castles) | tree-castle-by-area (no 2×2 block) |
|---|---|---|
| 2 | Fibonacci **A000045** (`φ`) | Narayana's cows **A000930** (supergolden `≈ 1.4656`) |
| 3 | tribonacci **A000073** (`t ≈ 1.8393`) | **A006498** (golden `φ` via cyclotomic factor) |
| 4 | tetranacci **A000078** | tournaments **A000570** (Tetali; [[unique-tournament](pages/unique-tournament.md)]) |
| ∞ | `2^{A−1}` **A011782** | plastic-squared **A005251** (`ψ² ≈ 1.7549`) |

At every `h` the all-castle count strictly dominates the tree count (the tree constraint deletes the `(…, 2, 2, …)` adjacencies), so the two families never coincide. The mechanism is transparent at `h = 2`: dropping the tree ban restores compositions with adjacent parts `≥ 2`, lifting the growth constant from supergolden to `φ`. The **term-skipping** denominators of the tree family (`1 − q − q³`, `1 − q − q³ − q⁴`, …, which always omit the `q²` term because a tall column carries area `≥ 2`) are exactly what excludes the tribonacci denominator `1 − x − x² − x³` there - and exactly what this all-castle grading supplies.

## Fibonacci and tribonacci, on one ladder

The two rungs answer a standing question directly: **where do Fibonacci and tribonacci both enter the castle?** They are the `h = 2` and `h = 3` members of *this single family*.

- **Fibonacci (`h = 2`).** All castles of height `≤ 2` by area is a *new, cleaner* Fibonacci-in-castle appearance, distinct from the two already on the wiki: the prime-castle formula `2^{n−1} − F_{n−1}` ([[castle-by-area](pages/castle-by-area.md)]) and the tree-castle-by-width `h = 2` row ([[castle-graph](pages/castle-graph.md)]). Here Fibonacci is simply "compositions into `{1, 2}`" - the textbook interpretation - realized as a castle area count.
- **Tribonacci (`h = 3`).** This is the **castle's first tribonacci interpretation** anywhere on the wiki (the only prior mention was a mislabeled helper-function example in [[castle-snippets](pages/castle-snippets.md)], since corrected). It completes the cubic-constant map: the castle now realizes the tribonacci constant (`x³ = x² + x + 1`, this page), the supergolden (`x³ = x² + 1`, Narayana's cows on [[tree-castle-by-area](pages/tree-castle-by-area.md)]), and the plastic (`x³ = x + 1`, as `ψ²` and `2ψ²` on [[plastic-number](pages/plastic-number.md)]).

## Relation to the metallic-means classification

On the Axis-8 meta-classification of [[castle-classification](pages/castle-classification.md)] / [[metallic-means](pages/metallic-means.md)], the growth-by-area axis for this family is **not** metallic: the n-nacci constants for `h ≥ 3` are roots of `x^h = x^{h−1} + ⋯ + 1`, algebraic of degree `h`, none of which is a metallic mean `(a + √(a²+4))/2`. Only the `h = 2` rung (`φ`) lands on the metallic ladder. So the bounded-height-by-area family is a distinct algebraic family indexed by `h`, converging to `2` - a companion to (and denser than) the tree-castle-by-area family, which is *also* non-metallic for `h ≥ 2` (both are open research directions the wiki keeps flagging: metallic means appear as spectral radii, not as area growth constants; see [[castle-graph-spectral-radius](pages/castle-graph-spectral-radius.md)]).

## Reproduce

The `bounded_castles_by_area(h, A_max)` snippet on [[castle-snippets-strips](pages/castle-snippets-strips.md)] computes the table above from the recurrence, with a brute-force cross-check against the actual height-bounded skyline model (`sum(c)` over `product(range(1, h+1), repeat=w)`) that agrees term for term.

## Appearances in Sources

- [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] - the `F(w, h)` skyline model whose height bound `h` and area statistic this grading uses.

## Related Concepts

- [[pisot-number](pages/pisot-number.md)] - every n-nacci constant is Pisot; the ladder converges to the limit point 2 of the Pisot set.
- [[tree-castle-by-area](pages/tree-castle-by-area.md)] - the sparser sibling (2×2-block ban) that produces the term-skipping cubics instead; the closest neighbor on the wiki.
- [[castle-by-area](pages/castle-by-area.md)] - the `h → ∞` case (`2^{A−1}`, all compositions) and the area-re-indexing that this page bounds by height.
- [[plastic-number](pages/plastic-number.md)] - the third cubic constant (`ψ`, `x³ = x + 1`); this page adds the tribonacci constant (`x³ = x² + x + 1`) to the cubic-constant map.
- [[metallic-means](pages/metallic-means.md)] - the family the `h = 2` rung (`φ`) belongs to and the `h ≥ 3` rungs sit near but outside.
- [[castle-graph](pages/castle-graph.md)] - the tree-castle-by-width Fibonacci/Jacobsthal/k-Fibonacci ladder, the width-axis cousin of this area-axis ladder.
- [[weakly-unimodal-composition](pages/weakly-unimodal-composition.md)] - the composition ↔ castle correspondence this result rests on, in its convex (stack) form.
- [[unique-tournament](pages/unique-tournament.md)] - the graph-theoretic side of the `h = 4` tree row `A000570` in the table above.
- [[aocp-generating-permutations-tuples](pages/aocp-generating-permutations-tuples.md)] - the by-area enumeration behind `bounded_castles_by_area` is Knuth's Algorithm M with an area filter.

## Footnotes

[^1]: Verified by execution: brute-force enumeration of every height-bounded skyline `c ∈ {1, …, h}^w` (all widths `w` with `Σ c ≤ A_max`), bucketed by area, agrees term for term with the composition recurrence `a(A) = Σ_{p=1}^{h} a(A−p)` for `h = 2, 3, 4, 5` and `A ≤ 14`. The GF `1/(1 − x − ⋯ − x^h)` is the standard OGF for compositions into parts `{1, …, h}` (sequence (SEQ) of `{x, x², …, x^h}`; [[symbolic-method](pages/symbolic-method.md)] SEQ construction).

[^2]: OEIS (fetched 2026-09-17): https://oeis.org/A000073 - tribonacci, "a(n) = a(n-1) + a(n-2) + a(n-3)", GF `x²/(1 − x − x² − x³)`, data `0, 0, 1, 1, 2, 4, 7, 13, 24, 44, 81, 149, 274`, comment "number of compositions of n-2 with no part greater than 3"; tribonacci constant `1.839286755…`, the real root of `x³ − x² − x − 1`. https://oeis.org/A000078 - tetranacci, GF `x³/(1 − x − x² − x³ − x⁴)`, "number of compositions of n-3 with no part greater than 4". Offsets `A000073(A+2)`, `A000078(A+3)`, `A001591(A+4)` follow from the numerator power `x^{h−1}` in each GF. A000045 (Fibonacci) and A011782 (`2^{n−1}`) are standard.

[^salem2]: [[salem-1963-algebraic-numbers-fourier-analysis](pages/salem-1963-algebraic-numbers-fourier-analysis.md)] Ch. II Exercise p.21 [synthesis] L1491-1498 - every natural integer a ≥ 2 is "a limit point for the numbers of the class S", from the roots of `z^n(z − a) − 1 = 0`. Pisot checks by execution (2026-09-25, own computation; NumPy roots of `x^h − x^{h−1} − … − 1` for `h = 2..12`, SymPy factorization of `x^n(x − 2) − 1` for `n = 1..7`, all irreducible and Pisot).
