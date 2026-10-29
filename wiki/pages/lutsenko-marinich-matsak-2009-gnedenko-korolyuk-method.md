---
title: "Lutsenko, Marinich & Matsak (2009) - Some applications of the Gnedenko-Korolyuk method to empirical distributions"
category: Sources
summary: Lutsenko, Marinich and Matsak restate Kolmogorov's limit theorem for the one-sample statistic, with the limit law K(z) = 1 − 2 Σ (−1)^{k−1} exp(−2k²z²), and Smirnov's limit theorems for two samples, and prove the Gnedenko-Korolyuk theorem in full. For two samples of equal size n, every merged order is equally likely, its running difference is a lattice path of 2n steps of ±1 from 0 back to 0, and reflecting in the lines y = c and y = −c gives C(2n, n) − 2 Σ (−1)^{k−1} C(2n, n − kc) paths that meet neither line (Lemma 2.2), hence the exact law of the two-sample statistic D_{n,n} and, by Stirling's formula, Smirnov's limits 1 − e^{−2z²} and K(z). The paper's own proof of Kolmogorov's theorem goes through the Brownian bridge and this two-sample limit. On the castle side, the paths are the Kolmogorov castles of width 2n + 1, and Lemma 2.2 with c = h counts those of height at most h.
tags: [source, paper, kolmogorov-smirnov, two-sample-test, empirical-distribution, reflection-principle, lattice-paths, bridge, brownian-bridge, limit-law, kolmogorov-castle]
sources: [lutsenko-marinich-matsak-2009-gnedenko-korolyuk-method]
created: 2026-10-28
updated: 2026-10-28
---

# Lutsenko, Marinich & Matsak (2009) - Some applications of the Gnedenko-Korolyuk method to empirical distributions

**Source:** `raw/lutsenko-marinich-matsak-2009-gnedenko-korolyuk-method.pdf` (text layer at `raw/lutsenko-marinich-matsak-2009-gnedenko-korolyuk-method.txt`, extracted with `pdftotext -layout`; the PDF is git-ignored, the text is tracked). E. O. Lutsenko, O. V. Marinich and I. K. Matsak, "Some applications of the Gnedenko-Korolyuk method to empirical distributions", *Theory of Probability and Mathematical Statistics* 78 (2009), pp. 133-146, translated by O. I. Klesov from *Teor. Imovir. ta Matem. Statyst.* 78 (2008); free access at https://www.ams.org/journals/tpms/2009-78-00/S0094-9000-09-00767-4 (DOI 10.1090/S0094-9000-09-00767-4).[^1] The text layer garbles most displayed formulas, so formulas on this page are cited by synthesis and were checked by execution.
**Date ingested:** 2026-10-28
**Type:** paper (PDF, 14 pp.)

## Notation used on this page

The page keeps the paper's `n`, `m`, `c` and `z` and renames the symbols that clash with the wiki's ([[castle-notation](pages/castle-notation.md)]). Footnote quotes keep the paper's symbols.

| paper | meaning | written here as |
|---|---|---|
| `C_{2n}^{n−c}` | binomial coefficient | `C(2n, n − c)` |
| `S_k` | the running difference of the merged sample after `k` values | the lead `a_k − b_k` (`S` is the signed castle count) |
| `K(z)` | Kolmogorov's limit law | `K⋆(z)` (`K` is the sandpile group and the KMS matrix) |
| `D_n`, `D^+_{m,n}`, `D_{m,n}` | the one-sample statistic and the one-sided and two-sided two-sample statistics | the same |
| `Φ_n(z)`, `Φ^+_n(z)` | the exact laws of `√(n/2) D_{n,n}` and `√(n/2) D^+_{n,n}` | the same |
| `W⁰(t)` | the Brownian bridge | the same |

## Summary

**The statistics.** For a sample of size `n` from a continuous distribution function `F`, with empirical distribution function `F*_n`, Kolmogorov's statistic is `D_n = sup_t |F*_n(t) − F(t)|`, and Kolmogorov proved (Theorem 1.1)

```
lim_{n→∞} P(√n D_n < z)  =  K⋆(z)  =  1 − 2 Σ_{k≥1} (−1)^{k−1} exp(−2k²z²);
```

Kolmogorov's paper wrote `D` and `Φ(z)` for `D_n` and `K⋆(z)`.[^2] For two independent samples of sizes `n` and `m ≤ n`, with empirical distribution functions `F*_n` and `G*_m`, the one-sided and two-sided statistics are `D^+_{m,n} = sup_t (F*_n(t) − G*_m(t))` and `D_{m,n} = sup_t |F*_n(t) − G*_m(t)|`, and with `n̂ = mn/(m + n)` Smirnov showed that `√n̂ D^+_{m,n}` and `√n̂ D_{m,n}` tend in law to `1 − exp(−2z²)` and `K⋆(z)`.[^3]

