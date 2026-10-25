---
title: Hardin identity seminar - towers, words, and one change of basis
category: Concepts
summary: A seminar on the Hardin word identity. Split the signed tower count P(6, L) = 1, 1, 7, 49, 231, 833, … by the parity of the last column; the even half 1, 4, 16, 56, 192, … is divisible by 2^L, leaving 1, 2, 4, 7, 12, 21, 37, 65 (A005251, binary strings with no isolated 1). The stops explain it - towers as a 7 × 7 signed transfer matrix, the involution JD (reflect heights, flip odd signs) that splits it into two sectors, a basis in which the even sector matrix is twice an integer matrix (the 2^L), a three-state pending-letter automaton for the words, and a 0/1 change of basis S with det −1 that conjugates one matrix into the other. The same argument at k = 4m + 2 proves the identity for every m, with Hardin's A202882, A203094, A203184, whose "Empirical" recurrences hold. A closing stop places A005251 among tree castles by area and, at height 4, Tetali's unique tournaments. One snippet block reproduces every value.
tags: [concept, castle, seminar, pedagogy, teaching, signed-tower-count, transfer-matrix, symmetry, bijection, hardin, words, automaton, oeis, a005251, plastic-number]
sources: [oeis-mining-pe502, tetali-1998-unique-tournaments]
created: 2026-09-26
updated: 2026-10-25
---

# Hardin identity seminar - towers, words, and one change of basis

**Thesis.** A signed count of towers and a count of binary words are the same sequence up to the factor `2^L`, because their two transfer matrices are conjugate by a 0/1 change of basis that also matches the start and end vectors. The sectors that make this possible come from a symmetry of the tower matrix.

**Structure.** Stops 0-7, worked at `k = 6` (`m = 1`), where every matrix is `3 × 3`; the general case is Stop 6. The Snippet block reproduces every value. The symmetry and the sectors are on [[tower-parity-sectors](pages/tower-parity-sectors.md)], and the proof for every `m` on [[hardin-word-identity](pages/hardin-word-identity.md)].

## Stop 0 - the observation

Removing the bottom row of a castle leaves **towers**. Towers of height at most `k` on a base of length `L` are given by their column heights `c_1, …, c_L ∈ {0, …, k}`, and with the bottom row they form a castle of height at most `k + 1` ([[castle-notation](pages/castle-notation.md)]). Their **blocks** are counted by the total descent, with the ground at height 0 on both sides, and the **signed tower count** is `P(k, L) = Σ (−1)^{blocks}` ([[signed-tower-count](pages/signed-tower-count.md)], [[castle-sign](pages/castle-sign.md)]). At `k = 6`:

```
P(6, L)  =  1, 1, 7, 49, 231, 833, …
```

Split the towers by the parity of the last column's height:

```
even last column:   1,  4,  16,  56, 192, 672, 2368, 8320, …
odd last column:    0, −3,  −9,  −7,  39, 161,  215, −431, …
```

The even half is divisible by `2^L` for every `L ≤ 7`, and the quotient is

```
1, 2, 4, 7, 12, 21, 37, 65, …        =  A005251: binary strings of length L + 1 with no isolated 1
```

(`000, 011, 110, 111` are the four of length 3.)[^1] Stops 1 to 5 explain both the factor `2^L` and the binary strings, for every `L`.

## Stop 1 - towers as a matrix

Build the towers left to right, one column at a time. A step from height `a` down to height `b` ends `max(0, a − b)` blocks, so the step contributes the sign `1` if `a ≤ b` and `(−1)^{a − b}` if `a > b`. These signs are the entries of the **signed transfer matrix** `M̃_k`, of size `(k+1) × (k+1)`, and `P(k, L) = e_0ᵀ M̃_k^L v`, with `e_0` the start at height 0 and `v_b = (−1)^b` the final drop from height `b` to the ground ([[tower-parity-sectors](pages/tower-parity-sectors.md)], Part 1).

*Idea:* a nearest-neighbor rule on column heights gives a transfer matrix, and a transfer-matrix count is C-finite.

