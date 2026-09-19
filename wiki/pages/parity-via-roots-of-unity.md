---
title: Generalizing the parity sign (roots of unity)
category: Concepts
summary: The (T±P)/2 even/odd trick, generalized — replace the sign (−1)^blocks with an m-th root of unity ω^blocks and count castles by block count modulo m via character sums; the same character, applied to the index instead of a statistic, is the EGF parity projector (e^x ± e^{−x})/2.
tags: [concept, castle, parity, roots-of-unity, character, pedagogy]
sources: [project-euler-502-castle-factoring, project-euler-502-representations]
created: 2026-09-14
updated: 2026-09-19
---

# Generalizing the parity sign (roots of unity)

## The question

The [[castle-sign](pages/castle-sign.md)] trick counts *even*-block castles by weighting each block with the sign `(−1)^blocks` and projecting `(T ± P)/2`. That sign is the **character of order 2**. This page asks: what if "even" were "divisible by 7", or "≡ 3 mod 4", or "not divisible by 4"? The answer is the same trick with a different character — an *m*-th root of unity in place of `−1`.

## Review: the order-2 character

Weight a tower by `(−1)^blocks`; the signed total is `P = Σ (−1)^blocks`. Because `(1 + (−1)^{b})/2 = 1` for even `b` and `0` for odd `b`, the projector `(1 ± (−1)^blocks)/2` isolates each parity class:[^1]

```
(T + P)/2 = even-block towers      (T − P)/2 = odd-block towers
```

The two ingredients are a **character** `χ_0 = 1` (the trivial one, giving the unsigned total `T`) and `χ_1 = (−1)^blocks` (giving `P`), combined by **character orthogonality** `½ Σ_{j} χ_j(b) χ_j(r)⁻¹ = [b ≡ r mod 2]`.

## The generalization: m-th roots of unity

To constrain `blocks ≡ r (mod m)`, take `ω = e^{2πi/m}` and weight each block by `ω`, so a tower with `b` blocks carries `ω^b`. The character-weighted counts are

```
P_j(k,L) = Σ_{towers} ω^{j·blocks},       j = 0, 1, …, m−1
```

(`P_0` is the unsigned `T`; for `m = 2`, `P_1` is the signed `P`.) Character orthogonality over the cyclic group of order *m* — `(1/m) Σ_j ω^{j(b−r)} = 1` when `b ≡ r (mod m)` and `0` otherwise — then gives the master formula:

```
# { towers with blocks ≡ r (mod m) } = (1/m) Σ_{j=0}^{m−1} ω^{−jr} P_j.
```

For `m = 2` this is exactly `(T ± P)/2`. So the parity idea *is* a root-of-unity formula — the `m = 2` case of a general construction.

## The exponential generating function (EGF) twin — the same character on the index

The projector has a second, older face, usually met in **exponential** generating functions. For any EGF `A(x) = Σ a_n x^n/n!`, the substitution `x → −x` applies the *same* order-2 character `(−1)^n` to the **index** rather than to a statistic:

```
(A(x) + A(−x))/2 = Σ_{n even} a_n x^n/n!,      (A(x) − A(−x))/2 = Σ_{n odd} a_n x^n/n!.
```

This is literally the castle's `(T ± P)/2`, with the character carried by the index variable instead of by `blocks`. The canonical instance is `A(x) = e^x` (the all-ones sequence): `(e^x + e^{−x})/2 = Σ_{n even} x^n/n!`, which the [[generating-functions-topic](pages/generating-functions-topic.md)] page uses to count even-0 ternary strings as `(3^n+1)/2` — the "classical form of the `(A±P)/2` trick."

So the EGF parity projector and the castle sign are **one character sum, `½(χ₀ + χ₁)` over the cyclic group of order 2**, differing only in *which variable carries the character*:

| face | variable carrying `(−1)` | projector |
|---|---|---|
| EGF (index parity) | the index `n`, via `x → −x` | `(A(x) ± A(−x))/2` |
| ordinary generating function (OGF) (castle sign) | the statistic `blocks`, via the weight `(−1)^blocks` | `(T ± P)/2` |

The castle wants *block* parity, not *width* parity, so the EGF's `x → −x` (which filters by index — in the castle's OGF, the width) is the wrong axis. The castle must route the character through the block statistic, and that routing *is* the sign `s(C) = (−1)^blocks`. That is the answer to "how do you get EGF parity out of an OGF": make the parity a **sign in the weight** — the sign homomorphism — the OGF counterpart of the EGF's substitution-in-the-index. The duality holds at every `m`: the generalization `ω^{blocks}` above extends the *statistic* side, while `(1/m) Σ_j A(ω^j x)` extends the *index* side (substituting the main variable rather than a statistic).

## Computing P_j

The beauty is that `P_j` is no harder than `P` was. Each block is one `D` step, so a peak `U V D` multiplies its interior tower's weight by one extra `ω^j`. The tower grammar therefore gives the same recurrence with the peak weight `ω^j` instead of `−1`:[^2]

