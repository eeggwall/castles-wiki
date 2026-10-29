---
title: Von Neumann castles
category: Concepts
summary: The castle of a hereditarily finite set is a bottom block carrying the castles of its members left to right, one empty column between neighbors, and the von Neumann castle vN(n) is the castle of the ordinal n = {0, 1, …, n − 1}, so vN(2) = (2, 1, 3) and vN(3) = (2, 1, 3, 1, 3, 2, 4). For n ≥ 1, vN(n) has width 2^n − 1, height n + 1, area (n + 1)2^{n−1} (A057711) and column heights s_2(i) + (i mod 2), with s_2 the binary weight; its skyline rises by 2 and falls by the ruler function A001511. Its blocks form the binomial tree, C(n, d) of them in row d + 1, so vN(n) has 2^n blocks and is an even-block castle. The castle of a plane tree is an alternating skyline of odd width, every alternating skyline is the castle of exactly one plane tree, and so the alternating castles with b blocks number the Catalan number C_{b−1}; the castles of sets with b blocks number A004111(b). Under Ackermann's coding every natural number m has a castle ack(m): its block count is 1 plus the block counts of the castles of the positions of its binary 1s (A116549), its width 2·A033922(m) − 1 and its height 1 + A010096(m), vN(n) = ack(A034797(n)), and the m with an odd-block castle ack(m) are A372325.
tags: [concept, castle, von-neumann-castle, ordinal, hereditarily-finite-set, ackermann-coding, binomial-tree, plane-tree, alternating, catalan, binary-weight, ruler-function, block-count, parity, oeis, verification]
sources: [project-euler-502-brute-force, analytic-combinatorics-ch1-ogfs]
created: 2026-10-28
updated: 2026-10-28
---

# Von Neumann castles

## Definition

A castle of width `w` and height `h` is a skyline `(c_1, …, c_w)` with `1 ≤ c_i ≤ h` and some `c_i = h` ([[castle-polyomino](pages/castle-polyomino.md)]). Its blocks are the maximal runs of columns in each row, so two blocks of one row are separated by a lower column, and every block sits on a block of the row below.[^blocks]

Von Neumann defined each ordinal as the set of the ordinals before it: "Jede Ordnungszahl ist die Menge der ihr vorangehenden Ordnungszahlen", every ordinal is the set of the ordinals that precede it.[^vn] So `0 = ∅`, `1 = {0}`, `2 = {0, 1}`, `3 = {0, 1, 2}`, and in general `n = {0, 1, …, n − 1}` and `n + 1 = n ∪ {n}`.[^wpnat] A set is **hereditarily finite** when it is finite and its members are hereditarily finite, down to the empty set; every von Neumann natural number is one.[^hf]

The **castle of a set** `x`, written `castle(x)`, is built from the castles of its members:

- `castle(∅)` is a single block, the skyline `(1)`;
- if `x` has the members `y_1, …, y_m` in a chosen order, `castle(x)` is a bottom block carrying `castle(y_1), …, castle(y_m)` from left to right, with one empty column between neighbors. The bottom block is exactly as wide as what it carries.

Every block sits on the block below it, and the blocks of one row are separated by an empty column, so `castle(x)` is a castle. It depends on the order of the members, which the section *The castle of every natural number* fixes. The same rule turns a plane tree, a root with an ordered sequence of subtrees, into a castle.

The **von Neumann castle** `vN(n)` is the castle of the ordinal `n` with its members in increasing order: the bottom block carrying `vN(0), vN(1), …, vN(n − 1)`. It is written `vN(n)` because `V(w, h)` is the set of even-block castles of width `w` and height `h` ([[castle-notation](pages/castle-notation.md)]).

*Example.* `vN(0) = (1)`, `vN(1) = (2)`, `vN(2) = (2, 1, 3)` and `vN(3) = (2, 1, 3, 1, 3, 2, 4)`. In the last drawing each cell of `vN(3)` shows the ordinal whose castle has the cell's block as its bottom block:

