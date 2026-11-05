---
title: "Edwards and Allen (2021) - Fibonacci numbers squared, golden rectangle numbers and Jacobsthal numbers from two types of tile"
category: Sources
summary: Kenneth Edwards and Michael A. Allen tile a board with squares and (1, 1)-fences, two unit posts with a unit gap. Every tiling is a sequence of three metatiles, the free square (length 1), the filled fence (length 3) and the bifence (length 4), so the tilings of an n-board are A006498(n); splitting the odd and even cells gives F_{n+1}² tilings of a 2n-board and F_{n+1}F_{n+2} of a (2n + 1)-board, and counting by tiles gives the Jacobsthal numbers J_{n+1}. Two Pascal-like triangles count the tilings with k fences, by tiles (A059259) and by length (A335964). In castle terms the metatiles are the tree skylines of height at most 3 read as compositions into parts 1, 3 and 4; the odd-even split is the wiki's interleaving map, the tiles are the columns and the fences are the blocks above the bottom row.
tags: [source, paper, fence-tiles, tiling, fibonacci, jacobsthal, tree-castle, pascal-like-triangle, combinatorial-proof, oeis]
sources: [edwards-allen-2021-fibonacci-squared-fence-tiles]
created: 2026-11-03
updated: 2026-11-03
---

# Edwards and Allen (2021) - Fibonacci numbers squared, golden rectangle numbers and Jacobsthal numbers from two types of tile

**Source:** `raw/edwards-allen-2021-fibonacci-squared-fence-tiles.pdf` (text layer at `raw/edwards-allen-2021-fibonacci-squared-fence-tiles.txt`, extracted with `pdftotext -layout`; the PDF is git-ignored, the text is tracked). K. Edwards and M. A. Allen, "New Combinatorial Interpretations of the Fibonacci Numbers Squared, Golden Rectangle Numbers, and Jacobsthal Numbers Using Two Types of Tile", arXiv:2009.04649v3 (2020), published in the *Journal of Integer Sequences* 24 (2021), Article 21.3.8.[^1] The text layer stacks binomial coefficients and subscripts on separate lines; the formulas below are read from the PDF.
**Date ingested:** 2026-11-03
**Type:** paper (PDF)

## Notation used on this page

| paper | meaning | castle reading |
|---|---|---|
| `n`-board | a strip of `n` unit cells | |
| square `S`, fence `F` | a unit square; a `(1, 1)`-fence, two unit posts with a gap of one cell | a column of height 1; one block above the bottom row |
| free square, filled fence, bifence | the metatiles `S`, `FS` (a fence with a square in its gap) and `FF` (two interlocked fences), of lengths 1, 3 and 4 | the columns `(1)`, `(1, 2)` and `(1, 3)` |
| `A_n` | the tilings of an `n`-board | the tree skylines of height at most 3 and area `n − 1` |
| `n`-tiling, `B_n` | a tiling by `n` tiles; their number | the tree skylines of height at most 3 and width `n − 1` |
| `f_n` | `F_{n+1}`, the square-domino tilings of an `n`-board | the skylines of height at most 2 and area `n` |
| `J_n` | the Jacobsthal numbers, `J_n = J_{n−1} + 2J_{n−2}`, `J_0 = 0`, `J_1 = 1` (A001045) | |
| `⟨n, k⟩`, `[n, k]` | the `n`-tilings with `k` fences; the tilings of an `n`-board with `k` fences | the tree skylines of height at most 3 by width, or by area, and blocks |

The paper writes `⟨n, k⟩` with angle brackets stacked like a binomial coefficient; this page writes it on one line.

## Summary

**Metatiles.** A `(w, g)`-fence is two posts of size `w × 1` with a gap of size `g × 1`, and the paper tiles boards with squares and `(1, 1)`-fences.[^2] A fence's gap must be filled by a square or by a post of a second fence, so every tiling is a sequence of three metatiles: the free square, the filled fence `FS` of length 3 and the bifence `FF` of length 4. Conditioning on the last metatile gives `A_n = δ_{n,0} + A_{n−1} + A_{n−3} + A_{n−4}` (Theorem 1), and `A_n` is A006498: `1, 1, 1, 2, 4, 6, 9, 15, 25, 40, …`.[^3]

**Fibonacci squares.** Lemma 1 puts the contents of the odd cells of a tiling on one board and the contents of the even cells on another; the two posts of a fence lie on consecutive cells of one parity and become a domino. So the fence-square tilings of a `2n`-board correspond to the ordered pairs of square-domino tilings of two `n`-boards, and those of a `(2n + 1)`-board to the pairs of an `(n + 1)`-board and an `n`-board. Theorem 2 follows: `A_{2n} = f_n² = F_{n+1}²` (A007598) and `A_{2n+1} = f_n f_{n+1}`, a golden rectangle number (A001654).[^4] The same split by cell number modulo `m` handles `(1, m − 1)`-fences (Theorem 3).[^4]

