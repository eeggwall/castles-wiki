---
title: "Méndez, Iomin, Campos and Horsthemke (2015) - Mesoscopic description of random walks on combs"
category: Sources
summary: Méndez, Iomin, Campos and Horsthemke study a continuous-time random walk on the regular comb, a one-dimensional backbone with an identical branch of N nodes crossing it at every node, a walker that steps right, left, up or down with probability 1/4 on the backbone and away from the backbone with probability q on a branch, and a waiting time with density φ_0(τ) at every node. Decimating the branches turns the walk into one on the backbone alone with a renormalized waiting-time density φ(s), Equation (2.24). For finite N and a waiting time with finite moments the transport is always normal, with mean backbone waiting time ⟨t⟩ = (1 + 2N) t̄ at q = 1/2, Equation (3.3), and diffusion coefficient D = a²/(2⟨t⟩), Equation (3.7). For N → ∞ the bias decides: normal diffusion for q < 1/2, the subdiffusion x²(t) = a² √(2t/(π t̄)) at q = 1/2, and stochastic localization (a bounded mean-square displacement) for q > 1/2; a power-law waiting time scales each regime by its exponent γ.
tags: [source, paper, comb-model, random-walk, continuous-time-random-walk, anomalous-diffusion, subdiffusion, diffusion-coefficient, mean-square-displacement, stochastic-localization, tree-castle]
sources: [mendez-iomin-campos-horsthemke-2015-random-walks-on-combs]
created: 2026-10-29
updated: 2026-10-29
---

# Méndez, Iomin, Campos and Horsthemke (2015) - Mesoscopic description of random walks on combs

**Source:** `raw/mendez-iomin-campos-horsthemke-2015-random-walks-on-combs.pdf` (git-ignored) and its text layer `raw/mendez-iomin-campos-horsthemke-2015-random-walks-on-combs.txt` (tracked, extracted with `pdftotext -layout`). Vicenç Méndez, Alexander Iomin, Daniel Campos and Werner Horsthemke, "Mesoscopic description of random walks on combs", arXiv:1509.01670v1 [cond-mat.stat-mech], 5 September 2015, https://arxiv.org/abs/1509.01670, published as *Physical Review E* 92, 062112 (2015); the arXiv version was the one read.[^1]
**Date ingested:** 2026-10-29
**Type:** paper (8 pp.)

## Notation used on this page

| paper | meaning | written here as |
|---|---|---|
| `a` | the lattice spacing of the backbone and the branches | the same |
| `N` | the number of nodes of each branch | the same |
| `q` | the probability of a step away from the backbone on a branch | the same |
| `φ_0(τ)`, `t̄` | the waiting-time density at a node and its mean | the same |
| `φ(s)`, `⟨t⟩` | the effective waiting-time density for the backbone, in Laplace space, and its mean | the same |
| `D` | the diffusion coefficient, `x²(t) = 2Dt` | the same |

## Summary

**The comb and the walk.** "The simplest comb model, shown in Fig. 1, is formed by a principal axis, called the backbone, which is a one-dimensional lattice with spacing `a`, and identical branches that cross the backbone perpendicularly at each node." At a node of the backbone the walker jumps right, left, up or down with probability 1/4 each (Figure 2); on a branch it moves away from the backbone with probability `q` and back with probability `1 − q`; at the end of a branch, the node `y = Na`, it is reflected. Before each jump it waits a random time with density `φ_0(τ)`. The paper introduces the comb as the model of anomalous transport in percolation clusters of White and Barma, Weiss and Havlin, and Arkhincheev and Baskin.[^2]

**The backbone walk.** Following the decimation of Kahng and Redner, the time a walker spends between entering a branch and returning to the backbone is treated as extra waiting time at the node where the branch meets the backbone. The balance equations on the branches, solved with the two roots `λ_±` of (2.9) and the reflecting end (2.16)-(2.17), reduce the comb to a walk on the backbone alone, governed by the generalized master equation (2.1) with the effective waiting-time density

```
φ(s)  =  φ_0(s) / ( 2 − (1 − q) φ_0(s)² / (1 − (1 − q) φ_0(s) G(q, φ_0(s))) ),        (2.24)
```

with `G` from (2.21)-(2.22).[^3]

**Finite branches.** For a waiting time with finite moments, `φ_0(s) ≃ 1 − s t̄`, the backbone waiting time has the finite mean

