---
title: "AOCP Generating Permutations & Tuples (Knuth TAOCP Vol. 4)"
category: Sources
summary: Knuth's combinatorial-generation algorithms — mixed-radix add-one tuple generation (Algorithm M) and reflected Gray code (Algorithm G); the castle's brute enumerator is Algorithm M with uniform radix h.
tags: [knuth, taocp, generation, mixed-radix, gray-code, brute-force, source]
sources: [aocp-generating-permutations-tuples]
created: 2026-09-13
updated: 2026-09-13
---

# AOCP Generating Permutations & Tuples (Knuth TAOCP Vol. 4)

**Source:** https://charlesreid1.com/wiki/AOCP/Generating_Permutations_and_Tuples (notes on Knuth, *The Art of Computer Programming*, Vol. 4A, combinatorial generation)
**Date ingested:** 2026-09-13
**Type:** article (MediaWiki notes page); algorithmic-methods reference

## Summary

Algorithms for **generating** (exhaustively listing) all tuples, in two orderings.

**Mixed-radix add-one (Algorithm M).** To run through every tuple `(a_1,…,a_n)` with `0 ≤ a_j < m_j`, treat the tuple as a number in the mixed-radix system `[m_1,…,m_n]` and repeatedly **add one with carry** until overflow.[^1] It starts from binary/decimal counting (`2^n`, `10^n` strings) and generalizes to arbitrary per-position bounds; for small *n* it is just nested `for` loops over `a_j ∈ 0..m_j−1`.[^2] Each step "visits" a tuple and hands it to the consumer.

**Reflected Gray code (Algorithm G).** An alternative order in which **exactly one bit changes per step** (e.g. `n=4`: `0000, 0001, 0011, 0010, …`).[^3] It is defined by the reflected recurrence `Γ_{n+1} = 0Γ_n, 1Γ_n^R` (prefix `0` to the list, then `1` to its reversal), so consecutive strings differ in one bit; the bit to flip is chosen by the **ruler function** ρ(k).[^4] The page notes its appearances — Baudot telegraph code (`Γ_5`) and the Chinese-ring puzzle.[^5]

## Relevance to the castle

The connection is concrete and lives in the brute-force enumerator:

- **The castle brute-force is Algorithm M with uniform radix.** A castle of width *w*, height *h* is a column-height tuple `c ∈ {1..h}^w` — exactly a mixed-radix space with all `m_j = h`. The reference enumerator ([[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)]) does `product(range(1,h+1), repeat=w)`, which *is* the "add one in radix `[h,h,…,h]` and visit" of Algorithm M (verified: the space has size `h^w`). So the brute enumerator that grounds the whole verified solution is a direct instance of this algorithm.
- **The `2^n` binary-string count** is the [[binary-string-bijection](pages/binary-string-bijection.md)]: generating all length-*w* binary strings by counting `0…0` to `1…1` is precisely enumerating the configurations of one length-*w* block.
- **Gray-code ordering** is a lens on the castle's local structure: successive one-coordinate changes are the smallest moves in the mixed-radix space, and the castle's block-count / `is_unimodal` deltas under such a single-column change connect to the [[monotone-streak-factorization](pages/monotone-streak-factorization.md)] view.

**A seminar / research thread — Knuth's generation algorithms in castle space.** Systematically translating Vol. 4's combinatorial-generation algorithms into the castle's mixed-radix `{1..h}^w` space is a self-contained, accessible research direction (and a good seminar): Algorithm M is already the castle brute-force; a **castle Gray code** would order castles so each step changes one column height by one — inducing a bounded, predictable change in block count and in the [[castle-sign](pages/castle-sign.md)] — which could give a loopless enumerator, an incremental parity/`P` update, and a combinatorial handle on the even/odd split. Restricting the generation to *valid* castles (max height exactly *h*, and the even-block filter) is the interesting twist Knuth's generic algorithms do not handle out of the box. Tracked in the wiki TODO.

## Key Takeaways

- **Algorithm M** — mixed-radix add-one generation of all tuples `0 ≤ a_j < m_j`; nested `for` loops for small *n*.[^1][^2]
- **Algorithm G** — reflected Gray code `Γ_{n+1} = 0Γ_n, 1Γ_n^R`, one bit changing per step, flip position given by the ruler function.[^3][^4]
- The castle **brute-force enumerator is Algorithm M with all radices `= h`** (`{1..h}^w`, size `h^w`) — verified.
- Enumerating length-*w* binary strings (the `2^n` case) is exactly the block-configuration count of the [[binary-string-bijection](pages/binary-string-bijection.md)].

## Entities & Concepts

- [[project-euler-502-brute-force](pages/project-euler-502-brute-force.md)] — the castle enumerator, an instance of Algorithm M.
- [[binary-string-bijection](pages/binary-string-bijection.md)] — the `2^n` binary-string enumeration.
- [[castle-by-area](pages/castle-by-area.md)] — the by-area enumeration, another exhaustive tuple listing.
- [[monotone-streak-factorization](pages/monotone-streak-factorization.md)] — the single-coordinate-change lens Gray code suggests.

Linked from the source but not yet ingested: (none new for this wiki).

## Relation to Other Wiki Pages

An algorithmic-methods reference: it names the exhaustive-generation procedure behind the castle's brute-force cross-check (Algorithm M = mixed-radix enumeration of `{1..h}^w`) and connects the `2^n` binary case to the block bijection. Gray-code order is recorded as a possible lens on single-column moves, not a used technique.

## Footnotes

[^1]: [[aocp-generating-permutations-tuples](pages/aocp-generating-permutations-tuples.md)] §"Arbitrary string permutations"/"Algorithm M" L19-71 — "run through all cases in which 0 ≤ a_j < m_j ... adding unity to the number [a_1, ..., a_n] in the mixed-radix number system [m_1, ..., m_n] ... visits all n-tuples by repeatedly adding 1 to the mixed-radix number until overflow occurs."
[^2]: [[aocp-generating-permutations-tuples](pages/aocp-generating-permutations-tuples.md)] §"Binary/Decimal string permutations"/"Algorithm M" L9-15, L73-81 — "generate all 2^n binary strings ... start at 0, and keep adding 1 ... 10^n such strings ... if the number of slots (n) is small, we can write it out using nested for loops: for a_1 in range 0 to (m_1 - 1): ..."
[^3]: [[aocp-generating-permutations-tuples](pages/aocp-generating-permutations-tuples.md)] §"Gray Binary Code Generation Algorithm" L85 — "it produces permutations such that each permutation changes only one bit. For example, for n=4, we have 0000, 0001, 0011, 0010, 0111, 0101, 0100, etc."
[^4]: [[aocp-generating-permutations-tuples](pages/aocp-generating-permutations-tuples.md)] §"Recurrence Relation"/"Algorithm G" L96-169 — "Γ_{n+1} = 0 Γ_n, 1 Γ_n^R ... The last string of Γ_n equals the first string of Γ_n^R so exactly one bit changes each step ... j = rho(k) (rho is the ruler function)"; one-bit-change property re-verified for n=4 during ingest.
[^5]: [[aocp-generating-permutations-tuples](pages/aocp-generating-permutations-tuples.md)] §"Baudot Code"/"Chinese ring puzzle" L129-139 — "The baudot telegraph machine uses Γ_5 gray code ... Chinese ring puzzle ... The state of the puzzle can be represented with binary notation."
