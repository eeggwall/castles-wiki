# PE 502 castles as an upgrade of the $(n-1)!$ cycle-count proof

## Warm-up: labelled cycles

A cycle on $n$ labelled items is a cyclic arrangement - an ordering up to rotation. The number of such directed cycles is $(n-1)!$, with two standard proofs:

1. **Quotient by rotation.** $n!$ linear orderings collapse under the free $\mathbb{Z}/n$ rotation action, so $n!/n = (n-1)!$ cycles.
2. **Fix a starting point.** Every cycle can be written uniquely starting with the item labelled $1$; the remaining $n-1$ items order freely, so $(n-1)!$ cycles.

Both proofs are instances of a bigger machine (Foata, sign, cycle-follow) that reappears in PE 502.

## Castle setup (recap)

From https://charlesreid1.com/wiki/Project_Euler/502:

- Grid of width $w$, target max-height exactly $h$.
- Blocks are $1 \times \ell$ rectangles; on each row, adjacent blocks have $\ge 1$ unit of gap.
- Row 1 is a single block of length $w$.
- Total block count is **even**.
- $F(w,h)$ = number of such castles.

$F(4,2)=10$ checks quickly: bottom block is forced, and even parity forces exactly 1 block on row 2 (blocks-of-3 on row 2 don't fit). A single block on row 2 is a choice $0 \le a < b \le 4$, giving $\binom{5}{2}=10$.

## The central analogy (from the wiki)

**permutation cycles ↔ castle peaks/excursions**

| Permutations | Castles |
|---|---|
| element $i$ | skyline step |
| disjoint cycle | disjoint `U...D` peak |
| parenthesized cycles | peaks separated by `R` gaps |
| cycle count | peak count |
| $\operatorname{sgn}(\sigma) = (-1)^{n-c}$ | $s(C) = (-1)^{\text{blocks}(C)}$ |

## Connection 1: Castle sign ↔ $(1 \pm \operatorname{sgn})/2$ trick

Weight each castle by $(-1)^{\text{blocks}}$, splitting the total count $T$ into even- and odd-block halves via $(T \pm P)/2$. This is exactly the $(1 \pm \operatorname{sgn})/2$ trick used to peel $A_n$ out of $S_n$. The wiki gives the closed form

$$F(w,h) \;=\; \tfrac{1}{2}\!\left(h^w - (h-1)^w - P(h-1,w) + P(h-2,w)\right)$$

where $P(k,w)$ is the signed-count polynomial. Sanity check for $F(4,2)$: $h^w = 16$, $(h-1)^w = 1$, $P(1,4) = -4$, $P(0,4) = 1$ from the 16 binary column-height strings, giving $F(4,2) = (16 - 1 + 4 + 1)/2 = 10$. Matches.

## Connection 2: Castle Foata transform ↔ Foata's fundamental transformation

Foata's fundamental transformation is the standard bijection

$$\Phi : S_n \;\longleftrightarrow\; S_n$$

between one-line permutations and canonical cycle words: write each cycle starting with its largest element, order cycles by that largest element increasingly, then drop the parentheses. Parentheses recover from left-to-right maxima.

The castle analogue: flatten the tower to its column-height word $c_1 \ldots c_L$ (dropping the `R` "parentheses"). Peaks become **maximal positive runs**, and each peak's "leader" is the first column of that run - the records of the sequence, in perfect analogy with cycle-leaders as left-to-right maxima. The record set is

$$\{i : c_i > 0 \text{ and } (i = 1 \text{ or } c_{i-1} = 0)\}.$$

For $F(4,2) = 10$ these are exactly the 10 length-4 binary strings with one positive run: `1000, 0100, 0010, 0001, 1100, 0110, 0011, 1110, 0111, 1111`.

Ten one-peak castles ↔ single-cycle structural analogue. Note that $3! = 6 \ne 10$: the analogy is one-cycle ↔ one-peak in **structure**, not in count, because castle rows have arbitrary integer widths while cycles have unit-labelled elements. The correspondence is at the level of factoring, not cardinality.

## Connection 3: Monotone streak factorization ↔ $O(n)$ cycle-following

Take first differences $d_i = c_{i+1} - c_i$; split into up-runs, flat runs, down-runs. Block count = sum of down-run magnitudes = $\sum_i \max(0, c_i - c_{i+1})$. One linear scan produces the factorization, described on the wiki as "the castle version of Knuth's $O(n)$ cycle-following loop."

From that scan, the signed count satisfies a rational-function recurrence:

$$\operatorname{num}_k = 2\operatorname{den}_{k-1} - \operatorname{num}_{k-1}, \qquad \operatorname{den}_k = \operatorname{den}_{k-1}(1 - 2x) + x\,\operatorname{num}_{k-1},$$

evaluated with Kitamasa or Berlekamp-Massey to reach $F(10^{12}, 100)$ and $F(100, 10^{12})$.

## The caveat worth flagging

**Block count $\ne$ peak count.** A tall peak can be several stacked blocks. So the $(-1)^{\text{blocks}}$ sign atom and the peak-count analogue of cycle count are different statistics on the same castle. The Foata bijection is with peaks; the sign is measured on blocks.

That is the fingerprint of a genuinely richer combinatorial object than plain permutations - the castle sits somewhere between "cycles of a permutation" and "cycles with multiplicity/height."

## Tying back to $(n-1)!$

The elementary proof of $(n-1)!$ is the degenerate case: one cycle, no factoring, sign trivial. The castle machinery is running the same three moves at industrial scale:

| $(n-1)!$ proof move | Castle counterpart |
|---|---|
| divide by $n$ (quotient by rotation) | castle sign / signed-count halving |
| canonical form starting from element $1$ | castle Foata: canonical form starting from each peak's leftmost positive column |
| cycle-follow the permutation to read off cycles | monotone streak scan to read off peaks |

PE 502 is essentially: take the toolkit that proves $(n-1)!$, upgrade every step to a version that handles stacked, width-weighted, sign-selected cycles, and you get a closed form plus a fast recurrence.
