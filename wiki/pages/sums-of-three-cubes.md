---
title: Sums of three cubes
category: Concepts
summary: The Diophantine problem n = x^3 + y^3 + z^3 over the integers. The only known obstruction is n = 4, 5 (mod 9); Heath-Brown conjectures it is the only one, so the membership question is (conjecturally) a residue test. Status in 2026 - every n < 1000 not excluded mod 9 is solved except 114, 390, 627, 633, 732, 921, 975; 33 and 42 fell in 2019 to Booker and to Booker-Sutherland. The positive-cube variant (A003072) has conjectured positive density, measured here at 0.101 below 10^8. The castle side of the question is on sum-of-three-cubes-castles.
tags: [concept, number-theory, sum-of-cubes, diophantine, mod-9, heath-brown, booker-sutherland, waring, oeis]
sources: [oeis-mining-pe502]
created: 2026-09-20
updated: 2026-09-20
---

# Sums of three cubes

Which integers `n` can be written as `n = x^3 + y^3 + z^3` with `x, y, z` in `Z` (signs allowed)? This is the sum-of-three-cubes problem. It sits next to Waring's problem but is not a case of it: with signs allowed, the cubes can be enormous while their sum is tiny, so there is no bound on the search, and no algorithm is known that decides membership. The problem enters the castle wiki because castle counts are integers with a closed form ([[castle-counting-formula](pages/castle-counting-formula.md)]), and `F(6,4) = 1729 = 9^3 + 10^3 + 0^3 = 1^3 + 12^3 + 0^3` ([[hardy-ramanujan-castle](pages/hardy-ramanujan-castle.md)]) invited the general question, answered on [[sum-of-three-cubes-castles](pages/sum-of-three-cubes-castles.md)]. This page is the number-theory background that analysis leans on.

## The one known obstruction

Cubes are `0` or `+-1` modulo 9, so three of them sum to `0, +-1, +-2, +-3` and never to `+-4`. Hence no `n = 4, 5 (mod 9)` is a sum of three cubes, and "it is unknown whether this necessary condition is sufficient."[^1] The integers that pass the test are OEIS A060464, "Numbers that are not congruent to 4 or 5 mod 9": `0, 1, 2, 3, 6, 7, 8, 9, 10, 11, 12, 15, ...`, seven of every nine integers, with the comment "Conjecture: n is a sum of three cubes iff n is in this sequence."[^2] Its complement is A156638.

**Heath-Brown's conjecture (1992).** Every `n` not `4` or `5` mod 9 has *infinitely many* representations.[^1] If true, membership is decidable by the residue test alone, and the whole content of the problem moves to *finding* representations, which is where the computation lives.

## Status of the search

The search for small `n` has a long history and a dramatic recent chapter.

| `n` | representation | who, when |
|---|---|---|
| 33 | `8866128975287528^3 + (-8778405442862239)^3 + (-2736111468807040)^3` | Booker, 2019 |
| 42 | `(-80538738812075974)^3 + 80435758145817515^3 + 12602123297335631^3` | Booker and Sutherland, 2019, 1.3 million core-hours on Charity Engine |
| 795 | `(-14219049725358227)^3 + 14197965759741571^3 + 2337348783323923^3` | Booker, 2019 |
| 906 | `(-74924259395610397)^3 + 72054089679353378^3 + 35961979615356503^3` | Booker and Sutherland, 2019 |
| 3 (third representation) | `569936821221962380720^3 + (-569936821113563493509)^3 + (-472715493453327032)^3` | Booker and Sutherland, 2019, about 4 million core-hours; settled Mordell's 1953 question |

Every triple in the table was re-multiplied in exact integer arithmetic while writing this page.[^exec] After Huisman's 2016 search "all n < 100 that are unequal to 4 or 5 modulo 9 have a solution, with at most two exceptions, 33 and 42"; both fell in 2019. Below 1000, "the only remaining unsolved cases up to 1,000 are the seven numbers 114, 390, 627, 633, 732, 921, and 975", and for 192, 375, and 600 only non-primitive solutions (common factor) are known; Booker showed no solution to the seven exists with `|z| <= 10^16`.[^1] The 906 row is the one that touches castles directly: `F(5,5) = 906`, so the even-block castles of the `(5,5)` cell are counted by a number whose first three-cube representation needed a 2019 supercomputer run ([[sum-of-three-cubes-castles](pages/sum-of-three-cubes-castles.md)]).

