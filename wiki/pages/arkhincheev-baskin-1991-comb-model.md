---
title: "Arkhincheev and Baskin (1991) - Anomalous diffusion and drift in a comb model of percolation clusters"
category: Sources
summary: Arkhincheev and Baskin derive the diffusion equation on the axis of a comb, a conducting line with ribs going to infinity on which motion along the line is possible only on the line itself (diffusion tensor D_xx = D_1 δ(y), D_yy = D_2). The density on the axis obeys an equation in which the first time derivative is replaced by a fractional derivative of order 1/2, (∂^{1/2}/∂t^{1/2} − (D_1/(2D_2^{1/2})) ∂²/∂x²) n = 0, and the mean-square displacement along the axis is exactly ⟨x²(t)⟩ = D_1 (πt/D_2)^{1/2}. Integrating over the ribs gives the continuous-time random walk form with the same exponent. Diffusion becomes conventional again in a weakly conducting surrounding medium, or when the ribs have a finite average length L, where ⟨x²(t)⟩ ∝ D_1 t/L for t ≫ L²/D_2. In an electric field the center of gravity of a packet slows as t^{−1/2}; simulations of drift on percolation clusters give a mobility exponent near 1/3 against the comb's 1/2. The paper credits the comb model and the exponent to Weiss and Havlin (1986), whose Green's function it calls an incorrect Gaussian extrapolation.
tags: [source, paper, comb-model, anomalous-diffusion, subdiffusion, fractional-calculus, fractional-time-derivative, continuous-time-random-walk, percolation, drift, tree-castle]
sources: [arkhincheev-baskin-1991-comb-model]
created: 2026-10-29
updated: 2026-10-29
---

# Arkhincheev and Baskin (1991) - Anomalous diffusion and drift in a comb model of percolation clusters

**Source:** `raw/arkhincheev-baskin-1991-comb-model.pdf` (git-ignored) and its text layer `raw/arkhincheev-baskin-1991-comb-model.txt` (tracked, extracted with `pdftotext -layout`). V. E. Arkhincheev and É. M. Baskin, "Anomalous diffusion and drift in a comb model of percolation clusters", *Soviet Physics JETP* 73 (1), July 1991, pp. 161-165, the English translation (by A. Tybulewicz) of *Zh. Eksp. Teor. Fiz.* 100, 292-300; free PDF from the JETP archive, https://jetp.ras.ru/cgi-bin/dn/e_073_01_0161.pdf.[^1] The text layer drops most formulas and garbles the rest, so formulas on this page were read from the page images and are cited by synthesis.
**Date ingested:** 2026-10-29
**Type:** paper (5 pp.)

## Notation used on this page

| paper | meaning | written here as |
|---|---|---|
| `x`, `y` | the coordinate along the axis of the comb and along its ribs | the same |
| `D_1`, `D_2` | the diffusion coefficients along the axis and along the ribs | the same |
| `G(x, y, t)` | the Green's function of the diffusion problem | the same |
| `θ` | the exponent in `⟨x²(t)⟩ ∝ t^{2/(2+θ)}` | the same |
| `L` | the average length of the ribs | the same |
| `p`, `k` | the Laplace variable of `t` and the Fourier variable of `x` | the same |

## Summary

**The problem.** Anomalous diffusion on fractals means a mean-square displacement `⟨x²(t)⟩ ∝ t^{2/(2+θ)}` (1), with `θ` the critical exponent, established numerically on percolation clusters and by renormalization on Sierpiński-type fractals, but without a derived diffusion equation. A model of percolation clusters with "dead ends", the comb of Figure 1, "was proposed in Ref. 3", G. H. Weiss and S. Havlin, *Physica A* 134 (1986) 474, which found `θ = 2` by generating functions; "However, the diffusion equation was not derived and incorrect extrapolation to the Gaussian form was proposed for the Green's function."[^2]

