---
title: The A005251 bijection - compositions ↔ no-010 strings
category: Analyses
summary: The open "A005251 bijection" is closed by an explicit, constraint-preserving map. A composition (c_1,…,c_w) of n with no two adjacent parts ≥ 2 (= tree castles of area n by unlimited height) corresponds to the length-(n−1) binary string 0^{c_1−1} 1 0^{c_2−1} 1 ⋯ 1 0^{c_w−1} avoiding the factor 010 (the OEIS interpretation of A005251). The classic "cut the n−1 gaps" encoding does it: a part ≥ 2 is a nonempty zero-block, two adjacent parts ≥ 2 put a zero on each side of a boundary 1 — exactly the factor 010 — so "no two adjacent parts ≥ 2" translates term for term to "no factor 010." Verified as an exact bijection onto the avoid-010 set for n ≤ 11. Offsets against canonical OEIS A005251 (a(0)=0): compositions of n = A005251(n+2), avoid-010 length N = A005251(N+3). This ties tree-castle-by-area to the avoid-010 reading, and a third node — minimum-tower-spacing (h=2, g=2) castles by width — joins the same web; Hardin's distinct no-isolated-1 family (A005251(N+2) at length N) is one trivial bit-shift away.
tags: [analysis, castle, bijection, a005251, plastic-number, composition, binary-string, hardin, tree-castle, tower-spacing, verification]
sources: [oeis-mining-pe502]
created: 2026-09-18
updated: 2026-09-19
---

# The A005251 bijection

## The two objects that met at the same recurrence

**A005251** — `0, 1, 1, 1, 2, 4, 7, 12, 21, 37, 65, 114, …` (canonical Online Encyclopedia of Integer Sequences (OEIS) offset 0, `a(0)=0`), satisfying `a(n) = 2a(n−1) − a(n−2) + a(n−3)`, the plastic-squared recurrence ([[plastic-number](pages/plastic-number.md)]) — appears in the castle world through two independently-derived objects:

