---
title: Fibonacci castle sub-families
category: Concepts
summary: Sub-families of the Fibonacci castles cut out by a rule on the Fibonacci tower (the second row, a 0/1 string with no two adjacent 1s), counted as castles of width w and exact height 2. First thread - the chain of Fibonacci-word castles (towers that occur in the infinite Fibonacci word, a Sturmian word; w + 1 of them from w = 3, linear growth) inside the balanced castles (towers in which any two pieces of equal length differ by at most one 1; exactly A005598(w)/2 = A049703(w) of them, 1, 2, 4, 7, 12, 18, 27, 38, …, growing like w³/(2π²)) inside all Fibonacci castles (F_{w+2} − 1, growing like φ^w). The 56-column castle from the Fibonacci word's prefix lies in the innermost family. Second thread - families cut out by the gaps between height-2 columns, each with generating function L(x)·x·R(x)/(1 − Σ x^{g+1}): maximal castles (no column can be raised; Padovan A000931(w + 6), plastic growth), spaced castles (height-2 columns ≥ 3 apart; A000930(w + 2) − 1 = A077868(w − 1), supergolden growth, in bijection with the Fibonacci castles of w + 1 cells), and the (d, k)-run-length-limited castles of recording codes, whose growth is 2^capacity; (1, 3), the MFM constraint, and (2, ∞), the spacing rule, share the supergolden growth through the factor z³ − z² − 1.
tags: [concept, castle, castle-type, fibonacci, fibonacci-tower, fibonacci-word, sturmian, balanced-word, totient, sub-family, maximal-independent-set, padovan, plastic-number, narayana-cows, supergolden, run-length-limited, capacity, oeis]
sources: [project-euler-502]
created: 2026-10-04
updated: 2026-10-06
---

# Fibonacci castle sub-families

A Fibonacci castle ([[fibonacci-castle](pages/fibonacci-castle.md)]) is determined by its **Fibonacci tower**, its second row read as a string of 0s and 1s with a 1 at each height-2 column and no two adjacent 1s. A rule on the tower cuts out a sub-family. On this page every count is a count of **castles** of width `w` and exact height 2. A rule may admit the all-zero tower; that tower is counted among the towers but never among the castles, since the flat row it would give has no column at height 2.

## The Fibonacci word and balanced towers

### Fibonacci-word castles

A **Fibonacci-word castle** is a Fibonacci castle whose tower occurs somewhere in the infinite Fibonacci word `0, 1, 0, 0, 1, 0, 1, 0, 0, 1, …`, the limit of the substitution `0 → 01`, `1 → 0` started from `0`.[^a003849] The Fibonacci word is a Sturmian word,[^a003849] and a Sturmian word has exactly `n + 1` distinct factors (pieces) of each length `n`: Sturmian words are the binary words of block complexity `c(n) = n + 1`, the aperiodic words of minimal complexity.[^berstel-c] So there are `w + 1` Fibonacci-word towers of length `w`. The word contains `00` but never `000` (its 1s are isolated and the runs of 0s between them have length 1 or 2), so the all-zero tower is a factor only at lengths 1 and 2.[^exec] The Fibonacci-word castles therefore number

| `w` | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Fibonacci-word castles | 1 | 2 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 |

that is `w` at `w = 1, 2` and `w + 1` from `w = 3` on: linear growth.[^exec]

- **Example.** The prefix of length 56 is the tower of a Fibonacci castle of width 56, on [[fibonacci-castle](pages/fibonacci-castle.md)]. Its height-2 columns, counted from 1, are at the upper Wythoff numbers `⌊kφ²⌋ = 2, 5, 7, 10, …` (A001950); counted from 0 they are `1, 4, 6, 9, …`, the Wythoff compound sequence A003622, of which the Fibonacci word is the characteristic function.[^a003849][^a003622]

### Balanced castles

A 0/1 string is **balanced** if any two of its factors of equal length contain numbers of 1s that differ by at most 1.[^berstel-bal] A **balanced castle** is a Fibonacci castle whose tower is balanced. Three facts about balanced binary words carry over:

- the finite balanced words are exactly the finite Sturmian words, the factors of infinite Sturmian words;[^berstel-28]
- the balanced binary words of length `n` number `B(n) = 1 + Σ_{i=1}^{n} (n + 1 − i) φ(i)`, with `φ` Euler's totient; the first proof is Lipatov's (1982);[^berstel-32][^a005598]
- `B(n) = n³/π² + O(n²)`.[^berstel-36]

