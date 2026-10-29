---
title: "Korolyuk (1955) - On the discrepancy of empirical distributions for two independent samples"
category: Sources
summary: Korolyuk, in Russian, finds the exact laws of the one-sided and two-sided two-sample statistics D⁺(n, m) and D(n, m) when one sample size is a multiple of the other, m = pn, and recovers the exact one-sample laws in the limit p → ∞. He restates the limit theorems of Kolmogorov and Smirnov, credits Smirnov with the exact one-sided one-sample law, and states that the case n = m was solved in his joint paper with B. V. Gnedenko (Doklady 1951). Every arrangement of the merged samples is equally likely; the lead moves +1 for a value of one sample and −p for a value of the other, and the orders whose lead reaches c are counted by splitting each at its first passage through c, with N_k(c) = (c/k) C(k, (k − c)/(p + 1)) first passages at step k (Theorem 1). The two-sided law (Theorem 3) is an alternating sum over the alternate passages through c and −c. At p = 1 the first-passage sum is C(2n, n − c), the count of the Kolmogorov castles whose X peaks reach height c + 1.
tags: [source, paper, kolmogorov-smirnov, two-sample-test, lattice-paths, ballot-theorem, first-passage, reflection-principle, kolmogorov-castle]
sources: [korolyuk-1955-two-independent-samples]
created: 2026-10-28
updated: 2026-10-28
---

# Korolyuk (1955) - On the discrepancy of empirical distributions for two independent samples

**Source:** `raw/korolyuk-1955-two-independent-samples.pdf` (git-ignored) and its text layer `raw/korolyuk-1955-two-independent-samples.txt` (tracked, extracted with `pdftotext -layout` from the OCR layer of the scan). В. С. Королюк (V. S. Korolyuk), "О расхождении эмпирических распределений для случая двух независимых выборок" ("On the discrepancy of empirical distributions for the case of two independent samples"), *Известия Академии наук СССР, серия математическая* (*Izvestiya Akad. Nauk SSSR, Ser. Mat.*) 19 (1955), pp. 81-96, presented by A. N. Kolmogorov, in Russian; full text from Math-Net.Ru, https://www.mathnet.ru/rus/im3524.[^1] The text layer garbles the formulas and the printed year of the running head, so formulas on this page were read from the page images and are cited by synthesis. English renderings of the Russian are the wiki's.
**Date ingested:** 2026-10-28
**Type:** paper (16 pp.)

## Notation used on this page

| paper | meaning | written here as |
|---|---|---|
| `S_n(x)`, `T_m(x)` | the empirical distribution functions of the samples `x_1, …, x_n` and `y_1, …, y_m` | the same |
| `D⁺(n, m)`, `D(n, m)` | `sup (S_n − T_m)` and `sup \|S_n − T_m\|` | the same |
| `C_N^n` | binomial coefficient | `C(N, n)` |
| `K(z)` | Kolmogorov's limit law | `K⋆(z)` (`K` is taken on the wiki, [[castle-notation](pages/castle-notation.md)]) |
| `ξ_k`, `S_k` | the steps `+1` or `−p` of the merged order and their partial sums | the steps and the lead |

## Summary

**The results being sharpened.** The introduction recalls that the work of Kolmogorov and Smirnov began the "nonparametric problems of statistics", with two problems: testing that one sample comes from a given continuous `F`, and testing that two samples come from the same continuous law. It restates Glivenko's theorem, Kolmogorov's theorem `P(√n D_n < z) → K⋆(z) = Σ_{k=−∞}^{∞} (−1)^k e^{−2k²z²}` for `z > 0`, Smirnov's exact formula for `P(√n D⁺_n < z)` with its limit `1 − e^{−2z²}`, and Smirnov's two-sample theorem: if `F` is continuous and `m/n = τ` is fixed, then

```
lim P( √(nm/(n + m)) D(n, m) < z )  =  K⋆(z),        lim P( √n D⁺(n, m) < z )  =  1 − e^{−2z²}   (z > 0).
```

Since these are limit statements, their practical use is "not always sufficiently justified", which raises the problem of the exact laws.[^2]

**What was known.** "The function `Φ_n(z)` was found already by N. V. Smirnov (1). In the particular case `n = m` the problem of finding the functions `Φ⁺_{nm}(z)` and `Φ_{nm}(z)` was solved in the joint work of the author with B. V. Gnedenko [see (2)]." Reference (2) is B. V. Gnedenko and V. S. Korolyuk, "О максимальном расхождении двух эмпирических распределений" ("On the maximal discrepancy of two empirical distributions"), *Doklady Akad. Nauk SSSR* 80, no. 4 (1951), pp. 525-528. The present paper finds `Φ⁺_{nm}` and `Φ_{nm}` for `m = np` with `p` an integer, and the limit `p → ∞` recovers Smirnov's `Φ⁺_n` and gives `Φ_n`.[^3]

