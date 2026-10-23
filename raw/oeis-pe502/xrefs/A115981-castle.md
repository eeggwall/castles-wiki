# Cross-link draft — A115981 (compositions that are not stacks) as the castles with more blocks than their height

Status: DRAFT for Charles to submit. Submit after, or together with, the A001523 comment
(`A001523-castle.md`), which it refers to.
Execution notes (field map, signature format, scope): see ../SUBMISSION-NOTES.md.
Checked against the live entry 2026-10-23 (A115981 revision #23, Feb 16 2025).

## Edits (lines to add)

All additions; nothing existing is changed.

**COMMENTS** (append after Gus Wiseman's comment):

```
For n >= 1, a(n) is also the number of castle polyominoes with n cells that have more blocks than their height, of any height and without the rule that the number of blocks is even (Project Euler, Problem 502: Counting Castles): the column heights form a composition of n and the blocks are the maximal horizontal runs of cells; every castle has at least as many blocks as its height, with equality exactly for the stacks counted by A001523. - _Chaz Reid_, Mon DD YYYY
```

**LINKS** (after Weisstein, the only link):

```
Project Euler, <a href="https://projecteuler.net/problem=502">Problem 502: Counting Castles</a>.
```

No CROSSREFS: the entry already says "The complement is counted by A001523."

## What the entry already has, and what this adds

The name, "compositions of n which cannot be viewed as stacks", and the formula
`a(n) = A011782(n) - A001523(n)` describe the same set. The comment adds the castle statistic that
separates it from its complement: these are the castles with n cells that need more blocks than
rows.

## Proof and verification

See `A001523-castle.md`: blocks >= height for every castle, with equality exactly for the weakly
unimodal column heights. The enumeration there checks the count against A115981 for n <= 18
(2026-10-23).