```
vN(0)   vN(1)   vN(2)   vN(3)           vN(3), by ordinal

                        . . . . . . #   . . . . . . 0
                . . #   . . # . # . #   . . 0 . 0 . 1
        #       # . #   # . # . # # #   0 . 1 . 2 2 2
#       #       # # #   # # # # # # #   3 3 3 3 3 3 3
```

The bottom block of `vN(3)` is the ordinal 3. It carries `vN(0)` in column 1, `vN(1)` in column 3 and `vN(2)` in columns 5 to 7, with the empty columns 2 and 4 between them.[^exec1]

## Width, height, area and columns

**Theorem 1.** For `n ≥ 1`, `vN(n)` has width `2^n − 1`, height `n + 1` and area `(n + 1)2^{n−1}`, and its column `i` has height

```
c_i  =  s_2(i) + (i mod 2),        i = 1, …, 2^n − 1,                         (1)
```

with `s_2(i)` the number of 1s in the binary form of `i`, the binary weight A000120.[^a120] The castle `vN(0) = (1)` has width 1, and the areas `1, 2, 6, 16, 40, 96, …` of `vN(0), vN(1), vN(2), …` are A057711(`n + 1`).[^a57711]

*Proof.* `vN(1) = (2)` satisfies (1). For `n ≥ 1`, `vN(n + 1)` is a bottom block carrying `vN(0), …, vN(n)`, and the bottom block with `vN(0), …, vN(n − 1)` on it is `vN(n)`. So

```
vN(n + 1)  =  vN(n), then a column of height 1, then vN(n) with every column raised by 1.   (2)
```

The width becomes `2(2^n − 1) + 1 = 2^{n+1} − 1` and the height grows by one. Column `2^n` has height `1 = s_2(2^n)`, and for `1 ≤ j < 2^n` column `2^n + j` has height `c_j + 1 = s_2(2^n + j) + (j mod 2)`, which is (1) for `vN(n + 1)`. By (1) the even and odd columns are

```
c_{2j}  =  s_2(j),        c_{2j+1}  =  s_2(j) + 2,
```

so the area is `2 Σ_{j < 2^{n−1}} s_2(j) + 2^n = (n − 1)2^{n−1} + 2^n = (n + 1)2^{n−1}`, since each of the `n − 1` binary digits is 1 in half of the numbers below `2^{n−1}`. ∎

By (2), `vN(n)` is the beginning of `vN(n + 1)` for `n ≥ 1`, so the von Neumann castles are the first `2^n − 1` columns of one infinite skyline, `2, 1, 3, 1, 3, 2, 4, 1, 3, 2, 4, 2, 4, 3, 5, …`. It starts at height 2 and then falls and rises in turn: into column `2j + 1` it rises by 2, and into column `2j` it falls by `1 + v_2(j)`, with `v_2(j)` the exponent of 2 in `j`. The falls `1, 2, 1, 3, 1, 2, 1, 4, …` are the ruler function A001511, which also numbers the disk moved at each step of the shortest solution of the Tower of Hanoi. `vN(n)` has `2^{n−1} − 1` falls, as many as there are moves for `n − 1` disks.[^ruler][^exec2]

## Blocks: the binomial tree

The **membership tree** of a set `x` has `x` at its root, and the children of each node are its members. Each block of `castle(x)` is the bottom block of the castle of exactly one node of this tree. A block in row `d + 1` belongs to a node at depth `d`, and the block below it to the node's parent.

The membership tree of the ordinal `n` is a root whose subtrees are the membership trees of `0, 1, …, n − 1`. A **binomial tree** of order `k` is a root whose children are binomial trees of orders `k − 1, k − 2, …, 1, 0`; it has `2^k` nodes, height `k`, and `C(k, d)` nodes at depth `d`.[^binom] The two recursions agree up to the order of the children, so the membership tree of `n` is the binomial tree of order `n`.

**Theorem 2.** Row `d + 1` of `vN(n)` has `C(n, d)` blocks, for `d = 0, …, n`, so `vN(n)` has `2^n` blocks. For `n ≥ 1` it is an even-block castle, one of the `A^e(2^n − 1, n + 1)` castles that Project Euler 502 counts ([[castle-sign](pages/castle-sign.md)]).