**The comb.** In the model "displacement in the `x` direction is possible only along the structure axis": `D_xx = D_1 δ(y)` and `D_yy = D_2`, the diffusion tensor (4), so the Green's function obeys

```
∂G/∂t − D_1 δ(y) ∂²G/∂x² − D_2 ∂²G/∂y²  =  δ(x) δ(y) δ(t).        (5)
```

The axis is the line `y = 0`, and its ribs go to infinity on both sides (Figure 1).[^3]

**On the axis.** A Laplace transform in `t` and a Fourier transform in `x` give `G(p, k, y) = exp(−(p/D_2)^{1/2}|y|)/(2(D_2 p)^{1/2} + D_1 k²)` (7), and from it `G(x, 0, t)` as an integral (8). The number of particles on the axis decreases, `∫ G(x, 0, t) dx = 1/(2(πD_2 t)^{1/2})` (9), and the mean-square displacement along the axis is

```
⟨x²(t)⟩  =  ⟨x² G⟩/⟨G⟩  =  D_1 (πt/D_2)^{1/2},        (10)
```

which the paper stresses is exact. The return probability decays as `G(0, 0, t) ∝ (D_1^{1/2} D_2^{1/4} t^{3/4})^{−1}` (12). In the `(p, k)` representation the axis density obeys `[2(D_2 p)^{1/2} + D_1 k²] G(p, k) = 1` (13), and with the fractional derivative defined by `(∂^α f/∂t^α)_p = p^α f(p)` this is

```
( ∂^{1/2}/∂t^{1/2}  −  (D_1/(2 D_2^{1/2})) ∂²/∂x² ) n(x, 0, t)  =  0,
∂^{1/2} n/∂t^{1/2}  =  (1/Γ(1/2)) ∫_0^t (∂n(x, τ)/∂τ) dτ/|t − τ|^{1/2},        (14)
```

the equation for the particle number on the axis. Its integrodifferential form comes from "the random disappearance and subsequent creation of a diffusing particle (disappearance from the axis and return to it) in the course of a random walk along the structure axis."[^4]

**The continuous-time random walk.** If particles delayed in the ribs are counted with those on the axis, the quantity is `G̃(x, t) = ∫ G(x, y, t) dy`, which obeys `[p + (D_1/2)(p/D_2)^{1/2} k²] G̃(p, k) = 1` (15), a continuity equation for a medium with time dispersion (16). This is the continuous-time random walk of Montroll and Weiss and of Shlesinger, in which the particle is delayed at each site and the number of particles is conserved; "The diffusion is still anomalous to the same exponent `θ = 2`", with a different Green's function (17).[^5]

**Back to conventional diffusion.** Immersing the comb in a poorly conducting medium with `D_0 ≪ D_2`, the tensor (18), gives the anomalous law (10) for `t ≪ D_1²/(D_2 D_0²)` and conventional diffusion `∝ D_0 t` for long times. "The transition to the conventional diffusion also occurs when the average length of the ribs `L` is finite. Then, for long times `t ≫ L²/D_2`, we obtain `⟨x²(t)⟩ ∝ D_1 t/L`."[^6]

**Drift and percolation clusters.** In a field `E` along the axis the mobility tensor is (19) and the Green's function (20)-(21); the center of gravity moves as `⟨x(t)⟩ = (μ_1 E/2)(πt/D_2)^{1/2}` (22), so its velocity decreases as `t^{−1/2}` (23), while the maximum of a packet moves differently (24)-(25), and the return probability decays as a power law (27) instead of exponentially (26). Simulations of drift on two-dimensional site-percolation lattices of size 400 or 500 near threshold give a mobility `μ(t) ∝ μ_0/t^γ` (28) with `γ` "approximately equal to 1/3", against "the 1/2 typical of a comb structure", and at long times in strong fields an exponential field dependence `μ(E) ∝ μ_0 exp(−eEL_c/T)` (29), from field-induced traps. The conclusion: "the presence of 'dead ends' leads to fractional time derivatives", whereas a homogeneous isotropic model has fractional spatial derivatives; for percolation clusters both enter, `(∂^S/∂t^S − Δ^ν) n = 0` (30) with `S(2 + θ) = ν` (31).[^7]