## Stop 2 - the symmetry `JD`

Consider two maps on heights: `J` reflects them (`c ↦ k − c`), and `D` flips the sign of every odd height. Neither commutes with `M̃_k`, but their **product does**: `JD · M̃_k = M̃_k · JD`. Reflecting the heights turns descents into ascents, and flipping the odd signs turns the signs back; entrywise, `JD · M̃_k · JD = (−1)^k M̃_k = (JD)² M̃_k` ([[tower-parity-sectors](pages/tower-parity-sectors.md)], Part 1).

For even `k`, `JD` squares to the identity, so it splits the heights' vector space into its `+1` and `−1` eigenspaces, and `M̃_k` preserves each. The `+1` eigenspace carries the towers with an even last column, so this is the **even/odd last-column split** of Stop 0, and each half satisfies the linear recurrence of its own factor of `char_k`.

*Idea:* the even/odd split is the eigenspace split of the involution `JD`, which commutes with `M̃_k`.

## Stop 3 - where the `2^L` comes from

Use the basis `f_c = e_c + (−1)^c e_{k−c}` of the even sector (`c = 0, 1, 2` at `k = 6`). Written in this basis, `M̃_k` restricted to the sector has **every entry even**, so it is `2 ×` an integer matrix:

```
R/2  =  [ 1   0  1 ]
        [ 0   0  1 ]              P_even(6, L)  =  2^L · e_0ᵀ (R/2)ᴸ 𝟙_even
        [ 1  −1  1 ]
```

This is the step that needs `k ≡ 2 (mod 4)`: then `k/2` is odd, so the middle height `k/2`, which the reflection fixes, lies in the odd sector, and every `f_c` of the even sector has two terms ([[hardin-word-identity](pages/hardin-word-identity.md)], Lemma 1).[^2]

*Idea:* in the basis adapted to the symmetry, the factor 2 per step appears as divisibility of the matrix entries by 2.

## Stop 4 - the words, as a machine

Now the other side. Read a binary string left to right and remember two things: the last letter, and whether a `1` is still **pending**, meaning it arrived after a `0` and still needs its right neighbor to be a `1` so it is not isolated. That gives three states, `(0, +)`, `(1, +)` satisfied, `(1, −)` pending, and a `3 × 3` transfer matrix:

```
W  =  [ 1  0  1 ]        from (0,+): read 0 → (0,+);  read 1 → (1,−)
      [ 1  1  0 ]        from (1,+): read 0 → (0,+);  read 1 → (1,+)
      [ 0  1  0 ]        from (1,−): read 0 → forbidden;  read 1 → (1,+)
```

Trace two words. `011` goes `(0,+) → (0,+) → (1,−) → (1,+)` and ends satisfied, so it is **accepted**. `010` goes `(0,+) → (0,+) → (1,−)`, and then the pending `1` sees a `0`, which is **forbidden**. A word is valid exactly when every pending `1` is followed by a `1` before the end, and the count is `W_1(L+1) = start · W^{L+1} · end`. For general `m` the alphabet is `{0, …, m}`, "not isolated" becomes "every nonzero letter is `≤` a neighbor", and the machine has `2m + 1` states ([[hardin-word-identity](pages/hardin-word-identity.md)], section *The word side*).

*Idea:* a local constraint on words becomes a finite automaton once a pending flag is added to the state.

## Stop 5 - one change of basis proves it

Two `3 × 3` matrices, `R/2` for towers and `W` for words, both generate `1, 2, 4, 7, 12, …`. The proof is a single 0/1 matrix `S` with **determinant `−1`**:

```
S  =  [ 1  0  1 ]
      [ 0  0  1 ]              (R/2) · S  =  S · W,      e_0ᵀ · S  =  start · W,      S · end  =  𝟙_even
      [ 0  1  0 ]
```

The first equation says `S` conjugates one machine into the other, and the other two match the start and end vectors. Then