**Counting the balanced towers** (own reasoning). A balanced string cannot contain both `00` and `11`, since those two factors of length 2 differ by two 1s. Exchanging 0 and 1 preserves balance, so it pairs the balanced strings with no `11` with the balanced strings with no `00`, and the strings with neither are the two alternating ones, `0101…` and `1010…`. Hence the balanced strings with no `11`, the balanced Fibonacci towers, number `(B(n) + 2)/2 = B(n)/2 + 1`. The all-zero tower is balanced, so

```
#{balanced castles of width w}  =  B(w)/2  =  A049703(w),        ~  w³ / (2π²).
```

| `w` | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `B(w)` (A005598) | 2 | 4 | 8 | 14 | 24 | 36 | 54 | 76 | 104 | 136 | 178 | 224 |
| balanced castles (A049703) | 1 | 2 | 4 | 7 | 12 | 18 | 27 | 38 | 52 | 68 | 89 | 112 |
| all Fibonacci castles | 1 | 2 | 4 | 7 | 12 | 20 | 33 | 54 | 88 | 143 | 232 | 376 |

Every Fibonacci castle up to width 5 is balanced. The first unbalanced ones have width 6, for example `(2, 1, 2, 1, 1, 1)`, whose tower `101000` contains the factors `101` and `000`.[^exec] A049703 is defined on the OEIS only as `A005598(n)/2`, with no combinatorial reading; the balanced castles give it one ([[castle-sequence-catalogue](pages/castle-sequence-catalogue.md)]).[^a049703]

### The chain

```
Fibonacci-word castles  ⊂  balanced castles  ⊂  Fibonacci castles
      w + 1                   ~ w³/(2π²)          F_{w+2} − 1 ~ (φ²/√5) φ^w
```

Every factor of the Fibonacci word is balanced, since the word is Sturmian, so the first inclusion holds.[^berstel-28] The balanced castles are the union over all Sturmian words, not only the Fibonacci word: each balanced tower is a factor of some infinite Sturmian word, of whatever slope.[^berstel-28] The 56-column castle from the Fibonacci word lies in the innermost family. It is not maximal: its last height-2 column is column 54, so column 56 could still be raised without creating two adjacent height-2 columns.[^exec]

## Gap lengths

### Towers by their gaps

A tower with at least one 1 is fixed by three pieces of data: the number `a ≥ 0` of leading 0s, the gaps `g_1, …, g_{m−1} ≥ 1` between consecutive 1s (the runs of height-1 columns between height-2 columns), and the number `b ≥ 0` of trailing 0s; its length is `a + m + Σ g_i + b`. Restricting the gaps to a set `G` and the two end runs to sets `L` and `R` cuts out a sub-family whose castles have generating function

```
Σ_w #{castles of width w} x^w  =  L(x) · x · R(x) / (1 − Σ_{g ∈ G} x^{g+1}),      L(x) = Σ_{a ∈ L} x^a,  R(x) = Σ_{b ∈ R} x^b
```

(own reasoning: a castle is a first 1, then a sequence of blocks "gap then 1", with the end runs on either side). The count is C-finite, and it grows like the largest root of `1 = Σ_{g ∈ G} x^{−(g+1)}`; the end sets change the constant, not the growth. All of the parent family is `L = R = {0, 1, 2, …}`, `G = {1, 2, …}`, giving `x/((1 − x)(1 − x − x²))` and `F_{w+2} − 1`.[^exec]

### Maximal castles

A **maximal castle** is a Fibonacci castle in which no further column can be raised to height 2 without making two height-2 columns adjacent: every gap is 1 or 2, and each end run is 0 or 1. Its tower is a maximal independent set of the path on the `w` columns. Example: `(2, 1, 1, 2, 1)`, tower `10010`; `(2, 1, 1, 1, 2)` is not maximal, since its middle column could be raised.

```
#{maximal castles of width w}  =  A000931(w + 6)  =  1, 2, 2, 3, 4, 5, 7, 9, 12, 16, 21, 28, …,
```

the Padovan numbers, which A000931 lists as the number of maximal independent vertex sets of the path graph;[^a000931] the generating function is `x(1 + x)²/(1 − x² − x³)`. They grow like the plastic number `ψ ≈ 1.3247`, the real root of `x³ = x + 1` ([[plastic-number](pages/plastic-number.md)]).[^exec] The 56-column castle from the Fibonacci word is not maximal: it ends in two height-1 columns, and the last of them could be raised.