**One-sided deviations (§1).** With the observations of both samples in increasing order `z_1 < ⋯ < z_N`, `N = n + m`, every one of the `N!` arrangements has probability `1/N!`, so every merged order is equally likely. Put `ξ_k = +1` when `z_k` is a value of the second sample and `ξ_k = −p` when it is a value of the first, and `S_k = ξ_1 + ⋯ + ξ_k`; then `m D⁺(n, m)` is the largest `S_k` (with the roles of the samples exchanged, which does not change the law). A particle that moves one unit right or `p` units left at each step stays left of the line `x = c` exactly when `m D⁺(n, m) < c`. Splitting each path that reaches `c` at its first passage, the number of such paths is

```
M  =  Σ_k N_k(c) · C(N − k, n − (k − c)/(p + 1)),        k ≡ c  (mod p + 1),                    (4)
```

where `N_k(c)` counts the paths that first reach `c` at step `k`, after `(k − c)/(p + 1)` steps to the left. They obey `N_k(c) = C(k, (k − c)/(p + 1)) − Σ_r N_r(c) C(k − r, (k − r)/(p + 1))` (5), whose solution is `N_k(c) = (c/k) C(k, (k − c)/(p + 1))`, and Theorem 1 follows:

```
P( √(nm/(n + m)) D⁺(n, m) < z )  =  1 − (c/C(N, n)) Σ_{k ≡ c (mod p+1)} (1/k) C(k, (k − c)/(p + 1)) C(N − k, n − (k − c)/(p + 1)),   (3)
```

with `c = [pz√(Nn/m)]`. Theorem 2 extends the one-sided law to arbitrary `n` and `m` through a determinant.[^4]

**Two-sided deviations (§2).** For `m = np`, `m D(n, m)` is the largest `|S_k|`, and Theorem 3 writes `P(m D(n, m) < c)` as `1 − (1/C(N, n))` times an alternating sum over `v = 1, …, [m/c]` of the paths that pass alternately through `c` and `−c` at least `v` times, each split at its alternate passages into pieces counted as in §1 (formula (16)). A reflection of coordinates, `x' = −x + β`, `t' = −t + T`, proves the identity (15) between path counts that the computation needs.[^5]

**One sample (§3).** Letting `p → ∞`, with `m/c → √n/z`, term by term in the formulas of §1 and §2 gives the exact laws of `√n D⁺_n`, which is Smirnov's formula, and of `√n D_n` for finite `n` (Theorem 4).[^6]

## The castle reading

For two samples of `n` values each, `p = 1`: the lead moves by `±1`, `m D⁺(n, n) = n D⁺_{n,n}` is the largest lead of one sample, and the merged orders are the Kolmogorov castles of width `2n + 1` ([[kolmogorov-castles](pages/kolmogorov-castles.md)]). The first passages through `c` at step `k` number `(c/k) C(k, (k − c)/2)`, the ballot numbers, and formula (4) adds up to `C(2n, n − c)` orders whose lead reaches `c`: the Kolmogorov castles in which a peak marked by that sample reaches height `c + 1`. So the Kolmogorov castles of width `2n + 1` whose peaks marked by one sample all have height at most `c` number `C(2n, n) − C(2n, n − c)`, the one-sided count of Gnedenko and Korolyuk for `n = m`.[^7]

## Key Takeaways

- **Gnedenko and Korolyuk (1951)** solved the case `n = m`, one-sided and two-sided, as this paper states.[^3]
- **Theorem 1.** For `m = pn`, the orders whose lead reaches `c` are counted by first passage, with `(c/k) C(k, (k − c)/(p + 1))` first passages at step `k`.[^4]
- **Smirnov's two-sample theorem**, restated with both its two-sided limit `K⋆` and its one-sided limit `1 − e^{−2z²}`.[^2]

## Entities & Concepts

- [[kolmogorov-castles](pages/kolmogorov-castles.md)] - the castles of the two-sample test with `n = m`; formula (4) at `p = 1` counts those whose `X` peaks reach a given height.

## Relation to Other Wiki Pages

[[smirnov-1944-approximation-distribution-laws](pages/smirnov-1944-approximation-distribution-laws.md)] is the survey cited here for Smirnov's exact one-sided law and its two-sample theorem. [[lutsenko-marinich-matsak-2009-gnedenko-korolyuk-method](pages/lutsenko-marinich-matsak-2009-gnedenko-korolyuk-method.md)] proves the `n = m` case of Gnedenko and Korolyuk in full by reflection, with the two-sided count `C(2n, n) − 2 Σ_{i≥1} (−1)^{i−1} C(2n, n − ic)`. [[kolmogorov-1933-determinazione-empirica](pages/kolmogorov-1933-determinazione-empirica.md)] is the source of Kolmogorov's theorem.

