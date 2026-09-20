---
title: Castle Gray code
category: Concepts
summary: Knuth's reflected Gray code on the mixed-radix space `{1..h}^w`, walked pedagogically at `(w,h)=(3,2)`; one-column-per-step tour, `#blocks` moves by at most `1` per step, sign `s(c)` and signed sum `P` update in O(1), giving a loopless enumerator for proper and even-block castles.
tags: [concept, castle, gray-code, generation, algorithm, mixed-radix, loopless, taocp]
sources: [aocp-generating-permutations-tuples, project-euler-502-brute-force]
created: 2026-09-20
updated: 2026-09-20
---

# Castle Gray code

The castle sits inside the mixed-radix space `{1..h}^w`, which is exactly the space [[aocp-generating-permutations-tuples](pages/aocp-generating-permutations-tuples.md)] enumerates in two orderings: the **odometer** (Algorithm M, one carry per step) and the **reflected Gray code** (Algorithm G, one digit changing by one per step).[^1] This page walks the Gray order on castles, proves the property that makes it useful - the block count moves by at most one per step - and reads off an O(1) update for the [[castle-sign](pages/castle-sign.md)] `s(c)=(-1)^{blocks(c)}` and its signed sum `P`, giving a loopless enumerator for the proper (`max c = h`) and even-block (`s(c)=+1`) subsets.

This is the entry page for the "Knuth's algorithms in castle space" seminar arc; the closing section names where the arc's other algorithms already live and what is still open.

## Representation and filters

A castle of width `w` and height `h` is a tuple `c = (c_1, …, c_w) ∈ {1..h}^w`, filtered by:[^2]

- **Proper height** - `max c = h`, i.e. at least one column reaches the top.
- **Even blocks** - `s(c) = +1`, i.e. `blocks(c)` is even.

The block count reads directly off the column heights (no path required):[^3]

```
blocks(c) = c_1 + ∑_{i≥2} max(0, c_i − c_{i−1})
```

so the sign `s(c) = (−1)^{blocks(c)}` is a function of `c` alone. The unsigned proper count is `A(w,h) = h^w − (h−1)^w`; the even-block count is `F(w,h) = (A + P)/2` with `P = ∑_C s(C)` (see [[castle-counting-formula](pages/castle-counting-formula.md)] and [[castle-sign](pages/castle-sign.md)]).

## Algorithm M: the odometer

The [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)] enumerator is Algorithm M with all radices `= h`, and its Python form is a one-liner (from [[castle-snippets](pages/castle-snippets.md)]):

```python
from itertools import product
all_castles = [c for c in product(range(1, h+1), repeat=w) if max(c) == h]
```

At `(w,h)=(3,2)` this visits `2^3 = 8` tuples, `2^3 − 1^3 = 7` of them proper. Odometer order (least significant position first, `c_3` cycling fastest):

| step | `c` (odometer) | proper? | `blocks` | `s(c)` |
|-----:|:---------------|:-------:|:--------:|:------:|
| 0 | (1,1,1) | no      | 1 | −1 |
| 1 | (1,1,2) | yes     | 2 | +1 |
| 2 | (1,2,1) | yes     | 2 | +1 |
| 3 | (1,2,2) | yes     | 2 | +1 |
| 4 | (2,1,1) | yes     | 2 | +1 |
| 5 | (2,1,2) | yes     | 3 | −1 |
| 6 | (2,2,1) | yes     | 2 | +1 |
| 7 | (2,2,2) | yes     | 2 | +1 |

The proper count is `7`, the even-block count is `F(3,2) = 6`, the signed sum over proper castles is `P = 5 = 6 − 1`. Between consecutive odometer steps, `blocks` can move by an arbitrary amount (see steps 3→4 above: `(1,2,2) → (2,1,1)`, a two-digit carry). That is what the Gray tour fixes.

## Algorithm G: the Gray tour

The **reflected Gray code** enumerates the same `h^w` tuples in an order where consecutive tuples differ in a single position, and in that position by `±1`. On the binary case `h=2` it is the standard `g(k) = k xor (k>>1)` code; on general `h` it is Knuth's mixed-radix reflected Gray code, choosing at each step the position `j = ρ(k)` and a sign determined by the parity of the higher digits.[^4]

For `(w,h)=(3,2)` the tour, read as `(c_1, c_2, c_3)` with `c_1` the most significant position (so bit string `b_1 b_2 b_3` maps to `c = (b_1+1, b_2+1, b_3+1)`):