```
e_0ᵀ (R/2)ᴸ 𝟙_even  =  e_0ᵀ (R/2)ᴸ S · end  =  e_0ᵀ S · Wᴸ · end  =  start · W^{L+1} · end  =  W_1(L+1),
```

and multiplying by `2^L` gives `P_even(6, L) = 2^L · W_1(L+1)`. ∎ Because `det S = −1`, `S` is invertible over the integers, and each tower-sector coordinate is an integer combination of word-state counts ([[hardin-word-identity](pages/hardin-word-identity.md)], section *The similarity state by state*).[^3]

*Idea:* two sequences given by transfer matrices are equal when the matrices are conjugate and the conjugation matches the boundary vectors.

## Stop 6 - every `k = 4m + 2` at once

Replace `k = 6` by `k = 4m + 2` and binary strings by words over `{0, …, m}`. The sector matrix is `(2m+1) × (2m+1)`, `S` is again 0/1 with determinant `±1`, and the same three equations hold for every `m`, proved entry by entry ([[hardin-word-identity](pages/hardin-word-identity.md)], Lemma 2):[^4]

| `m` | `k` | `P_even(k, L) / 2^L`, `L = 0, 1, 2, …` | words over | OEIS |
|---|---|---|---|---|
| 0 | 2 | `1, 1, 1, 1, …` | `{0}` | - |
| 1 | 6 | `1, 2, 4, 7, 12, 21, 37, …` | `{0, 1}` (no isolated 1) | A005251 |
| 2 | 10 | `1, 3, 9, 22, 51, 121, 292, …` | `{0, 1, 2}` | A202882 |
| 3 | 14 | `1, 4, 16, 50, 144, 422, 1268, …` | `{0, …, 3}` | A203094 |
| 4 | 18 | `1, 5, 25, 95, 325, 1121, 3985, …` | `{0, …, 4}` | A203184 |

R. H. Hardin recorded recurrences for A202882, A203094 and A203184 on the OEIS as "Empirical". Their coefficients are those of the characteristic polynomials `H_5`, `H_7`, `H_9` of the automata at `m = 2, 3, 4`, and the word counts satisfy the recurrence of that polynomial by the Cayley-Hamilton theorem, so the three recurrences hold.[^5]

*Idea:* the `k = 6` computation holds at every `k = 4m + 2`, with the same three equations.

## Stop 7 - where else A005251 lives

The word sequence of Stop 0 also counts:

- **Tree castles by area.** A tree castle has no filled `2 × 2` square, so no two adjacent columns are both `≥ 2`. By area, with unlimited height, these are compositions with no two adjacent parts `≥ 2`, counted by `A005251(n+2)` ([[tree-castle-by-area](pages/tree-castle-by-area.md)]). The classic "cut the gaps" encoding sends such a composition to a binary string with no factor `010` ([[a005251-bijection](pages/a005251-bijection.md)]). Strings avoiding `010` of length `N` and Hardin's no-isolated-1 strings of length `N + 1` both number `A005251(N + 3)`, and an explicit bijection joins them: split a string avoiding `010` at its `1`s, then turn each run of `r ≥ 1` zeros into `1^{r+1}` and each empty block into `0` ([[a005251-bijection](pages/a005251-bijection.md)]).
- **Tournaments.** The tree skylines of height at most 4 and area `n − 1`, which need not reach height 4, number `A000570(n)`, as do the tournaments on `n` vertices determined by their score sequences. The link is Tetali's theorem that such tournaments are built from four basic ones on 1, 3, 4 and 5 vertices ([[tetali-1998-unique-tournaments](pages/tetali-1998-unique-tournaments.md)], [[tree-castle-by-area](pages/tree-castle-by-area.md)]).[^6]
- **The plastic number.** The characteristic polynomial `μ³ − 2μ² + μ − 1` of the `m = 1` machine is the minimal polynomial of `ψ²`, the square of the plastic number, and it is also the characteristic polynomial of the three-state automaton for the strings avoiding `010` ([[a005251-bijection](pages/a005251-bijection.md)]). So the word counts, and with them the tree castles of unlimited height by area, grow like `ψ²` ([[plastic-number](pages/plastic-number.md)]).

