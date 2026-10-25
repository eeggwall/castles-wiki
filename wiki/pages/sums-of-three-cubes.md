---
title: Sums of three cubes
category: Concepts
summary: The Diophantine problem n = x^3 + y^3 + z^3 over the integers. No n = 4, 5 (mod 9) is a sum of three cubes, and Heath-Brown conjectured (1992) that every other n has infinitely many representations, which would make membership a residue test; whether membership is decidable is unknown. Below 1000 the unsolved n not excluded mod 9 are 114, 390, 627, 633, 732, 921, 975; 33 and 42 were solved in 2019 by Booker and by Booker and Sutherland. The sums of three positive cubes (A003072) are conjectured to have positive density; their fraction below 10^8 is 0.101. The castle side of the question is on sum-of-three-cubes-castles.
tags: [concept, number-theory, sum-of-cubes, diophantine, mod-9, heath-brown, booker-sutherland, waring, oeis]
sources: [oeis-encyclopedia]
created: 2026-09-20
updated: 2026-10-25
---

# Sums of three cubes

Which integers `n` can be written as `n = x^3 + y^3 + z^3` with `x, y, z` in `Z`, signs allowed? With signs allowed the cubes can be enormous while their sum is small, so a search for representations has no bound, and it is unknown whether membership is decidable.[^1] The question enters the castle wiki through the castle counts: `A^e(6, 4) = 1729 = 9^3 + 10^3 + 0^3 = 1^3 + 12^3 + 0^3` ([[hardy-ramanujan-castle](pages/hardy-ramanujan-castle.md)]), and [[sum-of-three-cubes-castles](pages/sum-of-three-cubes-castles.md)] asks which castle counts are sums of three cubes. `A^e(w, h)` is the number of castles of width `w` and height `h` with an even number of blocks, the count the Project Euler problem writes `F(w, h)` ([[castle-notation](pages/castle-notation.md)]).

## The obstruction modulo 9

Every cube is `0` or `±1` modulo 9, so a sum of three cubes is `0, ±1, ±2` or `±3` modulo 9 and never `±4`. Hence no `n ≡ 4, 5 (mod 9)` is a sum of three cubes, and "it is unknown whether this necessary condition is sufficient".[^1] The integers that pass the test are A060464, "Numbers that are not congruent to 4 or 5 mod 9": `0, 1, 2, 3, 6, 7, 8, 9, 10, 11, 12, 15, …`, seven of every nine integers. Its entry carries the comment "Conjecture: n is a sum of three cubes iff n is in this sequence"; the complement is A156638, "Numbers k such that k^2 + 2 == 0 (mod 9)", the integers congruent to 4 or 5 modulo 9.[^2]

**Heath-Brown's conjecture (1992).** Every `n` not congruent to 4 or 5 modulo 9 has infinitely many representations as a sum of three cubes. If it holds, membership is decided by computing `n` modulo 9.[^1]

## Representations found by search

| `n` | representation | found by |
|---|---|---|
| 33 | `8866128975287528^3 + (−8778405442862239)^3 + (−2736111468807040)^3` | Booker, 2019 |
| 42 | `(−80538738812075974)^3 + 80435758145817515^3 + 12602123297335631^3` | Booker and Sutherland, 2019, with 1.3 million hours of computing on the Charity Engine grid |
| 795 | `(−14219049725358227)^3 + 14197965759741571^3 + 2337348783323923^3` | Booker, 2019 |
| 906 | `(−74924259395610397)^3 + 72054089679353378^3 + 35961979615356503^3` | presented by Booker, 2019 |
| 3 (third representation) | `569936821221962380720^3 + (−569936821113563493509)^3 + (−472715493453327032)^3` | Booker and Sutherland, with a further 4 million computer-hours, settling Mordell's 1953 question |

Every triple in the table sums to its `n` in exact integer arithmetic.[^exec] After Huisman's 2016 search, "all n < 100 that are unequal to 4 or 5 modulo 9 have a solution, with at most two exceptions, 33 and 42", both solved in 2019. Booker showed that none of the then unresolved `n ≤ 1000` has a solution with `|z| ≤ 10^16`. "The only remaining unsolved cases up to 1,000 are the seven numbers 114, 390, 627, 633, 732, 921, and 975", and 192, 375 and 600 have no known primitive solutions (solutions with `gcd(x, y, z) = 1`).[^1] The number 906 is a castle count, `A^e(5, 5) = 906`.[^exec]

