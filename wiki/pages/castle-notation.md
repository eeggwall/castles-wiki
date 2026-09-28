---
title: Castle notation - castles, towers, and the parity term
category: Concepts
summary: The wiki's symbol conventions in one place, including the sandpile symbols (the reduced Laplacian L̃, Dhar's Δ, K(G), L̃⁻¹, a_v, avalanche statistics) the block-weighted and Motzkin-path layer (block weight t, M_k(t), the KMS matrix K(ρ), semi-perimeter s, B(x, y), Motzkin-path castles), and the area-grading layer (q, z, E(q, z), the q-Bessel N(q)/M(q), J_0, J_1, Π). Castle quantities are written width first, F(w, h); tower quantities are written tower height first, T(k, L) and P(k, L), where a tower sits on the castle's bottom row, so tower height k = castle height h − 1. T is the unsigned tower count (k+1)^L, P the signed ("parity") tower count Σ(−1)^blocks, and the parity term of F is S(w, h) = P(h−2, w) − P(h−1, w), so F(w, h) = [h^w − (h−1)^w − P(h−1, w) + P(h−2, w)]/2. P(0, L) = 1 is the trivial case; P(1, ·) is the parity ingredient for castles of height up to 2. Also lists the other things the letters P and T mean on the wiki, so the collisions are visible.
tags: [concept, castle, notation, reference, signed-tower-count, castle-sign, pedagogy]
sources: [project-euler-502-solution, project-euler-502-representations]
created: 2026-09-26
updated: 2026-09-27
---

# Castle notation - castles, towers, and the parity term

## Two kinds of object, two argument orders

The wiki counts two related objects, and they are indexed differently.

- A **castle** has width `w` and height `h` (every column at least 1, some column exactly `h`). Castle quantities put **width first**: `F(w, h)`.
- A **tower** is what sits on top of a castle's full-width bottom row. It is a row of column heights `c_1, …, c_L ∈ {0, …, k}` over a base of length `L`, where 0 means "nothing above the bottom row". Tower quantities put **tower height first**: `T(k, L)`, `P(k, L)`.[^1]

A tower of height `≤ k` plus the bottom row is a castle of height `≤ k + 1`. So the translation between the two is always

```
tower height  k  =  h − 1        (castle height h)          base length  L  =  w        (castle width w)
```

## The core symbols

| symbol | meaning | arguments |
|---|---|---|
| `F(w, h)` | castles of width `w`, height exactly `h`, with an **even** number of blocks (the Project Euler 502 count) | width, height |
| `odd(w, h)` | the same with an odd number of blocks | width, height |
| `A(w, h)` | all castles of width `w`, height exactly `h`: `h^w − (h−1)^w` | width, height |
| `T(k, L)` | all towers of height `≤ k` on a base of length `L`: `(k + 1)^L` | tower height, base length |
| `P(k, L)` | the **signed** tower count `Σ (−1)^{blocks}` over the same towers: the parity ingredient | tower height, base length |
| `S(w, h)` | the **parity term** of `F`: `F(w, h) − odd(w, h) = P(h−2, w) − P(h−1, w)` | width, height |
| `P_even(k, L)`, `P_odd(k, L)` | `P` restricted to towers whose last column is even / odd ([[tower-parity-sectors](pages/tower-parity-sectors.md)]) | tower height, base length |
| `char_k` | characteristic polynomial of the recurrence of `P(k, ·)` in `L` | tower height |

T is the **tower** count and P is the **parity** (signed) version of it. Both are tower quantities, so they are indexed by tower height.[^1]

## The one formula where both orders meet

```
F(w, h)  =  [ A(w, h) + S(w, h) ] / 2
         =  [ h^w − (h−1)^w  −  P(h−1, w)  +  P(h−2, w) ] / 2
```

