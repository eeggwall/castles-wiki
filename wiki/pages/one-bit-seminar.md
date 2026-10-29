---
title: One bit seminar - the parity clause as information
category: Concepts
summary: A seminar on Project Euler 502's even-block clause read as information, in aggregate and one castle at a time. In aggregate it costs one bit up to a correction that tends to 0, log₂ A^e(w, h) = log₂ A(w, h) − 1 + log₂(1 + S/A), because A^e = (A + S)/2 and the signed count S is exponentially smaller than A (S/A = −9.0·10⁻⁸ at w = 40, h = 3); the approximation w·log₂ h − 1 also misses a separate height correction (0.42 bits at w = 13, h = 10). The split is the projector (1 ± sign)/2, as for even and odd permutations. For one castle, raising column i changes the block count by [c_i ≥ c_{i−1}] − [c_{i+1} > c_i], so one chosen cell flips the parity at a weak local maximum or a strict local minimum; a random one-cell edit flips it 43-52% of the time, and a few castles (1 of 15 at w = 4, h = 2, 35 of 781 at w = 5, h = 4) have no one-cell edit that keeps their height and flips the parity. The bit is cheap to write (one hidden bit per castle) and easy to lose on a noisy line. In the growth rate of a family defined by a rule on neighboring columns it contributes nothing.
tags: [concept, castle, seminar, pedagogy, teaching, entropy, information, parity, castle-sign, steganography, compression, topological-entropy]
sources: [project-euler-502-observations, project-euler-502-solution]
created: 2026-09-26
updated: 2026-10-29
---

# One bit seminar - the parity clause as information

**Thesis.** Project Euler 502 counts castles with an even number of blocks. In aggregate that clause costs one bit, up to a correction that tends to 0, because the even-block castles are half of all castles up to an exponentially small signed count. For a single castle the clause is a sign that one chosen cell can usually flip, which makes it easy to write a message into and easy to destroy. In the growth rate per column it contributes nothing.

**Structure.** Seven stops (0 to 6). The Snippet at the end computes every value quoted. The pages behind it are [[castle-entropy](pages/castle-entropy.md)], [[castle-sign](pages/castle-sign.md)], [[castle-compression](pages/castle-compression.md)], [[castle-steganography](pages/castle-steganography.md)] and [[castle-phone-line](pages/castle-phone-line.md)]. Notation follows [[castle-notation](pages/castle-notation.md)].

## Stop 0 - the clause

A castle of width `w` and height `h` is a skyline of column heights in `1..h` with some column of height `h`. Its blocks are the maximal runs of cells in each row, and each rise in the skyline starts new ones. There are `A(w, h) = h^w − (h−1)^w` castles, and Project Euler asks for the number `A^e(w, h)` of those with an even number of blocks, which the problem statement writes `F(w, h)`.

If all `A` castles are equally likely, naming one takes `log₂ A` bits, and naming one of the even-block ones takes `log₂ A^e` bits. The difference `log₂ A − log₂ A^e` is the price of the clause.

## Stop 1 - one bit

```
 w   h   A^e(w,h)                log₂ A^e   log₂ A − 1   w·log₂ h − 1
 8   2   120                      6.907      6.994        7.000
12   2   2080                    11.022     11.000       11.000
12   3   261615                  17.997     18.008       18.020
40   3   6078831630016984399     62.398     62.398       62.399
```

The last column is the usual approximation, "each column is `log₂ h` bits, minus one bit for the parity". It carries two separate corrections:

- **the parity**, which costs `log₂ A − log₂ A^e = 1 − log₂(1 + S/A)` bits, with `S` the signed count of Stop 2, and tends to 1;
- **the height**, since a castle of height `h` must reach `h`: `log₂ A = w·log₂ h + log₂(1 − ((h−1)/h)^w)`. This term matters when `h` is large compared with `w`. At `w = 13, h = 10`, `log₂ A^e = 41.762` equals `log₂ A − 1` to three decimals and lies 0.42 bits below `w·log₂ h − 1`, and all of that gap is the height term, `log₂(1 − 0.9^13) = −0.423`.[^1]

