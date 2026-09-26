---
title: Hardin identity seminar - towers, words, and one change of basis
category: Concepts
summary: The seminar walk-through for the "Hardin word identity" arc. Start from a surprise - split the signed tower count P(6, L) = 1, 1, 7, 49, 231, 833, … by the parity of the last column, and the even half 1, 4, 16, 56, 192, … is exactly divisible by 2^L, leaving 1, 2, 4, 7, 12, 21, 37, 65 (A005251, binary strings with no isolated 1). Then explain it in six stops - towers as a 7×7 sign matrix, the hidden symmetry "reflect heights, flip odd signs" that splits it into two sectors, a basis in which the even sector matrix is exactly twice an integer matrix (the 2^L), a three-state "pending letter" automaton for the words, and a 0/1 change of basis S with det −1 that conjugates one matrix into the other and proves the identity in one line. The same argument at k = 4m + 2 gives Hardin's A202882, A203094, A203184 and proves his empirical recurrences (m ≤ 8). A closing stop connects A005251 to tree castles by area and, at height 4, to Tetali's unique tournaments. Every value is pinned by one runnable snippet block.
tags: [concept, castle, seminar, pedagogy, teaching, signed-tower-count, transfer-matrix, symmetry, bijection, hardin, words, automaton, oeis, a005251, plastic-number]
sources: [oeis-mining-pe502, tetali-1998-unique-tournaments]
created: 2026-09-26
updated: 2026-09-26
---

# Hardin identity seminar - towers, words, and one change of basis

**Thesis.** A signed count of towers and a count of binary words turn out to be the same sequence up to an exact factor `2^L`. The reason is not a bijection between the objects but a single change of basis between two small transfer matrices. It can be found by looking for a symmetry and proved by checking three matrix equations.

**Format.** About 60 minutes at one blackboard, seven stops, worked at `k = 6` (`m = 1`) where every matrix is `3 × 3`. The general case appears only at Stop 6. Every value quoted is pinned by the Snippet block at the end. The research pages behind it are [[tower-parity-sectors](pages/tower-parity-sectors.md)] (the symmetry and the sectors) and [[hardin-word-identity](pages/hardin-word-identity.md)] (the proof for all `m ≤ 8`).

## Stop 0 - the surprise

A **tower** of height `≤ k` on a base of length `L` is a row of column heights `c_1, …, c_L ∈ {0, …, k}`, sitting on a castle's bottom row, so together they form a castle of height `≤ k + 1` ([[castle-notation](pages/castle-notation.md)]). Its **blocks** are counted by the total downward step, with the ground at height 0 on both sides, and the **signed tower count** is `P(k, L) = Σ (−1)^{blocks}` ([[signed-tower-count](pages/signed-tower-count.md)], [[castle-sign](pages/castle-sign.md)]). At `k = 6`:

```
P(6, L)  =  1, 1, 7, 49, 231, 833, …
```

Split the towers by the parity of the last column's height:

```
even last column:   1,  4,  16,  56, 192, 672, 2368, 8320, …
odd last column:    0, −3,  −9,  −7,  39, 161,  215, −431, …
```

The even half is divisible by `2^L`, exactly, for every `L`, and the quotient is

```
1, 2, 4, 7, 12, 21, 37, 65, …        =  A005251: binary strings of length L + 1 with no isolated 1
```

(`000, 011, 110, 111` are the four of length 3.)[^1] Nothing about towers mentions binary strings or powers of 2. The seminar explains both.

## Stop 1 - towers as a matrix

Build a tower left to right, one column at a time. Stepping from height `a` to height `b` opens `max(0, a − b)` blocks on the way down, so the sign contributed is

```
s(a, b)  =  1  if a ≤ b,      (−1)^{a − b}  if a > b.
```

These signs form a `(k+1) × (k+1)` matrix `M_k`, and `P(k, L) = e_0ᵀ M_kᴸ v`, with `e_0` "start at height 0" and `v_b = (−1)^b` "drop back to the ground at the end". The whole count is one matrix power ([[tower-parity-sectors](pages/tower-parity-sectors.md)] Part 1).

*Idea:* local rules make transfer matrices, and transfer matrices make C-finite sequences.

## Stop 2 - the hidden symmetry