*Idea:* A005251 counts the even-sector signed towers divided by `2^L`, the words, and the tree castles by area; at height at most 4 the tree skylines meet the tournaments of A000570.

## Summary table

| step | tower side | word side |
|---|---|---|
| objects | height sequences, signed by `(−1)^{blocks}`, last column even | words over `{0..m}` with no nonzero strict local maximum |
| machine | `M̃_k` on `k + 1` heights, restricted to the even sector: `2 · (R/2)` on `2m + 1` coordinates | pending-flag automaton `W` on `2m + 1` states |
| why `2^L` | the sector matrix is exactly twice an integer matrix | - |
| bridge | `(R/2) S = S W`, boundary vectors matched, `det S = ±1` | same |
| result | `P_even(4m+2, L) = 2^L · W_m(L+1)` | proved for every `m` |

## Snippet

One block reproduces every number on this page: the tower matrix, the two sectors, the divisibility by `2^L`, the word count, the three `3 × 3` matrices of Stops 3-5, the three equations for `m ≤ 4`, and the table of Stop 6.

```python
import sympy as sp
from itertools import product

def M_signed(k):                           # one column step from height a to b: sign (-1)^(blocks ended)
    return sp.Matrix(k+1, k+1, lambda a, b: 1 if a <= b else (-1)**(a-b))

def sectors(k, Lmax):                      # P_even(k, L), P_odd(k, L) for L = 0..Lmax
    M, row = M_signed(k), sp.Matrix([[1] + [0]*k])
    ve = sp.Matrix([1 if b % 2 == 0 else 0 for b in range(k+1)])
    vo = sp.Matrix([(-1)**b if b % 2 else 0 for b in range(k+1)])
    E, O = [], []
    for _ in range(Lmax+1):
        E.append(int((row*ve)[0])); O.append(int((row*vo)[0])); row = row*M
    return E, O

def sector_half(m):                        # R/2: M restricted to the even sector in the basis f_c = e_c + (-1)^c e_(k-c), halved
    k = 4*m + 2
    B = sp.Matrix(k+1, 2*m+1, lambda r, c: (1 if r == c else 0) + ((-1)**c if r == k - c else 0))
    R = (B.T * M_signed(k).T * B) * (B.T * B).inv()
    return (R / 2).T

def hardin_word(w):                        # every nonzero letter is <= one of its neighbors
    return all(a == 0 or (i > 0 and w[i-1] >= a) or (i+1 < len(w) and w[i+1] >= a) for i, a in enumerate(w))

def W_count(m, n):
    return sum(hardin_word(w) for w in product(range(m+1), repeat=n))

def word_matrix(m):                        # automaton: (last letter, '+' satisfied / '-' pending)
    S = [(0, '+')] + [(a, s) for a in range(1, m+1) for s in ('+', '-')]
    idx, W = {s: i for i, s in enumerate(S)}, sp.zeros(2*m+1, 2*m+1)
    for (a, flag) in S:
        for b in range(m+1):
            if flag == '-' and b < a:
                continue
            W[idx[(a, flag)], idx[(0, '+') if b == 0 else ((b, '+') if b <= a else (b, '-'))]] += 1
    return W, S

def S_pattern(m):                          # the 0/1 change of basis, sector coordinates x word states
    _, states = word_matrix(m)
    def row(c):
        a = (c + 1) // 2
        if c == 0: return [1 if s == (0, '+') or s[1] == '-' else 0 for s in states]
        if c % 2:  return [1 if s[1] == '-' and s[0] >= a else 0 for s in states]
        return [1 if s == (a, '+') or (s[1] == '-' and s[0] > a) else 0 for s in states]
    return sp.Matrix([row(c) for c in range(2*m+1)])
```