*Proof.* The blocks in row `d + 1` are the nodes at depth `d` of the binomial tree of order `n`, and `Σ_d C(n, d) = 2^n`. ∎

The column formula gives the same total: every rise of `vN(n)` is 2, so `blocks = c_1 + Σ_{i ≥ 2} max(0, c_i − c_{i−1}) = 2 + 2(2^{n−1} − 1) = 2^n`.[^blocks]

| `n` | `vN(n)` | blocks by row, from the bottom | blocks |
|---|---|---|---|
| 0 | `(1)` | 1 | 1 |
| 1 | `(2)` | 1, 1 | 2 |
| 2 | `(2, 1, 3)` | 1, 2, 1 | 4 |
| 3 | `(2, 1, 3, 1, 3, 2, 4)` | 1, 3, 3, 1 | 8 |
| 4 | `(2, 1, 3, 1, 3, 2, 4, 1, 3, 2, 4, 2, 4, 3, 5)` | 1, 4, 6, 4, 1 | 16 |

Every entry agrees with brute-force enumeration.[^exec3] `vN(0)`, a single block, is the only odd-block von Neumann castle.

## Castles of trees are alternating castles

A leaf of a plane tree has a castle one column wide, and a node with `m` children puts `m − 1` empty columns between their castles, `ℓ − 1` in all for a tree with `ℓ` leaves. So the castle of a plane tree `t` has width `2ℓ − 1`. Its odd columns `1, 3, …, 2ℓ − 1` are the leaves from left to right, each one higher than the depth of its leaf, and the even column between two neighboring leaves is one higher than the depth of their deepest common ancestor. That ancestor has a smaller depth than either leaf, so every odd column is higher than its neighbors:

```
c_1 > c_2 < c_3 > c_4 < ⋯ < c_w,        w = 2ℓ − 1.                            (3)
```

An **alternating** castle is a castle of odd width that satisfies (3); the single column `(c_1)` is one. Among the shape types of [[castle-classification-shape](pages/castle-classification-shape.md)], they are the castles of the Zigzag type, whose differences `c_{i+1} − c_i` alternate in sign, with odd width and a fall first. They are not the zig-zag castles of [[zig-zag-castles](pages/zig-zag-castles.md)], whose differences are all `±1`.

**Theorem 3.** Every alternating castle is the castle of exactly one plane tree, its **block tree**, in which the children of a block are the blocks standing on it, from left to right. So `castle` maps the plane trees with `b` nodes one-to-one onto the alternating castles with `b` blocks, and these number the Catalan number `C_{b−1}`: `1, 1, 2, 5, 14, 42, 132, …` for `b = 1, 2, 3, …` ([[catalan-numbers](pages/catalan-numbers.md)]).

*Proof.* Let `c` be alternating, and let a block `B` of row `r` cover the columns `a, …, b`. In (3) every rise ends at an odd column and every fall starts at one, so `a` and `b` are odd. The neighbors of an odd column are lower, so an odd column of height `r` is a block of row `r` by itself. Hence if `a < b`, the odd columns of `B` reach row `r + 1`, and the columns of `B` of height exactly `r` are even and isolated: the blocks of row `r + 1` on `B` are separated by single empty columns, the first starts at column `a` and the last ends at column `b`. If `a = b`, `B` is one column of height `r` with nothing on it. So `c` is the castle of its block tree. The block tree of the castle of a plane tree is the tree itself, so the tree is unique, and the plane trees with `b` nodes number `C_{b−1}`.[^plane] ∎

None of the width `2ℓ − 1`, the height (one more than the height of the tree), the block count (the number of nodes) and the area (the sum of the widths of the blocks) depends on the order of the children.[^exec4]

## The castle of every natural number

Ackermann coded the hereditarily finite sets by the natural numbers. The code of a set `x` is

```
code(x)  =  Σ_{y ∈ x} 2^{code(y)},                                              (4)
```