Try two natural moves on heights: `J` reflects them (`c ↦ k − c`), and `D` flips the sign of every odd height. Neither commutes with `M_k`, but their **product does**: `JD · M_k = M_k · JD`. Reflecting heights turns descents into ascents, and flipping odd signs turns the signs back. One line of parity bookkeeping checks it entrywise ([[tower-parity-sectors](pages/tower-parity-sectors.md)] Part 1).

For even `k`, `JD` squares to the identity, so it splits the state space into its `+1` and `−1` eigenspaces, and `M_k` preserves each. That is the **even/odd last-column split** of Stop 0, and it is why each half is its own C-finite sequence with its own factor of the characteristic polynomial.

*Idea:* when a split looks numerical, look for a symmetry that commutes with the transfer matrix.

## Stop 3 - where the `2^L` comes from

Use the basis `f_c = e_c + (−1)^c e_{k−c}` of the even sector (`c = 0, 1, 2` at `k = 6`). Written in this basis, `M_k` restricted to the sector has **every entry even**, so it is `2 ×` an integer matrix:

```
R/2  =  [ 1   0  1 ]
        [ 0   0  1 ]              P_even(6, L)  =  2^L · e_0ᵀ (R/2)ᴸ 𝟙_even
        [ 1  −1  1 ]
```

The `2^L` is an exact rescaling of the sector matrix, not an asymptotic. This is the step that needs `k ≡ 2 (mod 4)`: then `k/2` is odd, so no height is fixed by the reflection and every `f_c` has two terms ([[hardin-word-identity](pages/hardin-word-identity.md)], "The two transfer matrices").[^2]

*Idea:* choose the basis the symmetry suggests, and hidden structure (here a factor of 2 per step) shows up as divisibility of the matrix entries.

## Stop 4 - the words, as a machine

Now the other side. Read a binary string left to right and remember two things: the last letter, and whether a `1` is still **pending**, meaning it arrived after a `0` and still needs its right neighbor to be a `1` so it is not isolated. That gives three states, `(0, +)`, `(1, +)` satisfied, `(1, −)` pending, and a `3 × 3` transfer matrix:

```
W  =  [ 1  0  1 ]        from (0,+): read 0 → (0,+);  read 1 → (1,−)
      [ 1  1  0 ]        from (1,+): read 0 → (0,+);  read 1 → (1,+)
      [ 0  1  0 ]        from (1,−): read 0 → forbidden;  read 1 → (1,+)
```

Trace two words on the board. `011` goes `(0,+) → (0,+) → (1,−) → (1,+)` and ends satisfied, so it is **accepted**. `010` goes `(0,+) → (0,+) → (1,−)`, and then the pending `1` sees a `0`, which is **forbidden**. A word is valid exactly when every pending letter pays its debt before the end, and the count is `W_1(L+1) = start · W^{L+1} · end`. For general `m` the alphabet is `{0, …, m}`, "not isolated" becomes "every nonzero letter is `≤` a neighbor", and the machine has `2m + 1` states ([[hardin-word-identity](pages/hardin-word-identity.md)], "Word side").

*Idea:* a local constraint on words becomes a finite automaton once you add a flag for unfinished business.

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

and multiplying by `2^L` gives `P_even(6, L) = 2^L · W_1(L+1)`. ∎ Because `det S = −1`, `S` is invertible over the integers, and each tower-sector coordinate is an integer combination of word-state counts ([[hardin-word-identity](pages/hardin-word-identity.md)], "What the similarity says combinatorially").[^3]

*Idea:* two C-finite sequences are equal if their transfer matrices are conjugate with matching boundary vectors. Finding `S` is solving linear equations; the 0/1 pattern is then read off and checked.

## Stop 6 - every `k = 4m + 2` at once

Replace `k = 6` by `k = 4m + 2` and binary strings by words over `{0, …, m}`. The sector matrix is `(2m+1) × (2m+1)`, `S` is again 0/1 with determinant `±1`, and the same three equations hold, verified symbolically for every `m ≤ 8`:[^4]

