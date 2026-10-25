---
title: The Hardin word identity - even-sector towers are 2^L times no-local-maximum words
category: Analyses
summary: For every m ≥ 0 and k = 4m + 2, the signed count of towers of height at most k with an even last column is P_even(k, L) = 2^L W_m(L + 1), where W_m(n) counts the words in {0, …, m}^n in which every nonzero letter is at most one of its neighbors (A005251, A202882, A203094, A203184). Proof - the even sector of the signed transfer matrix, halved, and a 2m + 1 state word automaton are conjugate by an explicit 0/1 matrix S with det S = (−1)^m, which also matches the start and end vectors. The automaton's characteristic polynomial is H_{2m+1}(μ) for m ≤ 10 (computed), so Hardin's "Empirical" recurrences on A202882, A203094, A203184 hold.
tags: [analysis, castle, signed-tower-count, transfer-matrix, bijection, hardin, oeis, words, sympy, verification, proof]
sources: [project-euler-502-castle-factoring]
created: 2026-09-16
updated: 2026-10-25
---

# The Hardin word identity

## Statement

For `m ≥ 0`, let `W_m(n)` be the number of words `w ∈ {0, 1, …, m}^n` in which every nonzero letter is at most one of its neighbors: `w_i ≤ w_{i−1}` or `w_i ≤ w_{i+1}`, with a virtual `0` beyond each end. Equivalently, no nonzero letter is a strict local maximum. `P_even(k, L)` is the sum of `(−1)^{blocks}` over the towers of height at most `k` on a base of length `L` whose last column has even height ([[castle-notation](pages/castle-notation.md)]); the empty tower, at `L = 0`, counts with last column 0.

**Theorem.** For every `m ≥ 0`, with `k = 4m + 2`, and every `L ≥ 0`,

```
P_even(k, L)  =  2^L · W_m(L + 1).                                             (1)
```

`W_0(n) = 1`, since the only word over `{0}` is `0^n`, and `P_even(2, L) = 2^L`. `W_1(n) = A005251(n+2)`, the binary strings with no isolated `1`. `W_2`, `W_3`, `W_4` are `A202882`, `A203094`, `A203184`, "n X 1 0..m arrays with every nonzero element less than or equal to some horizontal or vertical neighbor", with offset 1, so `W_m(n) = a(n)`.[^1] The identity was found numerically on [[tower-parity-sectors](pages/tower-parity-sectors.md)], which splits the signed tower count by the parity of the last column. The proof, in the sections *The tower side* to *The change of basis*, writes both sides of Equation (1) as the same transfer matrix in two bases.

## A worked example (m = 1, k = 6)

For `m = 1` the words are binary strings with no isolated `1`: every `1` has a neighbor `1`. The word side by brute force:

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

The four words of length 3 are `000, 011, 110, 111`, so `W_1(3) = 4 = A005251(5)`. The tower side, the even sector of the signed transfer matrix `M̃_k` of [[tower-parity-sectors](pages/tower-parity-sectors.md)] (entry `(−1)^{max(0, a−b)}` for a step from height `a` to height `b`):