so `code(∅) = 0`, and a set whose members have the codes `k_1 < ⋯ < k_s` has the code `2^{k_1} + ⋯ + 2^{k_s}`. Every natural number `m` is the code of exactly one set: its members are the sets whose codes are the positions of the 1s in the binary form of `m`, counted from 0 at the right.[^hf]

The **Ackermann castle** `ack(m)` is the castle of the set with code `m`, its members in increasing code: the 1s of the binary form of `m`, read from the lowest digit up, put the castles `ack(k_1), …, ack(k_s)` on the bottom block from left to right. The ordinal `n + 1 = n ∪ {n}` has the code `code(n) + 2^{code(n)}`, since `n` is not a member of `n`, so the codes of the ordinals are A034797, `0, 1, 3, 11, 2059, 2^{2059} + 2059, …`,[^a34797] and

```
vN(n)  =  ack(A034797(n)):        vN(2) = ack(3),   vN(3) = ack(11),   vN(4) = ack(2059).
```

The first sixteen, with the members listed by their codes:

| `m` | binary | members | `ack(m)` | width | height | blocks |
|---|---|---|---|---|---|---|
| 0 | `0` | none | `(1)` | 1 | 1 | 1 |
| 1 | `1` | 0 | `(2)` | 1 | 2 | 2 |
| 2 | `10` | 1 | `(3)` | 1 | 3 | 3 |
| 3 | `11` | 0, 1 | `(2, 1, 3)` | 3 | 3 | 4 |
| 4 | `100` | 2 | `(4)` | 1 | 4 | 4 |
| 5 | `101` | 0, 2 | `(2, 1, 4)` | 3 | 4 | 5 |
| 6 | `110` | 1, 2 | `(3, 1, 4)` | 3 | 4 | 6 |
| 7 | `111` | 0, 1, 2 | `(2, 1, 3, 1, 4)` | 5 | 4 | 7 |
| 8 | `1000` | 3 | `(3, 2, 4)` | 3 | 4 | 5 |
| 9 | `1001` | 0, 3 | `(2, 1, 3, 2, 4)` | 5 | 4 | 6 |
| 10 | `1010` | 1, 3 | `(3, 1, 3, 2, 4)` | 5 | 4 | 7 |
| 11 | `1011` | 0, 1, 3 | `(2, 1, 3, 1, 3, 2, 4)` | 7 | 4 | 8 |
| 12 | `1100` | 2, 3 | `(4, 1, 3, 2, 4)` | 5 | 4 | 8 |
| 13 | `1101` | 0, 2, 3 | `(2, 1, 4, 1, 3, 2, 4)` | 7 | 4 | 9 |
| 14 | `1110` | 1, 2, 3 | `(3, 1, 4, 1, 3, 2, 4)` | 7 | 4 | 10 |
| 15 | `1111` | 0, 1, 2, 3 | `(2, 1, 3, 1, 4, 1, 3, 2, 4)` | 9 | 4 | 11 |

Every entry agrees with brute-force enumeration.[^exec6]

Write `leaves(m)` for the number of leaves of the membership tree of the set with code `m`, the number of empty sets in it written out in full, and `rank(m)` for its rank, the smallest ordinal greater than the ranks of all its members, so that `rank(0) = 0`.[^rank]

**Theorem 4.** Let `m ≥ 1` have its binary 1s in the positions `k_1 < ⋯ < k_s`. Then

```
blocks(ack(m))  =  1 + blocks(ack(k_1)) + ⋯ + blocks(ack(k_s)),                  (5)
leaves(m)       =  leaves(k_1) + ⋯ + leaves(k_s),     width of ack(m) = 2·leaves(m) − 1,    (6)
rank(m)         =  1 + rank(k_s),                      height of ack(m) = rank(m) + 1,      (7)
```

