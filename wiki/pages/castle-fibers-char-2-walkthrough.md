---
title: Castle fibers seminar - char_2 across the primes
category: Concepts
summary: The seminar walk-through for the "Castle fibers" arc - one castle recurrence, P(2, L) = 1, 1, 3, 9, 19, 33, 59, 121, …, with characteristic polynomial char_2 = (x − 2)(x² − x + 2), followed through its fibers. p = 5 is a plain two-point fiber (period 24); p = 101 is the same shape, with the idempotent 76x² + 25x + 51 isolating the eigenvalue 2 (period 3400); p = 11 has three points because the quadratic splits exactly when p ≡ 1, 2, 4 (mod 7); p = 7 is fat, with a nilpotent, 6 ideals against 4 idempotents, and period 21 = 3 × 7; p = 2 is where everything meets, with x not a unit. Over Q the fibers assemble into P(2, L) = 2^L − U_L, the two parity sectors, split by the idempotent (x² − x + 2)/4, and over Z that idempotent and the inverse of x both need 1/2 because the sectors meet at (2, x); the norm relation α·ᾱ = 2 is the prime 2 splitting in Q(√−7). One pinned board summarizes all six primes.
tags: [concept, castle, seminar, pedagogy, teaching, ring, spectrum, finite-field, chinese-remainder-theorem, idempotent, nilradical, frobenius, quadratic-reciprocity, signed-tower-count, parity-sector]
sources: [calugareanu-hamburg-exercises-basic-ring-theory, oeis-mining-pe502]
created: 2026-09-26
updated: 2026-09-26
---

# Castle fibers seminar - `char_2` across the primes

**Thesis.** One castle recurrence lives in one integer ring, and every mod-`p` experiment on the wiki is a look at one fiber of that ring. Follow a single example through six primes and then back to `Q` and `Z`, and the separate facts of the "Castle fibers" arc become one picture.

**Format.** About 60 minutes at one blackboard, seven stops. Each stop is one prime (or `Q`, or `Z`), one computation, and one idea. Everything quoted is pinned under the board in the Snippet section and on [[castle-snippets-number-theory](pages/castle-snippets-number-theory.md)]. The theory pages behind it are [[castle-ring-spectrum](pages/castle-ring-spectrum.md)], [[chinese-remainder-theorem](pages/chinese-remainder-theorem.md)] and [[idempotent-decomposition](pages/idempotent-decomposition.md)].

## Stop 0 - the object

The signed tower count at tower height `k = 2` ([[signed-tower-count](pages/signed-tower-count.md)]), that is towers of height `≤ 2` above the bottom row, so castles of height `≤ 3` ([[castle-notation](pages/castle-notation.md)]), is

```
P(2, L) = 1, 1, 3, 9, 19, 33, 59, 121, 259, 529, 1035, 2025, …        P(L) = 3P(L−1) − 4P(L−2) + 4P(L−3)
```

Its characteristic polynomial is `char_2 = x³ − 3x² + 4x − 4 = (x − 2)(x² − x + 2)`.[^1] The recurrence lives in the ring `A = Z[x]/(char_2)`: integer polynomials, with `x³` replaced by `3x² − 4x + 4` whenever it appears, so that **multiplying by `x` is one step of the recurrence** ([[castle-cryptography-ring](pages/castle-cryptography-ring.md)] §3).

Reducing mod a prime `p` gives the **fiber** `A/pA = F_p[x]/(char_2 mod p)`. Its points are the distinct irreducible factors of `char_2 mod p` ([[castle-ring-spectrum](pages/castle-ring-spectrum.md)], "The picture"). The seminar reads one fiber per stop.

## Stop 1 - `p = 5`: a plain fiber

`char_2 ≡ (x − 2)(x² − x + 2) (mod 5)`, and the quadratic stays irreducible (its discriminant `−7 ≡ 3` is not a square mod 5). So the fiber has **two points**, with residue fields `F_5` and `F_25`. By the Chinese Remainder Theorem the ring splits:

```
F_5[x]/(char_2)  ≅  F_5 × F_25            (evaluate at x = 2;  reduce mod x² − x + 2)
```

Nothing repeats, so the fiber is **semisimple**, a product of fields with no nilpotents. Its 4 ideals are exactly the 4 idempotents (`0`, `1`, and the two "unit vectors"). The mod-5 period is `ord(x) = 24`: `ord(2) = 4` in `F_5^*`, and the root of the quadratic has order dividing `24 = 5² − 1` in `F_25^*`.[^2]

