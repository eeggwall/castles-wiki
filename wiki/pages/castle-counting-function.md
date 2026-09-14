---
title: Castle counting function F(w,h)
category: Concepts
summary: F(w,h), the number of valid castles on a w×h grid; PE 502 restricts it to even block counts and asks for a sum of three large evaluations mod 1e9+7.
tags: [concept, castle, counting-function, project-euler]
sources: [project-euler-502, project-euler-502-problem-setup, project-euler-502-representations, project-euler-502-solution, project-euler-502-brute-force]
created: 2026-09-13
updated: 2026-09-13
---

# Castle counting function F(w,h)

## Description

`F(w,h)` is the function that returns the number of valid [[castle-polyomino](pages/castle-polyomino.md)] configurations for a game grid *w* units wide and *h* units tall.[^1] It is the quantity Project Euler 502 asks the solver to compute.

**The even-block restriction is a special case.** As stated in Project Euler 502, `F(w,h)` counts only castles made from an **even** number of blocks.[^2] In this wiki's framing, that parity constraint is a restriction on top of the general castle object — the general and more interesting problem is counting *all* castles regardless of parity, of which the even-only count is a special case (see [[castle-polyomino](pages/castle-polyomino.md)]). The parity restriction is precisely what makes PE 502 hard and interesting rather than a trivial specialization.

**Notation: `A` for all castles, `F` for even.** The Solution subpage names the general (any-parity) count `A(w,h)` — the number of castles with bottom block of length *w* and height *exactly* *h* — and defines `F(w,h)` as `A(w,h)` restricted to an even total block count.[^5] This wiki adopts that convention: `A` is the parity-agnostic object of primary interest, and `F` its even-block special case. The odd-block count is simply `A − F`; it is deliberately left **unnamed** for now, since `G` is conventionally reserved for generating functions and a hasty symbol would be a poor early choice. (The reference Python module calls these `F_any = A = h^w − (h−1)^w`, `F`, and `F_odd = A − F`; `F_odd` is a code variable name, not a wiki symbol commitment.)[^6]

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

**A closed form exists.** `F(w,h)` is not only computable but has a closed form derived from a generalized Dyck grammar: `F(w,h) = [h^w − (h−1)^w − P(h−1,w) + P(h−2,w)] / 2`, where `P` is a signed tower count encoding the even-block rule. The derivation is the [[castle-counting-formula](pages/castle-counting-formula.md)]; it reproduces all three integer checkpoints exactly (verified during ingest). The large-parameter evaluations are carried out by the [[castle-count-algorithms](pages/castle-count-algorithms.md)] (a rational-function path and a Berlekamp–Massey path, routed by *h*).

**The composite answer.** The Solution subpage records the final value of the target sum only in obfuscated form (a base64 checksum). Following Project Euler etiquette, this wiki does not reproduce the decoded answer; the checksum is preserved on [[project-euler-502-solution](pages/project-euler-502-solution.md)].

## Appearances in Sources

- [[project-euler-502](pages/project-euler-502.md)] — introduces `F(w,h)`, gives the four checkpoint values, and states the target sum modulo 1 000 000 007.
- [[project-euler-502-problem-setup](pages/project-euler-502-problem-setup.md)] — invokes the scale of `F` (`F(13,10) = 3,729,050,610,636`, target height 10^12) to motivate a generating-function approach over direct enumeration.
- [[project-euler-502-representations](pages/project-euler-502-representations.md)] — derives the closed form for `F(w,h)` from the generalized Dyck grammar and verifies it against the checkpoints.
- [[project-euler-502-solution](pages/project-euler-502-solution.md)] — fixes the `A`/`F` notation, proves `T(k,L)=(k+1)^L`, and specifies the algorithms that evaluate the large targets.
- [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)] — names `F`, `F_odd`, `F_any = A` in code and confirms `A = F + F_odd` by direct enumeration.

## Related Concepts

- [[castle-polyomino](pages/castle-polyomino.md)] — the object `F(w,h)` counts; PE 502's even-block count is a special case of the general (parity-agnostic) count.
- [[castle-counting-formula](pages/castle-counting-formula.md)] — the closed-form derivation of `F(w,h)`.
- [[castle-count-algorithms](pages/castle-count-algorithms.md)] — how the large-parameter values are actually computed.
- [[generating-functions](pages/generating-functions.md)] — the intended method for computing `F(w,h)` at large parameters.

## Footnotes

[^1]: [[project-euler-502](pages/project-euler-502.md)] §"Project 502: Castle Polyominoes" L26 — "Let F(w,h) represent the number of valid castles, given grid parameters w and h."
[^2]: [[project-euler-502](pages/project-euler-502.md)] §"Project 502: Castle Polyominoes" L20 — "The castle is made from an even number of blocks."
[^3]: [[project-euler-502](pages/project-euler-502.md)] §"Project 502: Castle Polyominoes" L28 — "F(4,2) = 10, F(13,10) = 3729050610636, F(10,13) = 37959702514, and F(100,100) mod 1,000,000,007 = 841913936".
[^4]: [[project-euler-502](pages/project-euler-502.md)] §"Project 502: Castle Polyominoes" L30 — "Find (F(10^12,100) + F(10000,10000) + F(100,10^12)) mod 1,000,000,007."
[^5]: [[project-euler-502-solution](pages/project-euler-502-solution.md)] §"Notation" L5-6 — "A(w, h) - number of castles with bottom block of length w and height exactly h. F(w, h) - A(w, h) restricted to even total block count. This is what the problem asks for."
[^6]: [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)] §"What it computes" L10-11 — "F_odd(w, h) - odd-block-count castles, exact. Complement of F. F_any(w, h) - height exactly h, any parity: h^w - (h-1)^w"; the `brute["even"]+brute["odd"] == F_any` cross-check re-run exact during ingest for w,h ≤ 5."
