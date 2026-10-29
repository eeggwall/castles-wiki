---
title: "Kolmogorov (1933) - Sulla determinazione empirica di una legge di distribuzione"
category: Sources
summary: Kolmogorov defines the empirical distribution function F_n of n independent observations and the statistic D = sup |F_n(x) − F(x)|, and proves Theorem I - for every continuous F, the probability Φ_n(λ) that D < λ/√n tends, uniformly in λ, to Φ(λ) = Σ_{k=−∞}^{+∞} (−1)^k e^{−2k²λ²}. He tabulates Φ from 0 to 2.8 (Φ(1) = 0.7300, Φ(1.4) = 0.9603, Φ(0.83) ≈ 0.5), shows that Φ_n does not depend on F by mapping x to F(x), computes Φ_n exactly for λ = μ/√n by a recursion over the values of the empirical count, and rewrites that recursion as the probability that a random walk with Poisson steps stays strictly between −μ and μ and ends at 0. A local limit theorem for walks between two boundaries (Theorem II) evaluates it through the Green's function of the heat equation in a strip, an alternating sum of Gaussians over the images of the starting point, which gives the limit Φ(λ). On the castle side, Φ is the limit law of the heights of the Kolmogorov castles.
tags: [source, paper, kolmogorov-smirnov, empirical-distribution, limit-law, random-walk, heat-equation, method-of-images, kolmogorov-castle]
sources: [kolmogorov-1933-determinazione-empirica]
created: 2026-10-28
updated: 2026-10-28
---

# Kolmogorov (1933) - Sulla determinazione empirica di una legge di distribuzione

**Source:** `raw/kolmogorov-1933-determinazione-empirica.pdf` (the nine page images, git-ignored) and `raw/kolmogorov-1933-determinazione-empirica.txt` (tracked), an OCR text layer made with Tesseract's Italian model from the scan of *Giornale dell'Istituto Italiano degli Attuari*, vol. 4 (1933), in the digital library of the Biblioteca Nazionale Centrale di Roma, http://digitale.bnc.roma.sbn.it/tecadigitale/giornale/CFI0353791/1933/unico, images 93 to 101. A. Kolmogoroff, "Sulla determinazione empirica di una legge di distribuzione", *Giornale dell'Istituto Italiano degli Attuari* 4 (1933), pp. 83-91, in Italian.[^1] The text layer marks each page `[p. N]` and garbles most formulas, so formulas on this page were read from the page images, are cited by synthesis, and were checked by execution.
**Date ingested:** 2026-10-28
**Type:** paper (scan, 9 pp.)

## Notation used on this page

| paper | meaning | written here as |
|---|---|---|
| `F(x)`, `F_n(x)` | the distribution function and the empirical law of `n` observations | the same |
| `D` | `estr. sup \|F_n(x) − F(x)\|`, the least upper bound | `D_n` |
| `Φ_n(λ)`, `Φ(λ)` | `P(D < λ/√n)` and its limit | `Φ_n(λ)`, and `K⋆(λ)` for the limit (`K` is taken on the wiki, [[castle-notation](pages/castle-notation.md)]) |
| `S_k`, `R_{ik}` | the partial sums of the auxiliary walk, and the probability that it stays between the bounds and ends at `i` | the same (`S` is the signed castle count only on castle pages) |

## Summary

**The question.** For observations `X_1 ≤ ⋯ ≤ X_n` of a variable with distribution function `F`, the empirical law `F_n(x)` is 0 below `X_1`, `k/n` on `[X_k, X_{k+1})` and 1 from `X_n` on, so `n F_n(x)` counts the values that do not exceed `x`. Von Mises's `ω²` method had addressed how close `F_n` is to `F`; Kolmogorov asks for the law of `D_n = sup |F_n(x) − F(x)|`, and says that the problem came to him from Glivenko's recent work.[^2]

**Theorem I.** For every continuous `F`, the probability `Φ_n(λ)` of `D_n < λ/√n` tends, uniformly in `λ`, to

```
K⋆(λ)  =  Σ_{k=−∞}^{+∞} (−1)^k e^{−2k²λ²}  =  1 − 2 Σ_{k≥1} (−1)^{k−1} e^{−2k²λ²}.          [1]
```

The paper prints values of `K⋆` computed by N. Kogeknikov, among them `0.0028` at `λ = 0.4`, `0.1357` at 0.6, `0.7300` at 1, `0.8877` at 1.2, `0.9603` at 1.4, `0.9880` at 1.6 and `0.99932` at 2. It observes that `D_n ≤ 2.4/√n` is practically certain, that `K⋆(0.83)` is about `1/2`, and that for small `λ` the slowly converging series [1] can be replaced by `(√(2π)/λ) e^{−π²/(8λ²)}`.[^3]

**Reduction to the uniform law.** The variable `Y = F(X)` is uniform on `[0, 1]`, and `F_n(x) − F(x)` is the empirical deviation of `Y` at `F(x)`, so `Φ_n` does not depend on the continuous `F` (Lemma), and it suffices to take `F(x) = x` on `[0, 1]`.[^4]