## The castle reading

The graph of a tree castle is a comb with the bottom row as its axis and the columns as its ribs, all on one side and at most `h − 1` cells long ([[tree-castle-diffusion](pages/tree-castle-diffusion.md)]). Equation (14) is derived for ribs going to infinity; with ribs of finite length the paper's own long-time law `⟨x²(t)⟩ ∝ D_1 t/L` applies. On the battlement of height `h`, which alternates columns of heights 1 and `h`, the simple random walk spreads as `(4√(2/π) + o(1))√t` while the teeth look infinite, the order-1/2 regime, and as `2t/(h + 1)` at long times, proportional to `1/L` with `L = h − 1`; the two regimes meet at `t = 8(h + 1)²/π`.[^8]

## Key Takeaways

- **The order-1/2 equation.** On a comb with infinite ribs, the density on the axis obeys (14), a diffusion equation whose time derivative has order 1/2.[^4]
- **The exact displacement.** `⟨x²(t)⟩ = D_1 (πt/D_2)^{1/2}` on the axis, Equation (10).[^4]
- **Finite ribs restore normal diffusion.** For ribs of average length `L`, `⟨x²(t)⟩ ∝ D_1 t/L` once `t ≫ L²/D_2`.[^6]
- **The model is Weiss and Havlin's**, whose exponent `θ = 2` the paper confirms and whose Gaussian Green's function it rejects.[^2]

## Entities & Concepts

- [[tree-castle-diffusion](pages/tree-castle-diffusion.md)] - the tree castles as combs, where the order-1/2 regime is a window that closes near `t = 8(h + 1)²/π` on the battlement.

## Relation to Other Wiki Pages

[[mendez-iomin-campos-horsthemke-2015-random-walks-on-combs](pages/mendez-iomin-campos-horsthemke-2015-random-walks-on-combs.md)] cites this paper as one of the origins of the comb model and computes the long-time diffusion coefficient of a discrete comb exactly; [[yuste-abad-baumgaertner-2016-random-comb-model](pages/yuste-abad-baumgaertner-2016-random-comb-model.md)] treats teeth of random length. The contrast in the conclusion, fractional time derivatives from dead ends and fractional spatial derivatives in a homogeneous medium, is the contrast between this page and the space-fractional Laplacian of [[levy-flights](pages/levy-flights.md)].

## Footnotes