**Jacobsthal numbers.** Counted by the number of tiles in place of length, the metatiles hold 1, 2 and 2 tiles, so `B_n = δ_{n,0} + B_{n−1} + 2B_{n−2}` and `B_n = J_{n+1}` (Theorem 4).[^5]

**Two triangles.** `⟨n, k⟩`, the `n`-tilings with `k` fences, is the triangle A059259; `[n, k]`, the tilings of an `n`-board with `k` fences, is A335964; and `[n, k] = ⟨n − k, k⟩` (Identity 28), since `n − k` tiles of which `k` are fences have total length `n`.[^6] The rest of the paper proves identities for these numbers by counting tilings two ways, in the manner of Benjamin and Quinn, relates both triangles to Riordan arrays, and proves a conjecture from the OEIS entry for A059259 (Identity 25).[^7]

## The castle reading

- **The metatiles are tree skylines.** On [[tree-castle-by-area](pages/tree-castle-by-area.md)], a tree skyline of height at most 3 and area `A`, with a column of height 1 put in front, is a composition of `A + 1` into parts 1, 3 and 4: a column of height 1 is a part 1, and a column of height 1 followed by a column of height 2 or 3 is a part 3 or 4. Reading these parts as the free square, the filled fence and the bifence makes the tree skyline a fence-square tiling of an `(A + 1)`-board, and `A_{A+1}` is the count `A006498(A + 1)` of that page.[^exec]
- **Tiles are columns, fences are blocks.** Each column of the skyline with its leading column is one tile of the tiling (the filled fence and the bifence each cover two columns with two tiles), so a skyline of width `w` is a `(w + 1)`-tiling. A column of height `j` carries `j − 1` fences, so the fences number `A − w`, which for a tree skyline is its block count minus 1 ([[castle-graph](pages/castle-graph.md)]). Theorem 4 is then the count of the tree skylines of height at most 3 by width, `J_{w+2} = A001045(w + 2)`, and the triangles count them by blocks: by width as row `w + 1` of A059259, by area as row `A + 1` of A335964.[^exec]
- **Lemma 1 is the interleaving map.** The odd-even split of Lemma 1 is the map of [[n-nacci-disambiguation](pages/n-nacci-disambiguation.md)], Fibonacci section 5, which sends the tree skylines of height at most 3 onto pairs of skylines of height at most 2. A square-domino tiling of length `L` is a skyline of height at most 2 and area `L` ([[fibonacci-castle](pages/fibonacci-castle.md)]), so Theorem 2 is the identity `A006498(2n) = F_{n+1}²` of [[tree-castle-by-area](pages/tree-castle-by-area.md)] with a bijective proof.[^4][^exec]
- **The fences carry the sign.** Since the fences number the blocks minus 1, the tilings with an odd number of fences are the tree skylines with an even number of blocks, the parity that Project Euler 502 counts ([[castle-sign](pages/castle-sign.md)]).

## Key Takeaways

- **Squares and `(1, 1)`-fences tile in three metatiles of lengths 1, 3 and 4**, so the tilings of an `n`-board are A006498(n).[^3]
- **Splitting the odd and even cells** sends a tiling to a pair of square-domino tilings, giving `F_{n+1}²` and `F_{n+1}F_{n+2}`.[^4]
- **Counted by tiles, the tilings are the Jacobsthal numbers** `J_{n+1}`.[^5]
- **Counted by fences**, they fill the triangles A059259 (by tiles) and A335964 (by length).[^6]

## Entities & Concepts

- [[tree-castle-by-area](pages/tree-castle-by-area.md)] - the tree skylines of height at most 3 as compositions into parts 1, 3 and 4, A006498 and `A006498(2n) = F_{n+1}²`.
- [[n-nacci-disambiguation](pages/n-nacci-disambiguation.md)] - the interleaving map onto pairs of skylines of height at most 2.
- [[castle-graph](pages/castle-graph.md)] - the tree skylines by width, the Jacobsthal numbers at height 3, and the block count `1 + n − w`.
- [[fibonacci-castle](pages/fibonacci-castle.md)] - square-domino tilings as skylines of height at most 2.
- [[castle-sign](pages/castle-sign.md)] - the parity of the block count.
- [[metallic-means](pages/metallic-means.md)] - the Jacobsthal numbers as the sequence of copper, `σ_1^2 = 2`.

## Relation to Other Wiki Pages

The wiki's interleaving map on [[n-nacci-disambiguation](pages/n-nacci-disambiguation.md)] and the identity `A006498(2n) = F_{n+1}²` on [[tree-castle-by-area](pages/tree-castle-by-area.md)] are Lemma 1 and Theorem 2 of this paper read on tree skylines. The Jacobsthal count of the tree skylines of height at most 3 by width, Equation (1) of [[castle-graph](pages/castle-graph.md)] at `h = 3`, is Theorem 4.

## Footnotes