## Stop 2 - why one bit: a sign and a projector

Weight every castle by its sign `(−1)^{blocks}` and add up. The result is the signed count `S(w, h) = A^e(w, h) − A^o(w, h)`, the even-block castles minus the odd-block ones. Then

```
A^e  =  (A + S)/2            A^o  =  (A − S)/2
```

This is the projector `(1 ± sign)/2`, the same one that counts the even permutations of `n ≥ 2` points as `n!/2`, where the signed sum is 0 ([[castle-sign](pages/castle-sign.md)]).[^2] For castles the signed sum is not 0, but it is exponentially smaller than `A`:

```
S/A  =  −5.9·10⁻²  (w = 8, h = 2),    −7.8·10⁻³  (w = 12, h = 3),    −9.0·10⁻⁸  (w = 40, h = 3)
```

The reason is that `S(w, h) = P(h−2, w) − P(h−1, w)` is built from signed tower counts. `P(k, ·)` grows like `ρ_k^w`, where the spectral radius `ρ_k` of the signed transfer matrix is strictly less than `k + 1` ([[castle-graph-spectral-radius](pages/castle-graph-spectral-radius.md)], [[castle-counting-formula](pages/castle-counting-formula.md)]). So `S/A → 0`, `A^e/A → 1/2`, and the clause costs one bit in the limit.

*Idea:* a parity condition costs one bit whenever the signed sum is negligible next to the total, and the projector `(1 ± sign)/2` reduces the parity count to one signed sum.

## Stop 3 - one castle, one cell

Now take a single castle `c`. Raise column `i` by one cell. The block count changes by

```
Δ  =  [c_i ≥ c_{i−1}]  −  [c_{i+1} > c_i]            (with c_0 = 0, and no second term at the last column)
```

because the rise into column `i` grows exactly when column `i` was at least as tall as its left neighbor, and the rise out of it shrinks exactly when the right neighbor was taller.[^3] So `Δ` is `+1`, `0` or `−1`, and the parity flips exactly when `Δ = ±1`:

- raise a **weak local maximum** (at least as tall as its left neighbor and not shorter than its right one): `Δ = +1`;
- raise a **strict local minimum** (shorter than both neighbors): `Δ = −1`;
- raise any other column, on a slope or at the edge of a plateau: `Δ = 0`, no flip.

Lowering a column is the reverse move. For the castle `(1, 3, 2)`, raising the columns in turn gives `Δ = 0, 1, 0`.

**Exceptions.** A move must keep the castle a castle of height `h`: heights stay in `1..h`, and some column stays at `h`. That rule leaves a few castles with no flipping move. At `w = 4, h = 2`, the castle `(1, 2, 2, 1)` has none: raising a column of height 2 would exceed `h`, and each of its four legal moves, raising an end column or lowering a middle one, has `Δ = 0`.[^4] At `w = 6, h = 3` the two such castles are `(1, 2, 3, 3, 2, 1)` and `(3, 3, 1, 1, 3, 3)`.

At height at most 2 one rule chooses the flipping move for all but a few castles at once: change the top cell of the first odd column whose two neighbors have equal height, counting the outside as height 1. A column with equal neighbors is always a weak local maximum or a strict local minimum, so the move flips the parity, and it pairs the castles of width `w` and height at most 2 into pairs of opposite parity, leaving `2^{⌈w/2⌉}` castles of one parity unpaired, or none when `w ≡ 1 (mod 4)` ([[signed-tower-count](pages/signed-tower-count.md)], section *The case k = 1*).

| `w`, `h` | castles | castles with no flipping one-cell edit | random one-cell edit flips parity |
|---|---|---|---|
| 4, 2 | 15 | 1 | 42.9% |
| 6, 3 | 665 | 2 | 50.5% |
| 7, 3 | 2059 | 6 | 51.9% |
| 5, 4 | 781 | 35 | 48.6% |