## Footnotes

[^1]: [[korolyuk-1955-two-independent-samples](pages/korolyuk-1955-two-independent-samples.md)] p.81 L1-L20 [synthesis] - "ИЗВЕСТИЯ АКАДЕМИИ НАУК СССР Серия математическая", the author "В. С. КОРОЛЮК", the title "О РАСХОЖДЕНИИ ЭМПИРИЧЕСКИХ РАСПРЕДЕЛЕНИЙ ДЛЯ СЛУЧАЯ ДВУХ НЕЗАВИСИМЫХ ВЫБОРОК", "(Представлено академиком А. Н. Колмогоровым)" and the abstract; "Поступило 23.XI.1953" at p.96 L875-L876.
[^2]: [[korolyuk-1955-two-independent-samples](pages/korolyuk-1955-two-independent-samples.md)] pp.81-82 L21-L101 [synthesis] - "Работами А. Н. Колмогорова и Н. В. Смирнова было положено начало новой главе математической статистики, получившей название «непараметрические задачи статистики»", the two problems, the statistics `D_n`, `D⁺_n`, `D⁺(n, m)`, `D(n, m)`, the theorems of Glivenko, Kolmogorov and Smirnov (Theorems 1 and 2), "их использование в практических вопросах не всегда достаточно обосновано, так как все они носят характер предельных соотношений"; formulas read from the page image of p.82.
[^3]: [[korolyuk-1955-two-independent-samples](pages/korolyuk-1955-two-independent-samples.md)] p.83 L102-L112 and the references p.96 L877-L889 - "Функция Φ⁺_n(z) была найдена еще Н. В. Смирновым (1). В частном случае n = m задача разыскания функций Φ⁺_nm(z) и Φ_nm(z) была решена в совместной работе автора с Б. В. Гнеденко [см. (2)]."; "Г н е д е н к о Б. В. и К о р о л ю к В. С, О максимальном расхождении двух эмпирических распределений, Доклады Ак. наук СССР, т. LXXX, № 4 (1951), 525—528."
[^4]: [[korolyuk-1955-two-independent-samples](pages/korolyuk-1955-two-independent-samples.md)] §1 pp.83-85 L113-L267 [synthesis] - Theorem 1 and formula (3); "Заметим прежде всего, что любые взаимные расположения наблюдений обеих серий равновероятны", the steps `ξ_k = +1` or `−p`, "mD⁺(n, m) = sup S_k", the particle "может сдвигаться или на единицу вправо, или на p единиц влево", formula (4) and the recursion (5), the solution (7) `N_k(c) = (c/k) C_k^{(k−c)/(p+1)}`, and Theorem 2 with the determinants `A_r`; formulas read from the page images of pp.83-85. Formula (4) with `N_k(c) = (c/k) C(k, (k − c)/(p + 1))` checked by execution, footnote 7.
[^5]: [[korolyuk-1955-two-independent-samples](pages/korolyuk-1955-two-independent-samples.md)] §2 pp.86-89 L268-L482 [synthesis] - "§ 2. Двусторонние уклонения", the quantities (8)-(10), Theorem 3, the identity (15) "сумма слева определяет число путей из точки (0, 0) в точку (β, T), пересекающих прямую x = −α", the change of coordinates, and formula (16).
[^6]: [[korolyuk-1955-two-independent-samples](pages/korolyuk-1955-two-independent-samples.md)] §3 pp.89-96 L483-L875 [synthesis] - "§ 3. Уклонения между эмпирической и теоретической кривыми распределения", the limit `p → ∞`, "Эта формула была установлена Н. В. Смирновым", and Theorem 4 for `Φ_n(z)`, `0 < z ≤ √n`.
[^7]: Verified by execution (Python 3.11, 2026-10-28): `bin/python/kolmogorov_castles.py` items [6] and [13], run log `bin/python/kolmogorov_castles-run.log`. Formula (4) with `N_k(c) = (c/k) C(k, (k − c)/(p + 1))` against the number of merged orders whose lead reaches `c`, by enumeration, for `p = 1` (`n ≤ 8`) and `p = 2, 3` (`n ≤ 6`); at `p = 1` it equals `C(2n, n − c)`; the count `C(2n, n) − C(2n, n − c)` against enumeration of the Kolmogorov castles for `n ≤ 9`.