**The Gnedenko-Korolyuk theorem.** The paper credits Gnedenko and Korolyuk (1951) with "an ingenious combinatorial proof" of Smirnov's limits for `m = n` and the exact law of `D_{n,n}` for finite `n`. Theorem 1.2: with `c` the integer with `c − 1 < z√(2n) ≤ c`,

```
Φ^+_n(z)  =  P(√(n/2) D^+_{n,n} < z)  =  1 − C(2n, n − c)/C(2n, n),
Φ_n(z)    =  P(√(n/2) D_{n,n} < z)    =  1 − (2/C(2n, n)) Σ_{k=1}^{⌊n/c⌋} (−1)^{k−1} C(2n, n − kc),
```

for `(2n)^{−1/2} < z ≤ √(n/2)`.[^4] Korolyuk found the laws for all `m` and `n`, in "much more complicated" expressions.[^4]

**Two lemmas on lattice paths.** Let `L` be the polygonal lines of `2n` segments of slope `±1` from `(0, 0)` to `(2n, 0)`; there are `C(2n, n)` of them. Lemma 2.1: for `c ≤ n`, `C(2n, n) − C(2n, n − c)` of them have no point on the line `y = c`. The proof reflects the part of a line after its first point on `y = c`, which gives a bijection onto the lines from `(0, 0)` to `(2n, 2c)`, with `n + c` up-steps and `n − c` down-steps.[^5] Lemma 2.2: `C(2n, n) − 2 Σ_{i=1}^{⌊n/c⌋} (−1)^{i−1} C(2n, n − ic)` of them meet neither `y = c` nor `y = −c`. The proof is inclusion-exclusion over the classes `L_i` of lines that meet the two lines alternately at least `i` times: reflecting such a line after each of its first `i` alternate crossings, in `y = c`, then `y = 3c`, then `y = 5c`, …, ends it at `(2n, ±2ic)`, so `|L_i| = 2C(2n, n − ic) − |L_{i+1}|`, and `L_i` is empty for `i > ⌊n/c⌋`.[^6]

**Proof of Theorem 1.2.** Merge the two samples, sort the `2n` values, and record `+1` for a value of the first sample and `−1` for one of the second. The running sum after `k` values is the difference of the two empirical counts just above the `k`-th value, so `√(n/2) D_{n,n} < z` exactly when the running sum stays strictly between `−c` and `c`. Since the samples have the same distribution, all arrangements of the `+1`s and `−1`s are equally likely, and Lemmas 2.1 and 2.2 count the favorable ones.[^7] Corollary 2.2 then derives Smirnov's limits for `m = n` from Stirling's formula, `C(2n, n − kc)/C(2n, n) = exp(−2k²z² + o(1))`, with a truncation argument for the alternating sum.[^8]

**Kolmogorov's theorem through the Brownian bridge.** Section 3 gives the paper's proof of Theorem 1.1, which uses no general results on the weak convergence of measures such as Prokhorov's theorem. The uniform empirical process `β_n(t) = √n (F*_n(t) − t)` has the covariance `min(t, s) − ts` of the Brownian bridge `W⁰(t) = W(t) − tW(1)`, its maximum converges in law to that of `W⁰` by a modulus-of-continuity lemma (Lemma 3.1, Proposition 3.1), and the law of the maximum of `|W⁰|` is `K⋆(z)` because the two-sample process `√(n/2)(F*_n − G*_n)` has the same covariance and its maximum has the limit law of Corollary 2.2 (Proposition 3.2).[^9]

**Remarks.** Theorem 1.2 fails for discrete distributions, and the paper randomizes the order of tied values to recover it (Corollary 4.1); it also tests a location-scale family by comparing a sample with a simulated one through ratios of differences.[^10]

## The castle reading

Give column `i` of a merged order, for `i = 1, …, 2n + 1`, the height one more than the absolute running sum after `i − 1` values. The skyline is a Dyck-path castle of width `2n + 1`, each peak (maximal run of columns of height at least 2) carries the sample that is ahead on it, and these marked skylines are the Kolmogorov castles ([[kolmogorov-castles](pages/kolmogorov-castles.md)]). A Kolmogorov castle has height at most `h` exactly when its running sum stays strictly between `−h` and `h`, so Lemma 2.2 with `c = h` counts the Kolmogorov castles of width `2n + 1` and height at most `h`, and Lemma 2.1 with `c = h` those whose peaks marked by the first sample have height at most `h`. The height minus one is `n D_{n,n}`, and Corollary 2.2 becomes a limit law for castle heights: the share of the Kolmogorov castles of width `w` lower than `1 + x√(w − 1)` tends to `K⋆(x)`.

