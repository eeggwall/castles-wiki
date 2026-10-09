---
title: "Bayer & Diaconis (1992) - Trailing the dovetail shuffle to its lair"
category: Sources
summary: Bayer and Diaconis show that an a-shuffle of n cards (cut into a packets, riffle them together) gives a permutation with r rising sequences with probability C(a + n − r, n)/a^n. The proof is stars and bars - r − 1 cuts are forced between the rising sequences and the a − r spare cuts go into n + 1 bins - and summing over permutations is Worpitzky's identity a^n = Σ_r Eul(n, r) C(a + n − r, n). The castle use is the tower block-count identity T(w, b) = Σ_k N(w, k) C(b + w − k, w − 1), refined by descents, which has the same shape: under a = b + 1, n = w − 1, r = k the two binomials coincide, so the Bayer-Diaconis proof is the model for a bijective proof of the Narayana numerator. The paper's mixing results ((3/2) log₂ n riffle shuffles, cutoff, total variation through a sufficient statistic) are summarized for reference.
tags: [source, paper, permutations, descents, eulerian-numbers, worpitzky, stars-and-bars, tower, narayana, markov-chain, mixing]
sources: [bayer-diaconis-1992-dovetail-shuffle]
created: 2026-10-08
updated: 2026-10-08
---

# Bayer & Diaconis (1992) - Trailing the dovetail shuffle to its lair

