---
title: "On the Group of a Sandpile (Rossin, Algorithms Seminar 2000)"
category: Sources
summary: Summary (by D. Gouyou-Beauchamps) of Dominique Rossin's 16 October 2000 talk at the INRIA Algorithms Seminar - the abelian sandpile on a multigraph with a sink, recurrent configurations as a finite abelian group whose structure does not depend on the choice of sink, the identity as δ ⊕ (δ ⊕ δ)‾ from the fullest stable pile δ, the Tutte polynomial T_G(1,y) as the grain-count generating function of the recurrent configurations, the toppling ideal and its Gröbner basis (reduced monomials in bijection with recurrent configurations, giving an algorithm for the identity), and the worked example of the 2×2 grid with every cell joined twice to the sink, group Z/24 × Z/8 of order 192 - the planar dual of the castle (3,3,3). Also the wiki's route to Bak-Tang-Wiesenfeld (1987), Dhar (1990), Dhar-Ruelle-Sen-Verma (1995) and Cori-Rossin (2000).
tags: [source, sandpile, abelian-sandpile, critical-group, chip-firing, identity-element, tutte-polynomial, groebner-basis, toppling-ideal, planar-dual, cori-rossin, dhar, bak-tang-wiesenfeld, seminar-summary, inria]
sources: [rossin-2000-group-of-a-sandpile]
created: 2026-09-27
updated: 2026-09-27
---

# On the Group of a Sandpile (Rossin, Algorithms Seminar 2000)

**Source:** https://algo.inria.fr/seminars/sem00-01/rossin.html (cached as `raw/rossin-2000-group-of-a-sandpile.md`, a plain-text copy with the page's symbol-font characters restored from context)
**Publication:** Dominique Rossin (LIX, École polytechnique), "On the Group of a Sandpile", Algorithms Seminar (INRIA), 16 October 2000; summary by Dominique Gouyou-Beauchamps.
**Date ingested:** 2026-09-27
**Type:** seminar summary (about 5 pages, 13 references)

## Summary

The talk sets up the abelian sandpile on a connected multigraph with one distinguished vertex, the sink, which absorbs every grain that reaches it. A vertex holding at least as many grains as its degree topples, passing one grain along each edge; every configuration stabilizes to a unique stable configuration, and the number of topplings does not depend on the order.[^1] A configuration is recurrent when it is stable and comes back after sand is added; the recurrent configurations, added cell by cell and stabilized, form a finite abelian group whose structure does not depend on which vertex is the sink. The simplest recurrent configuration is `δ`, every vertex one grain short of toppling, and the identity of the group is `δ ⊕ (δ ⊕ δ)‾`, where the bar sends a stable pile `u` to `δ − u`.[^2] The Tutte polynomial enters through `T_G(1, y)`, which counts recurrent configurations by their number of grains.[^3]

The main body is algebraic. A configuration becomes a monomial, a toppling becomes a binomial, and the toppling polynomials together with `x_sink − 1` generate the toppling ideal, whose quotient has dimension equal to the order of the group. For a "toppling order" (grevlex with vertices ordered by distance to the sink) the toppling polynomials of all vertex subsets form a Gröbner basis, the well-connected subsets form a minimal one, and the map `u ↦ δ − u` is a bijection from the reduced monomials to the recurrent configurations. That yields an algorithm for the identity: start from `δ`, perform set topplings on well-connected subsets until none applies, then replace each count `n_i` by `d_i − n_i`.[^4] The talk says the identity "presents fractal aspects that we are not able yet to explain".[^5]

Two examples close it. The second is the `2 × 2` grid of four cells, each joined to the sink by two edges, whose group is `Z/24 × Z/8`, of order 192, with two generators.[^6] The reference list carries the classical sources: Bak, Tang and Wiesenfeld's 1987 paper introducing the model, Dhar's 1990 paper, Dhar, Ruelle, Sen and Verma's 1995 paper on the group structure, and Cori and Rossin's 2000 paper on the sandpile group of dual graphs, as well as Biggs's chip-firing and the critical group.[^7]

## Key Takeaways

- **The sink does not matter for the group.** The group structure is independent of the sink vertex, which is what lets the wiki's sink model fix the bottom-left cell without loss.[^2]
- **The identity recipe.** `Id = δ ⊕ (δ ⊕ δ)‾` from the fullest stable pile `δ` is the recipe used on every Sandcastles page, written there as `stab(2m − stab(2m))`.[^2]
- **The dual of the castle `(3, 3, 3)`.** The talk's `2 × 2` grid with every cell joined twice to the sink is exactly the planar dual of the `3 × 3` castle: its four vertices are the castle's four `2 × 2` blocks, joined where blocks share an edge, and each corner block meets the outer face along two edges. The talk's group, `Z/24 × Z/8` of order 192, is the sink-model group the wiki computes for `(3, 3, 3)` from the cells, `Z/8 × Z/24` with 192 recurrent piles - an outside instance of the dual-graph theorem the tide block rule rests on.[^6]
- **Tutte and Gröbner.** `T_G(1, y)` generates recurrent configurations by grain count, and the toppling ideal's Gröbner basis gives a second algorithm for the identity. Neither has been run on castles yet.[^3][^4]
- **One line to read with care.** The summary writes the group as "the product `G = Π_{i=1}^{n} Z/d_i Z`", having used `d_i` for vertex degrees. Read with degrees the line is false: the `2 × 2` square castle has four vertices of degree 2, so the product would have order 8, while its group is `Z/4` (4 spanning trees). The line is almost certainly the standard invariant-factor decomposition written with a reused letter, and nothing on the wiki is cited to it.[^8]

