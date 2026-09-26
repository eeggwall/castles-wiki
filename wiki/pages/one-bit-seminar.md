---
title: One bit seminar - the parity clause as information
category: Concepts
summary: The seminar walk-through for the "One bit" arc - Project Euler 502's even-block clause read as information, one castle at a time and in aggregate. The clause costs exactly one bit - log₂ F(w,h) = log₂ A(w,h) − 1 up to a correction that vanishes, because F = (A + S)/2 and the parity term S is exponentially smaller than A (S/A ≈ −9·10⁻⁸ at w = 40, h = 3); the familiar approximation w·log₂ h − 1 also carries an unrelated exact-height correction (0.42 bits at w = 13, h = 10). The bit is a sign, and (T ± P)/2 is the same projector as even and odd permutations. Object by object, raising column i changes the block count by [c_i ≥ c_{i−1}] − [c_{i+1} > c_i], so one chosen cell flips the parity at any weak local maximum or strict local minimum; a random one-cell edit flips it about half the time (43-52%), and a few castles (1 of 15 at w = 4, h = 2, 35 of 781 at w = 5, h = 4) cannot be flipped by any one-cell edit that keeps their height. That makes the bit cheap to write (steganography channel B, one bit per castle) and easy to lose (a coin flip on a noisy phone line). In the growth rate it disappears - every growth constant is an entropy rate, and the one bit is a boundary term. One runnable block pins every value.
tags: [concept, castle, seminar, pedagogy, teaching, entropy, information, parity, castle-sign, steganography, compression, topological-entropy]
sources: [project-euler-502-observations, project-euler-502-castle-factoring]
created: 2026-09-26
updated: 2026-09-26
---

# One bit seminar - the parity clause as information

**Thesis.** Project Euler 502 counts castles with an even number of blocks. That clause is worth **exactly one bit**. In aggregate it halves the count up to an exponentially small correction. For a single castle it is a sign that one well-chosen cell can flip, which makes it easy to write a message into and easy to destroy. In the growth rate, where every castle family's growth constant is an entropy, the bit disappears.

**Format.** About 60 minutes at one blackboard, seven stops. Every value quoted is pinned by the Snippet block at the end. The research pages behind it are [[castle-entropy](pages/castle-entropy.md)], [[castle-sign](pages/castle-sign.md)], [[castle-compression](pages/castle-compression.md)], [[castle-steganography](pages/castle-steganography.md)] and [[castle-phone-line](pages/castle-phone-line.md)]. Notation follows [[castle-notation](pages/castle-notation.md)].

## Stop 0 - the clause

A castle of width `w` and height `h` is a skyline of column heights `1..h` with some column exactly `h`. Its blocks are the runs of cells row by row, and each rise in the skyline starts new ones. There are `A(w, h) = h^w − (h−1)^w` castles in all, and Project Euler asks only for the ones with an even number of blocks, `F(w, h)`.

How much does "even" cost? If all `A` castles are equally likely, naming one takes `log₂ A` bits. Naming one of the even ones takes `log₂ F` bits. The difference is the price of the clause.

## Stop 1 - exactly one bit

```
 w   h   F(w,h)                  log₂ F     w·log₂ h − 1
 8   2   120                      6.907      7.000
12   2   2080                    11.022     11.000
12   3   261615                  17.997     18.020
40   3   6078831630016984399     62.398     62.399
```

The last column is the usual approximation, "each column is `log₂ h` bits, minus one bit for the parity". It gets closer as `w` grows. There are two separate corrections in it, and they should not be confused:

- **the parity**, which costs `log₂ A − log₂ F = 1 − log₂(1 + S/A)` bits, exactly one bit in the limit;
- **"height exactly `h`"**, which makes `log₂ A = w·log₂ h + log₂(1 − ((h−1)/h)^w)`. This is noticeable when `h` is large compared with `w`. At `w = 13, h = 10`, `log₂ F = 41.762` equals `log₂ A − 1` to three decimals but sits 0.42 bits below `w·log₂ h − 1`, and all of that gap is the exact-height term.[^1]

## Stop 2 - why one bit: a sign and a projector

Weight every castle by its sign `(−1)^{blocks}` and add up. Let `S(w, h)` be the result, the number of even castles minus the number of odd ones. Then

