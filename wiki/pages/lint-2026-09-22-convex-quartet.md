---
title: Lint Report 2026-09-22 - convex quartet
category: Maintenance
summary: Scoped lint over the multisets / klarner / bender / delest branch pages plus Bousquet-Mélou-Fédou 1995 - 0 errors, 4 warnings (stale "unread" claims), 11 info (cross-links added across all four source pages, two new own-reasoning connections)
tags: [lint, maintenance]
sources: []
created: 2026-09-22
updated: 2026-09-22
---

# Lint Report - 2026-09-22 - convex quartet

Scope: [[bender-1974-partitions-of-multisets](pages/bender-1974-partitions-of-multisets.md)], [[multiset-partitions](pages/multiset-partitions.md)], [[klarner-rivest-1974-convex-n-ominoes](pages/klarner-rivest-1974-convex-n-ominoes.md)], [[bender-1974-convex-n-ominoes](pages/bender-1974-convex-n-ominoes.md)], [[algebraic-languages-and-polyominoes-enumeration](pages/algebraic-languages-and-polyominoes-enumeration.md)], [[parallelogram-polyomino-dyck-bijection](pages/parallelogram-polyomino-dyck-bijection.md)], [[castle-perimeter](pages/castle-perimeter.md)], [[bousquet-melou-fedou-1995-convex-polyominoes](pages/bousquet-melou-fedou-1995-convex-polyominoes.md)], [[q-differential-system](pages/q-differential-system.md)], [[convex-polyomino](pages/convex-polyomino.md)], [[convex-polyomino-by-area](pages/convex-polyomino-by-area.md)]. Each branch was ingested without the others, and before this pass none of the four source pages linked another.

## Summary
- 🔴 Errors: 0
- 🟡 Warnings: 4
- 🔵 Info: 11

Phase 1 (mechanical) is clean for the scope. Wiki-wide it flagged only two false positives in [[lint-2026-09-22](pages/lint-2026-09-22.md)] (the empty `sources: []` of a report, and a literal link token in prose). The second was reworded.

## 🟡 Stale Claims (fixed)
- [[bender-1974-convex-n-ominoes](pages/bender-1974-convex-n-ominoes.md)] called Bousquet-Mélou-Fédou "unread". It now links the paper, whose series gives A067675's `2.91960`.
- [[bousquet-melou-fedou-1995-convex-polyominoes](pages/bousquet-melou-fedou-1995-convex-polyominoes.md)] said Bender and Klarner-Rivest "were not read", so the origin of `C ≃ 2.67564` was unknown. It is Bender's abstract value (his eq. (11) prints `2.67483`), and Klarner-Rivest give no prefactor.
- [[convex-polyomino](pages/convex-polyomino.md)] footnote 2 said Delest-Viennot "was not read for this page". It now cites the paper's p.169 formula directly.
- [[convex-polyomino-by-area](pages/convex-polyomino-by-area.md)] had a "Sources not yet read" section with every entry now ingested. Removed.

## 🔵 Missing Cross-References (added)
- Bender convex ↔ Klarner-Rivest ↔ Bousquet-Mélou-Fédou ↔ Delest-Viennot: all six pairs, in both directions where each page discusses the other.
- [[bender-1974-partitions-of-multisets](pages/bender-1974-partitions-of-multisets.md)] → [[bender-1974-convex-n-ominoes](pages/bender-1974-convex-n-ominoes.md)] (the "not to be confused with" line), and back.
- [[convex-polyomino](pages/convex-polyomino.md)] and [[convex-polyomino-by-area](pages/convex-polyomino-by-area.md)] → Delest-Viennot; [[convex-polyomino-by-area](pages/convex-polyomino-by-area.md)] → Bender convex.
- [[castle-perimeter](pages/castle-perimeter.md)] → [[convex-polyomino](pages/convex-polyomino.md)], Bousquet-Mélou-Fédou (Lin-Chang width × height is the convex counterpart of the castle's width × blocks).
- [[q-differential-system](pages/q-differential-system.md)] → Klarner-Rivest (their `B(x, xy)` recursion is a one-unknown q-shift equation).

## 🔵 Connections found with all four papers in view
- **One wrong prefactor, three papers.** Bender's abstract `f = 2.67564` is quoted by Delest-Viennot 1984 (p.170, `Γ = 2.67564...`) and Bousquet-Mélou-Fédou 1995 (p.59). Both attribute it jointly to Klarner-Rivest and Bender. Following OEIS, the wiki uses A067675's `2.91960`, which is also what the BMF series and the column sweep give.
- **Bender used what Klarner-Rivest couldn't.** Klarner-Rivest had the parallelogram series (19) but were "unable to make use of" it. Bender's adaptation, `P_1/(1 - P_2)` with `P_2` alternating, yields eleven digits of `gamma`.
- **β explains Klarner-Rivest's kernel** (own reasoning). Between peaks of heights `m` and `n`, β allows `min{m, n}` trough heights, which is exactly KR's transfer kernel. Summing over compositions reproduces A006958 through area 20. Written up on [[parallelogram-polyomino-dyck-bijection](pages/parallelogram-polyomino-dyck-bijection.md)] and [[klarner-rivest-1974-convex-n-ominoes](pages/klarner-rivest-1974-convex-n-ominoes.md)].
- **Delest-Viennot's q-analog question is Bousquet-Mélou-Fédou's theorem.** The §12(8) open problem (add area) is answered for convex polyominoes, using the same Schützenberger-style algebraic-language encoding.
- **One trisection, three cuts.** KR and Bender cut along rows, and Delest-Viennot cut along vertical lines, so their stacks stand sideways. In every version the stacks (convex castles) carry no exponential growth.
- **The multiset paper meets the ladder** (own reasoning). A single element repeated `n` times makes Bender's `v*` and `c*` into partitions and distinct-part partitions, so the Ferrers rung is the one-element case (checked `n <= 12`). This is the only real link from the multisets branch. Everything else there is the "blocks" homonym already on the page.

## 🔵 Not changed
- Delest-Viennot's types I/II/III are not mirror pairs (Table 1: 643892 vs 136949 at perimeter 24), so they were not identified with Bender's NE/NW slants.
- Klarner-Rivest, Bender convex, and Delest-Viennot have no `raw/` text or PDF tracked. Locators are page-only, as for other scanned PDFs.
