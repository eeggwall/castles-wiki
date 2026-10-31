---
title: "Yuste, Abad and Baumgaertner (2016) - Anomalous diffusion and FRAP dynamics in the random comb model"
category: Sources
summary: Yuste, Abad and Baumgaertner study the random comb, a backbone with equally spaced teeth whose lengths ℓ are drawn independently with P(ℓ) ∼ ℓ^{−(1+α)}. They restate the known exponents, ⟨x²(t)⟩ ∼ t^γ with γ = (1 + α)/2 for 0 < α < 1, t/ln t at α = 1 and normal diffusion for α > 1, the regular comb with infinite teeth being the case γ = 1/2, and compute the coefficient D_0(α) of ⟨x²⟩ = D_0 t^γ by a continuous-time random walk in which tooth excursions are waiting times on the backbone, checked against Monte Carlo simulations. For α > 1, D_0 = Σ²/τ with τ = 1 + θ t_R(ℓ)/(1 − θ) averaged over the teeth, θ the probability of entering a tooth from the backbone and t_R(ℓ) the mean return time from a tooth of length ℓ, which equals the number of sites of the equivalent ring (2ℓ + 1, or 2ℓ when the walker always steps back at the end of a tooth). Binding and unbinding slow the backbone motion by the factor (1 + κ)^{−γ}, and fluorescence-recovery (FRAP) curves on the comb follow a fractional diffusion equation that scaled Brownian motion fits closely but not exactly.
tags: [source, paper, comb-model, random-comb, random-walk, continuous-time-random-walk, anomalous-diffusion, subdiffusion, diffusion-coefficient, fractional-diffusion-equation, frap, tree-castle]
sources: [yuste-abad-baumgaertner-2016-random-comb-model]
created: 2026-10-29
updated: 2026-10-29
---

# Yuste, Abad and Baumgaertner (2016) - Anomalous diffusion and FRAP dynamics in the random comb model

**Source:** `raw/yuste-abad-baumgaertner-2016-random-comb-model.pdf` (git-ignored) and its text layer `raw/yuste-abad-baumgaertner-2016-random-comb-model.txt` (tracked, extracted with `pdftotext -layout`). S. B. Yuste, E. Abad and A. Baumgaertner, "Anomalous diffusion and FRAP dynamics in the random comb model", arXiv:1603.05972v1 [cond-mat.stat-mech], 18 March 2016, https://arxiv.org/abs/1603.05972, published as *Physical Review E* 94, 012118 (2016); the arXiv version was the one read.[^1]
**Date ingested:** 2026-10-29
**Type:** paper (35 pp., double-spaced)

## Notation used on this page

| paper | meaning | written here as |
|---|---|---|
| `ℓ`, `P(ℓ)` | the length of a tooth and its distribution, `P(ℓ) ∼ ℓ^{−(1+α)}` | the same |
| `α`, `γ` | the tail exponent of the tooth lengths and the diffusion exponent, `⟨x²⟩ ∼ t^γ` | the same |
| `D_0(α)` | `lim_{t→∞} ⟨x²⟩/t^γ` | the same |
| `θ` | the probability that a walker on the backbone enters the tooth at the next step | the same |
| `τ(ℓ)`, `τ` | the mean time until the next backbone step from the foot of a tooth of length `ℓ`, and its average over the teeth | the same |
| `t_R(ℓ)` | the mean time to return to the foot of a tooth after entering it | the same |
| `Σ²` | the variance of the distance between consecutive teeth (1 here) | the same |

## Summary

**The random comb.** Comb models "distribute a number of vertical teeth along a one-dimensional line (the backbone)", and excursions along the teeth act as trapping events that slow the motion along the backbone. In the regular comb the spacing and the length of the teeth are constant; "The case of a regular comb with infinite tooth length `ℓ → ∞` was discussed in Ref. [6]", Weiss and Havlin (1986), and gives `⟨x²⟩ ∝ t^{1/2}`. In the random comb the spacing stays regular and the length of each tooth is drawn independently with `P(ℓ) ∼ ℓ^{−(1+α)}`; Havlin, Kiefer and Weiss (1987) and Havlin and ben-Avraham (1987) showed `⟨x²(t)⟩ ∼ t^γ` with `γ = (1 + α)/2` for `0 < α < 1`, `t/ln(t)` at `α = 1` and normal diffusion for `α > 1`, so `α` tunes `γ` through `1/2 ≤ γ ≤ 1`.[^2]