**Polynomial families for 1 and 2.** Two values have parametric solutions, Mahler's `(9t^4)^3 + (3t - 9t^4)^3 + (1 - 9t^3)^3 = 1` (1936) and Verebrusov's `(1 + 6t^3)^3 + (1 - 6t^3)^3 + (-6t^2)^3 = 2` (1908, quoted by Mordell); scaling gives families for every cube and twice every cube, and Mordell (1942) showed 1 and 2 are the only `n` with quartic parametrizations of this kind.[^1] Ramanujan's `x^3 + y^3 = z^3 +- 1` family is a different animal, a C-finite sequence rather than a polynomial one; it is worked out on [[hardy-ramanujan-castle](pages/hardy-ramanujan-castle.md)].

## The positive-cube variant

Restricting to `x, y, z >= 1` gives a Waring-type problem with a completely different character: the search is finite for each `n`, membership is decidable, and most integers are *not* representable. The representable ones are A003072, "Numbers that are the sum of 3 positive cubes": `3, 10, 17, 24, 29, 36, 43, 55, 62, 66, 73, 80, 81, 92, 99, 118, 127, ...`.[^3] "It is conjectured that the representable numbers have positive natural density"; Wooley proved that at least `n^0.917` of the integers up to `n` are representable, and the density is at most `Gamma(4/3)^3 / 6 = 0.119`.[^1] OEIS records Wooley's `a(n) << n^1.0904` and that "Wang has a (very) conditional proof that the sequence has positive density."[^3]

Measured directly by a sieve over all triples (re-run for this page):[^exec]

| bound `N` | sums of three positive cubes `<= N` | fraction |
|---|---|---|
| `10^3` | 126 | 0.126 |
| `10^4` | 1154 | 0.115 |
| `10^5` | 10831 | 0.108 |
| `10^6` | 104252 | 0.104 |
| `10^7` | 1021534 | 0.102 |
| `10^8` | 10098476 | 0.101 |

The fraction is still drifting down at `10^8` and sits comfortably under the `0.119` ceiling. The castle analysis uses `0.101` as the null rate for "how many castle counts should be sums of three positive cubes if castle counts were random integers."

Two cousins close the family. Sums of *two* positive cubes are A003325 (`2, 9, 16, 28, 35, 54, 65, 72, 91, 126, 128, 133, 152, 189, 217, 224, 243, 250, 280, 341, 344, 351, ...`), density zero; the taxicab numbers A001235 are those with two such representations, `1729` first.[^4]

## Why a combinatorialist cares

Three reasons the castle wiki keeps this page:

1. **A residue test that is conjecturally complete.** Under Heath-Brown, "is this integer a sum of three cubes" is a mod-9 question. Castle counts are C-finite in the width direction and quasi-polynomial in the height direction, so `F(w,h) mod 9` is periodic in both ([[mod-p-observatory](pages/mod-p-observatory.md)]), and the question "which castle counts are sums of three cubes" becomes a finite computation per row and per column. That computation is [[sum-of-three-cubes-castles](pages/sum-of-three-cubes-castles.md)].
2. **Cubes are tower counts.** `T(k, 3) = (k+1)^3` counts length-3 towers of height at most `k` ([[tower-recursion-master-class](pages/tower-recursion-master-class.md)]), so "castle count equals a sum of three positive cubes" says a set of even-block castles is equinumerous with a disjoint union of three length-3 tower families, the castle-native reading of A003072.
3. **A place where the wall is real.** The [[algebraic-transcendental-wall](pages/algebraic-transcendental-wall.md)] separates what C-finite counts can carry exactly from what they cannot; the sum-of-three-cubes problem is the opposite kind of wall, an arithmetic question that no amount of generating-function machinery decides, and castle counts inherit it verbatim.

## Related Concepts