## Key Takeaways

- **Lemma 2.2.** `C(2n, n) − 2 Σ_{i=1}^{⌊n/c⌋} (−1)^{i−1} C(2n, n − ic)` lattice paths of `2n` steps `±1` from 0 to 0 stay strictly between `−c` and `c`, by repeated reflection and inclusion-exclusion.[^6]
- **Theorem 1.2.** Every merged order of two samples of size `n` is equally likely, so the exact law of `D_{n,n}` is Lemma 2.2 divided by `C(2n, n)`.[^4][^7]
- **Limits.** `√(n/2) D_{n,n}` tends in law to Kolmogorov's `K⋆(z) = 1 − 2 Σ (−1)^{k−1} exp(−2k²z²)`, and `√(n/2) D^+_{n,n}` to `1 − exp(−2z²)`.[^2][^8]
- **The castle use.** With `c = h`, Lemma 2.2 counts the Kolmogorov castles of width `2n + 1` and height at most `h`.

## Entities & Concepts

- [[kolmogorov-castles](pages/kolmogorov-castles.md)] - the castles of the two-sample test, counted by Lemma 2.2, with Kolmogorov's limit law for their heights.

## Relation to Other Wiki Pages

[[banderier-nicodeme-2010-bounded-discrete-walks](pages/banderier-nicodeme-2010-bounded-discrete-walks.md)] counts walks with any finite set of jumps between two walls by the kernel method and proves a Rayleigh limit law `exp(−2x²)` for the height of a bridge; for the jumps `±1` and walls at `±c` it counts the paths of Lemma 2.2, and its Rayleigh law is the one-sided limit of Corollary 2.2. [[zig-zag-castles](pages/zig-zag-castles.md)] counts the same `±1` walks on a bounded set of heights by the path matrix `A_path`. [[kolmogorov-1933-determinazione-empirica](pages/kolmogorov-1933-determinazione-empirica.md)] is Kolmogorov's paper with Theorem 1.1, [[smirnov-1944-approximation-distribution-laws](pages/smirnov-1944-approximation-distribution-laws.md)] states Smirnov's two-sample theorem, and [[korolyuk-1955-two-independent-samples](pages/korolyuk-1955-two-independent-samples.md)] credits the case `n = m` to Gnedenko and Korolyuk (1951) and extends it to samples of sizes `n` and `pn`.

## Footnotes