*Idea:* reducing mod `p` turns eigenvalues into elements of finite fields, and the period is the `lcm` of their orders ([[finite-fields](pages/finite-fields.md)]).

## Stop 2 - `p = 101`: the same shape, and the idempotent

`101 ≡ 3 (mod 7)`, and the shape is the same as at 5: two points, `F_101 × F_{101²}`. The period is now `3400 = lcm(100, 3400)` ([[castle-ring-invariant-factors](pages/castle-ring-invariant-factors.md)] §1).

The split can be written as explicit elements. The **idempotent** that is `1` on the `(x − 2)` point and `0` on the other is

```
e_1  =  (x² − x + 2)/4  =  76x² + 25x + 51   (mod 101)          e_1² = e_1,   e_1 + e_2 = 1,   e_1 e_2 = 0
```

It is Lagrange interpolation: the other factor, divided by its value at `x = 2`. Since `x·(x² − x + 2) ≡ 2·(x² − x + 2)`, multiplying by `e_1` keeps only the eigenvalue 2: **`x^L · e_1 = 2^L · e_1`** ([[idempotent-decomposition](pages/idempotent-decomposition.md)]).[^3]

*Idea:* a splitting of a ring and its idempotents are the same thing (exercise 17.19).

## Stop 3 - `p = 11`: three points, and why

Mod 11 the quadratic splits too: `char_2 ≡ (x − 2)(x + 4)(x − 5)`, three points, all `F_11`, and 8 idempotents. The period drops to 10, since every eigenvalue lives in `F_11^*`.

Which primes do this? The quadratic `x² − x + 2` splits mod an odd `p ≠ 7` exactly when its discriminant `−7` is a square mod `p`, and quadratic reciprocity turns that into a condition on `p mod 7`:

```
x² − x + 2 splits mod p   ⇔   p ≡ 1, 2, 4 (mod 7)          (checked for every prime 3 ≤ p < 200, p ≠ 7)
```

So `11 ≡ 4` splits, while `3, 5, 101` (`≡ 3, 5, 3`) do not.[^4] It is the `char_2` analogue of the `char_1` rule "`p ≡ 1 (mod 4)`" on [[finite-fields](pages/finite-fields.md)].

*Idea:* the shape of every fiber is decided by one number-theoretic rule. The observatory's factor signatures are not random ([[mod-p-observatory](pages/mod-p-observatory.md)]).

## Stop 4 - `p = 7`: a fat fiber

`7` divides the discriminant `disc(char_2) = −112 = −2⁴·7`, and the fiber gets a repeated factor: `char_2 ≡ (x − 2)(x + 3)² (mod 7)`. It still has two points, but it is **fat**:

- `(x − 2)(x + 3)` is a nonzero **nilpotent**: its square is a multiple of `char_2`. The fiber is not semisimple.
- It has **6 ideals but only 4 idempotents**. The extra ideals `(x + 3)` and `(x − 2)(x + 3)` cut partway into the fat factor.
- **Frobenius** `a ↦ a^7`, a linear map on the fiber, loses rank: rank 2 instead of 3. Its fixed space still has dimension 2, one per point.
- The period is **`21 = 3 × 7`**. Throw away the nilpotents and the reduced fiber `F_7[x]/((x − 2)(x + 3))` has period 3; the nilradical contributes exactly the extra factor 7 ([[castle-ring-spectrum](pages/castle-ring-spectrum.md)] §3).[^5]

*Idea:* repeated factors mean nilpotents, and nilpotents mean an extra factor of `p` in the period. The book's local-ring exercise `R/M^n` (13.26) is the reason `F_7[x]/((x + 3)²)` behaves like one fat point.

## Stop 5 - `p = 2`: where everything meets

`char_2 ≡ x²(x + 1) (mod 2)`. Two points, `(2, x)` and `(2, x + 1)`, and the first is fat. Here even `x` fails to be a unit: it lies in the fat point. Every castle count agrees mod 2, since `P(2, L) ≡ T(2, L) = 3^L ≡ 1` (signs disappear mod 2), so the sequence mod 2 is `1, 1, 1, …`.[^6]

*Idea:* 2 is the one prime that divides `char_2(0) = 4` (the product of the eigenvalues), and the next two stops show everything difficult happens here.

## Stop 6 - over `Q`: the two sectors

