---
title: "Smirnov (1944) - Approximation of distribution laws of random variables from empirical data"
category: Sources
summary: Smirnov's survey, in Russian, of the empirical distribution function S_n(x) of n observations of a continuous law F. It gives the laws of the order statistics, the exact law of the one-sided deviation D⁺_n = sup (S_n − F) and its limit P(√n D⁺_n < λ) → 1 − e^{−2λ²} (Theorem 3), Glivenko's theorem and bounds on the largest deviations in long runs of samples, the number of times S_n crosses F or a band around it (Theorems 6 to 8), with Kolmogorov's law Σ (−1)^k e^{−2k²λ²} for sup |S_n − F| as a corollary credited to Kolmogorov, and, in a closing review, the two-sample theorem (Theorem 9). For two samples of sizes n_1 and n_2 growing with a fixed ratio, the probability that D(n_1, n_2) = sup |S_{n_1} − S_{n_2}| is at most λ/√n, with n = n_1 n_2/(n_1 + n_2), tends to the same law, for every continuous F. On the castle side, Theorem 9 with n_1 = n_2 is the limit law of the heights of the Kolmogorov castles.
tags: [source, paper, kolmogorov-smirnov, two-sample-test, empirical-distribution, order-statistics, limit-law, kolmogorov-castle]
sources: [smirnov-1944-approximation-distribution-laws]
created: 2026-10-28
updated: 2026-10-28
---

# Smirnov (1944) - Approximation of distribution laws of random variables from empirical data

**Source:** `raw/smirnov-1944-approximation-distribution-laws.pdf` (git-ignored) and its text layer `raw/smirnov-1944-approximation-distribution-laws.txt` (tracked, extracted with `pdftotext -layout` from the OCR layer of the scan). Н. В. Смирнов (N. V. Smirnov), "Приближение законов распределения случайных величин по эмпирическим данным" ("Approximation of distribution laws of random variables from empirical data"), *Успехи математических наук* (*Uspekhi Matematicheskikh Nauk*) 10 (1944), pp. 179-206, in Russian; full text from Math-Net.Ru, https://www.mathnet.ru/rus/rm8798.[^1] The text layer garbles most formulas, so formulas on this page were read from the page images and are cited by synthesis. English renderings of the Russian are the wiki's.
**Date ingested:** 2026-10-28
**Type:** paper (survey, 28 pp.)

## Notation used on this page

| paper | meaning | written here as |
|---|---|---|
| `S_n(x)` | the empirical distribution function of `n` observations | the same (`S` is the signed castle count only on castle pages) |
| `D⁺_n`, `D_n` | `sup (S_n(x) − F(x))` and `sup \|S_n(x) − F(x)\|` | the same |
| `D(n_1, n_2)` | `sup \|S_{n_1}(x) − S_{n_2}(x)\|` for two samples | the same; `D_{n,n}` at `n_1 = n_2 = n` |
| `Φ(λ)` | `Σ_{k=−∞}^{+∞} (−1)^k e^{−2k²λ²}` | `K⋆(λ)` (`K` is taken on the wiki, [[castle-notation](pages/castle-notation.md)]) |

## Summary

**Scope.** The introduction sets the problem of judging a continuous distribution law from `n` observations without grouping them into intervals, and names the work of von Mises, Kolmogorov, Glivenko and the author as the source of the results the survey presents. Throughout, `F` is continuous and increasing, and the observations are put in increasing order `x_1 < x_2 < ⋯ < x_n`, the variational series; `S_n(x)` is 0 below `x_1`, `k/n` on `[x_k, x_{k+1})` and 1 from `x_n` on.[^2]

**Order statistics (§2).** The law of the `k`-th term is `Σ_{m≥k} C(n, m) F(x)^m (1 − F(x))^{n−m}`, with the minimum and the maximum as special cases, and Theorems 1 and 2 give normal limits for terms with rank near `nλ`, the empirical quantiles.[^3]