with `blocks(ack(0)) = leaves(0) = 1`. So `ack(m)` has A116549(`m`) blocks, width `2·A033922(m) − 1` and height `1 + A010096(m)`. Its height depends only on the length of the binary form of `m`: `ack(m)` has height `h` exactly when `A014221(h − 2) ≤ m < A014221(h − 1)`, that is, height 1 at `m = 0`, 2 at `m = 1`, 3 for `m = 2, 3`, 4 for `4 ≤ m < 16`, 5 for `16 ≤ m < 65536` and 6 for `65536 ≤ m < 2^{65536}`.

*Proof.* (5) counts the nodes of the membership tree, a root and the trees of its members (section *Blocks: the binomial tree*). (6) holds because the leaves of a tree with a nonempty root are the leaves of the root's subtrees, and the width is Theorem 3's `2ℓ − 1`. For (7), the height of `ack(m)` is one more than the height of the membership tree, which is the rank. The sets of rank at most `r` are those with the codes below `A014221(r)`, the number of sets of rank at most `r`.[^a14221] By induction on `r`: the only set of rank 0 is `∅`, of code 0, and `A014221(0) = 1`; for `r ≥ 1` a set has rank at most `r` exactly when all of its members have rank at most `r − 1`, that is, codes below `A014221(r − 1)`, and by (4) that holds exactly when its own code is below `2^{A014221(r − 1)} = A014221(r)`. So the rank never decreases as the code grows, the member of largest rank is the last, of code `k_s`, and (7) follows, together with the range of `m` at each height.

These are the recursions of three OEIS entries. A116549 is defined by `a(0) = 1` and `a(m + 2^n) = a(n) + a(m)` for `0 ≤ m < 2^n`, which is (5) split at the highest binary digit, and Thomas Anton's comment on it reads `a(n)` as the number of pairs of braces of the `n`-th set written out in full, under the same coding.[^a116549] A033922, the base-2 digital convolution sequence, has `a(0) = 1` and `a(n) = a(k_1) + ⋯ + a(k_i)` for `n = 2^{k_1} + ⋯ + 2^{k_i}`, which is (6).[^a33922] A010096, the iterated logarithm `log2*(n)`, has the program `a(n) = if(n < 1, 0, 1 + a(logint(n, 2)))`, which is (7), since `k_s = ⌊log_2 m⌋`.[^a10096] ∎

**Single columns.** `ack(m)` has width 1 exactly when its set has one leaf, that is, when the set is `∅`, `{∅}`, `{{∅}}`, …, each the set whose only member is the one before. These are the Zermelo ordinals, `0 = { }` and `S(a) = {a}`,[^zermelo] with the codes `0, 1, 2, 4, 16, 65536, …` of A014221, at which A033922 is 1.[^a33922] The Zermelo ordinal `n` is the single column `(n + 1)`, and the von Neumann ordinal `n` is `vN(n)`, of width `2^n − 1`.[^exec6]

**Block parity.** By (5), `ack(m)` has an odd number of blocks exactly when an even number of the positions `k_1, …, k_s` are numbers whose own castles have an odd number of blocks. That is the rule of A372325, "Numbers whose binary expansion has an even number of 1's among positions listed in this sequence", and every position of a 1 of `m` is less than `m`, so by induction on `m` the `m` with an odd-block castle `ack(m)` are the terms of A372325, `0, 2, 5, 7, 8, 10, 13, 15, 16, 18, …`.[^a372325] By (5) they are also the `m` with A116549(`m`) odd. The rest, the `m < 64` with an even-block castle `ack(m)`, are `1, 3, 4, 6, 9, 11, 12, 14, 17, 19, 20, 22, 25, 27, 28, 30, 32, 34, 37, 39, 40, 42, 45, 47, 48, 50, 53, 55, 56, 58, 61, 63`, among them the codes 1, 3 and 11 of the ordinals 1, 2 and 3.[^exec6]

**The castles of sets by blocks.** The block tree of `ack(m)` gives back the set with code `m`, so distinct sets have distinct castles, and the castles of the sets with `b` blocks, their members in increasing code, number the sets with `b` pairs of braces. These are the rooted identity trees with `b` nodes, A004111: `1, 1, 1, 2, 3, 6, 12, 25, 52, 113, 247, 548, 1226, …` for `b = 1, 2, 3, …`.[^a4111] Among the five alternating castles with 4 blocks, `(2, 1, 3) = ack(3)` and `(4) = ack(4)` are castles of sets.[^exec5]