[^1]: [[lutsenko-marinich-matsak-2009-gnedenko-korolyuk-method](pages/lutsenko-marinich-matsak-2009-gnedenko-korolyuk-method.md)] p.133 L1-L13, p.146 L978-L979 [synthesis] - the running heads "Teor Imovr. ta Matem. Statist. Vip. 78, 2008" and "Theor. Probability and Math. Statist. No. 78, 2009, Pages 133–146", the title and the authors, "Received 2/JUL/2007" and "Translated by O. I. KLESOV".
[^2]: [[lutsenko-marinich-matsak-2009-gnedenko-korolyuk-method](pages/lutsenko-marinich-matsak-2009-gnedenko-korolyuk-method.md)] §1 Theorem 1.1 p.133 L39-L53 [synthesis] - Kolmogorov's statistic `D_n = sup |F*_n(t) − F(t)|`, the limit `lim P(√n D_n < z) = K(z) = 1 − 2 Σ_{n≥1} (−1)^{n−1} exp(−2n²z²)` for continuous `F` (formula garbled in the text layer), and "Kolmogorov used a different notation in [1], namely D and Φ(z) instead of Dn and K(z), respectively."
[^3]: [[lutsenko-marinich-matsak-2009-gnedenko-korolyuk-method](pages/lutsenko-marinich-matsak-2009-gnedenko-korolyuk-method.md)] §1 eq. (2) pp.133-134 L54-L83 [synthesis] - "The next steps are due to Smirnov [2]", the limits `1 − exp(−2z²)` and `K(z)` for `√n̂ D^+_{m,n}` and `√n̂ D_{m,n}`, and "n̂ = mn/(m + n), and Fn∗(t) and G∗m(t) are the empirical distribution functions constructed from two independent identically distributed samples of sizes n and m, respectively, m ≤ n."
[^4]: [[lutsenko-marinich-matsak-2009-gnedenko-korolyuk-method](pages/lutsenko-marinich-matsak-2009-gnedenko-korolyuk-method.md)] §1 Theorem 1.2 p.134 L84-L115 - "Gnedenko and Korolyuk [3] found in 1951 an ingenious combinatorial proof of equality (2) for m = n. Moreover, the explicit distribution of the statistic Dn,n is obtained in [3] for finite n."; equalities (3) and (4) (garbled in the text layer; the paper's description of `c`, "the minimal integer that does not exceed z√(2n)", is read with the proof at L332-L335, where `√(n/2) D_{n,n} < z` becomes `sup |S_k| < c`); "The explicit expressions for the distributions of the statistics D+m,n and Dm,n are found by Korolyuk [4] for all m and n. However these expressions are much more complicated as compared to relations (3) and (4)." Checked by execution, footnote 11.
[^5]: [[lutsenko-marinich-matsak-2009-gnedenko-korolyuk-method](pages/lutsenko-marinich-matsak-2009-gnedenko-korolyuk-method.md)] §2 Lemma 2.1 p.135 L143-L171 - "Reflecting, with respect to the line y = c, the part of the polygonal line to the right of the first intersection point with y = c we obtain a new polygonal line starting at the point (0; 0) and ending at the point (2n; 2c)."
[^6]: [[lutsenko-marinich-matsak-2009-gnedenko-korolyuk-method](pages/lutsenko-marinich-matsak-2009-gnedenko-korolyuk-method.md)] §2 Lemma 2.2 and proof pp.135-137 L193-L304 [synthesis] - the classes `L_1`, `L_2`, … of lines meeting `y = c` and `y = −c` alternately at least `i` times, the successive reflections in `y = c`, `y = 3c`, `y = 5c`, the recursion `|L_i| = 2C_{2n}^{n−ic} − |L_{i+1}|`, the end at `i = [n/c]`, and the alternating sum. Checked by execution, footnote 11.
[^7]: [[lutsenko-marinich-matsak-2009-gnedenko-korolyuk-method](pages/lutsenko-marinich-matsak-2009-gnedenko-korolyuk-method.md)] §2 proof of Theorem 1.2 pp.137-138 L307-L392 [synthesis] - "Now we merge two samples … and obtain the sample z1, z2, …, z2n; we write its elements in the ascending order", the signs `ε_k = ±1` and the sums `S_k`, "According to the symmetry … all allocations of the symbols 1 and −1 in the sequence (εi) have the same probability.", and Lemmas 2.1 and 2.2 applied to `sup S_k < c` and `sup |S_k| < c`.
[^8]: [[lutsenko-marinich-matsak-2009-gnedenko-korolyuk-method](pages/lutsenko-marinich-matsak-2009-gnedenko-korolyuk-method.md)] §2 Corollary 2.2 and proof pp.138-140 L395-L544 [synthesis] - the limits (5) `1 − e^{−2z²}` and (6) `K(z)` for `z > 0`, Stirling's formula giving `C_{2n}^{n−kc}/C_{2n}^{n} = e^{−2k²z² + o(1)}`, and the bound on the alternating tails.
[^9]: [[lutsenko-marinich-matsak-2009-gnedenko-korolyuk-method](pages/lutsenko-marinich-matsak-2009-gnedenko-korolyuk-method.md)] §1 p.134 L121-L125, §3 pp.140-144 L546-L825 [synthesis] - the proof "does not use general results on the weak convergence of measures such as Prokhorov's theorem"; the Brownian bridge `W⁰(t) = W(t) − tW(1)` with covariance `min(t, s) − ts`, the uniform empirical process with the same covariance, Lemma 3.1 and Propositions 3.1 and 3.2, and "Equality (10) follows from Proposition 3.2, … and in view of Corollary 2.2. The Kolmogorov theorem is proved." The text layer drops the absolute value bars in (9) and (10).
[^10]: [[lutsenko-marinich-matsak-2009-gnedenko-korolyuk-method](pages/lutsenko-marinich-matsak-2009-gnedenko-korolyuk-method.md)] §4 pp.144-145 L827-L924 [synthesis] - Remark 2, "Naturally, Theorem 1.2 does not hold for discrete random variables", the randomized statistics and Corollary 4.1; Remark 3, the test of a location-scale family with the samples `ξ̄_j` and `η̄_j`.
[^11]: Verified by execution (Python 3.11, 2026-10-28): `bin/python/kolmogorov_castles.py` items [3] and [6], run log `bin/python/kolmogorov_castles-run.log`. Lemma 2.2 against the reflection sum `Σ_k (−1)^k C(2n, n + kc)` and the path-matrix count for `n < 40`, and against enumeration of all merged orders for `n ≤ 9`; Lemma 2.1 against enumeration for `n ≤ 9`.