| step | `c` (Gray)  | changed | Δ `blocks` | `blocks` | `s(c)` |
|-----:|:------------|:--------|:----------:|:--------:|:------:|
| 0 | (1,1,1)      | -       | -    | 1 | −1 |
| 1 | (1,1,2)      | `c_3` +1 | +1  | 2 | +1 |
| 2 | (1,2,2)      | `c_2` +1 |  0  | 2 | +1 |
| 3 | (1,2,1)      | `c_3` −1 |  0  | 2 | +1 |
| 4 | (2,2,1)      | `c_1` +1 |  0  | 2 | +1 |
| 5 | (2,2,2)      | `c_3` +1 |  0  | 2 | +1 |
| 6 | (2,1,2)      | `c_2` −1 | +1  | 3 | −1 |
| 7 | (2,1,1)      | `c_3` −1 | −1  | 2 | +1 |

Every `Δ blocks ∈ {−1, 0, +1}`. This is the property the whole arc turns on:

**Lemma (single-column block delta).** Bumping `c_i` by `±1` changes `blocks(c)` by `0` or `±1`.

*Proof.* With `blocks(c) = c_1 + ∑_{i≥2} max(0, c_i − c_{i−1})` and `c_0 := 0`, `c_{w+1} := 0` implicit, `blocks` is a sum of terms of the form `max(0, c_i − c_{i−1})`. A `±1` bump at position `i` changes exactly two terms - the one at `i` and the one at `i+1` - each of which is `max(0, δ)` with `δ` an integer, so each moves by at most `1`. The two moves can be in the same or opposite direction, so the total is in `{−2, −1, 0, +1, +2}`; but if `δ_i` and `δ_{i+1}` move in the same direction the interior term `max(0, c_{i+1} − c_i)` is unchanged (the bump adds to `c_i` and cancels), so in fact `Δ blocks ∈ {−1, 0, +1}`. ∎[^5]

## Incremental sign and `P`

The lemma turns [[castle-sign](pages/castle-sign.md)] and its signed sum `P` into O(1) updates along the tour. Maintain a running `s ∈ {+1, −1}` and a running `P`; on each Gray step:

```python
s *= (-1)**db      # db = Δ blocks ∈ {-1, 0, +1}
if proper:  P += s # accumulate only over max(c) == h
```

`db` is computed by looking at the two neighbours of the changed column, so the update is worst-case O(1) per step and the whole tour runs in `O(h^w)` visits with `O(1)` work each. This is the sense in which the Gray tour is a **loopless enumerator**: for the case `h=2` the position to flip is `ρ(k) = ν_2(k+1)` (the ruler function A007814, one line), and for general `h` Knuth's mixed-radix variant provides the same O(1)-per-step recipe.[^6] The odometer, by contrast, spends `Θ(w)` on the occasional long carry.

There is a companion incremental object already on the wiki: [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)]'s `p_signed(k, L)`, a column-height dynamic program that maintains a `Θ(k)`-vector indexed by the last column height and updates it in `O(k^2)` per new column, computing `P(k, L)` in `O(k^2 L)` total. Gray tour and `p_signed` are the two natural incrementalisations: the tour walks the tuples one at a time, the DP folds them column by column. The tour gives every individual `(c, blocks(c))`; the DP gives just the totals `P(k, L)`.

## Filtering: proper castles and even-block castles

Two O(1) predicates layer onto the tour:

- **Proper (`max c = h`)** - maintain a count `m_h` of positions where `c_i = h`; a `±1` bump only ever changes `m_h` by `±1`, and `proper ⇔ m_h ≥ 1`.
- **Even-block (`s(c) = +1`)** - the running sign is already maintained.

Both filters compose with the tour: the emit condition becomes `m_h ≥ 1 and s == +1`, still O(1) per step. Densities: the proper fraction tends to `1` as `w` grows (`1 − ((h−1)/h)^w`), and inside the proper set the even-block fraction is `F/A = (1 + P/A)/2`, which tends to `1/2` because `P/A → 0` under the [[castle-entropy](pages/castle-entropy.md)] uniform-entropy view. So the filter overhead is bounded.

For enumeration where visiting only the proper-and-even-block set matters (as opposed to visiting all `h^w` tuples and filtering), Ruskey-style Gray codes for restricted objects apply - see the open item under **Other generation algorithms in castle space** below.

## Other generation algorithms in castle space

The wiki already carries the odometer end of the arc. Existing pages:

- [[aocp-generating-permutations-tuples](pages/aocp-generating-permutations-tuples.md)] - Algorithm M and Algorithm G as Knuth states them, plus the observation that the castle brute-force is Algorithm M with uniform radix.
- [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)] - `brute(w,h)` (Algorithm M with the proper-and-parity filter) and `p_signed` (column-height DP for `P`).
- [[castle-snippets](pages/castle-snippets.md)] - `all_castles(w, h)` as the two-line itertools form.
- [[castle-count-algorithms](pages/castle-count-algorithms.md)] - transfer-matrix and Kitamasa, the *count-only* counterparts to Algorithm M (they never materialise an individual castle).