Stop dividing by `p` and work with fractions. Over `Q`, `char_2` has two irreducible factors, the two **parity sectors** of [[tower-parity-sectors](pages/tower-parity-sectors.md)]:

```
Q[x]/(char_2)  ≅  Q × Q(√−7)          P(2, L)  =  2^L  −  U_L,     U_L = 0, 1, 1, −1, −3, −1, 5, 7, −3, −17, …
```

`2^L` is the even-last-column sector (the dominant eigenvalue 2) and `−U_L` is the odd sector, where `U_L` is the Lucas sequence of the roots `α, ᾱ = (1 ± √−7)/2` (OEIS A107920).[^7] The idempotent that separates the sectors is the rational element

```
e  =  (x² − x + 2)/4
```

and **Stop 2's `e_1` is this `e` reduced mod 101**, with `1/4 ≡ 76`. Every odd fiber inherits the sector split from this one rational element.

*Idea:* the fibers are shadows of one object over `Q`. Their idempotents come from the rational idempotent by reduction.

## Stop 7 - over `Z`: the whole picture

Now the integer ring `A = Z[x]/(char_2)` itself.

- **The sectors meet at `(2, x)`.** Mod 2 the sector factors become `x − 2 ≡ x` and `x² − x + 2 ≡ x(x + 1)`, which share the point `(2, x)`. Their resultant is `4 = 2²`: they can only meet over 2.[^8]
- **So `A` has no idempotents besides 0 and 1.** A splitting of `A` would split its spectrum in two, but the two sectors are glued at `(2, x)`. The rational `e = (x² − x + 2)/4` needs the `1/4`. The same happens to `x`: `x·(x² − 3x + 4) = 4` in `A`, so `x^{−1} = (x² − 3x + 4)/4` exists in every odd fiber but not in `A`. Everything that goes wrong between `A` and its fibers goes wrong at 2, like `5` being idempotent mod 10 but not in `Z` ([[castle-ring-spectrum](pages/castle-ring-spectrum.md)] §5).
- **The only fat fibers are over 2 and 7**, the primes dividing `disc(char_2) = −112`.
- **2 splits in `Q(√−7)`.** Mod 2 the quadratic `x² − x + 2 ≡ x(x + 1)` has two roots, so the prime 2 splits into `α` and `ᾱ` in the ring of integers `Z[(1 + √−7)/2]`, with `α·ᾱ = 2`. This is the same norm relation that explains the `d = 3` linear-complexity deficits of the castle cryptosystem ([[castle-ring-invariant-factors](pages/castle-ring-invariant-factors.md)] §5), now read as the prime 2 splitting.[^9]

*Idea:* one integer ring, one spectrum. The observatory's rows are its fibers, the sectors are its components, and the prime 2 is where they meet.

## The board

Everything above on one table, `char_2` across six primes:

| `p` | `char_2 mod p` (degree, multiplicity) | points | fat? | Frobenius (rank, fixed dim) | ideals / idempotents | period of `P(2, ·) mod p` |
|---|---|---|---|---|---|---|
| 2 | (1,1), (1,**2**) | 2 | yes | (2, 2) | 6 / 4 | - (`x` not a unit; sequence `≡ 1`) |
| 3 | (1,1), (2,1) | 2 | no | (3, 2) | 4 / 4 | 8 |
| 5 | (1,1), (2,1) | 2 | no | (3, 2) | 4 / 4 | 24 |
| 7 | (1,1), (1,**2**) | 2 | yes | (2, 2) | 6 / 4 | 21 = 3 × 7 |
| 11 | (1,1), (1,1), (1,1) | 3 | no | (3, 3) | 8 / 8 | 10 |
| 101 | (1,1), (2,1) | 2 | no | (3, 2) | 4 / 4 | 3400 |

Reading down the columns is the seminar's summary. For odd `p ≠ 7` the number of points is decided by `p mod 7`. Fat rows are exactly the primes dividing `−112`. Frobenius rank drops exactly on fat rows, and its fixed dimension always equals the number of points. Ideals equal idempotents exactly on non-fat rows.

## Snippet

The board is one call, built from the snippets on [[castle-snippets-number-theory](pages/castle-snippets-number-theory.md)] (`char_k`, `x_order`, `frobenius_profile`, `fiber_ideal_count`):