### Spaced castles

A **spaced castle** is a Fibonacci castle whose height-2 columns are at least 3 apart: every gap is at least 2, equivalently the tower has no `101`. Example: `(2, 1, 1, 2)`, tower `1001`; `(2, 1, 2)` is not spaced. The binary words of length `n` with at least two 0s between successive 1s number `A000930(n + 2)` (Narayana's cows),[^a000930] and removing the all-zero word,

```
#{spaced castles of width w}  =  A000930(w + 2) − 1  =  A077868(w − 1)  =  1, 2, 3, 5, 8, 12, 18, 27, 40, 59, …,
```

growing like the supergolden ratio `≈ 1.4656`, the real root of `x³ = x² + 1`.[^a077868][^exec]

**Spaced castles and Fibonacci castles by area** (own reasoning). A Fibonacci castle with `n` cells is a tiling of a strip of `n` cells by squares and dominoes that uses a domino and has no two dominoes side by side (two adjacent height-2 columns would be adjacent dominoes). Mark each of the `n − 1` internal cell boundaries with 1 if it lies inside a domino, as on [[fibonacci-castle](pages/fibonacci-castle.md)] for all castles of exact height 2. Adjacent dominoes put marks two boundaries apart (`101`), and non-adjacent dominoes put them at least three apart, so this is a bijection from the Fibonacci castles with `n` cells onto the spaced castles of width `n − 1`. That is why the q-Fibonacci castles by number of cells ([[q-fibonacci-castle](pages/q-fibonacci-castle.md)]) and the spaced castles by width share the counts `1, 2, 3, 5, 8, 12, …`.[^exec] The spacing rule on [[tower-spacing-castles](pages/tower-spacing-castles.md)] is different: it spaces raised regions, which may be wide, by wide valleys.

### Run-length-limited castles

A **`(d, k)`-RLL castle** is a Fibonacci castle whose tower is `(d, k)`-run-length-limited: the runs of 0s between successive 1s have length at least `d`, and every run of 0s, the end runs included, has length at most `k`.[^mrs-def] With `d ≥ 1` every such castle is a Fibonacci castle. Example: `(2, 1, 1, 1, 2)`, tower `10001`, is a `(1, 3)`-RLL castle; `(1, 1, 1, 1, 2)` is not, since its leading run of four 0s exceeds `k = 3`.

| `(d, k)` | where the constraint is used | castles, `w = 1..10` | growth | capacity `log₂` (Marcus-Roth-Siegel Table 3.1) |
|---|---|---|---|---|
| `(1, 3)` | flexible disk drives (MFM) | 1, 2, 4, 7, 10, 15, 22, 32, 47, 69 | `1.4656` (supergolden) | `.5515` |
| `(1, 7)` | magnetic tape | 1, 2, 4, 7, 12, 20, 33, 54, 86, 138 | `1.6013` | `.6793` |
| `(2, 7)` | magnetic tape | 1, 2, 3, 5, 8, 12, 18, 27, 38, 54 | `1.4313` | `.5174` |
| `(2, 10)` | CD, DVD | 1, 2, 3, 5, 8, 12, 18, 27, 40, 59 | `1.4558` | `.5418` |
| `(2, ∞)` | the spaced castles | 1, 2, 3, 5, 8, 12, 18, 27, 40, 59 | `1.4656` (supergolden) | `.5515` |
| `(1, ∞)` | all Fibonacci castles | 1, 2, 4, 7, 12, 20, 33, 54, 88, 143 | `φ ≈ 1.6180` | `.6942` |

The capacity of a constraint is `log₂` of the growth of its sequences, and the castle counts grow at the same rate.[^mrs-table][^exec] The uses are those listed on [[fibonacci-castle](pages/fibonacci-castle.md)]. Of these counts, only the `(1, 3)` row is in the OEIS (below); `(1, 7)`, `(2, 7)` and `(2, 10)` have no match (searched 2026-10-04).

**`(1, 3)` and `(2, ∞)` have the same growth.** Marcus, Roth and Siegel give the growth of `(d, k)`-RLL as the largest positive root of `z^{k+2} − z^{k+1} − z^{k−d+1} + 1 = 0`.[^mrs-table] At `(1, 3)` this is `z⁵ − z⁴ − z³ + 1 = (z − 1)(z + 1)(z³ − z² − 1)`, whose largest root is the supergolden ratio, the growth of the spaced castles: the MFM constraint and the spacing rule have equal capacity, `.5515` in the table (own factorization, checked by SymPy).[^exec]

**The `(1, 3)` castles, A003410 and A226136.** The same factor `1 + x` cancels from the `(1, 3)` generating function: `1 + x + x² + x³ = (1 + x)(1 + x²)` and `1 − x² − x³ − x⁴ = (1 + x)(1 − x − x³)`, so

```
Σ_w #{(1, 3)-RLL castles of width w} x^w  =  x(1 + x)(1 + x²)² / (1 − x − x³),
```

and the counts satisfy `a(w) = a(w − 1) + a(w − 3)` from `w = 7`, Narayana's cows' recurrence. The towers are the binary words with no `11` and no `0000`, which A003410 counts (`(1 + x)(1 + x²)/(1 − x − x³)`, `1, 2, 3, 5, 7, 10, 15, 22, …`).[^a003410] For `w ≥ 4` every such word contains a 1, so the `(1, 3)`-RLL castles of width `w` number exactly `A003410(w)`; at `w ≤ 3` the all-zero word is one of them and the castles number `A003410(w) − 1`. The castle generating function above is `A003410`'s minus `1 + x + x² + x³`. It is also the generating function that A226136, the positions of the positive integers in an ordering of the rational numbers generated by `x → x + 1` and `x → −1/x`, lists as a conjecture, and A226136 agrees with `A003410(n)` for `n = 4..35`, all its listed terms.[^a226136][^exec] So that conjecture is equivalent to `A226136(n) = A003410(n)` for `n ≥ 4`; the castle count is proved, the equality with A226136 is not. That equivalent form, "Conjecture: a(n) = A003410(n) for n >= 4" with `Cf. A003410`, was submitted to A226136 on 2026-10-06 and awaits approval.

## Computation

The checks behind the footnotes:

```python
from itertools import product
from math import gcd
def totient(k): return sum(1 for i in range(1, k + 1) if gcd(i, k) == 1)
def B(n): return 1 + sum((n + 1 - i) * totient(i) for i in range(1, n + 1))
def towers(n): return [t for t in product((0, 1), repeat=n) if all(not (t[i] == 1 == t[i+1]) for i in range(n - 1))]
def balanced(t):
    return all(max(s) - min(s) <= 1 for L in range(1, len(t) + 1) for s in [[sum(t[i:i+L]) for i in range(len(t) - L + 1)]])
word = "0"
while len(word) < 500: word = "".join("01" if ch == "0" else "0" for ch in word)
W = tuple(int(ch) for ch in word)
assert "000" not in word and "11" not in word
for n in range(1, 16):
    T = towers(n)
    factors = {W[i:i+n] for i in range(len(W) - n)}
    assert len(factors) == n + 1 and all(f in T and balanced(f) for f in factors)
    assert sum(1 for f in factors if 1 in f) == (n if n <= 2 else n + 1)
    assert sum(1 for t in T if 1 in t and balanced(t)) == B(n) // 2
print([B(n) // 2 for n in range(1, 13)])   # 1, 2, 4, 7, 12, 18, 27, 38, 52, 68, 89, 112

def gaps(t):                              # (leading 0s, gaps between 1s, trailing 0s)
    ones = [i for i, v in enumerate(t) if v]
    return ones[0], [ones[i+1] - ones[i] - 1 for i in range(len(ones) - 1)], len(t) - 1 - ones[-1]
def castles(n, ends, gap):
    return sum(1 for t in towers(n) if 1 in t and (lambda a, g, b: ends(a) and ends(b) and all(gap(x) for x in g))(*gaps(t)))
P = [1, 0, 0]                             # Padovan A000931
while len(P) < 30: P.append(P[-2] + P[-3])
N = [1, 1, 1]                             # Narayana's cows A000930
while len(N) < 30: N.append(N[-1] + N[-3])
for n in range(1, 16):
    assert castles(n, lambda a: a <= 1, lambda g: g in (1, 2)) == P[n + 6]                 # maximal
    assert castles(n, lambda a: True, lambda g: g >= 2) == N[n + 2] - 1                    # spaced
print([castles(n, lambda a: a <= 3, lambda g: 1 <= g <= 3) for n in range(1, 11)])        # (1, 3)-RLL
```

## Related Concepts

- [[fibonacci-castle](pages/fibonacci-castle.md)] - the parent family, its Fibonacci towers, and the 56-column castle from the Fibonacci word.
- [[castle-notation](pages/castle-notation.md)] - Fibonacci tower, balanced tower.
- [[castle-sequence-catalogue](pages/castle-sequence-catalogue.md)] - A049703 as an interlink candidate.
- [[castle-entropy](pages/castle-entropy.md)] - the parent family's `log₂ φ` bits per column; the two sub-families here grow polynomially, so they carry no positive entropy.

## Footnotes

[^a003849]: https://oeis.org/A003849 (fetched 2026-10-04) - "The infinite Fibonacci word (start with 0, apply 0->01, 1->0, take limit)."; comments "A Sturmian word." and "Characteristic function of A003622."; data `0, 1, 0, 0, 1, 0, 1, 0, 0, 1, …`, offset 0.
[^a003622]: https://oeis.org/A003622 (fetched 2026-10-04) - "The Wythoff compound sequence AA: a(n) = floor(n*phi^2) - 1, where phi = (1+sqrt(5))/2."; data `1, 4, 6, 9, 12, 14, 17, …`; the 1-indexed positions `⌊kφ²⌋` are https://oeis.org/A001950, "Upper Wythoff sequence (a Beatty sequence): a(n) = floor(n*phi^2)".
[^berstel-c]: https://ligm.univ-eiffel.fr/~berstel/Articles/2007SturmianThessalonique.pdf (J. Berstel, "Sturmian and Episturmian Words (A Survey of Some Recent Results)", CAI 2007, LNCS 4728, pp. 23-47, read 2026-10-04) §2.1 p.25 - an aperiodic episturmian word has "exactly one right special factor of each length", strict episturmian words with right special factors of degree `k` have `c_w(n) = kn + 1`, and "Strict episturmian words over two letters are exactly the Sturmian words. These are aperiodic words of minimal block complexity"; Theorem 1 (Morse-Hedlund, Coven-Hedlund) - "An infinite word w is eventually periodic if and only if there exists an integer n ≥ 1 such that c_w(n) ≤ n."
[^berstel-bal]: Berstel 2007 (as in [^berstel-c]) §4 p.32 - "A finite word w is balanced if, for each pair of factors x, y of w of equal length, ||x|_a − |y|_a| ≤ 1 for the letter a."
[^berstel-28]: Berstel 2007 (as in [^berstel-c]) §5 p.35 - "A finite Sturmian word is a word which is a factor of some (infinite) Sturmian word."; Proposition 28 - "A finite binary word is balanced if and only if it is a finite Sturmian word."
[^berstel-32]: Berstel 2007 (as in [^berstel-c]) §5 p.36, Proposition 32 - "The number of balanced binary words of length n is 1 + Σ_{i=1}^{n} (n + 1 − i)φ(i) where φ is the Euler's totient function. The first proof of this formula is perhaps [47]", reference [47] being E. P. Lipatov, "A classification of binary collections and properties of homogeneity classes", Problemy Kibernet. 39 (1982) 67-84.
[^berstel-36]: Berstel 2007 (as in [^berstel-c]) §5 p.36 - "usual number theory shows that g_1(n) = N³/π² + O(n²)", `g_1(n)` being the number of balanced words of length `n`.
[^a005598]: https://oeis.org/A005598 (fetched 2026-10-04) - "a(n) = 1 + Sum_{i=1..n} (n-i+1)*phi(i)."; comment "Also, the number of finite Sturmian words of length n."; data `1, 2, 4, 8, 14, 24, 36, 54, 76, 104, …`, offset 0.
[^a049703]: https://oeis.org/A049703 (fetched 2026-10-04) - "a(0) = 0; for n>0, a(n) = A005598(n)/2."; data `0, 1, 2, 4, 7, 12, 18, 27, 38, 52, 68, 89, …`; formulas and crossrefs only, no comment giving a combinatorial interpretation.
[^a000931]: https://oeis.org/A000931 (fetched 2026-10-04) - "Padovan sequence (or Padovan numbers): a(n) = a(n-2) + a(n-3) with a(0) = 1, a(1) = a(2) = 0."; comment "For n > 6, a(n) is the number of maximal matchings in the (n-5)-path graph, maximal independent vertex sets and minimal vertex covers in the (n-6)-path graph, [...]".
[^a000930]: https://oeis.org/A000930 (fetched 2026-10-04) - "Narayana's cows sequence: a(0) = a(1) = a(2) = 1; thereafter a(n) = a(n-1) + a(n-3)."; comment "a(n+2) equals the number of binary words of length n, having at least two zeros between every two successive ones. - _Milan Janjic_, Feb 07 2015".
[^a077868]: https://oeis.org/A077868 (fetched 2026-10-04) - "Expansion of 1/((1-x)*(1-x-x^3))."; data `1, 2, 3, 5, 8, 12, 18, 27, 40, 59, 87, …`, offset 0.
[^mrs-def]: https://ronny.cswp.cs.technion.ac.il/wp-content/uploads/sites/54/2016/05/chapters1-9.pdf (B. H. Marcus, R. M. Roth, P. H. Siegel, "An Introduction to Coding for Constrained Systems", 5th ed. lecture notes, October 2001) p.3 §1.2 - "the runs of 0's have length at most k (the k-constraint)" and "the runs of 0's between successive 1's have length at least d (the d-constraint)"; the uses of the constraints as on [[fibonacci-castle](pages/fibonacci-castle.md)].
[^mrs-table]: Marcus-Roth-Siegel (as in [^mrs-def], read 2026-10-04) p.74 Example 3.3 - for `0 ≤ d ≤ k < ∞`, "λ(A_G(d,k)) is the largest positive solution of the equation z^{k+2} − z^{k+1} − z^{k−d+1} + 1 = 0", and "Table 3.1 (taken from [Imm91]) contains the capacity values of several (d, k)-RLL constrained systems"; Table 3.1 [synthesis] - column `d = 1`: `.5515` at `k = 3`, `.6793` at `k = 7`, `.6942` at `k = ∞`; column `d = 2`: `.5174` at `k = 7`, `.5418` at `k = 10`, `.5515` at `k = ∞`; capacity is `log λ` (Example 3.2, "capacity log λ ≈ .6942" for `λ = (1+√5)/2`), base 2.
[^a003410]: https://oeis.org/A003410 (fetched 2026-10-04) - "Expansion of (1+x)(1+x^2)/(1-x-x^3)."; comment "a(n) is the number of binary words of length n that have no pair of adjacent 1's and have no 0000 subwords." (E. Deutsch, Feb 15 2010); data `1, 2, 3, 5, 7, 10, 15, 22, 32, 47, …`, offset 0.
[^a226136]: https://oeis.org/A226136 (fetched 2026-10-04) - "Positions of the positive integers in the ordering of rational numbers as generated by the rules: 1 is in S, and if nonzero x is in S, then x+1 and -1/x are in S."; formula "Conjecture: a(n) = a(n-1)+a(n-3) for n>6. G.f.: -x*(x+1) * (x^2+1)^2 / (x^3+x-1). - _Colin Barker_, Jul 03 2013"; data `1, 2, 4, 7, 10, 15, 22, 32, 47, 69, 101, …`.
[^exec]: Verified by execution (Python 3, SymPy, 2026-10-04), block above and a SymPy check of the generating function: the `(1, 3)` generating function equals `x(1+x)(1+x²)²/(1−x−x³)` and its first 35 coefficients equal the 35 listed terms of A226136; the gap generating function matches brute force for the parent family, the maximal, spaced and `(1, 3)`, `(1, 7)`, `(2, 7)`, `(2, 10)`-RLL castles for `w ≤ 14`; maximal castles number `A000931(w + 6)` and spaced castles `A000930(w + 2) − 1` for `w ≤ 15`; the domino-boundary map is a bijection from the Fibonacci castles with `n` cells onto the spaced castles of width `n − 1` for `n = 2..15`; the growth rates are the largest roots `1.3247, 1.4656, 1.6013, 1.4313, 1.4558` and `log₂` of them match Table 3.1; `z⁵ − z⁴ − z³ + 1 = (z − 1)(z + 1)(z³ − z² − 1)`. Also: for `n ≤ 15` the Fibonacci word (generated by the substitution, 500 letters) has `n + 1` factors of length `n`, all of them balanced Fibonacci towers, with the all-zero tower among them only for `n ≤ 2`, and the word has no `000`; the balanced Fibonacci castles of width `w ≤ 15` number `B(w)/2`; every Fibonacci castle of width at most 5 is balanced and `(2, 1, 2, 1, 1, 1)` is not; the 56-letter prefix has its last 1 at position 54.