**Polynomial families for 1 and 2.** Mahler's identity `(9t^4)^3 + (3t − 9t^4)^3 + (1 − 9t^3)^3 = 1` (1936) and Verebrusov's `(1 + 6t^3)^3 + (1 − 6t^3)^3 + (−6t^2)^3 = 2` (1908, quoted by Mordell) give infinitely many representations of 1 and 2, and scaling gives representations of every cube and every twice a cube. By Mordell (1942), 1 and 2 are the only numbers with representations parameterized by quartic polynomials in this way.[^1][^exec] Ramanujan's family `a_n^3 + b_n^3 = c_n^3 + (−1)^n` is of another kind: the sequences `a_n, b_n, c_n` satisfy a linear recurrence with constant coefficients ([[hardy-ramanujan-castle](pages/hardy-ramanujan-castle.md)]).

## Sums of three positive cubes

With `x, y, z ≥ 1` the search for each `n` is finite. The representable numbers are A003072, "Numbers that are the sum of 3 positive cubes": `3, 10, 17, 24, 29, 36, 43, 55, 62, 66, 73, 80, 81, 92, 99, 118, 127, …`.[^3] Wikipedia states the following for sums of three non-negative cubes, which differ from sums of three positive cubes by the sums of at most two cubes, a set of density 0: "It is conjectured that the representable numbers have positive natural density"; Wooley showed that `Ω(n^0.917)` of the numbers from 1 to `n` are representable; and the density is at most `Γ(4/3)^3/6 = 0.1187`.[^1][^exec] The OEIS entry records "Wooley, improving on Davenport and others, shows that a(n) << n^1.0904" and "Wang has a (very) conditional proof that the sequence has positive density".[^3]

The fraction of the integers up to `N` that are sums of three positive cubes, by a sieve over all triples:[^exec]

| `N` | sums of three positive cubes `≤ N` | fraction |
|---|---|---|
| `10^3` | 126 | 0.126 |
| `10^4` | 1154 | 0.115 |
| `10^5` | 10831 | 0.108 |
| `10^6` | 104252 | 0.104 |
| `10^7` | 1021534 | 0.102 |
| `10^8` | 10098476 | 0.101 |

The fraction decreases through `10^8` and stays below the bound `0.1187`. [[sum-of-three-cubes-castles](pages/sum-of-three-cubes-castles.md)] uses `0.101` as the rate at which integers of the size of the castle counts are sums of three positive cubes.

The sums of two positive cubes are A003325 (`2, 9, 16, 28, 35, 54, 65, 72, 91, 126, 128, 133, …`), and the taxicab numbers A001235 are the sums of two positive cubes in more than one way, the first being 1729.[^4]

## Relation to the castles

1. **Residues of the castle counts.** If Heath-Brown's conjecture holds, a castle count is a sum of three cubes exactly when it is not 4 or 5 modulo 9. For each height `h`, `A^e(·, h)` mod 9 is eventually periodic in the width, since it satisfies a linear recurrence with integer coefficients ([[mod-p-observatory](pages/mod-p-observatory.md)]); [[mod-9-equidistribution](pages/mod-9-equidistribution.md)] computes how often the castle counts fall in the residues 4 and 5, a fraction that tends to `2/9`.
2. **Cubes are tower counts.** `T(k, 3) = (k+1)^3` is the number of towers of height at most `k` on a base of length 3 ([[castle-counting-formula](pages/castle-counting-formula.md)], the Lemma in the section *Tower count*). So `A^e(w, h) = a^3 + b^3 + c^3` with `a, b, c ≥ 1` says that the even-block castles of width `w` and height `h` are as many as the towers on a base of length 3 of heights at most `a − 1`, `b − 1` and `c − 1` taken together.
3. **An arithmetic question.** The recurrence of a castle count gives its residues but not its representations as sums of cubes, which have to be searched for.

## Related Concepts