```
⟨t⟩  =  t̄ ( 2(1 − q)^{1−N} q^N + 4q − 3 ) / (2q − 1),        (3.2)
lim_{q → 1/2} ⟨t⟩  =  (1 + 2N) t̄,                              (3.3)
```

and the motion along the backbone is normal diffusion, `x²(t) = 2Dt` with `D = a²/(2⟨t⟩)` (3.7), confirmed by simulations for `N = 2, 3, 6` (Figure 4). "The transport is diffusive for finite `N`, regardless `q` and the specific form of `φ_0(τ)`, as long as it has finite moments." A waiting time with a power-law tail, `φ_0(τ) ∼ τ^{−1−γ}`, makes it anomalous, `x²(t) = a² τ_0 (t/τ_0)^γ/(⟨t⟩ Γ(1 + γ))` (3.8).[^4]

**Infinite branches.** As `N → ∞`, `⟨t⟩` stays finite for `q < 1/2` and grows without bound for `q ≥ 1/2`. With finite moments of `φ_0`, the mean-square displacement for large `t` is (3.13)

```
x²(t)  =  a² (2q − 1)/(4q − 3) · t/t̄,          q < 1/2,
x²(t)  =  a² √(2t/(π t̄)),                       q = 1/2,
x²(t)  =  a² q/(2q − 1) · (1 − e^{−αt}),         q > 1/2,
```

with `α = (2q − 1)²/((4q² − 3q + 1) t̄)` (3.14). "For `q = 1/2`, we obtain the well known result of subdiffusive transport with the MSD `∼ √t`." For `q > 1/2` the walker is trapped in the branches and the mean-square displacement stays bounded, stochastic localization; for `q < 1/2` advection toward the backbone gives normal diffusion. Simulations with `N = 10³` confirm the three behaviors (Figure 6). A power-law waiting time gives `t^γ` for `q < 1/2`, `t^{γ/2}` for `q = 1/2`, and localization again for `q > 1/2` (3.15)-(3.16).[^5]

## The castle reading

At `q = 1/2` with one time unit per step, `φ_0(τ) = δ(τ − 1)`, the walk is the simple random walk on the comb: every node moves to each neighbor with the same probability, and the end of a branch steps back. Equations (3.3) and (3.7) then give `x²(t) = 2Dt = t/(1 + 2N)` with `a = t̄ = 1`, and `1/(1 + 2N)` is the share of backbone edges among the `1 + 2N` edges of one period of the comb. On a tree castle the same count gives `(w − 1)/(n − 1)`, the stationary probability that a step is horizontal ([[tree-castle-diffusion](pages/tree-castle-diffusion.md)]). The castle teeth stand on one side and on every other backbone cell at most, and they have at most `h − 1` cells, so every tree castle is in the finite-branch case: normal diffusion at long times. The infinite-branch law `√(2t/π)` is reproduced by the walk on this comb with branches of 4000 nodes up to `t = 10^5`.[^6]

## Key Takeaways

- **Finite branches always give normal diffusion**, with `⟨t⟩ = (1 + 2N) t̄` and `D = a²/(2⟨t⟩)` for the unbiased walk.[^4]
- **Infinite unbiased branches give `x²(t) = a² √(2t/(π t̄))`**, the comb's subdiffusion with exponent 1/2.[^5]
- **Bias away from the backbone localizes**: for `q > 1/2` the mean-square displacement stays bounded.[^5]
- **The branches become a waiting time**: the comb reduces to a walk on the backbone with the waiting-time density (2.24).[^3]

## Entities & Concepts

- [[tree-castle-diffusion](pages/tree-castle-diffusion.md)] - the tree castles as combs; the coefficient (3.7) at `q = 1/2` is the share of backbone edges, and the castle version of that share is `(w − 1)/(n − 1)`.

## Relation to Other Wiki Pages

[[arkhincheev-baskin-1991-comb-model](pages/arkhincheev-baskin-1991-comb-model.md)] is reference [12] here, the continuum comb with its order-1/2 equation. [[yuste-abad-baumgaertner-2016-random-comb-model](pages/yuste-abad-baumgaertner-2016-random-comb-model.md)] cites this paper and computes the same kind of coefficient for teeth of random length. [[pach-tardos-2013-range-of-random-walk-on-comb](pages/pach-tardos-2013-range-of-random-walk-on-comb.md)] studies the simple random walk on the comb with infinite teeth on both sides, the `N → ∞`, `q = 1/2` case.

## Footnotes