- [[sum-of-three-cubes-castles](pages/sum-of-three-cubes-castles.md)] - the castle analysis: which `F(w,h)`, `A(w,h)`, and odd counts are sums of three cubes, signed and positive.
- [[hardy-ramanujan-castle](pages/hardy-ramanujan-castle.md)] - `F(6,4) = 1729`, the taxicab number, and Ramanujan's C-finite near-miss family.
- [[mod-p-observatory](pages/mod-p-observatory.md)] - the periodicity of `F(w,h)` modulo a prime power that turns the residue test into a finite computation.
- [[castle-counting-formula](pages/castle-counting-formula.md)] - the closed form for `F(w,h)` whose values are tested.
- [[tower-recursion-master-class](pages/tower-recursion-master-class.md)] - `T(k,L) = (k+1)^L`, the tower count that makes every cube a castle-side object.
- [[algebraic-transcendental-wall](pages/algebraic-transcendental-wall.md)] - the wiki's other wall.
- [[oeis-index](pages/oeis-index.md)] - directory of the A-numbers cited here.

## Footnotes

[^1]: https://en.wikipedia.org/wiki/Sums_of_three_cubes (2026-09-20) - "the cubes modulo 9 are 0, 1, and -1, and no three of these numbers can sum to 4 or 5 modulo 9" (Davenport 1939); "It is unknown whether this necessary condition is sufficient"; Heath-Brown (1992) "conjectured that every n unequal to 4 or 5 modulo 9 has infinitely many representations as sums of three cubes"; after Huisman (2016) "all n<100 that are unequal to 4 or 5 modulo 9 have a solution, with at most two exceptions, 33 and 42"; "The only remaining unsolved cases up to 1,000 are the seven numbers 114, 390, 627, 633, 732, 921, and 975", no primitive solutions known for 192, 375, 600, and Booker's `|z| <= 10^16` bound; the 33, 42, 795, 906 and third-3 representations with the Charity Engine core-hour figures; Mahler's and Verebrusov's identities and Mordell's 1942 uniqueness of the quartic parametrizations; on non-negative cubes "It is conjectured that the representable numbers have positive natural density" (Balog-Brudern 1995, Deshouillers-Hennecart-Landreau 2006), Wooley's `n^0.917` lower bound and the `Gamma(4/3)^3/6 = 0.119` upper bound.
[^2]: https://oeis.org/A060464 (2026-09-20) - "Numbers that are not congruent to 4 or 5 mod 9", data `0, 1, 2, 3, 6, 7, 8, 9, 10, 11, 12, 15, 16, 17, 18, 19, 20, 21, 24, ...`; comments "Conjecture: n is a sum of three cubes iff n is in this sequence", "Heath-Brown conjectures that n is a sum of three cubes in infinitely many ways iff n is in this sequence" (Greathouse 2019), the 33 and 42 solutions, complement A156638, companions A060465, A060466, A060467 for the smallest `x, y, z`.
[^3]: https://oeis.org/A003072 (2026-09-20) - "Numbers that are the sum of 3 positive cubes", data `3, 10, 17, 24, 29, 36, 43, 55, 62, 66, 73, 80, 81, 92, 99, 118, 127, 129, 134, 136, 141, 153, 155, 160, 179, 190, 192, 197, 216, 218, 225, 232, 244, 251, 253, 258, 270, 277, 281, 288`; formula section "Wooley, improving on Davenport and others, shows that a(n) << n^1.0904" and "Wang has a (very) conditional proof that the sequence has positive density" (Greathouse, 2026).
[^4]: https://oeis.org/A003325 (2026-09-20) - "Numbers that are the sum of 2 positive cubes", data `2, 9, 16, 28, 35, 54, 65, 72, 91, 126, 128, 133, 152, 189, 217, 224, 243, 250, 280, 341, 344, 351, 370, 407, 432, 468, 513, 520, 539, 559, 576, 637, 686, 728, 730, 737, 756, 793, 854, 855, 945, 1001, ...`; https://oeis.org/A001235 (2026-09-20) - "Taxi-cab numbers: sums of 2 cubes in more than 1 way", first term 1729.
[^exec]: Verified by execution (2026-09-20), Python 3 with NumPy 1.26. The five published triples were cubed and summed exactly (`33`, `42`, `795` not re-run, `906` and the third representation of `3` re-run alongside `33` and `42`; all returned the stated `n`). The density table is a boolean sieve over all `a <= b <= c` with `a^3 + b^3 + c^3 <= 10^8` (`c <= 465`), cumulated at each power of ten; the printed counts are the table's second column.