- [[sum-of-three-cubes-castles](pages/sum-of-three-cubes-castles.md)] - which counts `A^e(w, h)`, `A(w, h)` and `A^o(w, h)` are sums of three cubes, signed and positive.
- [[hardy-ramanujan-castle](pages/hardy-ramanujan-castle.md)] - `A^e(6, 4) = 1729`, the taxicab number, and Ramanujan's family of near-misses.
- [[mod-9-equidistribution](pages/mod-9-equidistribution.md)] - the fraction of castle counts in the residues 4 and 5 modulo 9, which tends to `2/9`.
- [[mod-p-observatory](pages/mod-p-observatory.md)] - the periodicity of the castle counts modulo a prime.
- [[castle-counting-formula](pages/castle-counting-formula.md)] - the formula for `A^e(w, h)` and the tower count `T(k, L) = (k+1)^L`.
- [[oeis-index](pages/oeis-index.md)] - the directory of the A-numbers cited here.

## Footnotes

[^1]: https://en.wikipedia.org/wiki/Sums_of_three_cubes (read 2026-10-16) - "the cubes modulo 9 are 0, 1, and −1, and no three of these numbers can sum to 4 or 5 modulo 9. It is unknown whether this necessary condition is sufficient"; Mahler's and Verebrusov's families, "These can be scaled to obtain representations for any cube or any number that is twice a cube", "1 and 2 are the only numbers with representations that can be parameterized by quartic polynomials as above" (Mordell 1942); after Huisman (2016) "all n < 100 that are unequal to 4 or 5 modulo 9 have a solution, with at most two exceptions, 33 and 42"; the representations of 33 and 795 (Booker), Booker's "no solutions for n = 42 or any of the other unresolved n ≤ 1000 with |z| ≤ 10^16"; 42 (Booker and Sutherland, "1.3 million hours of computing on the Charity Engine global grid"); the third representation of 3 ("a further 4 million computer-hours", settling "a 65-year-old question of Louis J. Mordell"); "Booker also presented a representation for 906"; "The only remaining unsolved cases up to 1,000 are the seven numbers 114, 390, 627, 633, 732, 921, and 975, and there are no known primitive solutions (i.e. gcd(x, y, z) = 1) for 192, 375, and 600"; Heath-Brown (1992) "conjectured that every n unequal to 4 or 5 modulo 9 has infinitely many representations", "it is unknown whether representing numbers as sums of cubes is decidable", "If Heath-Brown's conjecture is true, the problem is decidable"; on non-negative cubes, "It is conjectured that the representable numbers have positive natural density", Wooley's Ω(n^0.917), and "The density is at most Γ(4/3)^3/6 ≈ 0.119".
[^2]: https://oeis.org/A060464 (read 2026-10-16) - "Numbers that are not congruent to 4 or 5 mod 9", data `0, 1, 2, 3, 6, 7, 8, 9, 10, 11, 12, 15, 16, …`; comments "Conjecture: n is a sum of three cubes iff n is in this sequence" and "Heath-Brown conjectures that n is a sum of three cubes in infinitely many ways iff n is in this sequence" (Greathouse, 2019), with the solutions for 33 and 42.
[^3]: https://oeis.org/A003072 (read 2026-10-16) - "Numbers that are the sum of 3 positive cubes", data `3, 10, 17, 24, 29, 36, 43, 55, 62, 66, 73, 80, 81, 92, 99, 118, 127, 129, …`; formula section "Wooley, improving on Davenport and others, shows that a(n) << n^1.0904. Wang has a (very) conditional proof that the sequence has positive density" (Greathouse, 2026).
[^4]: https://oeis.org/A003325 (read 2026-10-16) - "Numbers that are the sum of 2 positive cubes", data `2, 9, 16, 28, 35, 54, 65, 72, 91, 126, 128, 133, 152, …`; https://oeis.org/A001235 (read 2026-10-16) - "Taxi-cab numbers: sums of 2 cubes in more than 1 way", first term 1729.
[^exec]: Verified by execution (Python 3.11 with SymPy and NumPy, 2026-10-16): each of the five triples cubed and summed exactly to its `n`; Mahler's and Verebrusov's identities expanded symbolically to 1 and 2; `Γ(4/3)^3/6 = 0.118679`; `A^e(5, 5) = 906` and `A^e(6, 4) = 1729` from the formula of castle-counting-formula; the density table by a boolean sieve over all `a ≤ b ≤ c` with `a^3 + b^3 + c^3 ≤ 10^8`, cumulated at each power of ten.