*Idea:* an aggregate fact (one bit) and a fact about each object (one cell flips it) are different statements, and the second has exceptions.

## Stop 4 - the bit is easy to lose

The last column of the table says that a random one-cell edit flips the parity about half the time. [[castle-phone-line](pages/castle-phone-line.md)] sends the 512 row castles of the cameraman image as tones through a simulated telephone line, and finds the block parity the most fragile statistic it measures: about 50% correct until the line is nearly perfect, and 83-86% correct when 99.9% of heights arrive exact. The height histogram and the slow trend of the skyline, which average over the row, survive every setting tested. On [[song-as-castle](pages/song-as-castle.md)], replacing one random column of a castle of width 17 and height 16 by a different random height flips the parity with probability 0.427, in the same range.

*Idea:* a bit that every column's error can flip is the least robust statistic on the line.

## Stop 5 - the bit is easy to write

The same fact makes the bit a channel: hide a message one bit per castle by setting each castle's parity, with one chosen cell where needed. [[castle-steganography](pages/castle-steganography.md)] (channel B) does this on the 512 row castles of the cameraman image. The 336 bits went into 336 rows; 161 rows needed a one-cell change and 175 already had the right parity. The untouched rows split 249 odd to 263 even, so the parity statistics do not reveal the change. The message survives a lossless PNG round trip exactly, and after a JPEG round trip 175 of the 336 bits are right, against 168 by chance.

*Idea:* the one-cell flip that writes a bit is the same move line noise makes, so the channel survives only lossless storage.

## Stop 6 - in the growth rate, the bit disappears

Divide by `w`. For a family of castles whose count by width grows like `ρ^w`, the entropy per column is `log₂ ρ` ([[castle-entropy](pages/castle-entropy.md)]). The parity's one bit, spread over `w` columns, contributes `1/w → 0`:

| family | growth by width `ρ` | bits per column |
|---|---|---|
| all castles of height `h` | `h` | `log₂ h` |
| Fibonacci castles, height 2 | golden, `φ = 1.618` | 0.694 |
| ridge castles, height 3 | silver, `1 + √2 = 2.414` | 1.272 |
| maximal castles, height 2 | plastic, `ψ = 1.325` | 0.406 |

The block count determines the parity, so given the block count the parity carries no further information, while given the area it does ([[castle-conditional-entropy](pages/castle-conditional-entropy.md)]).

*Idea:* a constraint that costs a bounded number of bits in total changes the counts and leaves the entropy per column unchanged.

## Summary table

| reading | what the parity clause is | number |
|---|---|---|
| aggregate count | a projector, `(A ± S)/2` | costs `1 − log₂(1 + S/A)` bits, tending to 1 |
| one castle | a sign, flipped by one chosen cell at a weak local maximum or strict local minimum | all but a few castles are one cell from the other parity |
| noise | the most fragile statistic on the phone line | a random one-cell edit flips it 43-52% of the time |
| channel | one hidden bit per castle | 161 one-cell changes for 336 bits |
| growth rate | a bounded term | contributes `1/w → 0` bits per column |

## Snippet

