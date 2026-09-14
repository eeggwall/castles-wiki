---
title: Castle counting function F(w,h)
category: Concepts
summary: F(w,h), the number of valid castles on a w×h grid; PE 502 restricts it to even block counts and asks for a sum of three large evaluations mod 1e9+7.
tags: [concept, castle, counting-function, project-euler]
sources: [project-euler-502, project-euler-502-problem-setup]
created: 2026-09-13
updated: 2026-09-13
---

# Castle counting function F(w,h)

## Description

`F(w,h)` is the function that returns the number of valid [[castle-polyomino](pages/castle-polyomino.md)] configurations for a game grid *w* units wide and *h* units tall.[^1] It is the quantity Project Euler 502 asks the solver to compute.

**The even-block restriction is a special case.** As stated in Project Euler 502, `F(w,h)` counts only castles made from an **even** number of blocks.[^2] In this wiki's framing, that parity constraint is a restriction on top of the general castle object — the general and more interesting problem is counting *all* castles regardless of parity, of which the even-only count is a special case (see [[castle-polyomino](pages/castle-polyomino.md)]). The parity restriction is precisely what makes PE 502 hard and interesting rather than a trivial specialization.

**Known checkpoints.** The source gives four values that any correct implementation must reproduce:[^3]

| grid (w, h) | F(w,h) |
|---|---|
| (4, 2) | 10 |
| (13, 10) | 3 729 050 610 636 |
| (10, 13) | 37 959 702 514 |
| (100, 100) | 841 913 936  (mod 1 000 000 007) |

Note that `F(13,10) ≠ F(10,13)` — the function is **not** symmetric in *w* and *h*, which follows from the asymmetric roles of width (the full base row) and height (the exact maximum) in the castle rules.

**The problem's target.** PE 502 asks for a single value combining three evaluations at large arguments, taken modulo 1 000 000 007:[^4]

```
(F(10^12, 100) + F(10000, 10000) + F(100, 10^12)) mod 1,000,000,007
```

The three arguments deliberately stress different regimes: a very wide/short grid, a large square grid, and a narrow/very tall grid — so a solution must handle both dimensions scaling independently and to sizes far beyond brute-force enumeration.

## Appearances in Sources

- [[project-euler-502](pages/project-euler-502.md)] — introduces `F(w,h)`, gives the four checkpoint values, and states the target sum modulo 1 000 000 007.
- [[project-euler-502-problem-setup](pages/project-euler-502-problem-setup.md)] — invokes the scale of `F` (`F(13,10) = 3,729,050,610,636`, target height 10^12) to motivate a generating-function approach over direct enumeration.

## Related Concepts

- [[castle-polyomino](pages/castle-polyomino.md)] — the object `F(w,h)` counts; PE 502's even-block count is a special case of the general (parity-agnostic) count.
- [[generating-functions](pages/generating-functions.md)] — the intended method for computing `F(w,h)` at large parameters.

## Footnotes

[^1]: [[project-euler-502](pages/project-euler-502.md)] §"Project 502: Castle Polyominoes" L26 — "Let F(w,h) represent the number of valid castles, given grid parameters w and h."
[^2]: [[project-euler-502](pages/project-euler-502.md)] §"Project 502: Castle Polyominoes" L20 — "The castle is made from an even number of blocks."
[^3]: [[project-euler-502](pages/project-euler-502.md)] §"Project 502: Castle Polyominoes" L28 — "F(4,2) = 10, F(13,10) = 3729050610636, F(10,13) = 37959702514, and F(100,100) mod 1,000,000,007 = 841913936".
[^4]: [[project-euler-502](pages/project-euler-502.md)] §"Project 502: Castle Polyominoes" L30 — "Find (F(10^12,100) + F(10000,10000) + F(100,10^12)) mod 1,000,000,007."