**Simulations.** A tooth of length `ℓ_k = ⌊r^{−α}⌋`, `r` uniform on `(0, 1)`, stands at every backbone site, so `P(ℓ) = ℓ^{−α} − (ℓ + 1)^{−α}` (1). A walker on a tooth moves only vertically; on the backbone it jumps up with probability 1/2 and left or right with probability 1/4 each; at the end of a tooth it either steps back or stays. The backbone is a periodic box of 200 to 1600 sites, run to `t ≤ 10^8`. The ratio `⟨x²⟩/t^γ` reaches a plateau, which estimates `D_0(α)` (Figure 3); `D_0` first decreases and then increases with `α`, and tends to `1/4` for teeth of length 1 everywhere.[^3]

**The coefficient by a continuous-time random walk.** The time a walker spends on a tooth is a waiting time between two backbone steps; drawing the tooth anew at each visit (an annealed version of the quenched comb) gives a continuous-time random walk. The survival on a tooth of length `ℓ` is that of a walker on a ring of `2ℓ` sites, `T_n(ℓ)` (6)-(7); its averages over the teeth give the waiting-time density `ψ(t) ∼ ψ̂_α t^{−(3+α)/2}` (19). For `0 < α < 1` the subdiffusive coefficient is (23), with `Σ² = 1`. For `α > 1` the mean waiting time is finite and `D_0 = Σ²/τ` (24), where a walker at the foot of a tooth reaches a neighboring backbone site after

```
τ(ℓ)  =  1 + θ t_R(ℓ)/(1 − θ)        (26)
```

steps on average, `θ` being the probability of entering the tooth. With the boundary of the simulations a tooth of length `ℓ` is equivalent to a ring of `2ℓ + 1` sites, and "for a periodic `N`-site lattice this return time is precisely identical with the number of lattice sites `N`", so `t_R(ℓ) = 2ℓ + 1`, `τ = (1 + 2θ⟨ℓ⟩)/(1 − θ)` (27), and at `θ = 1/2`, with `⟨ℓ⟩ = ζ(α)`, `D_0(α) = Σ²/(2 + 2ζ(α))` (28), or `(1 − θ)Σ²/(1 + 2θζ(α))` for general `θ` (29). If the walker at the end of a tooth always steps back, the ring has `2ℓ` sites, `t_R(ℓ) = 2ℓ`, `τ = 1 + 2⟨ℓ⟩` and `D_0(α) = Σ²/(1 + 2θ(1 − θ)^{−1}ζ(α))`. At `α = 1`, `⟨x²(t)⟩ ∼ (Σ²/ψ̂_1) t/ln(t)` (30). Both formulas agree with the simulations.[^4]

**Binding and FRAP.** A walker that binds with rate `K_on` and unbinds with rate `K_off` takes `1 + κ` time units per jump on average, `κ = K_on/K_off`, so `D_κ/D_0 = (1 + κ)^{−γ}` (31). In a FRAP experiment the particles in a spot of the backbone are removed and the spot refills; the refilling follows the fractional diffusion equation `∂c/∂t = K_γ ₀D_t^{1−γ} ∂²c/∂x²` (33), with the Riemann-Liouville derivative, solved in Laplace space (35)-(38) and inverted with a Fox `H`-function for an infinite system (40), and with `[1 − C_L(t)]^{−1} ∝ t^γ` for a finite one (51). A diffusion equation with a time-dependent coefficient, scaled Brownian motion, cannot reproduce these recovery curves exactly, though the difference is small.[^5]

## The castle reading