```
>>> [(sp.Matrix([[1] + [0]*6]) * M_signed(6)**L * sp.Matrix([(-1)**b for b in range(7)]))[0] for L in range(6)]
[1, 1, 7, 49, 231, 833]
>>> E, O = sectors(6, 7); E, O
([1, 4, 16, 56, 192, 672, 2368, 8320], [0, -3, -9, -7, 39, 161, 215, -431])
>>> [e // 2**L for L, e in enumerate(E)], all(e % 2**L == 0 for L, e in enumerate(E))
([1, 2, 4, 7, 12, 21, 37, 65], True)
>>> [W_count(1, n) for n in range(1, 9)]
[1, 2, 4, 7, 12, 21, 37, 65]
>>> sector_half(1), word_matrix(1)[0], S_pattern(1)
(Matrix([
[1,  0, 1],
[0,  0, 1],
[1, -1, 1]]), Matrix([
[1, 0, 1],
[1, 1, 0],
[0, 1, 0]]), Matrix([
[1, 0, 1],
[0, 0, 1],
[0, 1, 0]]))
>>> def three_equations(m):
...     R2, (W, states), S = sector_half(m), word_matrix(m), S_pattern(m)
...     start = sp.Matrix(1, len(states), [1 if s == (0, '+') else 0 for s in states])
...     end = sp.Matrix([1 if s[1] == '+' else 0 for s in states])
...     e0 = sp.Matrix([[1] + [0]*(2*m)])
...     one_even = sp.Matrix([1 if d % 2 == 0 else 0 for d in range(2*m+1)])
...     return R2*S == S*W, e0*S == start*W, S*end == one_even, S.det()
>>> [three_equations(m) for m in range(5)]
[(True, True, True, 1), (True, True, True, -1), (True, True, True, 1), (True, True, True, -1), (True, True, True, 1)]
>>> [[sectors(4*m + 2, 6)[0][L] // 2**L for L in range(7)] for m in range(1, 5)]
[[1, 2, 4, 7, 12, 21, 37], [1, 3, 9, 22, 51, 121, 292], [1, 4, 16, 50, 144, 422, 1268], [1, 5, 25, 95, 325, 1121, 3985]]
>>> [[W_count(m, n) for n in range(1, 8)] for m in range(1, 5)]
[[1, 2, 4, 7, 12, 21, 37], [1, 3, 9, 22, 51, 121, 292], [1, 4, 16, 50, 144, 422, 1268], [1, 5, 25, 95, 325, 1121, 3985]]
```

`sector_half` derives `R/2` from `M̃_k` itself, so the `3 × 3` matrix of Stop 3 is computed, not copied.

## Exercises

1. Run the automaton `W` by hand on `0110` and `0100`. Which is accepted, and at which letter does the other fail?
2. Check `P(6, L) = P_even + P_odd` for `L ≤ 7` from the two rows of Stop 0.
3. Why does the method need `k ≡ 2 (mod 4)`? Compute the even sector at `k = 4` (`1, 3, 9, 25, 69, …`, [[tower-parity-sectors](pages/tower-parity-sectors.md)] Part 3) and see where the divisibility by `2^L` fails.
## Appearances in Sources

- [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] - the signed tower count `P(k, ·)` whose sectors the seminar splits.
- [[tetali-1998-unique-tournaments](pages/tetali-1998-unique-tournaments.md)] - the tournament end of Stop 7.

## Related Concepts