| `m` | `k` | `P_even(k, L) / 2^L`, `L = 0, 1, 2, …` | words over | OEIS |
|---|---|---|---|---|
| 0 | 2 | `1, 1, 1, 1, …` | `{0}` | - |
| 1 | 6 | `1, 2, 4, 7, 12, 21, 37, …` | `{0, 1}` (no isolated 1) | A005251 |
| 2 | 10 | `1, 3, 9, 22, 51, 121, 292, …` | `{0, 1, 2}` | A202882 |
| 3 | 14 | `1, 4, 16, 50, 144, 422, 1268, …` | `{0, …, 3}` | A203094 |
| 4 | 18 | `1, 5, 25, 95, 325, 1121, 3985, …` | `{0, …, 4}` | A203184 |

R. H. Hardin recorded recurrences for A202882, A203094 and A203184 on the OEIS as *empirical*. They are the characteristic polynomials of these automata, so the conjugacy proves them.[^5] For general `m` the three equations reduce to a finite entrywise check that has not been written out, so the identity is a theorem for `m ≤ 8`.

*Idea:* one small example, done carefully, is the whole family.

## Stop 7 - where else A005251 lives

The word sequence of Stop 0 turns up well beyond towers:

- **Tree castles by area.** A tree castle has no filled `2 × 2` square, so no two adjacent columns are both `≥ 2`. By area, with unlimited height, these are compositions with no two adjacent parts `≥ 2`, counted by `A005251(n+2)` ([[tree-castle-by-area](pages/tree-castle-by-area.md)]). The classic "cut the gaps" encoding sends such a composition to a binary string with no factor `010`, term for term ([[a005251-bijection](pages/a005251-bijection.md)]). One bit-shift turns that into Hardin's no-isolated-1 strings.
- **Tournaments.** At height 4 instead of unlimited height, tree castles by area match the tournaments determined by their score sequences (A000570). The structural reason is Tetali's theorem that such tournaments are built from four basic ones on 1, 3, 4 and 5 vertices ([[tetali-1998-unique-tournaments](pages/tetali-1998-unique-tournaments.md)]).[^6]
- **The plastic number.** All of these grow like `ψ²`, the square of the plastic number, because the characteristic polynomial of the `m = 1` machine is the minimal polynomial of `ψ²` ([[plastic-number](pages/plastic-number.md)]).

*Idea:* a sequence that matches in two places is a thread to pull; this one runs from signed towers to words to compositions to tournaments.

## The board

| step | tower side | word side |
|---|---|---|
| objects | height sequences, signed by `(−1)^{blocks}`, last column even | words over `{0..m}` with no nonzero strict local maximum |
| machine | `M_k` on `k + 1` heights, restricted to the even sector: `2 · (R/2)` on `2m + 1` coordinates | pending-flag automaton `W` on `2m + 1` states |
| why `2^L` | the sector matrix is exactly twice an integer matrix | - |
| bridge | `(R/2) S = S W`, boundary vectors matched, `det S = ±1` | same |
| result | `P_even(4m+2, L) = 2^L · W_m(L+1)` | proved for `m ≤ 8` |

## Snippet

One block reproduces every number above: the tower matrix, the two sectors, the divisibility by `2^L`, the word count, the three `3 × 3` matrices of Stops 3-5, the three equations for `m ≤ 4`, and the table of Stop 6.