```
F  =  (A + S)/2            (even)             odd  =  (A − S)/2
```

This is the projector `(1 ± sign)/2`, the same one that splits permutations into even and odd, where `|A_n| = n!/2` because the signed sum vanishes ([[castle-sign](pages/castle-sign.md)]).[^2] For castles the signed sum is not zero, but it is exponentially smaller than `A`:

```
S/A  =  −5.9·10⁻²  (w = 8, h = 2),    −7.8·10⁻³  (w = 12, h = 3),    −9.0·10⁻⁸  (w = 40, h = 3)
```

The reason is that `S = P(h−2, w) − P(h−1, w)` is built from signed tower counts, which grow like `ρ^w` with `ρ` well below `h` ([[castle-counting-formula](pages/castle-counting-formula.md)], [[generating-function-gallery](pages/generating-function-gallery.md)]). So `F/A → 1/2`, and "even" is worth one bit.

*Idea:* a parity condition costs one bit whenever the signed sum is negligible next to the total, and a projector turns the parity into arithmetic.

## Stop 3 - one castle, one cell

Now take a single castle. Raise column `i` by one cell. The block count changes by

```
Δ  =  [c_i ≥ c_{i−1}]  −  [c_{i+1} > c_i]            (with c_0 = 0, and no second term at the last column)
```

because the rise into column `i` grows exactly when column `i` was at least as tall as its left neighbour, and the rise out of it shrinks exactly when the right neighbour was taller.[^3] So `Δ` is `+1`, `0` or `−1`, and the parity flips exactly when `Δ = ±1`:

- raise a **weak local maximum** (at least as tall as both neighbours): `Δ = +1`;
- raise a **strict local minimum** (shorter than both): `Δ = −1`;
- a cell on the slope of a staircase, or on the edge of a plateau: `Δ = 0`, no flip.

Lowering is the same move in reverse. So almost every castle is **one chosen cell** away from the other parity ([[castle-steganography](pages/castle-steganography.md)] uses the raise-a-maximum and lower-a-minimum cases).

**Almost, not all.** A move must keep the castle a castle: heights stay in `1..h`, and some column stays at `h`. That rule blocks a few castles completely. At `w = 4, h = 2`, the castle `(1, 2, 2, 1)` has no parity-flipping one-cell edit. Its only flipping move would raise the plateau top above the height cap, and every other move is a slope or plateau-edge move with `Δ = 0`.[^4]

| `w`, `h` | castles | castles with no flipping one-cell edit | random one-cell edit flips parity |
|---|---|---|---|
| 4, 2 | 15 | 1 | 42.9% |
| 6, 3 | 665 | 2 | 50.5% |
| 7, 3 | 2059 | 6 | 51.9% |
| 5, 4 | 781 | 35 | 48.6% |

*Idea:* an aggregate fact ("exactly one bit") and an object fact ("one cell flips it") are different statements, and the second one has exceptions.

## Stop 4 - the bit is easy to lose

The last column of the table says a **random** one-cell nudge flips the parity about half the time. So under noise the parity is the first thing to go. [[castle-phone-line](pages/castle-phone-line.md)] plays castles as tones through a simulated telephone line. The block parity sits at a coin flip until the line is almost perfect: 83% correct even when 99.9% of heights arrive exact. Meanwhile the height histogram and the slow trend of the skyline survive every setting. [[song-as-castle](pages/song-as-castle.md)] measured a 44% flip rate for random single-column edits, in the same range.

*Idea:* one bit that depends on every column is the least robust statistic a castle has. Robustness runs opposite to how much of the object a statistic depends on.

## Stop 5 - the bit is easy to write

The same fact makes the bit a channel. Hide a message one bit per castle by setting each castle's parity, fixing it with one chosen cell when needed. [[castle-steganography](pages/castle-steganography.md)] (channel B) did this on the 512 row castles of the cameraman image. 336 bits went into 336 rows, 161 rows needed a one-cell change and 175 already had the right parity. The change is invisible in the parity statistics, since untouched rows split 249 odd to 263 even, a coin flip. The message survives a lossless PNG round trip exactly and is destroyed by JPEG (175 of 336 bits, chance level): Stop 4 again.