A tree castle is a comb with its bottom row as the backbone, and the tooth of each column has `c_i − 1` cells ([[tree-castle-diffusion](pages/tree-castle-diffusion.md)]). A castle of height `h` has teeth of at most `h − 1` cells, so every tooth-length distribution on castles of bounded height has a finite mean, the `α > 1` side, and the walk diffuses normally at long times. For the simple random walk, the walker at the foot of a tooth enters it with probability `θ = 1/3` and steps back at the end of the tooth, so `t_R(ℓ) = 2ℓ` and Equation (26) gives `τ(ℓ) = 1 + ℓ`: one backbone step in every `1 + ℓ` steps, the share of backbone edges among the `1 + ℓ` edges of one period when every site carries a tooth of `ℓ` cells. On a tree castle the share is `(w − 1)/(n − 1)`. The exponents `(1 + α)/2 < 1` need teeth of unbounded length, which a castle of fixed height does not have.[^6]

## Key Takeaways

- **Random teeth tune the exponent**: `γ = (1 + α)/2` for `0 < α < 1`, `t/ln t` at `α = 1`, normal diffusion for `α > 1` (restated from Havlin, Kiefer and Weiss).[^2]
- **The finite-mean coefficient is a count of returns**: `D_0 = Σ²/τ` with `τ(ℓ) = 1 + θ t_R(ℓ)/(1 − θ)` and `t_R(ℓ)` the number of sites of the equivalent ring.[^4]
- **The regular comb with infinite teeth** gives `⟨x²⟩ ∝ t^{1/2}`.[^2]
- **Binding** divides the effective time by `1 + κ`, so `D_κ/D_0 = (1 + κ)^{−γ}`.[^5]

## Entities & Concepts

- [[tree-castle-diffusion](pages/tree-castle-diffusion.md)] - the tree castles as combs with teeth of at most `h − 1` cells; Equation (26) at `θ = 1/3` gives the backbone share `1/(1 + ℓ)`.

## Relation to Other Wiki Pages

[[mendez-iomin-campos-horsthemke-2015-random-walks-on-combs](pages/mendez-iomin-campos-horsthemke-2015-random-walks-on-combs.md)] is reference [11] here, the regular comb with finite or infinite branches. [[arkhincheev-baskin-1991-comb-model](pages/arkhincheev-baskin-1991-comb-model.md)] is the continuum comb with the order-1/2 equation, the `γ = 1/2` end of the range. [[half-sum-castles](pages/half-sum-castles.md)] applies the Riemann-Liouville fractional sum, the counterpart of the derivative in Equation (33), to castle generating functions, as multiplication by `(1 − x)^{−α}`.

## Footnotes