[^1]: [[edwards-allen-2021-fibonacci-squared-fence-tiles](pages/edwards-allen-2021-fibonacci-squared-fence-tiles.md)] title page L1-L18 [synthesis] - "New Combinatorial Interpretations of the Fibonacci Numbers Squared, Golden Rectangle Numbers, and Jacobsthal Numbers Using Two Types of Tile", "arXiv:2009.04649v3 [math.CO] 4 Oct 2020", "Kenneth Edwards and Michael A. Allen", Mahidol University; the journal reference "Journal of Integer Sequences 24, Article 21.3.8 (2021)" from https://arxiv.org/abs/2009.04649 (read 2026-11-03).
[^2]: [[edwards-allen-2021-fibonacci-squared-fence-tiles](pages/edwards-allen-2021-fibonacci-squared-fence-tiles.md)] §1 p.2 L54-L55 - "A (w, g)-fence tile is composed of two subtiles (called posts) of size w × 1 separated by a gap of size g × 1."
[^3]: [[edwards-allen-2021-fibonacci-squared-fence-tiles](pages/edwards-allen-2021-fibonacci-squared-fence-tiles.md)] §2 pp.2-3 L82-L111 [synthesis] - "To tile adjacent cells by starting with a single fence we must fill the gap with either a square or the post of another fence. These generate what we will refer to as the filled fence (F S) and bifence (F F ) metatiles"; "The bifence clearly has a length of 4. The filled fence has length 3"; Theorem 1, `A_n = δ_{n,0} + A_{n−1} + A_{n−3} + A_{n−4}`, "three possible metatiles and these have lengths of 1, 3, and 4"; "An≥0 = 1, 1, 1, 2, 4, 6, 9, 15, 25, 40, 64, 104, 169, 273, 441, 714, 1156, . . . is A006498."
[^4]: [[edwards-allen-2021-fibonacci-squared-fence-tiles](pages/edwards-allen-2021-fibonacci-squared-fence-tiles.md)] §2 pp.3-4 L112-L153 [synthesis] - Lemma 1: "Tile an n-board (an (n + 1)-board) with the contents of the odd-numbered cells of the given 2n-board ((2n + 1)-board) fence-square tiling and tile a second n-board (an n-board) with the contents of the even-numbered cells. The posts of any fence (which always lie on two consecutive odd or even cells) get mapped to a domino."; Theorem 2, `A_{2n} = f_n²`, `A_{2n+1} = f_n f_{n+1}`, "where fn = Fn+1"; Theorem 3 for `(1, m − 1)`-fences by cell number modulo `m`.
[^5]: [[edwards-allen-2021-fibonacci-squared-fence-tiles](pages/edwards-allen-2021-fibonacci-squared-fence-tiles.md)] §1 p.2 L65-L69 and §2 p.4 L154-L161 [synthesis] - the Jacobsthal numbers "Jn≥0 = 0, 1, 1, 3, 5, 11, 21, 43, 85, 171, . . . (A001045)", Equation (1); Theorem 4, "If Bn is the number of n-tilings using squares and fences then Bn = Jn+1"; "As the three possible metatiles contain 1, 2, and 2 tiles".
[^6]: [[edwards-allen-2021-fibonacci-squared-fence-tiles](pages/edwards-allen-2021-fibonacci-squared-fence-tiles.md)] §5 pp.10-11 L474-L506 and §6 pp.15-16 L745-L782 [synthesis] - "We define h nk i as the number of n-tilings which contain exactly k fences", "the triangle is sequence A059259", Figure 2; "We define [ nk ] as the number of tilings of an n-board which contain exactly k fences", Figure 3 "(A335964)"; Identity 28, `[n, k] = ⟨n − k, k⟩`, "If a tiling contains n − k tiles of which k are fences, the total length is n."
[^7]: [[edwards-allen-2021-fibonacci-squared-fence-tiles](pages/edwards-allen-2021-fibonacci-squared-fence-tiles.md)] §§3-6 pp.4-20 L166-L167, L624-L680 and L859-L882 [synthesis] - "The proofs of Identities 1, 2, and 3 (and of Identities 6, 7, 8, and 9 in the next section) follow the techniques of Benjamin and Quinn [3]."; Theorem 5 and Theorem 6, the triangles as the Riordan arrays `(1/(1 − x²), x/(1 − x))` and `(1/[(1 − x)(1 − x²)], x/(1 − x)²)`; "This allows us to prove a conjecture given in the OEIS entry for A059259 concerning A071921".
[^exec]: Verified by execution (Python 3.11 with SymPy, 2026-11-03): `bin/python/tree_castle_by_area.py` item [7], run log `bin/python/tree_castle_by_area-run.log`. The composition map sends the tree skylines of height at most 3 and area `A ≤ 14` onto the fence tilings of an `(A + 1)`-board, with `w + 1` tiles and `A − w` fences, one less than the block count; the counts by area and fences against row `A + 1` of A335964 (`A ≤ 10`), by width against `A001045(w + 2)` (`w ≤ 10`), and by width and fences against row `w + 1` of A059259 (`w ≤ 9`), OEIS data read 2026-11-03; the fence tilings of `2n` and `2n + 1` cells against `F_{n+1}²` and `F_{n+1}F_{n+2}` for `n ≤ 9`.
