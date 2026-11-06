---
title: Feistel network - ciphers that map castles to castles
category: Concepts
summary: A Feistel network builds a permutation from functions that need not be invertible - a round adds a keyed function of one half of the input to the other half and swaps the halves - and a keyed family of rounds is a secret-key cipher. Its three shapes in the sources are balanced, generalized (halves of sizes N_left and N_right, Black and Rogaway) and maximally unbalanced (one half a single bit, which at N = 2^n is the Thorp shuffle, Morris, Rogaway and Stegers); cycle walking restricts a cipher to a subset at no loss of security. On castles the halves of a skyline read in base h are its left and right column halves, cycle walking from the h^w skylines onto the A(w, h) castles of height h costs (h^w + 1)/(A + 1) calls on average (1.34 at (13, 10)), and rank, encipher, unrank turns any cipher on [0, A − 1] into one on the castles. At (13, 10) the generalized Feistel bound covers about 2^9.4 chosen-plaintext queries and 16 passes of the Thorp shuffle about 2^28.5 chosen-ciphertext queries.
tags: [concept, castle, cryptography, cipher, secret-key, feistel, unbalanced-feistel, thorp-shuffle, cycle-walking, format-preserving-encryption, rank-unrank]
sources: [black-rogaway-2002-arbitrary-finite-domains, morris-rogaway-stegers-2009-thorp-shuffle]
created: 2026-11-05
updated: 2026-11-06
---

# Feistel network

## Description

A **cipher** is a family of permutations of one set, one permutation for each key. A **Feistel network** builds such permutations from round functions that need not be invertible. Split each point of the set into a left half and a right half. A round keeps the right half, adds a function `f_j` of it to the left half, and swaps the two:

```
(left, right)  ↦  (right, left + f_j(right))
```

The addition is taken in the left half's group: exclusive-or on bit strings, or addition modulo the size of the half. Subtracting `f_j(right)` undoes the round, so the network is a permutation whatever the round functions are, and a key that selects the round functions makes it a cipher.[^1] The symbols follow [[castle-notation](pages/castle-notation.md)], section *Cipher symbols*: `N` is the number of points, `t` the number of rounds, and `ν` the number of queries an attacker asks.

The sources treat three shapes:

- **Balanced.** Equal halves of `n/2` bits each, the construction Black and Rogaway cite to the IBM report on Lucifer, with security bounds by Luby and Rackoff for three and four rounds.[^2] With a fixed number of rounds, a balanced network realizes too few permutations to be information-theoretically secure much beyond `√N` queries, which is as far as the usual proofs reach; Morris, Rogaway and Stegers also recall that "a Feistel-determined permutation is always even".[^3]
- **Generalized.** Halves in `Z_{N_left}` and `Z_{N_right}` with `N_left·N_right ≥ N`, the sizes alternating from round to round; this is Black and Rogaway's `Fe[t, N_left, N_right]`, and their Theorem 2 bounds three rounds by about `((ν + N_left·N_right − N)² + ν²)(1/N_left + 1/N_right)/2`.[^4]
- **Maximally unbalanced.** One half a single bit: a round moves the first bit to the end and flips it by a function of the other `n − 1` bits. At `N = 2^n` this is the Thorp shuffle, and `4r` passes of `n` rounds resist about `N^{1−1/r}` chosen-ciphertext queries.[^5]