*Idea:* a statistic that is cheap to change is a good place to hide a bit, and for the same reason a bad place to store one.

## Stop 6 - in the growth rate, the bit disappears

Divide by `w`. The entropy per column of a castle family is `log₂ ρ`, where `ρ` is its growth constant ([[castle-entropy](pages/castle-entropy.md)]). The parity's one bit, spread over `w` columns, contributes `1/w → 0`. So every growth constant the wiki has catalogued is an **entropy rate**:

| family | growth constant `ρ` | bits per column |
|---|---|---|
| height `≤ h`, no other rule | `h` | `log₂ h` |
| golden rule | `φ = 1.618` | 0.694 |
| silver rule | `1 + √2 = 2.414` | 1.272 |
| plastic rule | `ψ = 1.325` | 0.406 |

Conditioning refines the picture. Knowing a castle's block count `B` already tells you its parity, so the parity bit is redundant with `B`, but not with its area `N`. That is one reason area is the better single summary of a castle ([[castle-conditional-entropy](pages/castle-conditional-entropy.md)]).

*Idea:* a boundary constraint is visible in finite counts and invisible in rates. Rates measure the rule, and boundary terms measure the question asked about it.

## The board

| reading | what the parity clause is | number |
|---|---|---|
| aggregate count | a projector `(A ± S)/2` | costs `1 − log₂(1 + S/A)` bits, exactly 1 in the limit |
| one castle | a sign, flipped by one chosen cell at a weak max or strict min | all but a few castles are one cell from the other parity |
| noise | the most fragile statistic | a random one-cell edit flips it ~50% of the time |
| channel | one hidden bit per castle | 161 one-cell changes for 336 bits |
| growth rate | a boundary term | contributes `1/w → 0` bits per column |

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

A = lambda w, h: h**w - (h - 1)**w         # all castles of width w, height exactly h
S = lambda w, h: P(h - 2, w) - P(h - 1, w) # parity term: (even castles) - (odd castles)
F = lambda w, h: (A(w, h) + S(w, h)) // 2  # the Project Euler 502 count

def castles(w, h):
    return [c for c in product(range(1, h + 1), repeat=w) if max(c) == h]