## Entities & Concepts

- [[sandpile-group](pages/sandpile-group.md)] - the game, the group, sink independence, and the planar-dual block matrices in both models.
- [[sandpile-identity](pages/sandpile-identity.md)] - the identity element and its recipe.
- [[sandpile-census](pages/sandpile-census.md)] - the groups of every castle to 16 cells.
- [[sandcastle-clock](pages/sandcastle-clock.md)] - adding one grain as adding in the group.
- [[castle-avalanches](pages/castle-avalanches.md)] - the Bak-Tang-Wiesenfeld model and Dhar's theorem.
- [[sandcastle-seminar](pages/sandcastle-seminar.md)] - the seminar walk-through of all of the above on one castle.
- [[castle-graph](pages/castle-graph.md)] - the castle graph and its planar dual.

## Relation to Other Wiki Pages

This is the first ingested source for the Sandcastles pages, which until now rested on a Wikipedia summary and on papers the wiki has not read. It confirms, from a primary-literature summary, the three facts those pages use most: sink independence, the identity recipe, and the dual-graph theorem (through its reference to Cori and Rossin and through its `2 × 2` grid example, which is the dual of the castle `(3, 3, 3)`). It does not treat the wiki's tide model, the castle-specific block rules, clocks, or avalanche statistics; those remain the wiki's own computations. It opens two threads the wiki has not followed: the Tutte polynomial of a castle graph evaluated at `x = 1`, and the Gröbner-basis algorithm for the identity. The papers in its reference list are cited on the Sandcastles pages as known through this summary, not read, except three that are now ingested: reference [9], Dhar, Ruelle, Sen and Verma ([[dhar-ruelle-sen-verma-1995-algebraic-aspects](pages/dhar-ruelle-sen-verma-1995-algebraic-aspects.md)]), which computes the `2 × 2` grid's group itself; reference [1], whose full-length companion by Bak, Tang and Wiesenfeld is [[bak-tang-wiesenfeld-1988-self-organized-criticality](pages/bak-tang-wiesenfeld-1988-self-organized-criticality.md)]; and Dhar 1990 ([[dhar-1990-self-organized-critical-sandpile](pages/dhar-1990-self-organized-critical-sandpile.md)]).

## Footnotes

[^1]: [[rossin-2000-group-of-a-sandpile](pages/rossin-2000-group-of-a-sandpile.md)] §1-2 [synthesis] L17-21, L31 - multigraph with a sink numbered `n` that collects all grains; toppling decreases a vertex by its degree and increases each neighbour; "Moreover this configuration is unique, and the number of topplings is independent of the way in which û is obtained from u".
[^2]: [[rossin-2000-group-of-a-sandpile](pages/rossin-2000-group-of-a-sandpile.md)] §2 L33, L37-39 - "The simplest example of a recurrent configuration is δ = (d_1 − 1, d_2 − 1, ..., d_{n−1} − 1, 0)"; "the group structure does not depend on the sink choice in the graph G"; "Then the identity of the sandpile group is Id = δ ⊕ (δ ⊕ δ)‾".
[^3]: [[rossin-2000-group-of-a-sandpile](pages/rossin-2000-group-of-a-sandpile.md)] §2 L35 - "Then T_G(1,y) is the the generating function (a polynomial) of the recurrent configurations according to the number of sand grains."
[^4]: [[rossin-2000-group-of-a-sandpile](pages/rossin-2000-group-of-a-sandpile.md)] §3 [synthesis] L45-80 - toppling ideal generated by `x_n − 1` and the toppling polynomials; Theorems 1-3 (Gröbner basis for a toppling order, minimal basis from well-connected sets, bijection `Φ(u) = δ − u` between reduced monomials and recurrent configurations); Proposition 1 and the identity algorithm at L80.
[^5]: [[rossin-2000-group-of-a-sandpile](pages/rossin-2000-group-of-a-sandpile.md)] Abstract L11 - "This element presents fractal aspects that we are not able yet to explain."
[^6]: [[rossin-2000-group-of-a-sandpile](pages/rossin-2000-group-of-a-sandpile.md)] §4 L92-94 - "Our second example is the 2 × 2 grid consisting of 4 cells, each connected twice to the sink. The sandpile group of this grid ... is the product of two cyclic group of orders 24 and 8"; "the order of the group is 192". The identification with the dual of `(3, 3, 3)` and the comparison with the wiki's `Z/8 × Z/24` (192 recurrent piles, pinned in the Snippet of [[sandpile-group](pages/sandpile-group.md)]) are the wiki's own.
[^7]: [[rossin-2000-group-of-a-sandpile](pages/rossin-2000-group-of-a-sandpile.md)] References [synthesis] L98-116 - [1] Bak, Tang, Wiesenfeld, PRL 59 (1987) 381-384; [3] Biggs, J. Algebraic Combin. 9 (1999) 25-45; [5] Cori, Rossin, Europ. J. Combin. 21 (2000) 447-459; [9] Dhar, Ruelle, Sen, Verma, J. Phys. A 28 (1995) 805-831; [10] Dhar, PRL 64 (1990) 1613-1616.
[^8]: [[rossin-2000-group-of-a-sandpile](pages/rossin-2000-group-of-a-sandpile.md)] §2 L37 - "this group is equal to the product G = Π_{i=1}^{n} Z/d_i Z", with `d_i` introduced as the degree at L17. The counterexample `(2, 2)` (group `Z/4`) is pinned on [[sandpile-group](pages/sandpile-group.md)]; the reading as invariant factors is the wiki's.
