---
title: "Abelian sandpile model (Chau, 1993)"
category: Sources
summary: A three-page Physical Review E Rapid Communication in the abelian sandpile programme. It states the model in Dhar's form (toppling h_i → h_i − Δ_ji, det Δ recurrent states, two-point function G = Δ⁻¹) and proposes a method for higher-order correlation functions and the avalanche-size distribution. The wiki records the paper's framing and its reference list, which maps the early abelian sandpile literature (Dhar, Creutz, Dhar-Majumdar, Lee-Liang-Tzeng, Ruelle-Sen, Markošová-Markoš, Chau-Cheng); its computational method is not summarized here.
tags: [paper, source, sandpile, abelian-sandpile, self-organized-criticality, bibliography, correlation-function, avalanche]
sources: [chau-1993-abelian-sandpile-model]
created: 2026-09-27
updated: 2026-09-27
---

# Abelian sandpile model (Chau, 1993)

**Source:** `raw/chau-1993-abelian-sandpile-model.pdf` (a scan with no text layer, git-ignored; cited by page).
**Publication:** H. F. Chau, "Abelian sandpile model", *Physical Review E* **47** (1993) R3815-R3817, Rapid Communications; received 5 January 1993. University of Illinois at Urbana-Champaign.[^1]
**Date ingested:** 2026-09-27
**Type:** paper (PDF, 3 pp.)

## Scope of this page

This page records the paper's framing and its references. The method it proposes (conditional correlation functions and an algorithm for the avalanche-size distribution) is not summarized on the wiki.

## Framing

The paper places itself in the line of work that began with Bak, Tang and Wiesenfeld's self-organized criticality. Dhar showed that a finite cellular automaton whose toppling is triggered by local height is described by a finite abelian group, and models of this type are collectively called Abelian sandpile models (ASMs).[^2] In these models the total number of self-organized critical states and the two-point correlation function can be calculated exactly. Other quantities had been found by several groups, extensions to other triggering conditions existed, and the relation between the ASM, percolation and spanning trees had begun to be explored.[^2] The stated aim is an exact and efficient way to compute correlation functions to any finite order, and from them the distribution of avalanche sizes, which the abstract presents as more efficient and accurate than simulation.[^3]

The model is stated in Dhar's form. There are `N` cells with local heights (sometimes real numbers), a unit of sand is added at a random cell with probability `μ(i)`, and a cell above its triggering level topples by `h_i → h_i − Δ_ji` for all `i` (eq. 1).[^4] Following Dhar, the number of self-organized critical states is `det Δ`, which for real heights is the volume of the phase space of recurrent states, and the two-point function, the average number of topplings at `j` caused by a grain added at `i`, is `G_ij = Δ⁻¹_ij`.[^4] The toppling is written with `Δ_ji`, the transpose of Dhar's `z_j → z_j − Δ_ij`, which makes no difference for a symmetric castle Laplacian ([[castle-notation](pages/castle-notation.md)]).

## References as a map of the early literature

The reference list is a compact guide to the abelian sandpile papers of 1987-1992, most not yet on the wiki:[^5]

| ref. | work | on the wiki |
|---|---|---|
| [1] | Bak, Tang and Wiesenfeld, *Phys. Rev. Lett.* 59 (1987) 381; *Phys. Rev. A* 38 (1988) 364 | cited on [[castle-avalanches](pages/castle-avalanches.md)] |
| [2] | Dhar, *Phys. Rev. Lett.* 64 (1990) 1613 | [[dhar-1990-self-organized-critical-sandpile](pages/dhar-1990-self-organized-critical-sandpile.md)] |
| [3] | Creutz, *Comput. Phys.* 5 (1991) 198 | not yet |
| [4] | Dhar and Majumdar, *J. Phys. A* 23 (1990) 4333; Lee, Liang and Tzeng, *Phys. Rev. Lett.* 67 (1991) 1479 and 68 (1992) 1442(E); Lee and Tzeng, *Phys. Rev. A* 45 (1992) 1253; Ruelle and Sen, *J. Phys. A (Lett.)* 25 (1992) L1257 | not yet |
| [5] | Gabrielov (unpublished) | - |
| [6] | Chau and Cheng, *Phys. Rev. A* 46 (1992) 2981, and unpublished | not yet |
| [7] | Markošová and Markoš, *Phys. Rev. A* 46 (1992) 3531; Peng, *J. Phys. A* 25 (1992) 5279; Chau and Cheng (unpublished) | not yet |
| [8] | Chau and Cheng, *Phys. Lett. A* 157 (1991) 103 | [[chau-cheng-1991-deterministic-soc-sandpile](pages/chau-cheng-1991-deterministic-soc-sandpile.md)] |
| [9] | Grimmett, *Percolation* (Springer, 1989) | not yet |