def one_cell_edits(c, h):                  # move one column up or down by 1, stay a castle of height exactly h
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
>>> [(w, h, F(w, h), round(log2(F(w, h)), 3), round(w * log2(h) - 1, 3)) for w, h in [(8, 2), (12, 2), (12, 3), (40, 3)]]
[(8, 2, 120, 6.907, 7.0), (12, 2, 2080, 11.022, 11.0), (12, 3, 261615, 17.997, 18.02), (40, 3, 6078831630016984399, 62.398, 62.399)]
>>> [(w, h, '%.1e' % (S(w, h) / A(w, h))) for w, h in [(8, 2), (12, 3), (40, 3)]]
[(8, 2, '-5.9e-02'), (12, 3, '-7.8e-03'), (40, 3, '-9.0e-08')]
>>> round(log2(F(13, 10)), 3), round(log2(A(13, 10)) - 1, 3), round(13 * log2(10) - 1, 3)
(41.762, 41.762, 42.185)
>>> [flip_stats(w, h) for w, h in [(4, 2), (6, 3), (7, 3), (5, 4)]]
[(15, 1, 0.429), (665, 2, 0.505), (2059, 6, 0.519), (781, 35, 0.486)]
>>> [c for c in castles(4, 2) if not any(blocks(e) % 2 != blocks(c) % 2 for e in one_cell_edits(c, 2))]
[(1, 2, 2, 1)]
>>> all(blocks(c[:i] + (c[i] + 1,) + c[i+1:]) - blocks(c) == delta_raise(c, i) for c in product(range(5), repeat=5) for i in range(5))
True
```

## Exercises for the room

1. Check the formula for `Δ` on `(1, 3, 2)` by raising each column in turn.
2. Show that `(1, 2, 2, 1)` at `h = 2` has no flipping edit by listing its legal one-cell edits and their block counts.
3. At `w = 13, h = 10`, split the 0.42-bit gap into the parity part and the exact-height part using `log₂(1 − 0.9^13)`.
4. (Open.) Describe exactly which castles have no flipping one-cell edit. In the examples found, plateaus are pinned by the height cap (`(1, 2, 2, 1)`, `(1, 2, 3, 3, 2, 1)`) or by the cap and the floor together (`(3, 3, 1, 1, 3, 3)`). Is that always the mechanism?
5. (Open.) Find a parity-reversing involution on castles of width `w`, height `h`, pairing even with odd castles except for about `|S|` of them. That would be the object-by-object version of "exactly one bit".

## What is still open

These are the R-department items feeding Arc 8 in `IDEAS.md`:
- **Parity-bit object-by-object survival.** Stop 3 gives the flip rule and the small exceptional set; exercises 4 and 5 are the open parts.
- **Rule-generated-castle detector.** A predicate for low-complexity-but-irregular castles, the middle tier of [[castle-compression](pages/castle-compression.md)].

## Appearances in Sources

- [[project-euler-502-observations](pages/project-euler-502-observations.md)] - "parity via signs", the `(A + P)/2` trick.
- [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] - the castle sign as the analogue of the permutation sign.

## Related Concepts

- [[castle-entropy](pages/castle-entropy.md)] - uniform entropy and entropy rate; this page is its classroom version.
- [[castle-sign](pages/castle-sign.md)] - the sign, the projector, and the permutation analogy.
- [[castle-steganography](pages/castle-steganography.md)] / [[castle-phone-line](pages/castle-phone-line.md)] - the bit written and the bit lost.
- [[castle-compression](pages/castle-compression.md)] / [[castle-conditional-entropy](pages/castle-conditional-entropy.md)] - description length and conditioning on block count and area.
- [[castle-notation](pages/castle-notation.md)] - `A`, `S`, `F` and `P(k, L)`.
- [[tower-recursion-master-class](pages/tower-recursion-master-class.md)] / [[hardin-identity-seminar](pages/hardin-identity-seminar.md)] / [[hear-the-shape-seminar](pages/hear-the-shape-seminar.md)] / [[oeis-mining-seminar](pages/oeis-mining-seminar.md)] / [[castle-fibers-char-2-walkthrough](pages/castle-fibers-char-2-walkthrough.md)] - the other seminar pages.
- [[sandcastle-seminar](pages/sandcastle-seminar.md)] - the Sandcastles seminar, following the 16-cell silver castle `(3,2,1,2,2,1,2,3)` through the whole sandpile story.


## Footnotes

[^1]: Verified by execution (Python 3.10, 2026-09-26): `F(w, h) = (A + S)/2` with `S = P(h−2, w) − P(h−1, w)` from the signed-tower dynamic program; the table values and `S/A` ratios are pinned in the Snippet, and `log₂ F(13, 10) = 41.762 = log₂ A(13, 10) − 1` to three decimals against `13·log₂ 10 − 1 = 42.185`. The `w = 8, 12` rows match [[castle-entropy](pages/castle-entropy.md)].
[^2]: [[project-euler-502-observations](pages/project-euler-502-observations.md)] §"Parity via signs" L13 - "Even-block-count is enforced by (A + P)/2, where A is the unsigned total and P is the signed count with (-1)^{blocks}. A symmetry trick that recurs in many combinatorial-enumeration problems."; [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] §"The sign of a castle" L116-123 - "(T + P)/2 = even-block castles, (T - P)/2 = odd-block castles ... exactly the (1 ± sgn)/2 trick".
[^3]: Verified by execution (Python 3.10, 2026-09-26): `delta_raise(c, i)` equals the change in `blocks` for every sequence in `{0..4}^5` and every column `i`, as pinned; `blocks` is the ascent form `c_1 + Σ max(0, c_i − c_{i−1})` of [[castle-sign](pages/castle-sign.md)].
[^4]: Verified by execution (Python 3.10, 2026-09-26): exhaustive over all castles of the listed `(w, h)` and all one-cell `±1` edits that keep heights in `1..h` and some column at `h`; `flip_stats` pinned in the Snippet. The exceptional castles found include `(1, 2, 2, 1)` at `h = 2`, `(1, 2, 3, 3, 2, 1)` and `(3, 3, 1, 1, 3, 3)` at `h = 3`.