`A` and `F` are castle quantities (width first), and the two `P` terms are tower quantities (tower height first) evaluated at tower heights `h − 1` and `h − 2` and base length `w` ([[castle-counting-formula](pages/castle-counting-formula.md)]).

**Worked case `h = 2`.** `P(0, L) = 1` (the only tower of height 0 is empty, with no blocks), so

```
F(w, 2)  =  [ 2^w − 1 − P(1, w) + 1 ] / 2  =  ( 2^w − P(1, w) ) / 2
```

and at `w = 2`, `P(1, 2) = −2` gives `F(2, 2) = (4 + 2)/2 = 3`, the three castles `(1,2), (2,1), (2,2)`.[^2] This is why `P(1, ·)` is interesting: it is the parity ingredient for castles of height up to 2 (towers are binary strings, and each run of 1s is one block on the second row), not "castles of height 1".

## Trivial and first cases

| tower height `k` | castle heights it serves | `P(k, L)` |
|---|---|---|
| 0 | the bottom row alone (castle height 1) | `1` for every `L` |
| 1 | castles of height `≤ 2` | `1, 0, −2, −4, −4, 0, 8, 16, …` = `Re((1+i)^{L+1})` |
| 2 | castles of height `≤ 3` | `1, 1, 3, 9, 19, 33, 59, 121, …` |

## Reading conventions

- **"Height" means castle height `h`** unless the sentence is about towers. Phrases like "towers of height `≤ 1`" or "`P(1, L)`" refer to tower height and are glossed with the castle height where it matters.
- **`P(k, w)`** on a few pages ([[fractional-width-and-height](pages/fractional-width-and-height.md)], [[mod-9-equidistribution](pages/mod-9-equidistribution.md)]) is `P(k, L)` evaluated at base length `L = w`, the castle width, exactly as it appears in the formula for `F`.
- **Generating functions.** The source derivation also writes `P_k` and `E_k` for the tower generating functions in `x` (the sums over `L`), not for single values ([[castle-counting-formula](pages/castle-counting-formula.md)], [[generalized-dyck-grammar](pages/generalized-dyck-grammar.md)]).

## Sandpile symbols

The sandpile pages run grains on the castle graph (cells as vertices, edge-sharing cells joined) with a **sink** where grains vanish: one chosen cell in the **sink model**, or the whole bottom row, the ground, in the **tide model** ([[sandpile-group](pages/sandpile-group.md)]). Heights count grains from 0, and a cell topples when it holds at least as many grains as it has neighbours.