- [[hardin-word-identity](pages/hardin-word-identity.md)] - the proof for every `m` and the state-by-state reading of `S`.
- [[tower-parity-sectors](pages/tower-parity-sectors.md)] - the symmetry `JD`, the sectors, and the factors `H_d`, `V_d` of `char_k`.
- [[a005251-bijection](pages/a005251-bijection.md)] / [[tree-castle-by-area](pages/tree-castle-by-area.md)] - Stop 7's compositions and strings.
- [[signed-tower-count](pages/signed-tower-count.md)] / [[castle-sign](pages/castle-sign.md)] - the signed count and the block sign.
- [[plastic-number](pages/plastic-number.md)] - the `ψ²` growth of the `m = 1` case.
- [[tower-recursion-master-class](pages/tower-recursion-master-class.md)] - the seminar on the tower count `T(k, L) = (k+1)^L` and the signed tower count.
- [[castle-fibers-char-2-walkthrough](pages/castle-fibers-char-2-walkthrough.md)] - the seminar following `P(2, ·)` and `char_2` through its fibers modulo primes.
- [[hear-the-shape-seminar](pages/hear-the-shape-seminar.md)] - the seminar on castle spectra and Kac's question.
- [[oeis-mining-seminar](pages/oeis-mining-seminar.md)] - the seminar on OEIS mining as a research method.
- [[one-bit-seminar](pages/one-bit-seminar.md)] - the seminar on the parity clause as information.
- [[sandcastle-seminar](pages/sandcastle-seminar.md)] - the seminar following the 16-cell castle `(3, 2, 1, 2, 2, 1, 2, 3)`, silver by spectrum, through its sandpile group, clock, identity and avalanches.
- [[q-thread-seminar](pages/q-thread-seminar.md)] - the q-thread seminar, castles by area from compositions through prime castles and the sign as a character to the q-Bessel closed form.
- [[pell-castle-strip](pages/pell-castle-strip.md)], [[castle-cryptography](pages/castle-cryptography.md)], [[song-as-castle](pages/song-as-castle.md)] - the seminars on the Pell strip, on a public-key system built from the signed tower count, and on audio as castles.


## Footnotes

[^1]: https://oeis.org/A005251 (read 2026-10-16) - "a(n+3) is the number of n-bit sequences that avoid 010"; (read 2026-10-25) "For n>=3, a(n) is the number of binary strings of length n-2 without any maximal runs of ones of length 1. - Félix Balado, Aug 25 2025", so the binary strings of length `N` with no isolated 1 number `A005251(N+2)`. Verified by execution (Python 3.11 with SymPy, 2026-10-16): `sectors(6, 7)` gives the even and odd rows, their sum is `P(6, L) = 1, 1, 7, 49, 231, 833, 2583, 7889` for `L ≤ 7`, and every even term is divisible by `2^L` with quotient `W_count(1, L+1)`.
[^2]: Verified by execution (Python 3.11 with SymPy, 2026-10-16): `sector_half(1)`, computed from `M̃_6` in the basis `f_c`, is the displayed matrix; Lemma 1 of [[hardin-word-identity](pages/hardin-word-identity.md)] proves the closed form `(R/2)[c, d] = [c even]·(−1)^d·[d ≤ c] + [d even]·[d > c]` for every `m`; the even sector at `k = 4` is `1, 3, 9, 25, 69, 193, 541`.
[^3]: Verified by execution (Python 3.11 with SymPy, 2026-10-16): `three_equations(1)` returns `(True, True, True, −1)`.
[^4]: Verified by execution (Python 3.11 with SymPy, 2026-10-16): `three_equations(m)` holds for `m = 0..4` with `det S = 1, −1, 1, −1, 1`, and `P_even(4m+2, L)/2^L = W_count(m, L+1)` for `m = 1..4`, `L ≤ 6`; [[hardin-word-identity](pages/hardin-word-identity.md)] checks the equations for `m ≤ 10` and proves them for every `m`.
[^5]: https://oeis.org/A202882, https://oeis.org/A203094, https://oeis.org/A203184 (read 2026-10-16) - R. H. Hardin's entries, "Number of n X 1 0..m arrays with every nonzero element less than or equal to some horizontal or vertical neighbor", with "Empirical: a(n) = ..." recurrence lines whose coefficients are those of `H_5`, `H_7`, `H_9` (checked).
[^6]: [[tetali-1998-unique-tournaments](pages/tetali-1998-unique-tournaments.md)] p.157 L31-34, L39-41 [synthesis] - the enumeration `u_n = u_{n−1} + u_{n−3} + u_{n−4} + u_{n−5}` for `n > 5` and Theorem 1, exactly four basic strong tournaments in the class Unique, into which every other one decomposes by strong components.