**One-sided deviations (§3).** The law `P⁺(λ) = P(D⁺_n < λ/√n)` does not depend on `F` (Lemma 1), since `η = F(ξ)` is uniform on `[0, 1]`; Lemma 2 gives it exactly as a finite sum for `0 < λ < √n`, and Theorem 3 gives, for `λ > λ_0 > 0` and `λ³/√n → 0`, `P⁺(λ) = 1 − e^{−2λ²(1 + o(1))}`.[^4] From the bound behind Theorem 3 Smirnov derives Glivenko's theorem, that `S_n` converges to `F` uniformly with probability 1, and Theorems 4 and 5 describe the largest deviations met in a long sequence of independent samples, in analogy with Cramér's theorem on sums.[^5]

**Crossings and Kolmogorov's law (§4).** With `v_n` the number of points where `S_n` crosses `F` upward, `P(v_n ≤ t√n) → 1 − e^{−t²/2}` for `t ≥ 0` (Theorem 6). Theorems 7 and 8 count the exits from the band of width `λ/√n` above `F`, and from the band between `F − λ/√n` and `F + λ/√n`. At `t = 0` they give `P(√n D⁺_n < λ) → 1 − e^{−2λ²}` and

```
P(sup |S_n(x) − F(x)| < λ/√n)  →  Σ_{m=−∞}^{+∞} (−1)^m e^{−2m²λ²},                       (132)
```

independent of `F`, "this important result was first obtained by A. N. Kolmogorov".[^6]

**Two samples (§5).** The closing review states the author's theorem on two independent samples of sizes `n_1` and `n_2` from the same continuous law, with `D(n_1, n_2) = sup |S_{n_1}(x) − S_{n_2}(x)|` as the measure of discrepancy.

> **Theorem 9.** If `n_1` and `n_2` grow without bound with `n_2/n_1 = τ` fixed, then for every continuous `F`, `P(D(n_1, n_2) ≤ λ/√n) → Φ(λ)`, where `λ > 0`, `n = n_1 n_2/(n_1 + n_2) = n_2/(1 + τ)`, and `Φ(λ) = Σ_{k=−∞}^{+∞} (−1)^k e^{−2k²λ²}`.

The limit is the same as for `sup |S_n(x) − F(x)|`, formula (132). The proof is in the author's 1939 paper in the Bulletin of Moscow University, which the survey cites. The review then turns to von Mises's `ω²` criterion and the approximation of densities by histograms.[^7]

## The castle reading

For two samples of `n` values each, `n_1 = n_2 = n`, `τ = 1`, and Theorem 9 is a statement about `√(n/2) D_{n,n}`. Merging the two samples and giving column `i` the height `1 + |a_i − b_i|`, with `a_i` and `b_i` the numbers of values of each sample among the first `i − 1`, gives a Kolmogorov castle of width `w = 2n + 1` and height `1 + n D_{n,n}` ([[kolmogorov-castles](pages/kolmogorov-castles.md)]). Since `√(n/2) D_{n,n} = (height − 1)/√(w − 1)`, Theorem 9 says that the share of the Kolmogorov castles of width `w` with height at most `1 + λ√(w − 1)` tends to `K⋆(λ)`.

## Key Takeaways

- **Theorem 9.** `P(D(n_1, n_2) ≤ λ/√n) → Σ_k (−1)^k e^{−2k²λ²}`, `n = n_1 n_2/(n_1 + n_2)`, for samples of fixed ratio from one continuous law.[^7]
- **Kolmogorov's law** (132) is the same limit for one sample against `F`, credited to Kolmogorov.[^6]
- **One-sided limit.** `P(√n D⁺_n < λ) → 1 − e^{−2λ²}` (Theorem 3, and Theorem 7 at `t = 0`).[^4][^6]

## Entities & Concepts

- [[kolmogorov-castles](pages/kolmogorov-castles.md)] - the castles of the two-sample test; Theorem 9 is the limit law of their heights.

## Relation to Other Wiki Pages