[^1]: [[arkhincheev-baskin-1991-comb-model](pages/arkhincheev-baskin-1991-comb-model.md)] p.161 L1-L14 [synthesis] - the title "Anomalous diffusion and drift in a comb model of percolation clusters", the authors, "Buryat Scientifir Center, Siberian Division of the Academy of Sciences of the USSR, Ulan- Ude", "(Submitted 28 December 1990)", "Zh. Eksp. Teor. Fiz. 100,292-300 (July 1991)" and the abstract; the running foot "Sov. Phys. JETP 73 (I),July 1991" (L63, L140, L209, L283, L326) and "Translated by A. Tybulewicz" (L321).
[^2]: [[arkhincheev-baskin-1991-comb-model](pages/arkhincheev-baskin-1991-comb-model.md)] §1 p.161 L19-L57 and the references p.165 L303-L319 - Equation (1) and "Here, θ is the critical exponent of the anomalous diffusion process" (formula read from the page image); "A model allowing for the presence of "dead ends" in percolation systems (Fig. 1) was proposed in Ref. 3. The technique of generating functions was used in Ref. 3 to establish asymptotic behavior of the mean-square displacement along the axis of a structure and to show that it depends anomalously on time [Eq. (1)] with the exponent θ = 2. However, the diffusion equation was not derived and incorrect extrapolation to the Gaussian form was proposed for the Green's function."; "3G. H. Weiss and S. Havlin, Physica A (Utrecht) 134,474 (1986)."
[^3]: [[arkhincheev-baskin-1991-comb-model](pages/arkhincheev-baskin-1991-comb-model.md)] §2.1 pp.161-162 L39-L61, L64-L67 [synthesis] - "A special feature of the diffusion in our model is that displacement in the x direction is possible only along the structure axis. In other words, the diffusion coefficient Dxx differs from zero only for y = 0: Dxx = D1 δ(y). The diffusion coefficient along the ribs is of the conventional type: Dyy = D2."; "FIG. 1. Comb structure: the conducting axis (y = 0) has ribs going to infinity."; the tensor (4) and Equation (5) read from the page image of p.162.
[^4]: [[arkhincheev-baskin-1991-comb-model](pages/arkhincheev-baskin-1991-comb-model.md)] §2.1 p.162 L64-L79, L96-L139 [synthesis] - Equations (6)-(14) read from the page image of p.162; "It must be stressed that the results given by Eqs. (9) and (10) are exact and they follow from the integral representation of Eq. (8)."; "The integrodifferential nature of the diffusion equation (14) is a consequence of the random disappearance and subsequent creation of a diffusing particle (disappearance from the axis and return to it) in the course of a random walk along the structure axis."
[^5]: [[arkhincheev-baskin-1991-comb-model](pages/arkhincheev-baskin-1991-comb-model.md)] §2.1 p.162 L80-L127 [synthesis] - "This formulation of the random-walk problem differs from the case of a continuous distribution of the delay times (continuous-time random walk-CTRW), first discussed in Refs. 5 and 6. The difference is this: in the latter problem the particle does not disappear but is delayed at each site with some probability."; "The diffusion is still anomalous to the same exponent θ = 2."; Equations (15)-(17) read from the page image; Refs. 5 and 6 are Montroll and Weiss (1965) and Shlesinger (1974), L313-L314.
[^6]: [[arkhincheev-baskin-1991-comb-model](pages/arkhincheev-baskin-1991-comb-model.md)] §2.1 pp.162-163 L129-L148 - "it is interesting to consider the transition from the anomalous to the conventional diffusion. For this transition to occur it is sufficient to immerse a comb structure in a poorly conducting medium with the diffusion coefficient D0 (D0 ≪ D2)"; "For short time intervals, namely when t ≪ D1²/D2D0², the anomalous diffusion of Eq. (10) applies, whereas for long times we have the conventional diffusion obeying the D0t law. The transition to the conventional diffusion also occurs when the average length of the ribs L is finite. Then, for long times t ≫ L²/D2, we obtain ⟨x²(t)⟩ ∝ D1t/L." (the inequalities and the last formula read from the page image of p.163, which the text layer garbles).
[^7]: [[arkhincheev-baskin-1991-comb-model](pages/arkhincheev-baskin-1991-comb-model.md)] §§2.2-4 pp.163-165 L150-L301 [synthesis] - Equations (19)-(32) read from the page images; "the velocity of the center of gravity decreases with time"; the lattice "of size L × L (L = 400 or 500)"; "It follows from these numerical calculations that the value of the exponent γ differs from the 1/2 typical of a comb structure and is approximately equal to 1/3."; "In the present paper the example of a comb structure is used to show that the presence of "dead ends" leads to fractional time derivatives."
[^8]: Verified by execution (Python 3.11 with NumPy, 2026-10-29): `bin/python/tree_castle_diffusion.py` item [5], run log `bin/python/tree_castle_diffusion-run.log`. The expected number of horizontal steps on the battlement extended in both directions, from the spectrum of its one-period walk, for `h = 11, 101, 1001, 2001` and `t` up to `10^9`.
