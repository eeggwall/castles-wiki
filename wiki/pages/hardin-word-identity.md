---
title: The Hardin word identity - even-sector towers are 2^L times no-local-maximum words
category: Analyses
summary: Proof that for k = 4m+2 the signed count of height-≤k towers with even last column equals 2^L times the number of (L+1)-letter words over {0..m} in which every nonzero letter is ≤ a neighbor (A005251, A202882, A203094, A203184). The word automaton has 2m+1 states and characteristic polynomial H_(2m+1); an explicit unimodular 0/1 change of basis S conjugates it to the halved even-sector transfer matrix and carries start and end vectors across. Verified symbolically for every m ≤ 8; the entries of all three matrices are given in closed form, so the general case is a finite entrywise check. Hardin's three "empirical" OEIS recurrences follow.
tags: [analysis, castle, signed-tower-count, transfer-matrix, bijection, hardin, oeis, words, sympy, verification, proof]
sources: [oeis-mining-pe502, project-euler-502-castle-factoring]
created: 2026-09-16
updated: 2026-09-26
---

# The Hardin word identity

## Statement

For `m ≥ 0`, let `k = 4m + 2` and let `W_m(n)` be the number of words `w ∈ {0, 1, …, m}^n` in which every nonzero letter is at most one of its neighbors (`w_i ≤ w_{i−1}` or `w_i ≤ w_{i+1}`; equivalently, no nonzero letter is a strict local maximum). Then for every `L ≥ 0`

```
P_even(k, L)  :=  Σ_{towers of height ≤ k on a length-L base, last column even} (−1)^{blocks}  =  2^L · W_m(L + 1).
```

`W_0 = 1`; `W_1(n) = A005251(n+2)` (binary strings with no isolated `1`); `W_2, W_3, W_4` are Hardin's A202882, A203094, A203184.[^3] The identity was found numerically on [[tower-parity-sectors](pages/tower-parity-sectors.md)]; this page proves it, for each `m ≤ 8` outright and for general `m` up to one finite entrywise check, by exhibiting the two sides as the same transfer matrix in two bases.

## A worked example (m = 1, k = 6)

Before any matrices, see the identity hold on the smallest nontrivial case. For `m = 1`, `k = 4·1 + 2 = 6`, and the words are binary strings with **no isolated `1`** — every `1` has a neighbor `1`, boundaries counting as `0`. Word side first, by brute force:

```python
from itertools import product

def is_hardin_word(w):                    # no nonzero letter is a strict local maximum
    for i, a in enumerate(w):
        if a == 0: continue
        if (i > 0 and w[i-1] >= a) or (i+1 < len(w) and w[i+1] >= a): continue
        return False
    return True

def W_bruteforce(m, n):
    return sum(1 for w in product(range(m+1), repeat=n) if is_hardin_word(w))
```

```
>>> [W_bruteforce(1, n) for n in range(1, 9)]            # = A005251(n+2)
[1, 2, 4, 7, 12, 21, 37, 65]
>>> [''.join(map(str, w)) for w in product(range(2), repeat=3) if is_hardin_word(w)]
['000', '011', '110', '111']
```

The four length-3 words with no isolated `1` are `000, 011, 110, 111` — `W_1(3) = 4 = A005251(5)`. Tower side, the even-last-column sector of the signed transfer matrix:

```python
import sympy as sp

def sector_even(k, Lmax):                 # the even-last-column sector: P_even(k, 0..Lmax)
    M = sp.Matrix(k+1, k+1, lambda a, b: 1 if a <= b else (-1)**(a-b))
    row = sp.Matrix([[1] + [0]*k])
    ve  = sp.Matrix([1 if b % 2 == 0 else 0 for b in range(k+1)])
    E = []
    for L in range(Lmax+1):
        E.append(int((row*ve)[0])); row = row*M
    return E
```

```
>>> sector_even(6, 7)                      # P_even(6, L) for L = 0..7
[1, 4, 16, 56, 192, 672, 2368, 8320]
>>> [e == 2**L * W_bruteforce(1, L+1) for L, e in enumerate(sector_even(6, 7))]
[True, True, True, True, True, True, True, True]
```

`1, 4, 16, 56, … = 2^L · A005251(L+3)` term for term — the whole identity, in numbers, before any change of basis appears.[^4]

## The two transfer matrices

**Tower side.** [[tower-parity-sectors](pages/tower-parity-sectors.md)] writes the even sector as `P_even(k, L) = e_0ᵀ Mᴸ v⁺` with `M = M_k` the signed transfer matrix and `v⁺ = [b even]`, and shows the sector is the `+1` eigenspace of the involution `JD`. A basis of that eigenspace is

