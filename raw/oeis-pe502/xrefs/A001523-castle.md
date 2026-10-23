# Cross-link draft — A001523 (stacks) as the castles with as many blocks as their height

Status: DRAFT for Charles to submit.
Execution notes (field map, signature format, scope): see ../SUBMISSION-NOTES.md.
Checked against the live entry 2026-10-23 (A001523 revision #135, May 30 2026).

## Edits (lines to add)

All additions; nothing existing is changed.

**COMMENTS** (append after the last comment):

```
For n >= 1, a(n) is also the number of castle polyominoes with n cells whose number of blocks equals their height, of any height and without the rule that the number of blocks is even (Project Euler, Problem 502: Counting Castles): the column heights c(1), ..., c(w) form a composition of n and the blocks are the maximal horizontal runs of cells, so each of the max(c) rows holds at least one block, and exactly one when c(1), ..., c(w) is weakly unimodal, that is, when the castle is a stack as in the first comment. - _Chaz Reid_, Mon DD YYYY
```

**LINKS** (insert in alphabetical order, after Flórez, Ramírez, and Villamizar and before
Rhoades):

```
Project Euler, <a href="https://projecteuler.net/problem=502">Problem 502: Counting Castles</a>.
```

No CROSSREFS: the entry already says "The complement is counted by A115981."

## What the entry already has, and what this adds

The first comment, "a(n) counts stacks of integer-length boards of total length n where no board
overhangs the board underneath", is the same set of objects: a stack is a castle with one block per
row. The entry also has the weakly unimodal compositions and links Flórez, Ramírez, and Villamizar on
restricted bargraphs. A comment that only renamed stacks as convex castles would repeat the first
comment, so this one adds the castle's own statistic: among all castles with n cells, the stacks are
exactly those with the fewest blocks, as many as their height. A115981 gets the complementary comment
(`A115981-castle.md`).

## Proof

A castle with n cells is a composition (c(1), ..., c(w)) of n; its blocks are the maximal runs of
cells in each row, so the number of blocks is c(1) + Sum_{i=2..w} max(0, c(i) - c(i-1)). Row r,
for 1 <= r <= h = max(c), consists of the columns with c(i) >= r, which is nonempty, so it holds at
least one block, and the castle has at least h blocks. It has exactly h blocks when every row is a
single run of columns, which holds for every r exactly when (c(i)) is weakly unimodal.

## Verification

Enumeration of all compositions of n <= 18 (2026-10-23): blocks >= height for every castle, with
equality exactly for the weakly unimodal ones; the castles with blocks = height number A001523(n),
and those with more blocks than height A115981(n).

```python
def comps(n):
    if n == 0: yield (); return
    for f in range(1, n + 1):
        for r in comps(n - f): yield (f,) + r
A001523 = [1,1,2,4,8,15,27,47,79,130,209,330,512,784,1183,1765,2604,3804,5504]
for n in range(1, 19):
    eq = sum(1 for c in comps(n) if c[0] + sum(max(0, c[i] - c[i-1]) for i in range(1, len(c))) == max(c))
    assert eq == A001523[n]
print("ok")
```