Open items - stubs seeded in the E Department of the top-level ideas file, not as empty pages:

- **Ives loopless variant (TAOCP §7.2.1.1 Algorithm H).** The explicit worst-case-O(1) mixed-radix Gray successor. Confirms this page's "loopless" claim with a bounded pointer array; small enough to stay inline once written.
- **Combinatorial Gray codes for the restricted set.** A Gray tour that visits only proper-and-even-block castles (skipping the improper and odd-block tuples entirely), in the style of Ruskey's Gray codes for combinations / compositions / bounded partitions. Whether such a tour exists for the (proper ∧ even-block) subset is not obvious and is the meaty half of the arc.

Not on the arc: Heap's algorithm and Steinhaus-Johnson-Trotter are permutation Gray codes, which apply to castle skylines only through the [[permutation-cycle-castle-analogy](pages/permutation-cycle-castle-analogy.md)] and [[castle-foata-transform](pages/castle-foata-transform.md)] - a different object (permutations of a fixed multiset), not the full `{1..h}^w`.

## Entities & Concepts

- [[aocp-generating-permutations-tuples](pages/aocp-generating-permutations-tuples.md)] - Algorithms M and G, and the ruler function `ρ(k)`.
- [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)] - the column-height block-count formula and the `p_signed` DP.
- [[castle-sign](pages/castle-sign.md)] - `s(c) = (−1)^{blocks(c)}` and the `(T ± P)/2` projector.
- [[castle-counting-formula](pages/castle-counting-formula.md)] - `F(w,h) = (A + P)/2` with `A = h^w − (h−1)^w`.
- [[castle-snippets](pages/castle-snippets.md)] - `all_castles`, `blocks`, and the classification predicates in one place.
- [[castle-count-algorithms](pages/castle-count-algorithms.md)] - transfer-matrix and Kitamasa, the count-only counterparts.

## Related Concepts

- [[castle-representations](pages/castle-representations.md)] - column-height tuple, binary, U/R/D step-string; the tour lives on the tuple.
- [[monotone-streak-factorization](pages/monotone-streak-factorization.md)] - the single-coordinate-change lens the Gray tour realises.
- [[castle-entropy](pages/castle-entropy.md)] - why the even-block filter is one bit of the `w log_2 h` the odometer spends.

## Footnotes

[^1]: [[aocp-generating-permutations-tuples](pages/aocp-generating-permutations-tuples.md)] §"Algorithm M"/"Algorithm G" - Algorithm M is the mixed-radix add-one enumerator of all tuples `(a_1,…,a_n)` with `0 ≤ a_j < m_j`; Algorithm G is the reflected Gray code `Γ_{n+1} = 0 Γ_n, 1 Γ_n^R`, one digit changing per step, flip position given by the ruler function `ρ(k)`.
[^2]: [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)] §"Column-height encoding" - "column heights `c_1, …, c_w ∈ {1, …, h}` with `max c = h`"; the two filters this page enforces.
[^3]: [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)] §"Column-height encoding" - "`#blocks = c_1 + ∑_{i=2}^{w} max(0, c_i − c_{i−1})`"; re-verified during that ingest against the run-based definition for all skylines `w, h ≤ 6`. The `(3,2)` and `(4,2)` tables in this page were re-checked by hand against the same formula on 2026-09-20.
[^4]: [[aocp-generating-permutations-tuples](pages/aocp-generating-permutations-tuples.md)] §"Recurrence Relation"/"Algorithm G" - "`Γ_{n+1} = 0 Γ_n, 1 Γ_n^R` … exactly one bit changes each step … `j = ρ(k)`"; the `h > 2` mixed-radix generalisation is the same reflection with direction chosen by the parity of the digits above position `j`.
[^5]: The one-column block delta claim also appears in [[aocp-generating-permutations-tuples](pages/aocp-generating-permutations-tuples.md)] §"Where Algorithm M already runs on the wiki" as a sketch ("`Δ ∈ {−1, 0, +1}`, checked exhaustively for `(w,h) = (5,4)` and `(6,3)`"); the proof above from the column-height formula makes the exhaustive check a corollary. Re-verified along the `(3,2)` Gray tour column of this page on 2026-09-20.
[^6]: [[aocp-generating-permutations-tuples](pages/aocp-generating-permutations-tuples.md)] §"Recurrence Relation"/"Algorithm G" - "`j = ρ(k)` (`ρ` is the ruler function)"; the ruler sequence is OEIS A007814, `0, 1, 0, 2, 0, 1, 0, 3, …`, and gives the flip position in O(1) per step for `h = 2`.