```python
import sympy as sp
from itertools import product

def M_signed(k):                           # one column step: sign (-1)^(blocks opened) going from height a to b
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

`sector_half` derives `R/2` from `M_k` itself rather than typing in the closed form, so the `3 × 3` matrix of Stop 3 is a computation, not an assumption.

## Exercises for the room

1. Run the automaton `W` by hand on `0110` and `0100`. Which is accepted, and at which letter does the other fail?
2. Check `P(6, L) = P_even + P_odd` for `L ≤ 7` from the two rows of Stop 0.
3. Why does the method need `k ≡ 2 (mod 4)`? Compute the even sector at `k = 4` (`1, 3, 9, 25, 69, …`, [[tower-parity-sectors](pages/tower-parity-sectors.md)] Part 3) and see where the divisibility by `2^L` fails.
4. (Open.) At `m = 1, L = 2` the identity reads `16 = 4 · 4`. Find a sign-reversing involution on the towers that leaves exactly `4 × 4` fixed objects, one "block of 4" per word. The wiki has none for general `L`.

## What is still open

These are the open items feeding Arc 3 in `IDEAS.md`:
- the general-`m` proof (a finite entrywise check of the three equations);
- a sign-reversing involution that realizes the `2^L` object by object;
- the two sector-assignment conjectures of [[tower-parity-sectors](pages/tower-parity-sectors.md)];
- the `h ≥ 5` tree-castle-by-area sequences, which have no OEIS match yet.

## Appearances in Sources

- [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] - the signed tower count `P(k, ·)` whose sectors the seminar splits.
- [[tetali-1998-unique-tournaments](pages/tetali-1998-unique-tournaments.md)] - the tournament end of Stop 7.

## Related Concepts

- [[hardin-word-identity](pages/hardin-word-identity.md)] - the full proof and the combinatorial reading of `S`; this page is its classroom version.
- [[tower-parity-sectors](pages/tower-parity-sectors.md)] - the symmetry `JD`, the sectors, and the closed-form factors `H_d`.
- [[a005251-bijection](pages/a005251-bijection.md)] / [[tree-castle-by-area](pages/tree-castle-by-area.md)] - Stop 7's compositions and strings.
- [[signed-tower-count](pages/signed-tower-count.md)] / [[castle-sign](pages/castle-sign.md)] - the signed count and the block sign.
- [[plastic-number](pages/plastic-number.md)] - the `ψ²` growth of the `m = 1` case.
- [[tower-recursion-master-class](pages/tower-recursion-master-class.md)] / [[castle-fibers-char-2-walkthrough](pages/castle-fibers-char-2-walkthrough.md)] - the other seminar pages.
- [[hear-the-shape-seminar](pages/hear-the-shape-seminar.md)] - the seminar on castle spectra and Kac's question.
- [[oeis-mining-seminar](pages/oeis-mining-seminar.md)] - the seminar on OEIS mining as a research method.
- [[one-bit-seminar](pages/one-bit-seminar.md)] - the seminar on the parity clause as information.


## Footnotes

[^1]: https://oeis.org/A005251 (2026-09-16) - "a(n+3) is the number of n-bit sequences that avoid 010"; the no-isolated-1 count of length `N` is `A005251(N+2)`, as reconciled on [[a005251-bijection](pages/a005251-bijection.md)]. Values re-verified by execution (Python 3.10, SymPy, 2026-09-26): `sectors(6, 7)` gives the even and odd rows, `P(6, L)` for `L ≤ 5` is `1, 1, 7, 49, 231, 833` and equals their sum, and every even term is divisible by `2^L` with quotient `1, 2, 4, 7, 12, 21, 37, 65 = W_count(1, L+1)`.
[^2]: Verified by execution (Python 3.10, SymPy, 2026-09-26): `sector_half(1)`, computed from `M_6` in the basis `f_c`, is the displayed `3 × 3` integer matrix; for `m ≤ 4` it agrees entrywise with the closed form `(R/2)[c, d] = [c even]·(−1)^d·[d ≤ c] + [d even]·[d > c]` stated on [[hardin-word-identity](pages/hardin-word-identity.md)].
[^3]: Verified by execution (Python 3.10, SymPy, 2026-09-26): `three_equations(1)` returns `(True, True, True, −1)`.
[^4]: Verified by execution (Python 3.10, SymPy, 2026-09-26): `three_equations(m)` holds for `m = 0..4` with `det S = 1, −1, 1, −1, 1`, and `P_even(4m+2, L)/2^L = W_count(m, L+1)` for `m = 1..4`, `L ≤ 6`. The `m ≤ 8` range is the symbolic verification recorded on [[hardin-word-identity](pages/hardin-word-identity.md)].
[^5]: https://oeis.org/A202882, https://oeis.org/A203094, https://oeis.org/A203184 (2026-09-16) - R. H. Hardin's entries with "Empirical: a(n) = …" recurrence lines; the word descriptions ("`n × 1` `0..m` arrays with every nonzero element `≤` some horizontal or vertical neighbor") match the words of Stop 4.
[^6]: [[tetali-1998-unique-tournaments](pages/tetali-1998-unique-tournaments.md)] p.157 L31-34, L39-41 [synthesis] - the enumeration `u_n = u_{n−1} + u_{n−3} + u_{n−4} + u_{n−5}` for `n > 5` and Theorem 1, exactly four basic strong tournaments in the class Unique, into which every other one decomposes by strong components.