**The exact law.** Take `λ = μ/√n` with `μ` an integer. Since `F_n` takes only the values `i/n` and is monotone, `D_n < μ/n` reduces to the conditions `|F_n(j/n) − j/n| < μ/n` at the points `j/n`, `j = 0, …, n` (eq. [4]). With `P_{ik}` the probability that these hold for `j ≤ k` and `F_n(k/n) − k/n = i/n`, `Φ_n(λ) = P_{0n}`, `P_{00} = 1`, `P_{ik} = 0` for `|i| ≥ μ`, and `P_{i,k+1} = Σ_j P_{jk} Q_{ji}^{(k)}`, with `Q_{ji}^{(k)}` a binomial probability for the number of observations in `(k/n, (k+1)/n]` (eqs. [5] to [12]). The substitution `R_{ik} = (n − k − i)! n^n e^{−k} P_{ik} / ((n − k)^{n−k−i} n!)` turns this into

```
R_{00} = 1,   R_{i0} = 0 (i ≠ 0),   R_{ik} = 0 (|i| ≥ μ),   R_{i,k+1} = Σ_j R_{jk} e^{−1}/(i − j + 1)!,
Φ_n(λ) = (n!/n^n) e^n R_{0n}                                                              [13]-[17]
```

which can be computed for any `n` and `μ`.[^5]

**A random walk between two walls.** Let `Y_1, Y_2, …` be independent with `P(Y_k = (i − 1)/μ) = e^{−1}/i!`, a Poisson count minus 1 scaled by `1/μ`, and `S_k = Y_1 + ⋯ + Y_k`. The probability that `|S_j| < 1` for `j = 0, …, k` and `S_k = i/μ` satisfies the same relations [14] to [16], so it equals `R_{ik}`: `Φ_n` is `(n!/n^n) e^n` times the probability that a walk of `n` steps with mean 0 stays strictly between the two walls and returns to 0.[^6]

**Theorem II and the limit.** For independent `Y_k` on a lattice of step `ε` with mean 0, variance `2b_k` and bounded third moments, the probability `R_{in}` that the walk stays between `a(t_k)` and `b(t_k)` and ends at `iε`, with `t_k = b_1 + ⋯ + b_k`, is `ε (u(0, 0, iε, t_n) + Δ)`, `Δ → 0` with `ε`, where `u` is the Green's function of the heat equation `∂f/∂t = ∂²f/∂s²` in the domain `a(t) < s < b(t)`. Kolmogorov places the theorem with an earlier note of his on the Laplace-Lyapunov theorem and defers its proof. In the present case `ε = 1/μ`, `a = −1`, `b = +1`, `t_n = 1/(2λ²)`, and the Green's function of the strip is the alternating sum over images

```
u(0, 0, s, t)  =  (1/(2√(πt))) Σ_{k=−∞}^{+∞} (−1)^k e^{−(s − 2k)²/(4t)},
```

so that `Φ_n(λ) = Σ (−1)^k e^{−2k²λ²} + R` with `R → 0` uniformly for `λ` above any fixed `λ_0 > 0`, which proves Theorem I for `λ = μ/√n` and then, by continuity of the limit, for all `λ`.[^7]

## The castle reading

The two-sample statistic `D_{n,n}` of the Kolmogorov castles has the same limit law `K⋆` ([[kolmogorov-castles](pages/kolmogorov-castles.md)]): the share of the Kolmogorov castles of width `w` with height at most `1 + x√(w − 1)` tends to `K⋆(x)`. Kolmogorov's proof and the castle count follow the same pattern. His `R_{0n}` is the probability that a walk stays strictly between two walls and returns to its start; the heights of the Kolmogorov castles of height at most `h` are the walks of `2n` steps `±1` that stay strictly between `−h` and `h` and return to 0. The castle count is an alternating sum of binomials over the reflections of the endpoint in the two walls, `Σ_k (−1)^k C(2n, n + kh)`, and Kolmogorov's limit is an alternating sum of Gaussians over the images of the starting point in the walls `s = ±1`, the reflection argument for the heat equation.

## Key Takeaways

- **Theorem I.** `P(D_n < λ/√n) → K⋆(λ) = Σ_k (−1)^k e^{−2k²λ²}` uniformly in `λ`, for every continuous `F`.[^3]
- **Values.** `K⋆(1) = 0.7300`, `K⋆(1.4) = 0.9603`, `K⋆(0.83) ≈ 1/2`; `D_n ≤ 2.4/√n` is practically certain.[^3]
- **Method.** An exact recursion for `Φ_n(μ/√n)`, read as a walk with Poisson steps confined between two walls, and a local limit theorem through the Green's function of the heat equation in a strip.[^5][^7]

## Entities & Concepts

- [[kolmogorov-castles](pages/kolmogorov-castles.md)] - the castles of the two-sample test, whose heights have the limit law `K⋆`.

## Relation to Other Wiki Pages

[[smirnov-1944-approximation-distribution-laws](pages/smirnov-1944-approximation-distribution-laws.md)] restates Theorem I, credits it to Kolmogorov, and adds the one-sided limit `1 − e^{−2λ²}` and the two-sample limit theorem. [[lutsenko-marinich-matsak-2009-gnedenko-korolyuk-method](pages/lutsenko-marinich-matsak-2009-gnedenko-korolyuk-method.md)] gives a second proof of Theorem I through the Brownian bridge and the two-sample count of Gnedenko and Korolyuk.