In the text, [2, 3] support the exact count of critical states and the two-point function, [4] the other exactly computed quantities, [5, 6] the extensions to other toppling triggers, and [7] the relation to percolation and spanning trees.[^2] [2] and [8] are also cited for elementary row operations and the equivalence of toppling rules.[^6]

## Relation to Other Wiki Pages

- [[dhar-1990-self-organized-critical-sandpile](pages/dhar-1990-self-organized-critical-sandpile.md)] - the model and results the paper builds on.
- [[chau-cheng-1991-deterministic-soc-sandpile](pages/chau-cheng-1991-deterministic-soc-sandpile.md)] - the companion paper on equivalent toppling rules (its ref. [8]).
- [[sandpile-group](pages/sandpile-group.md)] / [[castle-avalanches](pages/castle-avalanches.md)] - the castle sandpile pages; the reference table above lists the sources that would close their remaining gaps (the spanning-tree correspondence and the identity element).
- [[dhar-ruelle-sen-verma-1995-algebraic-aspects](pages/dhar-ruelle-sen-verma-1995-algebraic-aspects.md)] - now on the wiki, closing the "not yet" gap in ref. [4] above (Ruelle and Sen 1992, the direct predecessor of this 1995 paper's algebraic treatment).

## Footnotes

[^1]: raw/chau-1993-abelian-sandpile-model.pdf p.R3815 title block - "Abelian sandpile model", "H. F. Chau", "Department of Physics, University of Illinois at Urbana-Champaign", "(5 January 1993)"; *Physical Review E* volume 47, number 6, June 1993.
[^2]: raw/chau-1993-abelian-sandpile-model.pdf p.R3815 first paragraph [synthesis] - self-organized criticality from Bak, Tang and Wiesenfeld [1]; "Dhar pointed out that the finite cellular-automata type of model with toppling triggered by local height can be described by a finite Abelian group [2]"; "Both the total number of self-organized critical states and the two-point correlation function can be calculated exactly in these models [2,3]"; other quantities [4], other triggering conditions [5,6], and "the relation between the ASM, percolation, and spanning trees is also explored [7]".
[^3]: raw/chau-1993-abelian-sandpile-model.pdf p.R3815 abstract and second paragraph [synthesis] - "A systematic and simple method to find the correlation function of the Abelian sandpile model up to any finite order is developed", with "an algorithm for evaluating the distribution function of the avalanche size P(s)", described as "more efficient (and accurate) than the numerical simulation".
[^4]: raw/chau-1993-abelian-sandpile-model.pdf p.R3815 third paragraph [synthesis] - cells with local heights `h_i` "(or sometimes real numbers)", addition according to a probability distribution `μ(i)`, toppling `h_i → h_i − Δ_ji` (eq. 1); "the total number of self-organized critical states in an ASM is given by det Δ", interpreted for real heights "as the volume of the phase space of the recurrence states [5,6]"; `G_ij = Δ⁻¹_ij` [2].
[^5]: raw/chau-1993-abelian-sandpile-model.pdf p.R3817 References [1]-[9].
[^6]: raw/chau-1993-abelian-sandpile-model.pdf p.R3816 [synthesis] - "Further discussions of the role of elementary row operations on the ASM and the equivalence of toppling rules can be found elsewhere [2,8]."