```python
from itertools import product
from math import log2

def blocks(c):                             # each rise in the skyline starts new blocks
    return c[0] + sum(max(0, c[i] - c[i-1]) for i in range(1, len(c)))

def P(k, L):                               # signed tower count, towers of height <= k on a base of length L
    dp = {0: 1}
    for _ in range(L):
        nd = {}
        for a, wt in dp.items():
            for b in range(k + 1):
                nd[b] = nd.get(b, 0) + wt * (-1)**max(0, b - a)
        dp = nd
    return sum(dp.values())

A  = lambda w, h: h**w - (h - 1)**w         # castles of width w and height h
S  = lambda w, h: P(h - 2, w) - P(h - 1, w) # signed count: (even-block castles) - (odd-block castles)
Ae = lambda w, h: (A(w, h) + S(w, h)) // 2  # the Project Euler 502 count

def castles(w, h):
    return [c for c in product(range(1, h + 1), repeat=w) if max(c) == h]

def one_cell_edits(c, h):                  # move one column up or down by 1, stay a castle of height h
    for i in range(len(c)):
        for d in (1, -1):
            e = c[:i] + (c[i] + d,) + c[i+1:]
            if 1 <= e[i] <= h and max(e) == h:
                yield e

def delta_raise(c, i):                     # blocks(raise column i by 1) - blocks(c)
    left = c[i-1] if i > 0 else 0
    return (1 if c[i] >= left else 0) - (1 if i + 1 < len(c) and c[i+1] > c[i] else 0)

def flip_stats(w, h):                      # castles with no parity-flipping edit, and random-edit flip rate
    cs, stuck, flips, total = castles(w, h), 0, 0, 0
    for c in cs:
        es = list(one_cell_edits(c, h))
        f = sum(blocks(e) % 2 != blocks(c) % 2 for e in es)
        stuck += (f == 0); flips += f; total += len(es)
    return len(cs), stuck, round(flips / total, 3)
```

```
>>> [(w, h, Ae(w, h), round(log2(Ae(w, h)), 3), round(log2(A(w, h)) - 1, 3), round(w * log2(h) - 1, 3)) for w, h in [(8, 2), (12, 2), (12, 3), (40, 3)]]
[(8, 2, 120, 6.907, 6.994, 7.0), (12, 2, 2080, 11.022, 11.0, 11.0), (12, 3, 261615, 17.997, 18.008, 18.02), (40, 3, 6078831630016984399, 62.398, 62.398, 62.399)]
>>> [(w, h, '%.1e' % (S(w, h) / A(w, h))) for w, h in [(8, 2), (12, 3), (40, 3)]]
[(8, 2, '-5.9e-02'), (12, 3, '-7.8e-03'), (40, 3, '-9.0e-08')]
>>> round(log2(Ae(13, 10)), 3), round(log2(A(13, 10)) - 1, 3), round(13 * log2(10) - 1, 3), round(log2(1 - 0.9**13), 3)
(41.762, 41.762, 42.185, -0.423)
>>> [flip_stats(w, h) for w, h in [(4, 2), (6, 3), (7, 3), (5, 4)]]
[(15, 1, 0.429), (665, 2, 0.505), (2059, 6, 0.519), (781, 35, 0.486)]
>>> [c for c in castles(4, 2) if not any(blocks(e) % 2 != blocks(c) % 2 for e in one_cell_edits(c, 2))]
[(1, 2, 2, 1)]
>>> [c for c in castles(6, 3) if not any(blocks(e) % 2 != blocks(c) % 2 for e in one_cell_edits(c, 3))]
[(1, 2, 3, 3, 2, 1), (3, 3, 1, 1, 3, 3)]
>>> all(blocks(c[:i] + (c[i] + 1,) + c[i+1:]) - blocks(c) == delta_raise(c, i) for c in product(range(5), repeat=5) for i in range(5))
True
```

## Exercises

1. Check the formula for `Δ` on `(1, 3, 2)` by raising each column in turn.
2. Show that `(1, 2, 2, 1)` at `h = 2` has no flipping edit by listing its legal one-cell edits and their block counts.
3. At `w = 13, h = 10`, split the 0.42-bit gap into the parity part and the height part using `log₂(1 − 0.9^13)`.
4. Show that `(1, 2, 3, 3, 2, 1)` and `(3, 3, 1, 1, 3, 3)` at `h = 3` have no flipping edit, and find which moves the height cap and the floor rule out.

## Appearances in Sources