## Related Concepts

- [[castle-polyomino](pages/castle-polyomino.md)] - castles, skylines, and the blocks of a castle as the maximal runs of columns in each row.
- [[castle-sign](pages/castle-sign.md)] - the parity of the block count; every `vN(n)` with `n ≥ 1` is an even-block castle.
- [[castle-classification-shape](pages/castle-classification-shape.md)] - the Zigzag type, with differences alternating in sign; its castles of odd width that fall first are the alternating castles, the castles of plane trees.
- [[zig-zag-castles](pages/zig-zag-castles.md)] - a different family: neighboring columns differ by exactly 1.
- [[catalan-numbers](pages/catalan-numbers.md)] - the plane trees with `b` nodes, `C_{b−1}` of them, and so the alternating castles with `b` blocks.
- [[castle-notation](pages/castle-notation.md)] - `vN(n)`, `castle(x)`, `code(x)`, `ack(m)` and `s_2(i)`.
- [[castle-sequence-catalog](pages/castle-sequence-catalog.md)] - the von Neumann and Ackermann castle rows.

## Footnotes

[^blocks]: [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)] §"Column-height encoding" L20-27 - "A block is a maximal horizontal run of columns at a given level, so", "= c_1 + \sum_{i=2}^{w} \max(0, c_i - c_{i-1})", and "two runs at the same level are always separated by a strictly lower column".
[^vn]: https://acta.bibl.u-szeged.hu/13294/1/math_001_199-208.pdf (J. v. Neumann, "Zur Einführung der transfiniten Zahlen", *Acta litterarum ac scientiarum Regiae Universitatis Hungaricae Francisco-Josephinae, Sectio scientiarum mathematicarum* 1 (1923) 199-208, read 2026-10-28) - Einleitung, p.199: "Jede Ordnungszahl ist die Menge der ihr vorangehenden Ordnungszahlen.", followed by the ordinals 0 to 3 and ω written out, with "(O ist die leere Menge, (a, b, c, ...) die Menge mit den Elementen a, b, c, ...)".
[^wpnat]: https://en.wikipedia.org/wiki/Set-theoretic_definition_of_natural_numbers (read 2026-10-28) - §"Definition as von Neumann ordinals": "the natural numbers are defined recursively by letting 0 = {} be the empty set and n + 1 (the successor function) = n ∪ {n} for each n. In this way n = {0, 1, …, n − 1} for each natural number n."
[^hf]: https://en.wikipedia.org/wiki/Hereditarily_finite_set (read 2026-10-28) - "hereditarily finite sets are defined as finite sets whose elements are all hereditarily finite sets"; §"Ackermann coding": "In 1937, Wilhelm Ackermann introduced an encoding of hereditarily finite sets as natural numbers", "f(a) = Σ_{b∈a} 2^{f(b)}", "The inverse f^{−1}: ℕ → H_{ℵ0} of this function is given by f^{−1}(i) = {f^{−1}(j) ∣ BIT(i, j) = 1}"; §"Theories of finite sets": "All finite von Neumann ordinals are indeed hereditarily finite". The article writes `f` for the code.
[^rank]: https://en.wikipedia.org/wiki/Von_Neumann_universe (read 2026-10-28) - "The rank of a well-founded set is defined inductively as the smallest ordinal number greater than the ranks of all members of the set. In particular, the rank of the empty set is zero, and every ordinal has a rank equal to itself."
[^zermelo]: https://en.wikipedia.org/wiki/Natural_number (read 2026-10-28) - §"Set-theoretic definition": "Another construction sometimes called Zermelo ordinals defines 0 = { } and S(a) = {a} and is now largely only of historical interest."
[^binom]: https://en.wikipedia.org/wiki/Binomial_heap (read 2026-10-28) - §"Binomial heap": "A binomial tree of order 0 is a single node", "A binomial tree of order k has a root node whose children are roots of binomial trees of orders k − 1, k − 2, ..., 2, 1, 0 (in this order).", "A binomial tree of order k has 2^k nodes, and height k. The name comes from the shape: a binomial tree of order k has", then the binomial coefficient `C(k, d)`, "nodes at depth d".
[^plane]: [[analytic-combinatorics-ch1-ogfs](pages/analytic-combinatorics-ch1-ogfs.md)] §I.2.3 pp.34-35 - "The recursive specification of general trees leads to an implicit definition of their OGF, G = Z × SEQ(G) ⟹ G(z) = z/(1−G(z))", "G(z) = ½(1 − √(1−4z))", "For this reason the term Catalan tree is often employed as synonymous to 'general (rooted unlabelled plane) tree'."
[^a120]: https://oeis.org/A000120 (read 2026-10-28) - "Ones-counting sequence: number of 1's in binary expansion of n (or the binary weight of n)."
[^a57711]: https://oeis.org/A057711 (read 2026-10-28) - "a(0)=0, a(1)=1, a(n) = n*2^(n-2) for n >= 2."
[^ruler]: https://oeis.org/A001511 (read 2026-10-28) - "The ruler function: exponent of the highest power of 2 dividing 2n. Equivalently, the 2-adic valuation of 2n.", and "a(n) is the number of the disk to be moved at the n-th step of the optimal solution to Towers of Hanoi problem (comment from _Andreas M. Hinz_)."
[^a34797]: https://oeis.org/A034797 (read 2026-10-28) - "a(0) = 0; a(n+1) = a(n) + 2^a(n).", with the comments "The natural 1-1 correspondence between nonnegative numbers and hereditarily finite sets is given by f(A)=sum over members m of A of 2^f(m)." and "The next term, a(5) = 2^2059 + 2059, has 620 decimal digits and is too large to include. - _Olivier Gérard_, Jun 26 2001".
[^a14221]: https://oeis.org/A014221 (read 2026-10-28) - "a(n+1) = 2^a(n) with a(-1) = 0.", data "0, 1, 2, 4, 16, 65536" from `n = −1`, and "Number of sets of rank no more than n. - _Eric M. Schmidt_, Jun 29 2013 [Corrected by _Jianing Song_, Nov 24 2018]".
[^a116549]: https://oeis.org/A116549 (read 2026-10-28) - "a(0) = 1. a(m + 2^n) = a(n) + a(m), for 0 <= m <= 2^n - 1.", and the comment "Consider the following bijection between the natural numbers and hereditarily finite sets. For each n, write out n in binary. Assign to each set already given a natural number m the (m+1)-th digit of the binary number (reading from right to left). Let the set assigned to n contain all and only those sets which have a 1 for their digit. Then a(n) gives the number of pairs of braces appearing in the n-th set written out in full, e.g., for 3, we have {{{}}{}}, with 4 pairs of braces. - _Thomas Anton_, Mar 16 2019".
[^a33922]: https://oeis.org/A033922 (read 2026-10-28) - "Base-2 digital convolution sequence.", "Definition: a(0) = 1; for n > 0, let the base-2 representation of n be 2^k_1 + ... + 2^k_i, then a(n) = a(k_1) + ... + a(k_i).", and the cross-reference "A014221 (n such that a(n)=1)".
[^a10096]: https://oeis.org/A010096 and https://oeis.org/A230864 (read 2026-10-28) - A010096: "log2*(n) (version 1): number of times floor(log_2(x)) is used in floor(log_2(floor(log_2(...(floor(log_2(n)))...)))) = 0.", and the program "a(n)=if(n<1,0,1+a(logint(n,2))) \\ _Charles R Greathouse IV_, Oct 23 2015"; A230864: "a(1)=0; thereafter a(n) = A010096(n-1)", so the height of `ack(m)` is also `1 + A230864(m + 1)`.
[^a372325]: https://oeis.org/A372325 (read 2026-10-28) - "Numbers whose binary expansion has an even number of 1's among positions listed in this sequence.", data from `n = 1` "0,2,5,7,8,10,13,15,16,18,21,23,24,26,29,31,…", and the example "118 is in the sequence because 118 = 2^6 + 2^5 + 2^4 + 2^2 + 2^1, and an even number of the exponents 6,5,4,2,1 (namely 2,5) are in the sequence." (David A. Madore, Apr 27 2024).
[^a4111]: https://oeis.org/A004111 (read 2026-10-28) - "Number of rooted identity trees with n nodes (rooted trees whose automorphism group is the identity group).", and "There is a natural correspondence between rooted identity trees and finitary sets (sets whose transitive closure is finite); each node represents a set, with the children of that node representing the members of that set. When the set corresponding to an identity tree is written out using braces, there is one set of braces for each node of the tree; thus a(n) is also the number of sets that can be made using n pairs of braces. - _Franklin T. Adams-Watters_, Oct 25 2011".
[^exec1]: Verified by execution (Python 3.11, 2026-10-28): `bin/python/von_neumann_castles.py` item [1], run log `bin/python/von_neumann_castles-run.log`. The castles `vN(0)` to `vN(4)`, the drawings, and Equation (2) for `n = 1, …, 12`.
[^exec2]: Verified by execution (Python 3.11, 2026-10-28): `bin/python/von_neumann_castles.py` item [2], run log `bin/python/von_neumann_castles-run.log`. Theorem 1 for `n = 1, …, 14`, the areas against A057711 for `n = 0, …, 14`, the even and odd columns of `vN(7)` against A000120, and the rises of 2 and the falls against A001511 for `n ≤ 7` and against `1 + v_2(j)` for `n ≤ 14`.
[^exec3]: Verified by execution (Python 3.11, 2026-10-28): `bin/python/von_neumann_castles.py` item [3], run log `bin/python/von_neumann_castles-run.log`. The membership tree of `n` against the binomial tree of order `n` for `n ≤ 10`, the blocks of each row of `vN(n)` against `C(n, d)`, and the column formula against `2^n`, for `n ≤ 14`.
[^exec4]: Verified by execution (Python 3.11, 2026-10-28): `bin/python/von_neumann_castles.py` item [4], run log `bin/python/von_neumann_castles-run.log`. The castles of all 6918 plane trees with at most 10 nodes are alternating, with width `2ℓ − 1`, height one more than the tree's and as many blocks as nodes, and have the tree as their block tree; the 19204 alternating skylines of odd width at most 9 on the heights 1 to 5 are the castles of their block trees; the alternating castles with `b` blocks, enumerated directly, against A000108(`b − 1`) for `b ≤ 8`; the width, height, block count and area of the castles of sets unchanged when the root's members are reversed, for at most 10 blocks.
[^exec5]: Verified by execution (Python 3.11, 2026-10-28): `bin/python/von_neumann_castles.py` item [5], run log `bin/python/von_neumann_castles-run.log`. All hereditarily finite sets with at most 13 nodes, against A004111; their castles, members in increasing code (compared without computing the codes), are distinct, alternating, with as many blocks as nodes and width `2ℓ − 1`.
[^exec6]: Verified by execution (Python 3.11, 2026-10-28): `bin/python/von_neumann_castles.py` item [6], run log `bin/python/von_neumann_castles-run.log`. The table for `m ≤ 15`; Equations (5), (6) and (7) and the A116549 recursion for `m < 2^16`; the block counts, widths and heights against the data fields of A116549, A033922, A010096 and A230864; the heights against the ranges of A014221 for `m < 2^16` and at `m = 65536`; the widths equal to 1 exactly at `m = 0, 1, 2, 4, 16` below `2^16`, and `ack(65536) = (6)`; `vN(n) = ack(A034797(n))` for `n ≤ 4`; the parity rule for `m < 2^16`, the odd-block `m` against the data field of A372325 and its rule for `m < 2^16`, against its example 118 and non-example 8192, and against A116549 odd on its data field.