```python
import sympy as sp

def sector_even(k, Lmax):                 # P_even(k, L) for L = 0..Lmax
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

So `P_even(6, L) = 2^L · A005251(L+3)` for `L ≤ 7`.[^2]

## The tower side

Write `P_even(k, L) = e_0ᵀ M̃_k^L v⁺` with `v⁺ = ([b even])_{b=0..k}`: the descent weights of `M̃_k` miss only the final drop from the last column to the base, which has even size when the last column is even. For even `k`, the involution `JD` (reverse the heights, flip the sign of odd heights) commutes with `M̃_k`, and the even sector is its `+1` eigenspace ([[tower-parity-sectors](pages/tower-parity-sectors.md)], Part 1). For `k = 4m + 2`, a basis of that eigenspace is

```
f_c  =  e_c + (−1)^c e_{k−c},        c = 0, 1, …, 2m,
```

since the middle height `k/2 = 2m + 1` is odd and `e_{2m+1}` lies in the `−1` eigenspace. Writing `f_cᵀ M̃_k = Σ_d R[c, d] f_dᵀ` defines a `(2m+1) × (2m+1)` integer matrix `R`.

**Lemma 1.** Every entry of `R` is even, and

```
(R/2)[c, d]  =  [c even] · (−1)^d · [d ≤ c]  +  [d even] · [d > c].           (2)
```

*Proof.* For `d ≤ 2m`, `f_d` is the only basis vector with a nonzero entry in coordinate `d`, so `R[c, d]` is entry `d` of `f_cᵀ M̃_k`, that is `(−1)^{max(0, c−d)} + (−1)^c (−1)^{max(0, k−c−d)}`. For `c, d ≤ 2m`, `k − c − d ≥ 2`, so the second term is `(−1)^c (−1)^{k−c−d} = (−1)^d`. If `d ≤ c`, `R[c, d] = (−1)^d ((−1)^c + 1) = 2[c even](−1)^d`; if `d > c`, `R[c, d] = 1 + (−1)^d = 2[d even]`.

At `m = 2`, `k = 10`:

```
R/2  =  [[1, 0, 1, 0, 1], [0, 0, 1, 0, 1], [1, −1, 1, 0, 1], [0, 0, 0, 0, 1], [1, −1, 1, −1, 1]]
```

The starting vector is `e_0 = (f_0 + g_0)/2` with `g_0 = e_0 − e_k` in the `−1` eigenspace. The `−1` eigenspace is orthogonal to `v⁺`, and `f_dᵀ v⁺ = 2[d even]`, so

```
P_even(k, L)  =  2^L · e_0ᵀ (R/2)^L 𝟙_even,        𝟙_even = ([d even])_{d=0..2m}.   (3)
```

## The word side

Read a word left to right, remembering the last letter and whether it is **pending**: nonzero and larger than its left neighbor, so that it needs a right neighbor at least as large. The states are `(0, +)` and `(a, +)`, `(a, −)` for `a = 1, …, m` (`+` satisfied, `−` pending), `2m + 1` in all. From `(a, flag)`, reading `b` is forbidden if `flag = −` and `b < a`, since then the pending letter is a strict local maximum; otherwise the new state is `(0, +)` if `b = 0`, `(b, +)` if `0 < b ≤ a`, and `(b, −)` if `b > a`. Start in `(0, +)`, the virtual left `0`; accept in a satisfied state, since the virtual right `0` fails every pending letter. This accepts exactly the words counted by `W_m`, so with `W` the transition matrix, `start = e_{(0,+)}` and `end` the indicator of the satisfied states,

```
W_m(n)  =  start · W^n · end.
```

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
```

On `m = 1`: `011` is accepted, through `(0,+) → (0,+) → (1,−) → (1,+)`, since the second `1` is at least the pending `1`. `010` is rejected: after `(0,+) → (0,+) → (1,−)` the letter `0` is below the pending `1`. Each letter of `W` determines the state it leads to, so `W` is a 0/1 matrix, and the predecessors of each state are:

- `(0, +)`: the satisfied states `(0, +)` and `(a, +)`, `a = 1, …, m`;
- `(b, +)`, `b ≥ 1`: `(a, +)` for `a ≥ b`, and `(b, −)`;
- `(b, −)`, `b ≥ 1`: `(0, +)`, and `(a, +)`, `(a, −)` for `1 ≤ a < b`.

## The change of basis

Define the `(2m+1) × (2m+1)` matrix `S`, with rows indexed by the sector coordinates `c = 0, …, 2m` and columns by the word states, through the set `D(s)` of rows in which column `s` has a 1:

```
D((0, +))  =  {0},        D((b, +))  =  {2b},        D((b, −))  =  {0, 1, …, 2b − 1}.
```

At `m = 1` (states `(0,+)`, `(1,+)`, `(1,−)`) the three matrices are

```
R/2  =  [[1, 0, 1], [0, 0, 1], [1, −1, 1]]
W    =  [[1, 0, 1], [1, 1, 0], [0, 1, 0]]
S    =  [[1, 0, 1], [0, 0, 1], [0, 1, 0]]
```

and `(R/2)S = SW` with `det S = −1` can be read off entry by entry.

**Lemma 2.** For every `m ≥ 0`,

```
(R/2) · S  =  S · W,          e_0ᵀ · S  =  start · W,          S · end  =  𝟙_even,      (4)
```