| symbol | meaning | where |
|---|---|---|
| `L` | the Laplacian `D − A` of the castle graph: `D` the diagonal of cell degrees, `A` the adjacency matrix (not the castle count `A(w, h)`) | [[hear-the-shape-seminar](pages/hear-the-shape-seminar.md)], [[sandpile-group](pages/sandpile-group.md)] |
| `L̃` | the **reduced Laplacian**: `L` with the sink's rows and columns deleted (one cell's row and column in the sink model, every bottom-row cell's in the tide model, where each remaining cell keeps its full degree). Toppling cell `v` subtracts row `v` of `L̃` | [[sandpile-group](pages/sandpile-group.md)], [[castle-avalanches](pages/castle-avalanches.md)] |
| `Δ` | Dhar's toppling matrix of a general abelian sandpile; for a castle `Δ = L̃`. Stable heights differ by a shift between sources: Dhar `1..Δ_vv`, Chau-Cheng `≤ 0` (critical height moved to 0), the wiki `0..deg − 1`. Chau 1993 writes toppling as `h_i → h_i − Δ_ji`, the transpose, which is the same for a symmetric castle `L̃` | [[dhar-1990-self-organized-critical-sandpile](pages/dhar-1990-self-organized-critical-sandpile.md)] |
| `K(G)`, `K` | the sandpile group `Z^{n−1} / L̃ Z^{n−1}` of the recurrent configurations, of order `det L̃` (the number of spanning trees) | [[sandpile-group](pages/sandpile-group.md)], [[sandpile-census](pages/sandpile-census.md)] |
| `L̃⁻¹` | expected topplings: entry `(v, u)` is the mean number of topplings at `u` caused by a grain at `v` in the steady state (Dhar's `G = Δ⁻¹`); its row means give the mean avalanche | [[castle-avalanches](pages/castle-avalanches.md)], [[dhar-1990-self-organized-critical-sandpile](pages/dhar-1990-self-organized-critical-sandpile.md)] |
| `a_v` | Dhar's grain operator "add a grain at `v`, then stabilize"; the operators commute, and the order of `a_v` is the clock period | [[sandcastle-clock](pages/sandcastle-clock.md)], [[dhar-1990-self-organized-critical-sandpile](pages/dhar-1990-self-organized-critical-sandpile.md)] |
| completely deterministic | every grain operator acts the same on the recurrent configurations, `a_v = a_u`; for castles this happens only when `K` is trivial | [[chau-cheng-1991-deterministic-soc-sandpile](pages/chau-cheng-1991-deterministic-soc-sandpile.md)], [[sandpile-group](pages/sandpile-group.md)] |
| `stab(·)` | stabilization: topple until no cell is unstable | [[sandpile-identity](pages/sandpile-identity.md)] |
| `ln det L̃` | the entropy of the steady state (uniform on `det L̃` recurrent piles), written in words on the wiki, not as `S` | [[sandpile-group](pages/sandpile-group.md)] |

**Avalanche statistics.** Dynamical quantities are written in words, because the founding papers' letters (`T`, `D`, `F`, `S`, `L`) are core castle symbols here.

| written as | meaning | the founding papers wrote |
|---|---|---|
| avalanche **size** | number of topplings caused by one grain | `s` (BTW), `⟨T⟩` for its mean (Dhar) |
| avalanche **duration** | number of rounds, one round toppling every unstable cell at once | `T` (BTW, "lifetime"), `τ` (Dhar) |
| size distribution | probability of an avalanche of a given size; `∼ size^{−τ}` | `D(s)` (BTW) |
| weighted duration distribution | duration distribution weighted by size/duration; `∼ duration^{−α_w}` | `D(T)`, exponent `α` (BTW) |
| toppling rate, power spectrum | topplings per round over time, and its spectrum `∼ frequency^{−β}` (1/f noise when `β ≈ 1`) | `F(t)`, `S(f)` (BTW) |
| `τ`, `α_w`, `β`, `γ_g` | size exponent, weighted-duration exponent, spectral exponent, growth exponent (size `∼` duration`^{1+γ_g}`) | `τ`, `α`, `β`, `γ` (BTW) |
| `d`, `d_f` | lattice dimension, fractal dimension of avalanches | `D`, `d` (BTW); `d` (Dhar) |
| `ℓ` | side of a square (or `ℓ × ℓ` rectangle) lattice | `N`, `L` (BTW), `L` (Dhar) |
| grains, threshold `deg` | grains on a cell, toppling when a cell holds at least `deg` | `z`, `z_c` (BTW, read as a slope), `z_i ≤ Δ_ii` (Dhar) |

Sources: [[bak-tang-wiesenfeld-1988-self-organized-criticality](pages/bak-tang-wiesenfeld-1988-self-organized-criticality.md)], [[dhar-1990-self-organized-critical-sandpile](pages/dhar-1990-self-organized-critical-sandpile.md)], [[castle-avalanches](pages/castle-avalanches.md)].

## Weights, transfer matrices, and path models

The block weight, the semi-perimeter, and the Motzkin-path readings add a second layer of symbols. They keep the two argument orders above: tower quantities are indexed by tower height `k`, castle quantities by width and castle height.

| symbol | meaning | where |
|---|---|---|
| block weight `t` | a factor `t` per block, so a tower contributes `t^blocks`. The weighted sum over towers is `T(k, L)` at `t = 1`, `P(k, L)` at `t = −1`, and the roots-of-unity `P_j(k, L)` at `t = ω^j`. It has no symbol of its own: `P` stays the signed count | [[castle-sign-kms-matrix](pages/castle-sign-kms-matrix.md)], [[parity-via-roots-of-unity](pages/parity-via-roots-of-unity.md)] |
| `M_k(t)` | block-weighted tower transfer matrix on tower heights `0, …, k` (size `k + 1`, the castle height bound), entry `t^max(0, b − a)` (rises); the weighted tower sum is `e_0ᵀ M_k(t)ᴸ 𝟙` | [[castle-sign-kms-matrix](pages/castle-sign-kms-matrix.md)] |
| `M_k` | the signed transfer matrix of [[tower-parity-sectors](pages/tower-parity-sectors.md)], entry `(−1)^max(0, a − b)` (descents): the transpose of `M_k(−1)` | [[tower-parity-sectors](pages/tower-parity-sectors.md)] |
| `K(ρ)` | the Kac-Murdock-Szegő matrix `ρ^|a − b|`, with `ρ = √t`: `D_ρ M_k(ρ²) D_ρ⁻¹ = K(ρ)`; signed is `K(i)` | [[castle-sign-kms-matrix](pages/castle-sign-kms-matrix.md)] |
| `A_path`, `E_∂` | adjacency matrix of the path on the heights, and `diag(1, 0, …, 0, 1)`; `K(i)⁻¹ = (E_∂ − i·A_path)/2`. Written `A_path`, `E_bd` in ASCII text (`IDEAS.md`) | [[castle-sign-kms-matrix](pages/castle-sign-kms-matrix.md)] |
| `s` | semi-perimeter of a castle, `w + #blocks` (a castle quantity) | [[castle-perimeter](pages/castle-perimeter.md)] |
| `B(x, y)` | castle GF by width `x` and blocks `y` (Deutsch-Elizalde's bargraph GF; not `B(q, z)` of the area gradings below); `B(z, z)` is castles by semi-perimeter, `B(z, −z)` the signed version | [[deutsch-elizalde-2016-bargraphs-cornerless-motzkin](pages/deutsch-elizalde-2016-bargraphs-cornerless-motzkin.md)], [[castle-perimeter](pages/castle-perimeter.md)] |
| `M_n`, `M(x)` | Motzkin numbers and their GF | [[motzkin-numbers](pages/motzkin-numbers.md)], [[motzkin-castles](pages/motzkin-castles.md)] |
| Motzkin-path castle | castle type: 1-smooth (`\|c_{i+1} − c_i\| ≤ 1`) with `c_1 = c_w = 1`; `M_{w−1}` of them over all heights | [[castle-classification-shape](pages/castle-classification-shape.md)], [[motzkin-castles](pages/motzkin-castles.md)] |
| Motzkin strip of height `h` | 1-smooth skylines on **castle** heights `1, …, h` (`h` states); its transfer matrix is `I + A_path` | [[motzkin-castles](pages/motzkin-castles.md)] |
| cornerless Motzkin path | the tower word (castle lowered by one row) read with `U = +1`, `R = 0`, `D = −1`; Deutsch-Elizalde's `Δ` adds back the outer `U…D` | [[deutsch-elizalde-2016-bargraphs-cornerless-motzkin](pages/deutsch-elizalde-2016-bargraphs-cornerless-motzkin.md)], [[tower-word-language](pages/tower-word-language.md)] |
| peak `UD`, valley `DU` | in a tower word, a zero-width block and two touching blocks: the two castle rules | [[prodinger-2025-cornerless-motzkin-bargraphs](pages/prodinger-2025-cornerless-motzkin-bargraphs.md)], [[tower-word-language](pages/tower-word-language.md)] |

**Height bookkeeping for matrices.** A tower-height matrix (`M_k(t)`, `K(ρ)`, `M_k`) has size `k + 1` = the castle height bound `h`. A castle-height strip (the Motzkin strip, the Pell strip of [[pell-castle-strip](pages/pell-castle-strip.md)]) has `h` states, heights `1, …, h`. Both have `h` states; they differ in whether the states are labelled from 0 or from 1.

**Parity words.** "Even-block" always means the PE 502 parity. `F(w, h)` is reserved for height **exactly** `h`; a count over all heights (for example the even-block Motzkin-path castles) is described in words, not written `F`.

## Area gradings

The pages that count castles by area (the q-thread, [[q-thread-seminar](pages/q-thread-seminar.md)]) mark each statistic by its own variable. A castle of area `n` is a composition of `n`, so these are generating functions, not tables.

| symbol | meaning | where |
|---|---|---|
| `q` | marks area (cells) | [[castle-by-area](pages/castle-by-area.md)] and the pages below |
| `z` or `u` | marks width; `z → qz` raises a castle one row | [[castle-row-raising-equation](pages/castle-row-raising-equation.md)], [[castle-q-bessel-closed-form](pages/castle-q-bessel-closed-form.md)] |
| `x` | marks blocks on the q-Bessel page (`x = −1` is the block sign); `y` does the same on the add-a-column and ladder pages | [[castle-q-bessel-closed-form](pages/castle-q-bessel-closed-form.md)], [[castle-add-a-column-equation](pages/castle-add-a-column-equation.md)] |
| `B(q, z)`, `E(q, z)` | castle GF by area and width, unsigned and with the sign `(−1)^blocks`, empty castle included | [[castle-row-raising-equation](pages/castle-row-raising-equation.md)] |
| `N(q)`, `M(q)` | the q-Bessel numerator and denominator of the signed count, `Σ (even − odd) q^n = N/M − 1`; `q_0`, `q_1` are the first two zeros of `M` | [[castle-q-bessel-closed-form](pages/castle-q-bessel-closed-form.md)] |
| `J_0`, `J_1`, `Π` | Bousquet-Mélou-Fédou's q-Bessel series and the parallelogram GF `Π = Y J_1/J_0`, with width `X` and height `Y` in their slots | [[castle-q-bessel-closed-form](pages/castle-q-bessel-closed-form.md)], [[bousquet-melou-fedou-1995-convex-polyominoes](pages/bousquet-melou-fedou-1995-convex-polyominoes.md)] |
| `ρ`, `C` | growth and prefactor of the signed count by area, `even − odd ~ C(−ρ)^n`, `ρ = −1/q_0 = 1.62383` | [[castle-row-raising-equation](pages/castle-row-raising-equation.md)] |

## Sampling symbols

The random-castle pages ([[castle-samplers](pages/castle-samplers.md)]) keep the core symbols and add a few of their own.

| symbol | meaning | where |
|---|---|---|
| `V(w, h)` | the set of even-block castles of width `w`, height exactly `h`, so `\|V(w, h)\| = F(w, h)` | [[castle-samplers](pages/castle-samplers.md)], [[castle-native-gray-tour](pages/castle-native-gray-tour.md)], [[castle-bdd-zdd](pages/castle-bdd-zdd.md)] |
| `blocks(c)` | the block count of skyline `c`, `c_1 + Σ max(0, c_i − c_{i−1})` | [[castle-samplers](pages/castle-samplers.md)], [[castle-gray-code](pages/castle-gray-code.md)] |
| block weight `t`, area weight `q` | the measure `t^blocks q^area / Z` on castles, `Z` its normalizer; `t = q = 1` is uniform | [[castle-samplers](pages/castle-samplers.md)] |
| `N_i(state)` | the sampler's completion table: weighted ways to finish a castle with `i` columns left | [[castle-samplers](pages/castle-samplers.md)] |
| `g(b)` | density of states: castles in the cell with `b` blocks (the block profile), as estimated by Wang-Landau | [[castle-samplers](pages/castle-samplers.md)] |
| `H_n`, `H_n^{(2)}` | harmonic numbers `Σ 1/i` and `Σ 1/i²` | [[castle-samplers](pages/castle-samplers.md)], [[fractional-block-count](pages/fractional-block-count.md)] |
| `p` | the entry probability of a Bernoulli random rule | [[castle-samplers](pages/castle-samplers.md)] |

## Other meanings of P, T, and other shared letters on the wiki

These are local notations on specific pages and are unrelated to the tower counts, or reuse a letter from the tables above:

| symbol | meaning | where |
|---|---|---|
| `P_j(k, L)` | block count weighted by `ω^{j·blocks}` (a roots-of-unity generalization; `P_1` at `m = 2` is `P`) | [[parity-via-roots-of-unity](pages/parity-via-roots-of-unity.md)] |
| `P_0`, `P_α` | area-parity sums `Σ (−1)^{area}` and their fractional versions | [[fractional-block-count](pages/fractional-block-count.md)] |
| `P_h(q)` | the polynomial `q² + q³ + … + q^h` in the tree-castle generating function | [[tree-castle-by-area](pages/tree-castle-by-area.md)], [[castle-graph](pages/castle-graph.md)] |
| `P_h` | the path graph on `h` vertices | [[ramanujan-castles](pages/ramanujan-castles.md)] |
| `P_n` | the Pell numbers (written `Pell(n)` where they sit near tower counts) | [[pell-numbers](pages/pell-numbers.md)], [[metallic-means](pages/metallic-means.md)] |
| `P_1`, `P_2` | Bender's auxiliary series | [[convex-castle-cap-factor](pages/convex-castle-cap-factor.md)] |
| `T_h(w)`, `T_h(w, q)`, `T_2(w)`, `T_3(w)` | **tree-castle** counts (castles with no `2 × 2` block), not tower counts | [[tree-castle-by-area](pages/tree-castle-by-area.md)], [[castle-graph](pages/castle-graph.md)] |
| `M` | the Project Euler modulus `10⁹ + 7` | [[larger-prime-periodicity](pages/larger-prime-periodicity.md)] |
| `S(w, h)` | the parity term of `F` (this page), also used on [[castle-entropy](pages/castle-entropy.md)] | - |
| `S` | Dhar's entropy `S = ln det Δ` of the sandpile steady state; the wiki writes `ln det L̃` instead, keeping `S(w, h)` for the parity term | [[dhar-1990-self-organized-critical-sandpile](pages/dhar-1990-self-organized-critical-sandpile.md)] |
| `G` | a graph (as in `K(G)`), or Dhar's expected-toppling matrix `G = Δ⁻¹` (written `L̃⁻¹` on the wiki); never a castle count, and elsewhere reserved for generating functions | [[sandpile-group](pages/sandpile-group.md)], [[dhar-1990-self-organized-critical-sandpile](pages/dhar-1990-self-organized-critical-sandpile.md)] |
| `A`, `D` | the adjacency and degree matrices in `L = D − A`; `A(w, h)` with arguments is the castle count, `D` is also used for diagonal sign matrices on [[tower-parity-sectors](pages/tower-parity-sectors.md)] | [[hear-the-shape-seminar](pages/hear-the-shape-seminar.md)] |
| `α`, `α_w` | `α` is the fractional order on the F-Department pages ([[fractional-block-count](pages/fractional-block-count.md)]); BTW's weighted-duration exponent is written `α_w` | [[bak-tang-wiesenfeld-1988-self-organized-criticality](pages/bak-tang-wiesenfeld-1988-self-organized-criticality.md)] |
| `β`, `γ` | the spectral and growth exponents of avalanche statistics (`γ` written `γ_g`); elsewhere local roots and constants | [[bak-tang-wiesenfeld-1988-self-organized-criticality](pages/bak-tang-wiesenfeld-1988-self-organized-criticality.md)] |
| `ℓ` | side of a square lattice in sandpile statements, keeping `L` for the Laplacian and the tower base length | [[bak-tang-wiesenfeld-1988-self-organized-criticality](pages/bak-tang-wiesenfeld-1988-self-organized-criticality.md)], [[dhar-1990-self-organized-critical-sandpile](pages/dhar-1990-self-organized-critical-sandpile.md)] |
| `P_ρ(θ)` | the Poisson kernel `(1 − ρ²)/(1 − 2ρ cos θ + ρ²)`, the symbol of `K(ρ)` | [[castle-sign-kms-matrix](pages/castle-sign-kms-matrix.md)] |
| `M_n`, `M(x)`, `M(x, y)`, `M_k`, `M_k(t)`, `M(q)` | Motzkin numbers and GF; Deutsch-Elizalde's cornerless-path GF; the signed and block-weighted transfer matrices (see the table above); the q-Bessel denominator of the signed count by area (Area gradings above). The Project Euler modulus `M` has its own row | [[motzkin-numbers](pages/motzkin-numbers.md)], [[deutsch-elizalde-2016-bargraphs-cornerless-motzkin](pages/deutsch-elizalde-2016-bargraphs-cornerless-motzkin.md)], [[tower-parity-sectors](pages/tower-parity-sectors.md)], [[castle-sign-kms-matrix](pages/castle-sign-kms-matrix.md)] |
| `F(u)`, `G(u)`, `H(u)`, `K(u)` | Prodinger's automaton-layer GFs in the final-height variable `u`; `F(u)` is not `F(w, h)` and `K(u)` is not `K(ρ)` | [[prodinger-2025-cornerless-motzkin-bargraphs](pages/prodinger-2025-cornerless-motzkin-bargraphs.md)] |
| `K(q, z)`, `K(G)`, `K`, `K(w)` | the convex castle GF; the sandpile group `K(G)` (written `K`, or `K_sink`, `K_tide` by model, on the sandpile pages); a central-binomial sum; `K(ρ)` is the KMS matrix of the table above | [[prime-convex-castles](pages/prime-convex-castles.md)], [[sandpile-group](pages/sandpile-group.md)], [[half-sum-castles](pages/half-sum-castles.md)] |
| `τ` | the tribonacci constant on [[castle-perimeter](pages/castle-perimeter.md)] (`τ²` = growth of castles by semi-perimeter); the avalanche size exponent on the sandpile pages; on the Prodinger page, the peak weight, with `σ` the valley weight (the paper's prose states the reverse; its formulas use `τ` for `UD`) | [[castle-perimeter](pages/castle-perimeter.md)], [[bak-tang-wiesenfeld-1988-self-organized-criticality](pages/bak-tang-wiesenfeld-1988-self-organized-criticality.md)], [[prodinger-2025-cornerless-motzkin-bargraphs](pages/prodinger-2025-cornerless-motzkin-bargraphs.md)] |
| `ρ` | usually a spectral radius or growth constant (`ρ_k` on [[tower-parity-sectors](pages/tower-parity-sectors.md)]); on the KMS page, the matrix parameter `√t` | [[castle-sign-kms-matrix](pages/castle-sign-kms-matrix.md)] |
| `A(w, h)` vs `A_path` | all castles of width `w`, height `h` (the core table) vs the path adjacency matrix | [[castle-sign-kms-matrix](pages/castle-sign-kms-matrix.md)] |
| `E_k` vs `E_∂` vs `E(q, z)` | the tower GF of height `≤ k` in `x` vs `diag(1, 0, …, 0, 1)` vs the signed castle GF by area and width (Area gradings above) | [[castle-counting-formula](pages/castle-counting-formula.md)], [[castle-sign-kms-matrix](pages/castle-sign-kms-matrix.md)] |
| `Δ` | Dhar's toppling matrix on the sandpile pages (`Δ = L̃` for a castle); Deutsch-Elizalde's bijection from cornerless Motzkin paths to bargraphs; elsewhere a difference or a discriminant | [[deutsch-elizalde-2016-bargraphs-cornerless-motzkin](pages/deutsch-elizalde-2016-bargraphs-cornerless-motzkin.md)], [[dhar-1990-self-organized-critical-sandpile](pages/dhar-1990-self-organized-critical-sandpile.md)] |
| `V` | the valid-castle set `V(w, h)` (Sampling symbols above); in a tower word `U V D`, the sub-tower between a peak's `U` and `D` | [[castle-samplers](pages/castle-samplers.md)], [[castle-foata-transform](pages/castle-foata-transform.md)] |
| `H_n` vs `H_d(μ)` | harmonic numbers vs the rescaled factor polynomials of `char_k` | [[castle-samplers](pages/castle-samplers.md)], [[tower-parity-sectors](pages/tower-parity-sectors.md)] |
| `N_i(state)` vs `N(q)` | the samplers' completion table vs the q-Bessel numerator (Area gradings above) | [[castle-samplers](pages/castle-samplers.md)], [[castle-q-bessel-closed-form](pages/castle-q-bessel-closed-form.md)] |

## Related Concepts

- [[castle-counting-formula](pages/castle-counting-formula.md)] - the derivation of `F(w, h)` from `T` and `P`.
- [[signed-tower-count](pages/signed-tower-count.md)] - `P(k, L)` and its recurrences.
- [[castle-sign](pages/castle-sign.md)] - the sign `(−1)^{blocks}` and the `(T ± P)/2` split.
- [[tower-recursion-master-class](pages/tower-recursion-master-class.md)] - the seminar where towers and parity are introduced.
- [[sandpile-group](pages/sandpile-group.md)] - the reduced Laplacian `L̃` and the sandpile group ([[chau-cheng-1991-deterministic-soc-sandpile](pages/chau-cheng-1991-deterministic-soc-sandpile.md)] and [[chau-1993-abelian-sandpile-model](pages/chau-1993-abelian-sandpile-model.md)] use the same `Δ`); [[dhar-1990-self-organized-critical-sandpile](pages/dhar-1990-self-organized-critical-sandpile.md)] for the general toppling matrix `Δ`.
- [[castle-sign-kms-matrix](pages/castle-sign-kms-matrix.md)] - the block-weighted matrices `M_k(t)` and `K(ρ)`.
- [[motzkin-castles](pages/motzkin-castles.md)] - the Motzkin-path symbols and the path models of castles.

## Footnotes

[^1]: [[project-euler-502-solution](pages/project-euler-502-solution.md)] §"T(k, L) = (k+1)^L" L27-34 - "A tower of height ≤ k above a length-L block is a length-L binary string ... T(k, L) = ∑_b ∏_{runs} T(k-1, l) = ∑_b k^{ones(b)} = (1 + k)^L"; [[project-euler-502-representations](pages/project-euler-502-representations.md)] §"The tower word" L221 and §"The main formula" L350-367 - "A castle is U (tower) D. The bottom block is the outer U...D pair, and the tower is everything stacked on top of it" and "h^w = T(h-1,w) counts towers ... any parity. P(h-1,w) is the signed version".
[^2]: Verified by execution (Python 3.10, 2026-09-26): by brute force over all castles, `2F(w, h) = h^w − (h−1)^w − P(h−1, w) + P(h−2, w)` and `F − odd = P(h−2, w) − P(h−1, w)` for `2 ≤ h ≤ 4`, `w ≤ 6`; `P(0, L) = 1` for `L < 10`; `2F(w, 2) = 2^w − P(1, w)` for `w ≤ 9`; `F(2, 2) = 3`, `P(1, 2) = −2`.