```
P_{j,k} = (1 − ω^j + ω^j·P_{j,k−1}) / (1 − x(1 − ω^j) − ω^j·x·P_{j,k−1}),      P_{j,0} = 1/(1−x)
```

(`j = 0` is the unsigned `E_k = E_{k−1}/(1 − xE_{k−1})`; `m = 2, j = 1` is the signed `P_k = (2−P_{k−1})/(1−2x+xP_{k−1})`.)

**The k = 1 case.** A tower of height ≤ 1 is a binary string, and its block count is its number of maximal runs. There are `C(L+1, 2r)` strings with `r` runs, so

```
P_j(1,L) = Σ_r C(L+1, 2r) ω^{jr} = ½ [ (1 + √ω^j)^{L+1} + (1 − √ω^j)^{L+1} ].
```

For `m = 2, j = 1` this is `½[(1+i)^{L+1} + (1−i)^{L+1}] = Re((1+i)^{L+1})` — the familiar closed form, now seen as the order-2 member of a family.

## Applying it

- **Divisible by q** (`r = 0`): `# = (1/q) Σ_j P_j`.
- **Congruent to r mod q**: `# = (1/q) Σ_j ω^{−jr} P_j`.
- **Not divisible by q**: `total − (divisible by q)` — a difference of two character sums.

**Example — "not divisible by 4".** Take `m = 4`, `ω = i`. Then `P_1 = Σ i^{blocks}`, `P_2 = Σ (−1)^{blocks} = P` (the signed count), `P_3 = conj(P_1)`, and the "not divisible by 4" count is

```
T − ¼ (T + P_1 + P_2 + P_3) = (3T − P − 2·Re(P_1)) / 4.
```

So "not divisible by 4" costs exactly two new weighted counts, `Re(P_1)` and the familiar `P`, over the baseline `T` — the even/odd trick with one more character.

**Example — "divisible by 3" (k = 1, L = 4).** Height-≤1, length-4 towers are the 16 binary strings, with run counts `r = 0, 1, 2` of multiplicities `C(5,0), C(5,2), C(5,4) = 1, 10, 5`. Only `r = 0` is divisible by 3, so the answer is 1. The character formula agrees: `P_0 = 16`, `P_1 = 1 + 10ω + 5ω²`, `P_2 = 1 + 10ω² + 5ω`, and `(P_0+P_1+P_2)/3 = (18 + 15(ω+ω²))/3 = 1` (since `ω + ω² = −1`).

## The boundary: "power of 2"

One requested case does *not* fall out of this machinery: **"blocks is a power of 2"** is not a congruence condition. A root-of-unity character only sees the residue of `blocks mod m`, so it cannot tell `2` from `6` from `10` (all `≡ 2 mod 4`). "Power of 2" needs an indicator that depends on the *value*, not the residue — a genuinely different tool (e.g. a lacunary generating function `Σ_k z^{2^k}`, or a base-2 digit condition, which points toward the automatic-sequence world). So the honest boundary is: **characters count by residue; anything finer needs a different idea.**

## Appearances in Sources

- [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] — the sign `s(C) = (−1)^{blocks}` and the `(T±P)/2` projector.
- [[project-euler-502-representations](pages/project-euler-502-representations.md)] — the unsigned/signed generating functions whose peak weight `ω^j` generalizes.

## Related Concepts

- [[castle-sign](pages/castle-sign.md)] — the `m = 2` case this page generalizes.
- [[tower-recursion-master-class](pages/tower-recursion-master-class.md)] — the tower recursion whose "sign" step is replaced by `ω^j`.
- [[signed-tower-count](pages/signed-tower-count.md)] — the `P(k,L)` family (`P_1` in the `m=2` case).
- [[generating-functions-topic](pages/generating-functions-topic.md)] — the EGF parity projector `(e^x ± e^{−x})/2`, the same character applied to the index.
- [[mod-p-observatory](pages/mod-p-observatory.md)] — the mod-p periods, a different (additive) use of modular structure.
- [[block-count-constraints](pages/block-count-constraints.md)] — the full trichotomy (residue / sparse / semigroup), of which this page is the residue case.

## Footnotes

[^1]: [[project-euler-502-castle-factoring](pages/project-euler-502-castle-factoring.md)] §"The sign of a castle" L116-123 — "(T + P)/2 = even-block castles, (T - P)/2 = odd-block castles ... exactly the (1 ± sgn)/2 trick."
[^2]: [[project-euler-502-representations](pages/project-euler-502-representations.md)] §"Signed count" L316-329 — "The even-block rule is the hard constraint, and it enters as a sign. Weight each block, that is each D, by -1 ... one minus sign on the peak ... P_k = 1 + x P_k - (P_{k-1} - 1)(1 + x P_k)" — the peak weight `−1` that `ω^j` replaces.