```python
def fiber_board(k, primes):
    rows = []
    for p in primes:
        fl = sp.factor_list(sp.Poly(char_k(k), x, modulus=p))[1]
        shape = [(g.degree(), m) for g, m in fl]
        period = x_order(char_k(k), p) if p > 2 else None      # x is not a unit mod 2
        rows.append((p, shape, frobenius_profile(k, p), fiber_ideal_count(k, p), period))
    return rows
```

```
>>> for row in fiber_board(2, [2, 3, 5, 7, 11, 101]): print(row)
(2, [(1, 1), (1, 2)], (2, 2), (6, 4), None)
(3, [(1, 1), (2, 1)], (3, 2), (4, 4), 8)
(5, [(1, 1), (2, 1)], (3, 2), (4, 4), 24)
(7, [(1, 1), (1, 2)], (2, 2), (6, 4), 21)
(11, [(1, 1), (1, 1), (1, 1)], (3, 3), (8, 8), 10)
(101, [(1, 1), (2, 1)], (3, 2), (4, 4), 3400)
```

## Exercises for the room

1. Predict the board row for `p = 29` before computing it. (`29 ≡ 1 (mod 7)`: three points, not fat, Frobenius `(3, 3)`, 8 ideals and 8 idempotents; the period divides `28`.)
2. Run `fiber_board(4, [3, 5, 107])` and find the fat rows. (`disc(char_4) = −2¹⁶·3·107`.)
3. Write down the three idempotents of the `p = 11` fiber as Lagrange polynomials through `2, −4, 5`, and check that the rational `e` of Stop 6 reduces to the one at `2`, and `1 − e` to the sum of the other two.
4. Explain why every fiber of `char_2`, including `p = 2`, has at least two points, so no choice of prime lets the cryptosystem of [[castle-cryptography-ring](pages/castle-cryptography-ring.md)] avoid a CRT split of `char_2`. Then explain, using Stop 7, why the idempotents of the `p = 2` fiber cannot be reductions of Stop 6's `e`.

## Appearances in Sources

- [[calugareanu-hamburg-exercises-basic-ring-theory](pages/calugareanu-hamburg-exercises-basic-ring-theory.md)] - the ring theory behind each stop: CRT (17.20), idempotents and splittings (17.19), local rings (13.26), nilradical (13.11), Frobenius and Artin-Schreier (5.14, 5.16), what reduction preserves (4.10).
- [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] - `P(2, ·)` and `char_2`.

## Related Concepts

- [[castle-ring-spectrum](pages/castle-ring-spectrum.md)] - the theory page this seminar walks through.
- [[chinese-remainder-theorem](pages/chinese-remainder-theorem.md)] / [[idempotent-decomposition](pages/idempotent-decomposition.md)] - Stops 1-3 and 6.
- [[castle-ring-invariant-factors](pages/castle-ring-invariant-factors.md)] - unit groups and periods of the same fibers; the `α·ᾱ = 2` deficit of Stop 7.
- [[tower-parity-sectors](pages/tower-parity-sectors.md)] - the two sectors of Stop 6.
- [[finite-fields](pages/finite-fields.md)] / [[mod-p-observatory](pages/mod-p-observatory.md)] - Stops 1-4 one prime at a time.
- [[castle-cryptography-ring](pages/castle-cryptography-ring.md)] - the same ring used as a cryptosystem.
- [[tower-recursion-master-class](pages/tower-recursion-master-class.md)] - the companion seminar for the counting side.
- [[castle-snippets-number-theory](pages/castle-snippets-number-theory.md)] - the functions the board uses.
- [[hardin-identity-seminar](pages/hardin-identity-seminar.md)] - the seminar on the same parity sectors from the combinatorial side.
- [[hear-the-shape-seminar](pages/hear-the-shape-seminar.md)] - the seminar on castle spectra and Kac's question.
- [[oeis-mining-seminar](pages/oeis-mining-seminar.md)] - the seminar on OEIS mining as a research method.


## Footnotes