and `det S = ±1`.

*Proof.* Entry `(c, s')` of `(R/2)S` is `Σ_{d ∈ D(s')} (R/2)[c, d]`, and entry `(c, s')` of `SW` is the number of predecessors `s` of `s'` with `c ∈ D(s)`. By Equation (2):

- `s' = (0, +)`: both sides are `[c even]`, the left as `(R/2)[c, 0]` and the right from the satisfied predecessors, whose sets `D` are `{0}` and `{2a}`.
- `s' = (b, +)`: the left is `(R/2)[c, 2b] = [c even][c ≥ 2b] + [c < 2b]`; the right counts `(a, +)` with `a ≥ b` and `c = 2a`, plus `(b, −)` when `c ≤ 2b − 1`, which is the same.
- `s' = (b, −)`: the left is `Σ_{d=0}^{2b−1} (R/2)[c, d] = [c even][c ≤ 2b − 2] + #{a : 1 ≤ a < b, 2a > c}`, since the first term of Equation (2) sums to 1 over `d ≤ c` when `c` is even; the right counts `(0, +)` when `c = 0`, `(a, +)` with `1 ≤ a < b` when `c = 2a`, and `(a, −)` with `1 ≤ a < b` when `c ≤ 2a − 1`, which is the same.

Row 0 of `S` is the indicator of `(0, +)` and the states `(b, −)`, which is the row of `W` at `(0, +)`. Row `c` of `S` contains exactly one satisfied state if `c` is even (`(0, +)` or `(c/2, +)`) and none if `c` is odd, so `S · end = 𝟙_even`. For the determinant, the columns `(0, +)` and `(a, +)` are the unit vectors `e_0` and `e_{2a}`; removing them with their rows leaves the rows `2a − 1` and the columns `(b, −)`, with entries `[b ≥ a]`, a triangular matrix with 1s on the diagonal.

For `m ≤ 10`, the three equations hold and `det S = (−1)^m` (computed).[^3]

*Proof of the Theorem.* From `(R/2)S = SW`, `(R/2)^L S = S W^L`. By Equations (3) and (4),

```
2^{−L} P_even(k, L)  =  e_0ᵀ (R/2)^L 𝟙_even  =  e_0ᵀ (R/2)^L S · end  =  e_0ᵀ S · W^L · end  =  start · W^{L+1} · end  =  W_m(L+1).  ∎
```

## The similarity state by state

Since `det S = ±1`, `W = S⁻¹ (R/2) S`, and the sector coordinates after `L` columns, `r = e_0ᵀ (R/2)^L`, are integer combinations of the word-state counts `u = start · W^{L+1}`, the numbers of words of length `L + 1` that end in each state: `r S = u`. Solving with the sets `D(s)`:

```
r_0  =  u(0, +),        r_{2a}  =  u(a, +),
r_1  =  u(1, −) − u(0, +),        r_{2b−1}  =  u(b, −) − u(b−1, −) − u(b−1, +)   (b ≥ 2).
```

On the tower side, with `N_L(c)` the sum of `(−1)^{blocks}` over the towers of height at most `k` on a base of length `L` whose last column has height `c`,

```
r_d  =  ( (−1)^d N_L(d) + N_L(k − d) ) / 2^L.
```

Both readings were checked for `m = 1, 2` and `L ≤ 3`.[^3]

## Consequences for the OEIS

- `det(μI − W_m) = H_{2m+1}(μ) = Σ_i (−1)^i C(⌊(2m+1+i)/2⌋, i) μ^{2m+1−i}`, the even-sector factor of [[tower-parity-sectors](pages/tower-parity-sectors.md)], for `m ≤ 10` (computed). By the Cayley-Hamilton theorem, which says that a matrix satisfies its characteristic polynomial, `W_m(n)` satisfies the linear recurrence with characteristic polynomial `H_{2m+1}`. At `m = 2, 3, 4` these are the recurrences that **A202882**, **A203094** and **A203184** list as "Empirical", coefficient for coefficient; for example `H_5(μ) = μ⁵ − 3μ⁴ + 3μ³ − 4μ² + μ − 1` gives A202882's `a(n) = 3a(n−1) − 3a(n−2) + 4a(n−3) − a(n−4) + a(n−5)`.[^1] So the three recurrences hold.
- Each of these sequences is also a signed tower count: `a(n) = P_even(4m + 2, n − 1) / 2^{n−1}` in the OEIS indexing.