- **Tree castles of area `n`, unlimited height** ([[tree-castle-by-area](pages/tree-castle-by-area.md)], `h → ∞`). A tree castle (no `2×2` filled block) is a skyline with no two adjacent columns both `≥ 2`, so by area it is a **composition `(c_1, …, c_w)` of `n` with no two adjacent parts `≥ 2`**. Count: `A005251(n+2)`.
- **Binary strings avoiding the factor `010`** — the OEIS interpretation of A005251 ("`a(n+3)` is the number of `n`-bit sequences that avoid `010`"). Count of length `N`: `A005251(N+3)`. (Hardin's `W_1` object, [[hardin-word-identity](pages/hardin-word-identity.md)], is the *closely related but distinct* "no isolated `1`" family — `#{no-isolated-1, length N} = A005251(N+2)`, so avoid-`010` of length `N` and no-isolated-1 of length `N+1` share a count; the bijection below targets the avoid-`010` family, the cleaner match to compositions.)

Both hit the same recurrence with the same three-1 initial run, but the objects looked unrelated — one a constrained composition, the other a constrained binary string. The open question on `IDEAS.md` asked for an explicit bijection, or a Sunada-style common cover ([[isospectral-castles](pages/isospectral-castles.md)]) generating both. **It needs no cover: there is a direct, elementary, constraint-preserving bijection.**

## The bijection

Align the offsets first. Compositions of `n` (no-adj-`≥2`) number `A005251(n+2)`; avoid-`010` strings of length `n−1` also number `A005251(n+2)` (`= A005251((n−1)+3)`). So the equinumerous pair is

```
{ compositions of n with no two adjacent parts ≥ 2 }   ⟷   { binary strings of length n−1 avoiding 010 }.
```

The map is the **classic composition ↔ gap-string encoding**. Lay `n` unit cells in a row; there are `n−1` gaps between consecutive cells. A composition of `n` is a choice of which gaps are *part boundaries*: write a `1` at each boundary gap and a `0` at each interior (non-boundary) gap. Concretely, part `c_j` becomes a block of `c_j − 1` zeros, and blocks are joined by single `1`s:[^1]

```
(c_1, …, c_w)   ↦   0^{c_1−1} · 1 · 0^{c_2−1} · 1 · ⋯ · 1 · 0^{c_w−1}        (length n − 1).
```

The inverse splits the string at its `1`s and reads each maximal `0`-run of length `r` as a part `r + 1`. This is a bijection between *all* compositions of `n` and *all* length-`(n−1)` binary strings; the content is that it carries the two constraints onto each other.

## Why the constraints match — term for term

Read the constraint through the encoding:

- A part `c_j ≥ 2` ⟺ its block `0^{c_j−1}` is **nonempty** (contains at least one `0`).
- **Two adjacent parts** `c_j, c_{j+1}` both `≥ 2` ⟺ nonempty blocks on **both sides** of the boundary `1` between them ⟺ a `0` immediately before and a `0` immediately after that `1` ⟺ the factor **`0 1 0`** straddles the boundary.

Conversely, every `010` in the string must straddle a boundary, because the only `1`s in the string *are* boundaries (blocks are all-zero). So

```
"no two adjacent parts ≥ 2"     ⟺     "no factor 010".
```

The tree-castle constraint (no `2×2` filled block = no two adjacent columns `≥ 2`) *is* the avoid-`010` constraint, read across the composition ↔ gap-string dictionary. The bijection is verified exact — onto the full avoid-`010` set, no misses, no extras — for `n ≤ 11` (parts-side sizes `1, 2, 4, 7, 12, 21, 37, 65, 114, 200, 351`).[^2] (Avoid-`010` is *not* the same as Hardin's "no isolated `1`": those are different string families, equinumerous at lengths differing by one, so linking this bijection to Hardin's `W_1` object needs one further trivial bit-shift.)

Worked example (`n = 5`): the 12 no-adj-`≥2` compositions map to the 12 length-4 avoid-`010` strings.

| composition | string | | composition | string |
|---|---|---|---|---|
| `(1,1,1,1,1)` | `1111` | | `(1,4)` | `1000` |
| `(1,1,1,2)` | `1110` | | `(2,1,1,1)` | `0111` |
| `(1,1,2,1)` | `1101` | | `(2,1,2)` | `0110` |
| `(1,1,3)` | `1100` | | `(3,1,1)` | `0011` |
| `(1,2,1,1)` | `1011` | | `(4,1)` | `0001` |
| `(1,3,1)` | `1001` | | `(5)` | `0000` |

(Every string on the right avoids `010`; every composition on the left has no two adjacent parts `≥ 2`. Note `(2,1,2)` → `0110` and its would-be neighbor with adjacent 2s, e.g. `(2,2,1)`, is *excluded* — it would encode to `0101`, which contains `010`.)

## The four-node A005251 web

With this bijection, the plastic-squared sequence now has **four** castle-adjacent readings that are all explicitly linked, not just numerically coincident:

| object | count | A005251 offset | link |
|---|---|---|---|
| tree castles of area `n`, unlimited height (= compositions of `n`, no-adj-`≥2`) | `1, 2, 4, 7, 12, …` | `A005251(n+2)` | **this bijection** ↓ |
| avoid-`010` binary strings, length `N` | `1, 2, 4, 7, 12, …` | `A005251(N+3)` | ← bijection (with `N = n−1`) |
| minimum-tower-spacing `(h=2, g=2)` castles, width `w` | `2, 4, 7, 12, 21, …` | `A005251(w+3)` | row 2 is a width-`w` string avoiding `101` (a width-1 valley `1 0 1` between towers); avoid-`101` is the bit-flip of avoid-`010`, so same count ([[tower-spacing-castles](pages/tower-spacing-castles.md)]) |
| Hardin no-isolated-1 words / signed even-column towers `P_even(6,L)/2^L` | `1, 2, 4, 7, …` | `A005251(L+3)` (`= #{(L+1)`-bit no-isolated-1`}`) | the Hardin identity ([[hardin-word-identity](pages/hardin-word-identity.md)]); a bit-shift from the avoid-`010` family |

The middle two are the same object up to a bit-flip (a height-2 tower-spacing castle records, in its row 2, an avoid-`101` string, the `0↔1` complement of an avoid-`010` string), and this page's bijection connects them to the tree-castle-by-area composition side. The fourth (Hardin no-isolated-1 words / signed even-column towers) is the same sequence one bit-length over — no-isolated-1 of length `N+1` and avoid-`010` of length `N` share a count — reached through the sign-cancellation of the Hardin identity. So the "two apparently independent castle threads" the open item named are one thread, and the plastic-squared sequence is the fixed point where the tree-castle, avoid-`010`, tower-spacing, and Hardin families all coincide.[^3]

## What this closes and leaves

**Closed:** the explicit bijection between the two A005251 castle objects — no Sunada cover needed; it is the classic composition ↔ gap-string map, and the constraint correspondence "adjacent parts `≥ 2` ⟺ factor `010`" is a one-line proof.

**Still open** (from the Hardin thread, unaffected): the *sign-reversing involution* realizing the Hardin identity `P_even(4m+2, L) = 2^L · W_m` object by object ([[hardin-word-identity](pages/hardin-word-identity.md)]) — that is a different statement (it explains the `2^L` and the sign cancellation, not the plain-count bijection this page gives).

## Reproduce

`encode(c) = '1'.join('0'*(p-1) for p in c)` and its inverse `decode(s) = tuple(len(r)+1 for r in s.split('1'))` are the whole bijection; the constraint check (`no_adj2` ⟷ `'010' not in`) and the onto-verification are pinned on [[castle-snippets](pages/castle-snippets.md)].

## Appearances in Sources

- [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] - where A005251's multiple castle appearances were first catalogued.

## Related Concepts

- [[tree-castle-by-area](pages/tree-castle-by-area.md)] - the composition side (`h → ∞` tree castles by area), and where this bijection was posed as open.
- [[hardin-word-identity](pages/hardin-word-identity.md)] - the no-isolated-1 / avoid-010 side (`W_1`), and the still-open sign-reversing involution.
- [[tower-spacing-castles](pages/tower-spacing-castles.md)] - the third node: `(h=2, g=2)` tower-spacing castles are the same no-isolated-1 object in row 2.
- [[plastic-number](pages/plastic-number.md)] - `ψ²`, the growth constant all four nodes share; the sequence's three (now four) castle readings are tabulated there.
- [[castle-by-area](pages/castle-by-area.md)] - the composition-of-area framing this bijection uses.
- [[binary-string-bijection](pages/binary-string-bijection.md)] - the wiki's other castle ↔ binary-string encoding (the `T(k,L) = (k+1)^L` bijection), a cousin of the gap-string map here.
- [[unique-tournament](pages/unique-tournament.md)] - the `h = 4` row of the same tree-castle family, where Khovanova's basic strings `0, 001, 0011, 00101` encode compositions with parts in `{1, 3, 4, 5}` by the same composition-as-binary-string trick.
- [[block-count-constraints](pages/block-count-constraints.md)] - the sign-reversing involution realizing `P_even(4m+2, L) = 2^L · W_m` is a residue-class-mod-m block-count filter, the same residue branch this page axiomatizes.

## Footnotes

[^1]: The composition ↔ gap-string encoding is standard: compositions of `n` are in bijection with subsets of the `n−1` gaps (`2^{n−1}` of each). Here a `1` marks a chosen gap (part boundary) and a `0` an unchosen one; part `c_j` becomes `0^{c_j−1}` and consecutive parts are separated by a single `1`. Verified round-trip (`decode(encode(c)) = c`) for all no-adj-`≥2` compositions of `n = 5`.

[^2]: Verified by execution (2026-09-18): for `n = 5, 7, 9, 11`, the image `{ encode(c) : c a composition of n, no two adjacent parts ≥ 2 }` equals exactly `{ length-(n−1) binary strings with no factor 010 }` — same cardinality (`12, 37, 114, 351`), no element missing or extra. The constraint proof: a part `≥ 2` is a nonempty `0`-block; two adjacent parts `≥ 2` place a `0` on each side of their boundary `1`, i.e. a `010`; and every `010` straddles a boundary since all `1`s are boundaries.

[^3]: The four offsets, against the **canonical** OEIS A005251 (offset 0, `a(0)=0, a(1)=a(2)=a(3)=1`, data `0, 1, 1, 1, 2, 4, 7, 12, 21, …`): tree/compositions of `n` = `A005251(n+2)`; avoid-010 length `N` = `A005251(N+3)` (so `N = n−1` gives `A005251(n+2)`, matching the bijection); tower-spacing `(2,2)` width `w` = `A005251(w+3)`; `P_even(6,L)/2^L` = `A005251(L+3)` ([[hardin-word-identity](pages/hardin-word-identity.md)]). All re-verified 2026-09-18 against the OEIS matrix one-liner `A005251(n)` on [[castle-snippets](pages/castle-snippets.md)].