[^1]: [[yuste-abad-baumgaertner-2016-random-comb-model](pages/yuste-abad-baumgaertner-2016-random-comb-model.md)] p.1 L1-L39 [synthesis] - the title "Anomalous diffusion and FRAP dynamics in the random comb model", the authors "S. B. Yuste, E. Abad, and A. Baumgaertner" (Universidad de Extremadura, Badajoz and Mérida), "arXiv:1603.05972v1 [cond-mat.stat-mech] 18 Mar 2016" and the abstract. The journal reference is from the arXiv abstract page, https://arxiv.org/abs/1603.05972 (read 2026-10-29), "Journal reference: Phys. Rev. E 94, 012118 (2016)".
[^2]: [[yuste-abad-baumgaertner-2016-random-comb-model](pages/yuste-abad-baumgaertner-2016-random-comb-model.md)] §§I-II pp.2-6 L76-L86, L133-L137, L199-L216 and the references L1489-L1490, L1514 - "The basic idea is to distribute a number of vertical teeth along a one-dimensional line (the backbone), and to allow random walkers diffuse throughout the resulting structure, whereby occasional excursions along the teeth may be viewed as trapping events which slow down the particles' motion along the backbone."; "The case of a regular comb with infinite tooth length ℓ → ∞ was discussed in Ref. [6]. In the appropriate regime, this model yields subdiffusive behavior with anomalous diffusion exponent equal to 1/2, that is, ⟨x²⟩ ∝ t^{1/2}."; "In those references it was shown that the system exhibits anomalous subdiffusion along the backbone axis for 0 < α < 1, i.e., one has ⟨x²(t)⟩ ∼ t^γ with γ = (1 + α)/2. In contrast, for α > 1 there is a crossover to normal diffusion, that is, ⟨x²(t)⟩ ∼ t. At the crossover value α = 1 there is a logarithmic correction, and hence ⟨x²(t)⟩ ∼ t/ln(t)."; references [6] G. H. Weiss and S. Havlin (1986), [7] S. Havlin and D. ben-Avraham (1987), [26] S. Havlin, J. E. Kiefer and G. H. Weiss (1987).
[^3]: [[yuste-abad-baumgaertner-2016-random-comb-model](pages/yuste-abad-baumgaertner-2016-random-comb-model.md)] §§II-III pp.6-10 L217-L386 [synthesis] - Equations (1)-(4); "When a given walker was on a tooth (y > 0), its motion was restricted to the vertical direction (x(t) = const). As soon as the walker returned to the backbone (y = 0), it could either jump back to y = 1 with probability 1/2, or move along the x-axis with probability 1/2 (to the left with probability 1/4 or to the right with probability 1/4)."; "typically 200 ≤ M ≤ 1600"; "Typical simulation times were t ≤ 10^8"; "The diffusion coefficient is seen to display non-monotonic behavior, first it decreases and then it increases with increasing α."; the Figure 3 caption, "the asymptotic value D0(α → ∞) = 1/4, corresponding to a uniform teeth with ℓ = 1 everywhere."
[^4]: [[yuste-abad-baumgaertner-2016-random-comb-model](pages/yuste-abad-baumgaertner-2016-random-comb-model.md)] §IV pp.10-18 L389-L760 [synthesis] - "the CTRW model can be regarded as an annealed version of the comb model in which the length of a given tooth is drawn anew from the corresponding distribution upon each revisitation of the walker"; Equations (5)-(30); "A walker starting at (x, y = 0) can reach (x ± 1, y = 0) after one time step with probability 1−θ = 1/2 provided that it does not enter the tooth, or it may enter the tooth once with probability θ = 1/2"; "it is well known that for a periodic N-site lattice this return time is precisely identical with the number of lattice sites N [50, Eq. (4.172a)]"; "this boundary condition corresponds to treating a tooth of length ℓ like a ring with 2ℓ sites. Correspondingly, one has tR(ℓ) = 2ℓ and τ = 1 + 2⟨ℓ⟩, leading to D0(α) = Σ²/[1 + 2ζ(α)], or to D0(α) = Σ²/[1 + 2θ(1 − θ)^{−1}ζ(α)] for θ ≠ 1/2."
[^5]: [[yuste-abad-baumgaertner-2016-random-comb-model](pages/yuste-abad-baumgaertner-2016-random-comb-model.md)] §§V-VII and Appendix B pp.18-33 L762-L1306, L1379-L1479 [synthesis] - Equation (31) and "the time required to perform a transition between neighboring sites is increased by the factor (1 + κ)"; Equations (32)-(51), "where 0D_t^{1−γ} stands for the so-called Riemann-Liouville fractional derivative"; "One can see that is not posible to fully match the recovery curve obtained from the CTRW model simply by shifting horizontally the solution for the normal diffusion case"; "One can nevertheless see from the figure that the overall agreement is not too bad."
[^6]: Verified by execution (Python 3.11 with NumPy, 2026-10-29): `bin/python/tree_castle_diffusion.py` item [6], run log `bin/python/tree_castle_diffusion-run.log`. The simple random walk on one period of the comb with a tooth of `ℓ` cells at every site, `ℓ = 1, 2, 5, 30`: the fraction of horizontal steps at `t = 10^8` equals `1/(1 + ℓ)` to `10^{−6}`.