## Footnotes

[^1]: [[kolmogorov-1933-determinazione-empirica](pages/kolmogorov-1933-determinazione-empirica.md)] p.83 L1-L8 [synthesis] - the title "SULLA DETERMINAZIONE EMPIRICA DI UNA LEGGE DI DISTRIBUZIONE", the author "A. KOLMOGOROFF." and the Sunto, "Contributo allo studio della possibilità di determinare una legge di distribuzione conoscendo i risultati di un numero finito di prove."; the page numbers 83 to 91 in the running heads, L1-L394.
[^2]: [[kolmogorov-1933-determinazione-empirica](pages/kolmogorov-1933-determinazione-empirica.md)] §1 pp.83-84 L10-L46 [synthesis] - the observations in increasing order, "Si chiama legge empirica della distribuzione la funzione F_n(x)", "Pertanto nF_n(x) rappresenta il numero dei valori X_k che non superano il valore x", von Mises's "metodo ω²", and "all'impostazione del problema, qui trattato, sono stato condotto dalle recenti ricerche di Glivenko".
[^3]: [[kolmogorov-1933-determinazione-empirica](pages/kolmogorov-1933-determinazione-empirica.md)] §1 Theorem I and the table p.84 L48-L75 [synthesis] - Theorem I with formula [1] read from the page image; "Ecco intanto alcuni valori di Φ(λ) calcolati da N. Kogeknikov", the table for `λ = 0.0, 0.2, …, 2.8`; "la disuguaglianza D ≤ 2,4/√n può considerarsi come praticamente certa", "Φ(0,83) ~ 0,5", and the small-`λ` formula. The values quoted above, for `λ ≤ 2`, are `K⋆(λ)` truncated to the printed digits, checked by execution in footnote 8.
[^4]: [[kolmogorov-1933-determinazione-empirica](pages/kolmogorov-1933-determinazione-empirica.md)] §2 Lemma p.85 L88-L125 [synthesis] - "La funzione di probabilità Φ_n(λ) non dipende dalla funzione di distribuzione F(x) se questa è soltanto continua.", the uniform law of `Y = F(X)`, the reduction to `F(x) = x` on `0 ≤ x ≤ 1`, and `λ = μ/√n`.
[^5]: [[kolmogorov-1933-determinazione-empirica](pages/kolmogorov-1933-determinazione-empirica.md)] §2 eqs. [3]-[17] pp.86-88 L126-L237 [synthesis] - the reduction to the points `j/n` (eq. [4]), the events `E_{ik}` and probabilities `P_{ik}`, the recursion [9] with the binomial [12], the substitution [13] and the relations [14] to [17]; formulas read from the page images. The recursion [14]-[17] was checked against Monte Carlo by execution, footnote 8.
[^6]: [[kolmogorov-1933-determinazione-empirica](pages/kolmogorov-1933-determinazione-empirica.md)] §3 eqs. [18]-[19] p.88 L238-L260 [synthesis] - the variables `Y_k` with `P{Y_k = (i − 1)/μ} = e^{−1}/i!`, the sums `S_k`, the conditions [19] on `S_j` and `S_k = i/μ`, and "cioè a dire che si ha R_ik = R_ik"; the walls are at `±1` in the scaled walk, as in the application of Theorem II on p.90 with `a(t) = −1`, `b(t) = +1`.
[^7]: [[kolmogorov-1933-determinazione-empirica](pages/kolmogorov-1933-determinazione-empirica.md)] §3 Theorem II and the conclusion pp.89-91 L261-L394 [synthesis] - Theorem II, "la funzione di Green relativa all'equazione del calore", conditions a) to d), the relation to "una mia Nota" (Bulletin de l'Académie des Sciences de l'U.R.S.S., 1931, with the full proof announced for 1932), the case `ε = 1/μ`, `t_n = 1/(2λ²)`, `a(t) = −1`, `b(t) = +1`, the formula for `u(0, 0, s, t)`, "Il resto R di questa formula tende uniformemente a zero per n → ∞ nel caso in cui λ è maggiore di un assegnato λ_0 > 0", and "In merito alla dimostrazione del teorema II ci proponiamo ritornare in una ulteriore Nota."
[^8]: Verified by execution (Python 3.11, 2026-10-28): `bin/python/kolmogorov_castles.py` items [11] and [12], run log `bin/python/kolmogorov_castles-run.log`. The table values for `λ = 0.0, …, 2.0` against `K⋆(λ)` truncated; `K⋆(0.83) = 0.5038`; `1 − K⋆(2.4) = 2.0·10⁻⁵`; the recursion [14]-[17] against Monte Carlo estimates of `P(D_n < μ/n)` (200000 samples) at `(n, μ) = (5, 2), (10, 3), (16, 4)`, within 0.002, and its values at `λ = 1` for `n = 25, 100, 400, 1600`, decreasing to `K⋆(1) = 0.7300`.