[^1]: [[oeis-mining-pe502](pages/oeis-mining-pe502.md)] `mine-notes.md` §"Vein 1" L31-37 [synthesis] - "P(2): x^3 - 3x^2 + 4x - 4 (= (x-2)(x^2-x+2))" in the `P(k, ·)` family. The terms `1, 1, 3, 9, 19, 33, 59, 121, 259, 529, 1035, 2025` were recomputed from the recurrence `P(L) = 3P(L−1) − 4P(L−2) + 4P(L−3)` (2026-09-26) and match `p_signed(2, L)` on [[castle-snippets-number-theory](pages/castle-snippets-number-theory.md)] through `L = 9`.
[^2]: Verified by execution (Python 3.10, SymPy, 2026-09-26): `sp.factor_list(char_2, modulus=5)` gives `(x − 2)(x² − x + 2)`; `ord(x) = 24` in `F_5[x]/(char_2)` by stripping prime factors of the unit-group order `4 · 24`; `ord(2 mod 5) = 4`. The CRT split is [[calugareanu-hamburg-exercises-basic-ring-theory](pages/calugareanu-hamburg-exercises-basic-ring-theory.md)] Ex. 17.20.
[^3]: Verified by execution (Python 3.10, SymPy, 2026-09-26) under `crt_idempotents` on [[castle-snippets-number-theory](pages/castle-snippets-number-theory.md)]: `−25x² + 25x − 50 ≡ 76x² + 25x + 51 (mod 101)` is idempotent mod `char_2`, and the pair sums to 1 with product 0. Splitting ⇔ idempotent is [[calugareanu-hamburg-exercises-basic-ring-theory](pages/calugareanu-hamburg-exercises-basic-ring-theory.md)] Ex. 17.19.
[^4]: Verified by execution (Python 3.10, SymPy, 2026-09-26): for every prime `3 ≤ p < 200`, `p ≠ 7`, `x² − x + 2` has two factors mod `p` iff `p mod 7 ∈ {1, 2, 4}`; `char_2 mod 11 = (x − 2)(x + 4)(x − 5)`, period 10. The rule is quadratic reciprocity, `(−7/p) = (p/7)` for odd `p ≠ 7`.
[^5]: Verified by execution (Python 3.10, SymPy, 2026-09-26): `char_2 mod 7 = (x − 2)(x + 3)²`; `((x − 2)(x + 3))² ≡ 0 mod (char_2, 7)`; ideal count `∏ (m_i + 1) = 6`, idempotents `2^2 = 4`; Frobenius rank 2 and fixed dimension 2 (`frobenius_profile`); `ord(x) = 21` in the fiber and `3` in `F_7[x]/((x − 2)(x + 3))` (`reduced_period`). The local-ring fact is [[calugareanu-hamburg-exercises-basic-ring-theory](pages/calugareanu-hamburg-exercises-basic-ring-theory.md)] Ex. 13.26.
[^6]: Verified by execution (Python 3.10, SymPy, 2026-09-26): `char_2 mod 2 = x²(x + 1)`; `P(2, L) mod 2 = 1` for `L ≤ 11`. `P ≡ T (mod 2)` because the signed and unsigned counts differ only in signs, and `T(2, L) = 3^L` ([[signed-tower-count](pages/signed-tower-count.md)]).
[^7]: Verified by execution (2026-09-26): with `A = 1` and `U_L` satisfying `U_L = U_{L−1} − 2U_{L−2}`, `U_0 = 0`, `U_1 = 1`, the identity `P(2, L) = 2^L − U_L` holds for `L ≤ 11` (e.g. `529 = 512 + 17`, `U_9 = −17`). `−U_L = P_odd(2, L)` is the odd-sector sequence identified with `−A107920` on [[tower-parity-sectors](pages/tower-parity-sectors.md)]; the rational idempotent `(x² − x + 2)/4` is pinned under `sector_idempotent(2)` on [[castle-snippets-number-theory](pages/castle-snippets-number-theory.md)].
[^8]: Verified by execution (Python 3.10, SymPy, 2026-09-26): `sp.resultant(x − 2, x² − x + 2, x) = 4`; `x·(x² − 3x + 4) = char_2 + 4`, so `x·(x² − 3x + 4) ≡ 4` in `A` (`x_inverse(2)` on [[castle-snippets-number-theory](pages/castle-snippets-number-theory.md)]). The failure of idempotents and units to lift is [[calugareanu-hamburg-exercises-basic-ring-theory](pages/calugareanu-hamburg-exercises-basic-ring-theory.md)] Exs. 12.19 and 4.10.
[^9]: `x² − x + 2 ≡ x(x + 1) (mod 2)` has two distinct roots, so by the Dedekind criterion 2 splits into two primes of norm 2 in `Z[(1 + √−7)/2]`, generated by the roots `α, ᾱ = (1 ± √−7)/2`, whose product is the constant term 2 (Vieta). The same relation `α·ᾱ = 2` is derived and used on [[castle-ring-invariant-factors](pages/castle-ring-invariant-factors.md)] §5.