[^1]: [[mendez-iomin-campos-horsthemke-2015-random-walks-on-combs](pages/mendez-iomin-campos-horsthemke-2015-random-walks-on-combs.md)] p.1 L1-L25 [synthesis] - the title "Mesoscopic description of random walks on combs", the authors "Vicenç Méndez, Alexander Iomin, Daniel Campos, and Werner Horsthemke", their affiliations (Universitat Autònoma de Barcelona, Technion, Southern Methodist University), "arXiv:1509.01670v1 [cond-mat.stat-mech] 5 Sep 2015" and the abstract. The journal reference is from the arXiv abstract page, https://arxiv.org/abs/1509.01670 (read 2026-10-29), "Related DOI: https://doi.org/10.1103/PhysRevE.92.062112".
[^2]: [[mendez-iomin-campos-horsthemke-2015-random-walks-on-combs](pages/mendez-iomin-campos-horsthemke-2015-random-walks-on-combs.md)] §I-II pp.1-3 L53-L57, L97-L144, L171-L178 and the references L572-L580 [synthesis] - "The comb model was introduced to understand anomalous transport in percolation clusters [10–12]."; "The simplest comb model, shown in Fig. 1, is formed by a principal axis, called the backbone, which is a one-dimensional lattice with spacing a, and identical branches that cross the backbone perpendicularly at each node."; "the walker located at the ith node of the backbone may jump to the right, left, up or down with probability 1/4. We assume that the walker moves forward (away from the backbone) along the branches with probability q and back to the backbone with probability 1 − q."; "A special situation occurs at the end of the branches, where we have to impose reflecting boundary conditions"; references [10] S. R. White and M. Barma (1984), [11] G. H. Weiss and S. Havlin (1986), [12] V. Arkhincheev and E. Baskin (1991).
[^3]: [[mendez-iomin-campos-horsthemke-2015-random-walks-on-combs](pages/mendez-iomin-campos-horsthemke-2015-random-walks-on-combs.md)] §II pp.2-4 L56-L65, L69-L291 [synthesis] - "Kahng and Redner provided a mesoscopic, probabilistic description of random walks on combs, by using the successive decimation of the discrete-time Master equation"; "The time spent by the walker between its entry into the branches and its return to the backbone for the first time is treated as a contribution to the effective waiting time at the node where the branch crosses the backbone."; Equations (2.1)-(2.24); "The Laplace inversion of (2.24) yields φ(τ), which incorporates the dynamics along the branches and can be understood as the effective waiting time PDF for a walker moving along the backbone only."
[^4]: [[mendez-iomin-campos-horsthemke-2015-random-walks-on-combs](pages/mendez-iomin-campos-horsthemke-2015-random-walks-on-combs.md)] §III.A pp.4-5 L296-L340 [synthesis] - Equations (3.1)-(3.8); "If the random walk inside the branches is isotropic, q = 1/2, one obtains by the L'Hopital's rule from (3.2) lim_{q→1/2} ⟨t⟩ = (1 + 2N) t̄."; "the MSD along the backbone corresponds to normal diffusion x²(t) = 2Dt. The diffusion coefficient is given by D = a²/(2⟨t⟩)"; "The transport is diffusive for finite N, regardless q and the specific form of φ0(τ), as long as it has finite moments."; Figure 4 for N = 2, 3, 6.
[^5]: [[mendez-iomin-campos-horsthemke-2015-random-walks-on-combs](pages/mendez-iomin-campos-horsthemke-2015-random-walks-on-combs.md)] §§III.B-IV pp.5-7 L341-L532 [synthesis] - Equations (3.9)-(3.17); "For q = 1/2, we obtain the well known result of subdiffusive transport with the MSD ∼ √t."; "The walker is effectively trapped inside the branches, and stochastic localization (diffusion failure) occurs, x²(∞) < ∞"; Figure 6, "Symbols are the results of numerical simulations with N = 10³."; the conclusion "If N is finite and φ0(τ) has finite moments, both ⟨t⟩ and D are derived exactly ... In this case the transport is always normal diffusion."
[^6]: Verified by execution (Python 3.11 with NumPy, 2026-10-29): `bin/python/tree_castle_diffusion.py` item [6], run log `bin/python/tree_castle_diffusion-run.log`. The simple random walk on one period of this comb (the two branches folded into one) for `N = 2, 3, 6, 20`: the fraction of horizontal steps at `t = 10^8` equals `1/(1 + 2N)` to `10^{−6}`; for `N = 4000`, the slope of the expected number of horizontal steps in `√t` between `t = 10^4` and `10^5` is `0.79788`, against `√(2/π) = 0.79788`.