**Cycle walking** restricts a cipher on a larger set to a subset: apply it until the result lands in the subset. If the larger cipher is a uniformly random permutation, so is the restriction (Black and Rogaway's Theorem 1), and its cycles are the larger cipher's cycles with the points outside the subset erased.[^6]

A cipher is judged by the number of queries `ν` at which an attacker's **advantage**, how much more often it answers 1 against the cipher than against a uniformly random permutation, reaches 1/2.[^7] The public-key systems of [[castle-cryptography](pages/castle-cryptography.md)] are judged instead by the discrete-logarithm questions of [[castle-cryptography-round-two](pages/castle-cryptography-round-two.md)] (*The method*).

## Ciphers on castles

A castle of width `w` and height `h` is a skyline `(c_1, …, c_w)` with `1 ≤ c_i ≤ h` and some `c_i = h`, and there are `A(w, h) = h^w − (h − 1)^w` of them ([[castle-notation](pages/castle-notation.md)]). Three constructions turn a Feistel network into a cipher on castles.

**1. Column halves.** Read a skyline in `{1, …, h}^w` as the base-`h` number `Σ_i (c_i − 1) h^{i−1}`, column 1 the lowest digit. With `N_left = h^⌈w/2⌉` and `N_right = h^⌊w/2⌋`, the two halves of the generalized network are the first `⌈w/2⌉` columns and the remaining `⌊w/2⌋`, so each round adds a keyed function of one column half to the other, as base-`h` numbers with carries. The network permutes all `h^w` skylines.[^exec]

**2. Walking onto the castles.** Cycle walking from the `h^w` skylines onto the castles of height `h` enciphers the castles; its test of membership is whether some column reaches `h`. For a uniformly random permutation of `N′` points, the walk from a point of an `N`-point subset takes `(N′ + 1)/(N + 1)` calls on average, which here is `(h^w + 1)/(A(w, h) + 1)`:[^exec]

| `(w, h)` | (10, 2) | (8, 3) | (7, 4) | (6, 5) | (13, 10) |
|---|---|---|---|---|---|
| share of the castles in `{1, …, h}^w` | 0.999 | 0.961 | 0.867 | 0.738 | 0.746 |
| average calls | 1.00 | 1.04 | 1.15 | 1.36 | 1.34 |

At `(13, 10)` the `9^13` skylines below height 10 are about a quarter of the `10^13`, so the walk costs 1.34 calls.

**3. Rank, encipher, unrank.** [[song-as-castle](pages/song-as-castle.md)] ranks the castles of height `h` onto `[0, A − 1]` by the first column of height `h`, and unranks them. A cipher on `[0, A − 1]`, between rank and unrank, is a cipher on the castles. The cipher may itself pad: the generalized network runs on `N_left·N_right ≥ A` points, and the Thorp shuffle, whose theorems are proved for powers of two, on `2^n ≥ A` points, each walking back into `[0, A − 1]`.

**At `(13, 10)`,** with `A = 7,458,134,171,671`:

| construction | cipher runs on | padding | attack | queries at advantage 1/2 |
|---|---|---|---|---|
| generalized Feistel, 3 rounds, column halves `10^7 × 10^6` | the `10^13` skylines | none in the network; the walk to the castles takes 1.34 calls per castle | chosen plaintext | about `2^9.4` (674) |
| the same, with the castles as the domain | the `10^13` skylines | `9^13 ≈ 2.54·10^12` points | chosen plaintext | none: the bound exceeds 1 |
| generalized Feistel, 3 rounds, ranks split `2,673,773 × 2,789,367` | `[0, A + 19]` | 20 points | chosen plaintext | about `2^9.7` (816) |
| Thorp shuffle, 16 passes, on ranks | `[0, 2^43 − 1]` | 1.18 calls per castle | chosen ciphertext | about `2^28.5` |

The generalized bound says nothing once the padding exceeds about `√(N_left/2)` points for halves of equal size; that rules out taking the castles as the domain inside the skylines, and the square split of the ranks, `2,730,959²`, with 2,888,010 extra points.[^exec][^4] The Thorp shuffle covers about `2^19` times as many queries at the same size, against the stronger chosen-ciphertext attack.[^exec][^5]

**What the castle adds.** The castle supplies the domain, its rank and unrank, and the membership test of the walk; the security comes from the Feistel network and its proofs, which hold for any domain of the same size.

## Appearances in Sources

- [[black-rogaway-2002-arbitrary-finite-domains](pages/black-rogaway-2002-arbitrary-finite-domains.md)] - the prefix cipher, cycle walking (Theorem 1) and the generalized Feistel cipher (Theorem 2).
- [[morris-rogaway-stegers-2009-thorp-shuffle](pages/morris-rogaway-stegers-2009-thorp-shuffle.md)] - the Thorp shuffle as maximally unbalanced Feistel, proved secure by coupling.

## Related Concepts

- [[castle-cryptography](pages/castle-cryptography.md)] - the public-key series on the castle ring `F_p[x]/(char_k)`; this page is its secret-key counterpart.
- [[song-as-castle](pages/song-as-castle.md)] - the rank and unrank of the castles of height `h` used by construction 3, which also turn an 11-character video id into a castle.
- [[bayer-diaconis-1992-dovetail-shuffle](pages/bayer-diaconis-1992-dovetail-shuffle.md)] - the riffle shuffle, whose cut is binomial where the Thorp shuffle's is exactly in half.
- [[castle-notation](pages/castle-notation.md)] - the cipher symbols `N`, `N′`, `N_left`, `N_right`, `ν`, `t`, `r`, `f_j`.

## Footnotes

[^1]: [[black-rogaway-2002-arbitrary-finite-domains](pages/black-rogaway-2002-arbitrary-finite-domains.md)] §5 Fig. 3 L399-L436 and L451-L453 [synthesis] - each round sets `tmp ← (L + F_j(R)) mod a` (or `mod b`), `L ← R`, `R ← tmp`, and deciphering subtracts `F_j(L)`; "it is well-known that the Feistel construction produces a permutation"; [[morris-rogaway-stegers-2009-thorp-shuffle](pages/morris-rogaway-stegers-2009-thorp-shuffle.md)] Fig. 1 L66-L70 [synthesis] - the bit-string round sends `b ‖ x` to `x ‖ (b ⊕ F_K(x))`.
[^2]: [[black-rogaway-2002-arbitrary-finite-domains](pages/black-rogaway-2002-arbitrary-finite-domains.md)] §1 Related Work L167-L177 and reference 14 L634-L636 [synthesis] - a balanced Feistel network [14], Smith's 1971 IBM report on Lucifer, makes a block cipher on `2n` bits from a pseudorandom function on `n` bits, and Luby and Rackoff bound it for three and four rounds.
[^3]: [[morris-rogaway-stegers-2009-thorp-shuffle](pages/morris-rogaway-stegers-2009-thorp-shuffle.md)] §1 L185-L206 and Appendix B L929-L964 [synthesis] - balanced Feistel is information-theoretically insecure beyond `2^{n/2}` queries for a fixed number of rounds, by counting the permutations an `r`-round network realizes; L188 - "(recall that a Feistel-determined permutation is always even [28, Th 6.1])".
[^4]: [[black-rogaway-2002-arbitrary-finite-domains](pages/black-rogaway-2002-arbitrary-finite-domains.md)] §5 L379-L398, Theorem 2 L459-L497 and Appendix A L855-L870 [synthesis] - `Fe[r, a, b]` with `ab ≥ k` and alternating moduli `a`, `b`; the PRP advantage of three rounds is at most `((q + Δ)² + q²)/2^{n+1} · (⌈2^n/a⌉ + ⌈2^n/b⌉)` with `Δ = ab − k`, the surplus entering because one encipherment may visit every point of `[k, ab − 1]`.
[^5]: [[morris-rogaway-stegers-2009-thorp-shuffle](pages/morris-rogaway-stegers-2009-thorp-shuffle.md)] §1 L95-L128 and §4 L473-L545 [synthesis] - for `N = 2^n` the Thorp shuffle coincides with maximally unbalanced Feistel, whose round function takes `n − 1` bits to one bit; `n` rounds form a pass; Theorem 5 bounds the CCA advantage of `Th[N, r(4n − 2)]` by `(2q/(r + 1))(4nq/N)^r`, and `4r` passes give CCA security to `2^{n(1−1/r)}` queries.
[^6]: [[black-rogaway-2002-arbitrary-finite-domains](pages/black-rogaway-2002-arbitrary-finite-domains.md)] §4 L317-L367 [synthesis] - the cycle-walking cipher iterates `E_K` until it reaches a point of `M`; Theorem 1, `Cy_K` is a uniform random permutation of `M` when `E_K` is an ideal block cipher on `T ⊇ M`; the erased-cycle form is checked by execution, footnote exec.
[^7]: [[black-rogaway-2002-arbitrary-finite-domains](pages/black-rogaway-2002-arbitrary-finite-domains.md)] §2 L227-L241 [synthesis] - security is the maximum advantage of an adversary, the difference between the probabilities that it outputs 1 with the keyed oracle and with a random permutation; [[morris-rogaway-stegers-2009-thorp-shuffle](pages/morris-rogaway-stegers-2009-thorp-shuffle.md)] §4 L501-L513 [synthesis] - the number of queries for advantage 0.5 as the measure in the comparison of Thorp, Naor-Reingold and balanced Feistel bounds.
[^exec]: Verified by execution (Python 3.10 with NumPy 2.2 and SciPy 1.15, 2026-11-06): `bin/python/feistel_castle_ciphers.py`, run log `bin/python/feistel_castle_ciphers-run.log`. Item [1]: the base-`h` split of every skyline into column halves, and the generalized network with 3 to 5 rounds as a permutation of `[0, h^w − 1]` with its inverse, at five small sizes. Item [2]: the walk onto the castles of height `h` is a permutation whose cycles are the network's cycles with the skylines below height `h` deleted. Items [3] and [4]: over all permutations of 6 or 7 points, each permutation of the subset arises equally often, and the walk takes `(N′ + 1)/(N + 1)` calls on average. Item [5]: `A(w, h) = h^w − (h − 1)^w` against enumeration, and the table of shares and costs. Item [6]: Theorem 2 of Black and Rogaway at `(13, 10)` for the three splits of the table and the square split. Item [9]: Theorem 5 of Morris, Rogaway and Stegers at `n = 43` with 16 passes (`lg ν = 28.52`, against `lg ν = 9.40` for the column halves, a factor `2^19.1`), and `2^43/A(13, 10) = 1.18`.