- [[project-euler-502-observations](pages/project-euler-502-observations.md)] - the even-block count as half the sum of the unsigned and signed counts, which it writes `(A + P)/2`.
- [[project-euler-502-solution](pages/project-euler-502-solution.md)] - the split of towers into `(T + P)/2` even-block and `(T − P)/2` odd-block ones.

## Related Concepts

- [[castle-entropy](pages/castle-entropy.md)] - the entropy `log₂ A^e`, its two corrections, and the entropy per column of castle families.
- [[castle-sign](pages/castle-sign.md)] - the sign, the projector, and the permutation sign.
- [[castle-steganography](pages/castle-steganography.md)] and [[castle-phone-line](pages/castle-phone-line.md)] - the bit written into the cameraman image, and the bit lost on a telephone line.
- [[castle-compression](pages/castle-compression.md)] and [[castle-conditional-entropy](pages/castle-conditional-entropy.md)] - description length, and entropy conditioned on block count and area.
- [[castle-notation](pages/castle-notation.md)] - `A`, `A^e`, `A^o`, `S` and `P(k, L)`.
- [[tower-recursion-master-class](pages/tower-recursion-master-class.md)], [[hardin-identity-seminar](pages/hardin-identity-seminar.md)], [[hear-the-shape-seminar](pages/hear-the-shape-seminar.md)], [[oeis-mining-seminar](pages/oeis-mining-seminar.md)], [[castle-fibers-char-2-walkthrough](pages/castle-fibers-char-2-walkthrough.md)] - the other seminar pages.
- [[sandcastle-seminar](pages/sandcastle-seminar.md)] - a seminar following the 16-cell castle `(3, 2, 1, 2, 2, 1, 2, 3)`, silver by spectrum, through its sandpile group, clock, identity and avalanches.
- [[q-thread-seminar](pages/q-thread-seminar.md)] - a seminar on castles by area.
- [[half-derivative-seminar](pages/half-derivative-seminar.md)] - a seminar on the block count, the partial sum, the transfer matrix and the walk on a tree castle at order 1/2.
- [[pell-castle-strip](pages/pell-castle-strip.md)], [[castle-cryptography](pages/castle-cryptography.md)], [[song-as-castle](pages/song-as-castle.md)] - the seminar pages on the Pell strip, castle cryptography, and audio as castles.
- [[parity-via-roots-of-unity](pages/parity-via-roots-of-unity.md)] - the projector for the block count modulo `m`, with `m`-th roots of unity.

## Footnotes

[^1]: Verified by execution (Python 3.11, 2026-10-16): `A^e(w, h) = (A + S)/2` with `S = P(h−2, w) − P(h−1, w)` from the signed tower dynamic program, the table and the `S/A` ratios as in the Snippet, and `log₂ A^e(13, 10) = 41.762 = log₂ A(13, 10) − 1` to three decimals against `13·log₂ 10 − 1 = 42.185`, with `log₂(1 − 0.9^13) = −0.423`.
[^2]: [[project-euler-502-observations](pages/project-euler-502-observations.md)] §"Parity via signs" L13 - "Even-block-count is enforced by (A + P)/2, where A is the unsigned total and P is the signed count with (-1)^{blocks}."; [[project-euler-502-solution](pages/project-euler-502-solution.md)] §"The main formula" L55 - "Then (T + P)/2 counts towers with even block count and (T - P)/2 counts odd."
[^3]: Verified by execution (Python 3.11, 2026-10-16): `delta_raise(c, i)` equals the change in `blocks` for every sequence in `{0..4}^5` and every column `i`, as in the Snippet; `blocks` is the total ascent of [[castle-sign](pages/castle-sign.md)].
[^4]: Verified by execution (Python 3.11, 2026-10-16): all castles of the listed `(w, h)` and all one-cell `±1` edits that keep the heights in `1..h` and some column at `h`, as in the Snippet; the castles with no flipping edit at `w = 6, h = 3` are `(1, 2, 3, 3, 2, 1)` and `(3, 3, 1, 1, 3, 3)`.