**Source:** `raw/bayer-diaconis-1992-dovetail-shuffle.pdf` (text layer at `raw/bayer-diaconis-1992-dovetail-shuffle.txt`, extracted with `pdftotext -layout`; the PDF is git-ignored, the text is tracked). D. Bayer and P. Diaconis, "Trailing the dovetail shuffle to its lair", *Ann. Appl. Probab.* 2(2), 1992, pp. 294-313; JSTOR scan (stable URL http://www.jstor.org/stable/2959752), copy from https://www.stat.berkeley.edu/~aldous/157/Papers/bayer_diaconis.pdf.[^1] The text layer garbles most displayed formulas, so formulas on this page are cited by synthesis and were checked by execution.
**Date ingested:** 2026-10-08
**Type:** paper (PDF, 20 pp. + JSTOR cover page)

## Notation used on this page

The page keeps the paper's `n`, `a`, `r` (no clash inside this page) and renames two symbols that clash with the wiki's ([[castle-notation](pages/castle-notation.md)]). Footnote quotes keep the paper's symbols.

| paper | meaning | written here as |
|---|---|---|
| `n` | number of cards | `n` |
| `a` | number of packets of an a-shuffle | `a` |
| `r` | number of rising sequences of a permutation | `r` |
| `A_{n,r}` | Eulerian number: permutations of `n` with `r` rising sequences | `Eul(n, r)` (`A(w, h)` is the castle count) |
| `m` | number of riffle shuffles | written out in words (`m` is the m-smooth step bound) |

A **descent** of a sequence `s_1, …, s_n` is a position `i` with `s_i > s_{i+1}`; this is the same definition the tower pages use for column heights. A **rising sequence** of an arrangement of the cards `1, …, n` is a maximal run of consecutive values `j, j+1, …, j+l` that appear in increasing positions.[^2] A permutation has `r` rising sequences exactly when its inverse has `r − 1` descents.[^3]

## Summary

**The model.** In the Gilbert-Shannon-Reeds model of a riffle shuffle the deck is cut binomially and cards drop from each half with probability proportional to the half's size; backwards, each card goes to the left or right heap independently with probability 1/2.[^4] The **a-shuffle** generalizes this to `a` packets. The paper gives four equivalent descriptions: points of the unit interval under the map `x ↦ ax (mod 1)`; all cuts into `a` packets and all interleavings equally likely; the inverse, which deals each card into one of `a` piles uniformly and independently and stacks the piles; and packets of multinomial size riffled together one after another. In every description an a-shuffle followed by a b-shuffle is an ab-shuffle, so a sequence of ordinary riffle shuffles is a single a-shuffle with `a` a power of 2.[^5]

**Theorem 3: the probability of a permutation.** An a-shuffle of `n` cards produces a permutation with `r` rising sequences with probability `C(a + n − r, n)/a^n`.[^6] The proof counts the cuts of the ordered deck into `a` packets that can produce the permutation. Each packet stays in order when riffled, so each rising sequence is a union of packets. One cut must fall between each pair of successive rising sequences, which places `r − 1` cuts; the remaining `a − r` cuts go anywhere among the `n + 1` gaps of the deck (the `n` cards are the dividers), in `C(a + n − r, n)` ways.[^7] The paper also phrases this as colorings: dye the `a` packets distinct colors before riffling; the colorings that look like they came from a shuffle are the ones that refine the rising sequences.[^8]

**Worpitzky's identity.** Summing Theorem 3 over the `n!` permutations gives total probability 1, and there are `Eul(n, r)` permutations with `r` rising sequences, so

```
a^n  =  Σ_{r=1..n} Eul(n, r) · C(a + n − r, n),
```

which is Worpitzky's identity.[^9] As a generating function in `a` it reads `Σ_a a^n x^a = Σ_r Eul(n, r) x^r / (1 − x)^{n+1}`, the Eulerian polynomial over `(1 − x)^{n+1}` (own reasoning, checked by execution).[^18] The authors note that Theorem 3 can also be read off from Stanley's extension of Worpitzky's identity to partially ordered sets (*Enumerative Combinatorics* Vol. 1, Thm. 4.5.14) at the poset with no relations, and that the poset version "may have interesting shuffling interpretations".[^10]

**Consequences.** Theorem 3 extends earlier work of Shannon on equal probabilities for permutations with the same number of rising sequences.[^11] The number of rising sequences, observed along repeated a-shuffles, is itself a Markov chain (Corollary 2), because given that number the permutation is uniform.[^12] In the group algebra of the symmetric group, the sums `A_r` of all permutations with `r` rising sequences span a commutative semisimple algebra of dimension `n`; multiplication by the 2-shuffle element has eigenvalues `1, 1/2, …, 1/2^{n−1}` (Corollary 3), and the paper links this algebra to Solomon's descent algebra and to Hodge decompositions of Hochschild homology.[^13]

**How many shuffles.** The total variation distance from uniform stays near 1 and then falls by a factor of about 2 per shuffle, the cutoff phenomenon; for 52 cards it is `0.924, 0.614, 0.334, 0.167` after 5, 6, 7, 8 riffle shuffles.[^14] Theorem 4 places the cutoff at `(3/2) log₂ n` riffle shuffles, with an explicit profile in the normal distribution function.[^15] The proof uses two facts: the number of rising sequences is a sufficient statistic for both the shuffle distribution and the uniform one, so total variation can be computed on that one statistic; and the Eulerian numbers obey a central limit theorem, `Eul(n, ·)/n!` being the law of the integer part of a sum of `n` independent uniforms on `[0, 1]` (Tanny).[^16]

**Other developments.** Section 5 treats a guessing-game distance, the effect of a random cut, and face-up/face-down shuffles on the signed permutations, where Beals reduces the analysis to the ordinary model.[^17]

## The castle reading

A **tower** of width `w` is a column-height vector `c_1, …, c_w ≥ 0` with `blocks = c_1 + Σ_{i≥2} max(0, c_i − c_{i−1})` ([[tower-heap](pages/tower-heap.md)]). The tower block-count identity is

```
T(w, b)  =  Σ_{k=1..w} N(w, k) · C(b + w − k, w − 1),      Σ_b T(w, b) x^b  =  Narayana_w(x) / (1 − x)^w,
```

with `N(w, k)` the Narayana numbers, and the `k`-th term counts the towers with `k − 1` descents ([[narayana-numbers](pages/narayana-numbers.md)], [[tower-narayana-polynomial](pages/tower-narayana-polynomial.md)]). Both identities are a descent-indexed polynomial over a power of `(1 − x)`, and the binomials match exactly (own reasoning, checked by execution):[^18]

| Bayer-Diaconis | tower |
|---|---|
| `n` cards, `n + 1` gaps for cuts | `w` columns, `w` bins for blocks (`n = w − 1`) |
| `a` packets | `b + 1` (`a = b + 1`) |
| `r` rising sequences, `r − 1` forced cuts | `k`, with `k − 1` descents |
| `a − r` spare cuts | `b − k + 1` spare blocks |
| `C(a + n − r, n)` | `C(b + w − k, w − 1)` |
| `Eul(n, r)` permutations | `N(w, k)` towers |

The stars-and-bars factor is the same, but the objects differ: `r` runs over `1, …, n = w − 1` while `k` runs over `1, …, w`, so the dictionary does not send towers to permutations. What it gives is the model for a bijective proof of the Narayana numerator, which [[narayana-numbers](pages/narayana-numbers.md)] and [[viennot-heap-tower](pages/viennot-heap-tower.md)] record as unproved: a tower with `k − 1` descents would be built from a forced part, counted by `N(w, k)`, and `b − k + 1` spare blocks placed in `w` bins, as Theorem 3 builds a cut of the deck from `r − 1` forced cuts and `a − r` spare ones.

## Key Takeaways

- **Theorem 3.** An a-shuffle gives a permutation with `r` rising sequences with probability `C(a + n − r, n)/a^n`, by stars and bars over the cuts.[^6][^7]
- **Worpitzky's identity** is Theorem 3 summed over permutations.[^9]
- **The castle use.** The tower block-count identity has the same descent-indexed stars-and-bars shape, with matching binomials under `a = b + 1`, `n = w − 1`, `r = k`; Theorem 3's proof is the model for a bijective proof of the Narayana numerator (own reasoning).[^18]
- **Mixing.** About `(3/2) log₂ n` riffle shuffles mix `n` cards, with a sharp cutoff; total variation reduces to one sufficient statistic.[^15][^16]

## Entities & Concepts

- [[narayana-numbers](pages/narayana-numbers.md)] - the tower identity whose shape matches Worpitzky's.
- [[tower-heap](pages/tower-heap.md)] - the tower and its block count.
- [[viennot-heap-tower](pages/viennot-heap-tower.md)] - the "pick `k`, then a weak composition" reading of the tower identity.
- [[aocp-permutations](pages/aocp-permutations.md)] - permutations on the wiki.

## Relation to Other Wiki Pages

[[tower-narayana-polynomial](pages/tower-narayana-polynomial.md)] found the Narayana numerator and [[narayana-numbers](pages/narayana-numbers.md)] the descent refinement; this paper supplies the classical identity of the same shape and a proof of it by stars and bars. [[castle-samplers](pages/castle-samplers.md)] asks for the mixing time of a chain on castles; the method here, total variation computed on one sufficient statistic, rests on Theorem 3's exact formula, and the wiki has no formula of that kind for a castle chain.

## Footnotes

[^1]: [[bayer-diaconis-1992-dovetail-shuffle](pages/bayer-diaconis-1992-dovetail-shuffle.md)] cover page and p.294 L1-L5, L34-L41 [synthesis] - the JSTOR cover with "Source: The Annals of Applied Probability, Vol. 2, No. 2 (May, 1992), pp. 294-313" and the stable URL, and the first page with title and authors Dave Bayer (Columbia University) and Persi Diaconis (Harvard University).
[^2]: [[bayer-diaconis-1992-dovetail-shuffle](pages/bayer-diaconis-1992-dovetail-shuffle.md)] §2 p.297 L205-L209 [synthesis] - a rising sequence is a "maximal subset of an arrangement of cards" of successive face values in order; rising sequences do not intersect, and the example `A, 5, 2, 3, 6, 7, 4` is the two rising sequences `A, 2, 3, 4` and `5, 6, 7` interleaved.
[^3]: [[bayer-diaconis-1992-dovetail-shuffle](pages/bayer-diaconis-1992-dovetail-shuffle.md)] §1 p.295 L114-L116 and §3 p.305 L656-L662 [synthesis] - a permutation has a descent at `i` if `π(i) > π(i+1)`, and a permutation has `r` rising sequences if and only if its inverse has `r − 1` descents (the text layer garbles `π` and `π^{−1}`).
[^4]: [[bayer-diaconis-1992-dovetail-shuffle](pages/bayer-diaconis-1992-dovetail-shuffle.md)] §1 p.294 L56-L66 [synthesis] - the deck is cut into `k` and `n − k` cards with binomial probability; with `A` and `B` cards left in the two heaps the next card drops from the left with chance `A/(A + B)`; backwards, "Each card has an equal and independent chance of being pulled back into the left or right heap."
[^5]: [[bayer-diaconis-1992-dovetail-shuffle](pages/bayer-diaconis-1992-dovetail-shuffle.md)] §3 pp.299-301 L337-L387 [synthesis] - the geometric, maximum entropy, inverse and sequential descriptions of an a-shuffle, and Lemma 1: the four descriptions give the same distribution and "in each model an a-shuffle followed by a b-shuffle is equivalent to an ab-shuffle."
[^6]: [[bayer-diaconis-1992-dovetail-shuffle](pages/bayer-diaconis-1992-dovetail-shuffle.md)] §3 Theorem 3 p.301 L444-L449 [synthesis] - the probability that an a-shuffle results in `π` is `C(a + n − r, n)/a^n` with `r` the number of rising sequences of `π` (formula garbled in the text layer); checked by execution, footnote 18.
[^7]: [[bayer-diaconis-1992-dovetail-shuffle](pages/bayer-diaconis-1992-dovetail-shuffle.md)] §3 proof of Theorem 3 p.301 L452-L463 - "Thus, we want to count the number of ways of refining r rising sequences into a packets."; "the n cards form dividers creating n + 1 bins, into which the a - r spare cuts are allocated."
[^8]: [[bayer-diaconis-1992-dovetail-shuffle](pages/bayer-diaconis-1992-dovetail-shuffle.md)] §3 p.301 L465-L468 and Figs. 3-4 p.302 L489-L518 [synthesis] - coloring the packets before riffling; the count is of colorings of `π` "which look like they came from a shuffle", which refine the rising sequences; Fig. 4 places one cut between the two rising sequences of `A, 4, 2, 3, 5` and the other anywhere.
[^9]: [[bayer-diaconis-1992-dovetail-shuffle](pages/bayer-diaconis-1992-dovetail-shuffle.md)] §3 p.302 L497-L505 [synthesis] - summing Theorem 3 over all permutations gives 1, there are `A_{n,r}` (Eulerian) permutations with `r` rising sequences, and multiplying by `a^n` gives `a^n = Σ_r A_{n,r} C(a + n − r, n)`, "which is Worpitzky's identity."
[^10]: [[bayer-diaconis-1992-dovetail-shuffle](pages/bayer-diaconis-1992-dovetail-shuffle.md)] §3 p.302 L505-L509 - "a proof of Theorem 3 can be inferred from the proof of Theorem 4.5.14 in Stanley (1986), by considering the trivial poset consisting only of incomparable elements. Stanley's result is an extension of Worpitzky's identity to partially ordered sets, which may have interesting shuffling interpretations."
[^11]: [[bayer-diaconis-1992-dovetail-shuffle](pages/bayer-diaconis-1992-dovetail-shuffle.md)] §3 p.303 L539-L541 [synthesis] - Shannon showed that after `m < log₂ n` riffle shuffles all arrangements with `2^m` rising sequences have the same probability; Theorem 3 generalizes this.
[^12]: [[bayer-diaconis-1992-dovetail-shuffle](pages/bayer-diaconis-1992-dovetail-shuffle.md)] §3 Corollary 2 p.303 L550-L556 [synthesis] - along successive independent a-shuffles from the identity, the number of rising sequences forms a Markov chain; by Theorem 3 the conditional law of the permutation given that number is uniform, and a completeness condition (Rogers and Pitman) finishes the proof.
[^13]: [[bayer-diaconis-1992-dovetail-shuffle](pages/bayer-diaconis-1992-dovetail-shuffle.md)] §3 Corollary 3 pp.304-305 L590-L669 [synthesis] - the subalgebra generated by the sums `A_i` over permutations with `i` rising sequences is commutative and semisimple of dimension `n`, with explicit primitive idempotents; multiplying by the 2-shuffle element has the distinct eigenvalues `1, 1/2, …, 1/2^{n−1}`; connections to Hochschild homology (Barr, Gerstenhaber-Schack, Loday, Hanlon) and to Solomon's descent algebras.
[^14]: [[bayer-diaconis-1992-dovetail-shuffle](pages/bayer-diaconis-1992-dovetail-shuffle.md)] §1 Table 1 p.296 L145-L151, L173-L176 [synthesis] - total variation for 52 cards is 1.000 through four shuffles, then 0.924, 0.614, 0.334, 0.167, 0.085, 0.043 for five to ten; it "stays essentially at its maximum of 1 up to 5 shuffles, when it begins to decrease sharply by factors of 2 each time", the cutoff phenomenon of Aldous and Diaconis.
[^15]: [[bayer-diaconis-1992-dovetail-shuffle](pages/bayer-diaconis-1992-dovetail-shuffle.md)] §4 L694-L697, Theorem 4 p.307 L769-L777, Remarks 1-2 p.309 L890-L908 [synthesis] - with `m = log₂(n^{3/2} c)` shuffles, `c` fixed, the total variation tends to `1 − 2Φ(−1/(4c√3))` as `n → ∞`, `Φ` the standard normal distribution function, so about `(3/2) log₂ n` shuffles are needed; the text layer garbles `3/2` ("3 10g2 n", "321g2 n").
[^16]: [[bayer-diaconis-1992-dovetail-shuffle](pages/bayer-diaconis-1992-dovetail-shuffle.md)] §4 proof of Theorem 4 pp.307-308 L785-L804 [synthesis] - "the number of rising sequences is a sufficient statistic for both" the shuffle and uniform distributions, and total variation equals the total variation between the induced laws of a sufficient statistic; Tanny and Stanley show the Eulerian number divided by `n!` is the chance that a sum of `n` uniforms on `[0, 1]` lies between `j` and `j + 1`, giving the central limit theorem.
[^17]: [[bayer-diaconis-1992-dovetail-shuffle](pages/bayer-diaconis-1992-dovetail-shuffle.md)] §5 pp.310-311 L931-L1031 [synthesis] - §5.1 a guessing-game distance, §5.2 McGrath's formula after shuffles and a uniform cut, §5.3 face-up/face-down shuffles on the hyperoctahedral group and Beals's Theorem 5 reducing them to the ordinary model.
[^18]: Verified by execution (Python 3, 2026-10-08): for `n ≤ 6`, every permutation has (number of rising sequences) = (number of descents of its inverse) + 1; Worpitzky's identity holds for `a ≤ 8`, and its generating-function form to `x^20`; dealing each card of an ordered deck into one of `a` piles in all `a^n` ways and stacking the piles produces each permutation `π` from exactly `C(a + n − r, n)` deals, `r` the number of rising sequences of `π`, for `a = 2, 3` (Theorem 3); `C(b + w − k, w − 1) = C(a + n − r, n)` at `a = b + 1`, `n = w − 1`, `r = k` for `w ≤ 7`, `b ≤ 11`; and, by brute force over height vectors, the towers of width `w` with `b` blocks and `k − 1` descents number `N(w, k) C(b + w − k, w − 1)` for `w ≤ 6`, `b ≤ 8`. The undivided tower identity is the one verified on [[tower-narayana-polynomial](pages/tower-narayana-polynomial.md)].