[[kolmogorov-1933-determinazione-empirica](pages/kolmogorov-1933-determinazione-empirica.md)] is the paper that first proved (132). [[korolyuk-1955-two-independent-samples](pages/korolyuk-1955-two-independent-samples.md)] restates Theorem 9 together with its one-sided form, cites this survey for Smirnov's exact one-sided law, and finds the exact two-sample laws for samples of sizes `n` and `pn`.

## Footnotes

[^1]: [[smirnov-1944-approximation-distribution-laws](pages/smirnov-1944-approximation-distribution-laws.md)] p.179 L1-L3 [synthesis] - the title "ПРИБЛИЖЕНИЕ ЗАКОНОВ РАСПРЕДЕЛЕНИЯ СЛУЧАЙНЫХ ВЕЛИЧИН ПО ЭМПИРИЧЕСКИМ ДАННЫМ" and the author "Н. В. Смирнов"; the page numbers 179 to 206 at L40-L1416.
[^2]: [[smirnov-1944-approximation-distribution-laws](pages/smirnov-1944-approximation-distribution-laws.md)] Introduction and §1 pp.179-180 L4-L93 [synthesis] - the problem of continuous laws and grouping ("Эта редукция непрерывного распределения к дискретному вносит известный произвол"), "в работах Мизеса, Колмогорова, Гливенко, автора этой статьи и других математиков", the variational series (2) and the empirical function (3).
[^3]: [[smirnov-1944-approximation-distribution-laws](pages/smirnov-1944-approximation-distribution-laws.md)] §2 pp.181-185 L94-L344 [synthesis] - the law (6)-(7) of the `k`-th term, (8') and (8'') for the minimum and the maximum, and Theorems 1 and 2.
[^4]: [[smirnov-1944-approximation-distribution-laws](pages/smirnov-1944-approximation-distribution-laws.md)] §3 pp.186-193 L345-L702 [synthesis] - "§ 3. Закон распределения максимума односторонних уклонений", `D⁺_n` (43) and `P⁺(λ)` (44), Lemma 1 through `η = F(ξ)` (45)-(48), Lemma 2 (50), Theorem 3 with the conditions (59') `λ > λ_0 > 0` and (59'') `λ³/√n = ε_n = o(1)` and `P⁺(λ) = 1 − e^{−2λ²(1+o(1))}` (60); formulas read from the page images.
[^5]: [[smirnov-1944-approximation-distribution-laws](pages/smirnov-1944-approximation-distribution-laws.md)] §3 pp.193-195 L725-L823 [synthesis] - "Теорема Гливенко. С вероятностью, равной единице, можно утверждать, что последовательность эмпирических функций распределения … сходится к теоретическому закону распределения F(x) … равномерно относительно x", and Theorems 4 and 5, "вполне аналогичной теореме Крамера о суммах независимых величин".
[^6]: [[smirnov-1944-approximation-distribution-laws](pages/smirnov-1944-approximation-distribution-laws.md)] §4 pp.195-197 L824-L905 [synthesis] - Theorems 6, 7 and 8, the corollaries (128)-(129) and (132), "Этот важный результат был впервые получен А. Н. Колмогоровым [2]."
[^7]: [[smirnov-1944-approximation-distribution-laws](pages/smirnov-1944-approximation-distribution-laws.md)] §5.1 p.203 L1222-L1256 [synthesis] - "Оценка расхождения между эмпирическими кривыми распределения в двух независимых выборках", the measure `D(n_1, n_2)`, "Эта проблема решается [13] в предположении, что F(x) непрерывная всюду возрастающая функция x и выборки n_1 и n_2 достаточно велики", Theorem 9 (read from the page image), and "Предельный закон Φ(λ) здесь тот же самый, как и для верхней грани уклонений |S_n(x) − F(x)| (см. формулу (132) — следствие теоремы 8)"; reference [13] at L1415-L1416, "Оценка расхождения между эмпирическими кривыми распределения в двух независимых выборках, Бюллетень НИИМ МГУ, т. II, вып. 2 (1939)".