```
f_c  =  e_c + (−1)^c e_{k−c},        c = 0, 1, …, 2m        (k/2 = 2m+1 is odd, so no fixed middle vector)
```

Writing `f_cᵀ M = Σ_d R[c,d] f_dᵀ` gives a `(2m+1) × (2m+1)` integer matrix `R` with **every entry even**, and the halved matrix has the closed form[^1]

```
(R/2)[c, d]  =  [c even]·(−1)^d·[d ≤ c]  +  [d even]·[d > c].
```

```
>>> sector_half(2)                       # m = 2, k = 10
Matrix([[1, 0, 1, 0, 1], [0, 0, 1, 0, 1], [1, -1, 1, 0, 1], [0, 0, 0, 0, 1], [1, -1, 1, -1, 1]])
```

Since `e_0 = f_0/2 + (odd-sector part)` and `f_dᵀ v⁺ = 2·[d even]`, the sector sequence is

```
P_even(k, L)  =  2^L · e_0ᵀ (R/2)ᴸ 𝟙_even,        𝟙_even = ([d even])_{d=0..2m}.
```

The factor `2^L` is now visible as an exact rescaling of the sector matrix, not an asymptotic.

**Word side.** Read a word left to right, remembering the last letter and whether it is still *pending* - a nonzero letter that is larger than its left neighbor, and therefore needs its right neighbor to be at least as large. States: `(0, +)` and `(a, ±)` for `a = 1..m` (`+` satisfied, `−` pending), `2m + 1` in all. From `(a, flag)` read `b`: forbidden if `flag = −` and `b < a`; the new state is `(0, +)` if `b = 0`, `(b, +)` if `0 < b ≤ a`, `(b, −)` if `b > a`. Start in `(0, +)` (a virtual left neighbor `0`), end in any satisfied state:

```python
def word_states(m): return [(0, '+')] + [(a, s) for a in range(1, m+1) for s in ('+', '-')]

def word_matrix(m):
    S = word_states(m); idx = {s: i for i, s in enumerate(S)}
    W = sp.zeros(len(S), len(S))
    for (a, flag) in S:
        for b in range(m+1):
            if flag == '-' and b < a: continue
            new = (0, '+') if b == 0 else ((b, '+') if b <= a else (b, '-'))
            W[idx[(a, flag)], idx[new]] += 1
    return W, S
```

```
>>> word_matrix(2)[0]                    # states (0,+), (1,+), (1,-), (2,+), (2,-)
Matrix([[1, 0, 1, 0, 1], [1, 1, 0, 0, 1], [0, 1, 0, 0, 1], [1, 1, 0, 1, 0], [0, 0, 0, 1, 0]])
>>> W_m(n) = start · W^n · end  ==  brute-force count, m = 1, 2, 3, n <= 7
True
```

The "pending" flag, read on one word (`m = 1`, states `(0,+)`, `(1,+)`, `(1,−)`): **`011` is accepted** — start `(0,+)` → read `0` → `(0,+)` → read `1` (bigger than the left neighbor `0`, so it *owes* its right neighbor) → `(1,−)` pending → read `1` (≥ `1`) → `(1,+)` satisfied, and the word ends in a `+` state. **`010` is rejected** — start `(0,+)` → `(0,+)` → `(1,−)` pending → read `0`, but a pending `1` needs a right neighbor `≥ 1`, so `0` is forbidden. A pending letter is one that has not yet proved it isn't a strict local maximum; the word is valid iff every letter pays that debt before the word ends.

So `W_m(L+1) = (start·W) Wᴸ end`. Both sides of the identity are `(row vector)·(matrix)ᴸ·(column vector)` on `2m+1` states.

## The change of basis

Define the `(2m+1) × (2m+1)` matrix `S` with rows indexed by sector coordinates `c` and columns by word states `(b, flag)`:

```
S[0,      (b, flag)] = 1   iff  (b, flag) = (0, +)  or  flag = −
S[2a − 1, (b, flag)] = 1   iff  flag = −  and  b ≥ a                    (a = 1..m)
S[2a,     (b, flag)] = 1   iff  (b, flag) = (a, +)  or  (flag = −  and  b > a)
```

- odd sector coordinates are the cumulative sets "pending with letter `≥ a`"; even ones add the single satisfied state `(a, +)`.