## Snippet index

| snippet | computes |
|---|---|
| `W_bruteforce(m, n)` | `W_m(n)` by enumerating `{0, …, m}^n` |
| `sector_even(k, Lmax)` | `P_even(k, L)` from the signed transfer matrix |
| `word_matrix(m)` | the transition matrix `W` of the pending-flag automaton and its states |

## Appearances in Sources

- [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] - the block count as total descent, behind the entries of `M̃_k`.

## Related Concepts

- [[tower-parity-sectors](pages/tower-parity-sectors.md)] - the signed transfer matrix `M̃_k`, the involution `JD`, the split `P = P_even + P_odd`, and the factors `H_d`, `V_d` of `char_k`.
- [[hardin-identity-seminar](pages/hardin-identity-seminar.md)] - a seminar on the case `m = 1`.
- [[plastic-number](pages/plastic-number.md)] - at `m = 1`, `H_3` is the minimal polynomial of `ψ²`, and `W_1` is `A005251`.
- [[signed-tower-count](pages/signed-tower-count.md)] - `P(k, L)` and its characteristic polynomials `char_k`.
- [[castle-eigenvalue-oeis-crosswalk](pages/castle-eigenvalue-oeis-crosswalk.md)] - the split `P(6, L) = 2^L A005251(L + 3)` plus an order-4 remainder, and its dominant root `2ψ²`.
- [[tower-spacing-castles](pages/tower-spacing-castles.md)] - the skylines of height at most `m + 1` whose internal empty runs in every row have length at least 2, counted by `W_m(w + 1)`: an unsigned reading of the same words.
- [[tower-word-language](pages/tower-word-language.md)] - tower words as a regular language at fixed height, recognized by a finite automaton.
- [[castle-sign](pages/castle-sign.md)] - the sign `(−1)^{blocks}` and the block count as total ascent and descent.
- [[castle-notation](pages/castle-notation.md)] - tower height `k`, here `4m + 2`, and castle height `k + 1`.
- [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] - the family `P(k, ·)` that Equation (1) decomposes.

## Footnotes

[^1]: https://oeis.org/A202882, https://oeis.org/A203094, https://oeis.org/A203184 (read 2026-10-16) - "Number of n X 1 0..2 arrays with every nonzero element less than or equal to some horizontal or vertical neighbor" (and 0..3, 0..4), offset 1, with "Empirical: a(n) = 3*a(n-1) -3*a(n-2) +4*a(n-3) -a(n-4) +a(n-5)", "Empirical: a(n) = 4*a(n-1) -6*a(n-2) +10*a(n-3) -5*a(n-4) +6*a(n-5) -a(n-6) +a(n-7)", "Empirical: a(n) = 5*a(n-1) -10*a(n-2) +20*a(n-3) -15*a(n-4) +21*a(n-5) -7*a(n-6) +8*a(n-7) -a(n-8) +a(n-9)"; https://oeis.org/A005251 for `W_1`. The listed terms agree with `start · W^n · end` for `n ≤ 15`, `n ≤ 14`, `n ≤ 14`.
[^2]: Verified by execution (Python 3.11 with SymPy, 2026-10-16): `W_bruteforce(1, n)` for `n ≤ 8`; the four words of length 3; `P_even(6, L)` for `L ≤ 7` against `2^L W_bruteforce(1, L+1)`; Equation (1) for `m ≤ 3` and `L ≤ 6`, and `P_even(2, L) = 2^L`.
[^3]: Verified by execution (Python 3.11 with SymPy, 2026-10-16): for `m ≤ 10`, `R` computed from the basis `f_c` equals twice Equation (2), the three equations (4) hold, `det S = (−1)^m`, and `det(μI − W_m) = H_{2m+1}(μ)`; the coefficients of `H_5`, `H_7`, `H_9` equal Hardin's recurrences; the two readings of the sector coordinates for `m = 1, 2`, `L ≤ 3`, against the sums over all towers.