All three matrices in full, for `m = 1` (the smallest case — three states `(0,+)`, `(1,+)`, `(1,−)`):

```
>>> sector_half(1)                     # R/2, the tower side
Matrix([[1, 0, 1], [0, 0, 1], [1, -1, 1]])
>>> word_matrix(1)[0]                  # W, the word side
Matrix([[1, 0, 1], [1, 1, 0], [0, 1, 0]])
>>> S_pattern(1)                       # the change of basis
Matrix([[1, 0, 1], [0, 0, 1], [0, 1, 0]])
>>> sp.det(S_pattern(1)), sector_half(1)*S_pattern(1) == S_pattern(1)*word_matrix(1)[0]
(-1, True)
```

`(R/2)S = SW` is visible entry by entry in `3×3`, and `det S = −1` (unimodular) makes `S` an honest change of basis. The `m = 2` case is the `5×5` matrix below.

```
>>> S_pattern(2)
Matrix([[1, 0, 1, 0, 1], [0, 0, 1, 0, 1], [0, 1, 0, 0, 1], [0, 0, 0, 0, 1], [0, 0, 0, 1, 0]])
>>> S_pattern(2).inv()
Matrix([[1, -1, 0, 0, 0], [0, 0, 1, -1, 0], [0, 1, 0, -1, 0], [0, 0, 0, 0, 1], [0, 0, 0, 1, 0]])
```

`S` is a 0/1 matrix with determinant `±1`, and its inverse is a difference operator (entries `0, ±1`). It satisfies the three equations that make the identity a one-line computation:[^2]

```
(R/2) · S  =  S · W,          e_0ᵀ · S  =  start · W,          S · end  =  𝟙_even.
```

```
m=0: (R/2)S = SW: True   e0 S = start W: True   S end = 1_even: True   det S = 1
m=1: (R/2)S = SW: True   e0 S = start W: True   S end = 1_even: True   det S = -1
m=2: ...                                                                 det S = 1
  ⋮
m=8: (R/2)S = SW: True   e0 S = start W: True   S end = 1_even: True   det S = 1
```

**Proof of the identity, given the three equations.** `(R/2)ᴸ S = S Wᴸ`, hence

```
e_0ᵀ (R/2)ᴸ 𝟙_even  =  e_0ᵀ (R/2)ᴸ S · end  =  e_0ᵀ S · Wᴸ · end  =  (start·W) Wᴸ end  =  W_m(L+1),
```

and multiplying by `2^L` gives `P_even(k, L) = 2^L W_m(L+1)`. ∎

The three equations were verified symbolically for every `m ≤ 8`. All three matrices are given entrywise above, so the general-`m` statement is a finite case analysis on the indices `(c, b, flag)` that has not been written out; on the wiki the identity is a theorem for `m ≤ 8` and an explicitly-reduced conjecture beyond.

## What the similarity says combinatorially

`S` is unimodular, so `S⁻¹` is an integer matrix and the sector row vector after `L` columns is an integer combination of word-state counts:

```
e_0ᵀ (R/2)ᴸ  =  (start · W^{L+1}) · S⁻¹.
```

Reading the columns of `S⁻¹` (differences of consecutive cumulative sets), the **sector coordinate `2a` after `L` columns equals the number of words of length `L+1` ending in the satisfied state `(a, +)` minus the number ending pending in `(a, −)`**, and coordinate `2a − 1` is the number ending pending in `(a, −)` minus the number ending pending in `(a+1, −)`. Each sector coordinate is itself a signed tower count (over towers whose last column is `c` or `k − c`, with the `(−1)^c` weight, divided by `2^L`), so the identity holds state by state: the signed height-pair statistics of towers are the difference statistics of pending letters in words. A genuinely bijective (sign-reversing-involution) proof would turn this equality of state vectors into a matching of objects; the transfer-matrix proof does not need it.

## Consequences for Online Encyclopedia of Integer Sequences (OEIS)

- The word automaton has characteristic polynomial `H_{2m+1}(μ) = Σ_i (−1)^i C(⌊(2m+1+i)/2⌋, i) μ^{2m+1−i}` for every `m ≤ 8` (symbolic), so the recurrences Hardin recorded as "Empirical" on **A202882** (`m = 2`), **A203094** (`m = 3`) and **A203184** (`m = 4`) are the characteristic-polynomial recurrences of a 5-, 7-, 9-state automaton, hence proved. The odd-index `H` satisfy `H_{2m+1} = (1 + 2μ²) H_{2m−1} − μ⁴ H_{2m−3}`, and `det(μI − W_m)` satisfies the same recurrence for `m ≤ 8`, which is the route to a general proof by cofactor expansion.[^2]
- Each of these sequences now has a second interpretation: `2^{−L}` times the even-last-column signed tower count at height `4m + 2`, or in Hardin's indexing, `a(n) = P_even(4m+2, n−1) / 2^{n−1}`. Submission of the interpretation and the proved recurrences is a human act ([[oeis-cross-referencing](pages/oeis-cross-referencing.md)]).

## Snippet index

| snippet | teaches |
|---|---|
| `word_matrix(m)` | turn a local constraint on words into a finite automaton with a "pending" flag; count by matrix powers |
| `sector_half(m)` | restrict a matrix to an invariant subspace in an explicit basis and read off integer entries |
| `S_pattern(m)` + three equations | prove two C-finite sequences equal by conjugating their transfer matrices and matching boundary vectors |
| `sp.solve` on `R S = S W` | find the similarity first as an unknown matrix; the 0/1 pattern is then guessed and re-verified |

## Appearances in Sources

- [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] - the `P(k, ·)` family this identity decomposes.
- [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] - the block-count formula behind `M_k`.

## Related Concepts

- [[tower-parity-sectors](pages/tower-parity-sectors.md)] - the sector decomposition and the closed-form factor `H_d` this page's automaton realizes.
- [[plastic-number](pages/plastic-number.md)] - `m = 1`: `H_3` is the minimal polynomial of `ψ²`, and `W_1` is A005251.
- [[signed-tower-count](pages/signed-tower-count.md)] - `P(k, L)` and its OEIS rows.
- [[castle-eigenvalue-oeis-crosswalk](pages/castle-eigenvalue-oeis-crosswalk.md)] - where `2^L · A005251(L+3)` first appeared as the plastic component of `P(6, L)`.
- [[castle-sign](pages/castle-sign.md)] - the sign `(−1)^{blocks}` and its column-by-column factorization.
- [[tower-word-language](pages/tower-word-language.md)] - the wiki's other word-automaton object; the pending-flag construction here is the same technique.
- [[tower-spacing-castles](pages/tower-spacing-castles.md)] - the `g = 2` tower-spacing castles give the Hardin sequences (A202882 / A203094 / A203184) a plain *unsigned* geometric interpretation ("towers ≥ 2 apart" = "no isolated peak"), a third route alongside the signed identity here.
- [[hardin-identity-seminar](pages/hardin-identity-seminar.md)] - the classroom version: the `m = 1` case in seven stops, with runnable `sector_half` and `S_pattern`.


## Footnotes

[^1]: Verified by execution (SymPy 1.14): for `m = 0..8`, `R = (Bᵀ M_k) B (Bᵀ B)⁻¹` with `B` the matrix of the `f_c`, all entries of `R` even, and `R/2` equal to the stated closed form entrywise. `P_even(k, L) = 2^L e_0ᵀ (R/2)ᴸ 𝟙_even` re-checked against the direct sector sequences for `L ≤ 7`.

[^2]: Verified by execution (SymPy 1.14): `word_matrix(m)` counts agree with brute force for `m = 1, 2, 3`, `n ≤ 7`; `det(μI − W_m) = H_{2m+1}` for `m = 0..6` and the odd-index recurrence for `m ≤ 8`; `S_pattern(m)` satisfies `(R/2)S = SW`, `e_0ᵀ S = start·W`, `S·end = 𝟙_even`, `det S = ±1` for `m = 0..8`; the unique solution of the linear system for `S` at `m ≤ 3` (no free parameters) coincides with the pattern.

[^3]: https://oeis.org/A005251, https://oeis.org/A202882, https://oeis.org/A203094, https://oeis.org/A203184 (2026-09-16) - definitions and the "Empirical: a(n) = …" recurrence lines quoted on [[tower-parity-sectors](pages/tower-parity-sectors.md)].

[^4]: Verified by execution (SymPy 1.14, 2026-09-18): `W_bruteforce(1, ·) = [1, 2, 4, 7, 12, 21, 37, 65]` for `n = 1..8`, matching `A005251(n+2)`; the four length-3 no-isolated-`1` words are `000, 011, 110, 111`; `P_even(6, L) = [1, 4, 16, 56, 192, 672, 2368, 8320]` for `L = 0..7` equals `2^L · W_bruteforce(1, L+1)` term for term; and the `m = 1` matrices `R/2`, `W`, `S` with `det S = −1` and `(R/2)S = SW` are the three-state instance of [^2].
