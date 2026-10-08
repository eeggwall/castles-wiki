---
title: 1-smooth Pell castles by area
category: Analyses
summary: Count 1-smooth Pell castles, anchored at height 1 and reaching exact height 3, by cells rather than columns. Each castle contributes z^w q^n, with width w and area n; setting q = 1 forgets area and setting z = 1 forgets width. Last-column equations and exact-height subtraction give area generating function q^6/((1-q-q^2)(1-q^2-2q^3-q^4-q^5)) and area growth 1.666301937, compared with silver-ratio growth by width. A brief height-2 comparison explains the golden factor and distinguishes unrestricted smooth castles from Fibonacci and ridge castles.
tags: [analysis, castle, 1-smooth, pell, fixed-height, area, generating-function, transfer-matrix, pedagogy]
sources: [pe502-pell-castle-strip]
created: 2026-10-07
updated: 2026-10-07
---

# 1-smooth Pell castles by area

## 1. Fix height 3, then choose what to count by

A 1-smooth castle has neighbouring column heights differing by at most 1. This page counts only **Pell castles**: the first column has height 1, the last column is free, and the maximum height is exactly 3:

```
c_1 = 1,      |c_{i+1} - c_i| <= 1,      max_i c_i = 3.
```

The main family stays at **exact height 3**. Only the width and area vary. Both block parities are included; there is no even-block restriction here. The family and its width counts are on [[pell-castle](pages/pell-castle.md)].[^definition] Section 5.5 briefly compares the height-2 family that enters the subtraction; it does not change which castles the Pell count includes.

For example, `(1, 2, 3, 2)` qualifies, while `(1, 2, 2, 1)` never reaches height 3 and `(1, 3, 2)` has a forbidden jump.

**Exact height is not just a ceiling.** A strip with ceiling 3 may stay entirely at heights 1 and 2. A castle of exact height 3 must visit height 3 at least once. That distinction will supply a subtraction when we derive the generating function.

## 2. One castle, two measurements

For a skyline `c = (c_1, ..., c_w)`:

- **Width `w`** is the number of columns.
- **Area `n = c_1 + ... + c_w`** is the number of cells, including the bottom row.

For `(1, 2, 3, 2)`, the width is 4 and the area is 8. Those measurements group castles differently:

- Counting by width puts it with every other width-4 castle, whatever their areas.
- Counting by area puts it with every other area-8 castle, whatever their widths.

Changing the grading does not change the castle rules. It changes which measurement is held equal when castles are counted together.

## 3. Record both measurements with two variables

Use `z` to record width and `q` to record area. A single castle of width `w` and area `n` contributes the monomial `z^w q^n`.

The smallest Pell examples are:[^examples]

| castle | width | area | contribution |
|---|---:|---:|---|
| `(1, 2, 3)` | 3 | 6 | `z^3 q^6` |
| `(1, 1, 2, 3)` | 4 | 7 | `z^4 q^7` |
| `(1, 2, 2, 3)` | 4 | 8 | `z^4 q^8` |
| `(1, 2, 3, 2)` | 4 | 8 | `z^4 q^8` |
| `(1, 2, 3, 3)` | 4 | 9 | `z^4 q^9` |

Add one contribution for every Pell castle. Define

```
C_3(z, q) = sum over Pell castles of z^width q^area.
```

Thus the coefficient of `z^w q^n` is the number of Pell castles with **both** width `w` and area `n`. The subscript 3 records the fixed exact height; it is not another variable being summed over.

For Pell castles, grouping the first terms by width gives:[^examples]

```
C_3(z, q) = z^3 q^6
           + z^4 (q^7 + 2q^8 + q^9)
           + z^5 (q^8 + 4q^9 + 4q^10 + 3q^11 + q^12)
           + terms of width 6 and above.
```

The coefficient 2 in `2z^4 q^8` means there are two Pell castles of width 4 and area 8. The two variables do not stand for two different castle families; they record two statistics of the same objects.

## 4. Forget one measurement by setting its variable to 1

### 4.1 Count by width: set q = 1

Every area weight becomes 1. For example,

```
q^7 + 2q^8 + q^9  ->  1 + 2 + 1 = 4.
```

The four width-4 castles are combined regardless of area. Likewise, the width-5 polynomial has coefficient sum `1 + 4 + 4 + 3 + 1 = 13`. So

```
C_3(z, 1) = z^3 + 4z^4 + 13z^5 + 38z^6 + 105z^7 + 280z^8 + ... .
```

The coefficient of `z^w` counts every Pell castle of width `w`.[^specializations]

### 4.2 Count by area: set z = 1

Every width weight becomes 1. Castles of the same area are now combined even when their widths differ.

For area 8, there are three castles:[^examples]

```
(1, 2, 2, 3)       width 4
(1, 2, 3, 2)       width 4
(1, 1, 1, 2, 3)    width 5
```

The width-4 term contributes `2q^8`, and the width-5 term contributes another `q^8`. Their sum is `3q^8`. The area series begins

```
C_3(1, q) = q^6 + q^7 + 3q^8 + 6q^9 + 11q^10 + 22q^11
           + 40q^12 + 74q^13 + 135q^14 + 242q^15 + ... .
```

The coefficient of `q^n` counts every Pell castle of area `n`.[^specializations]

**Setting a variable to 1 means forgetting that measurement, not requiring the measurement itself to equal 1.** Both specializations still count only castles of exact height 3.

Both operations produce finite coefficient sums: at a fixed width there are only finitely many allowed skylines, and at a fixed area the width is at most the area because every column contains at least one cell.

## 5. Derive the Pell generating function from columns

### 5.1 A column's weight

Appending any column increases width by 1. Its area contribution is its height:

| appended column | contribution to width | contribution to area | weight |
|---|---:|---:|---|
| height 1 | 1 | 1 | `zq` |
| height 2 | 1 | 2 | `zq^2` |
| height 3 | 1 | 3 | `zq^3` |

Multiplying the column weights gives the castle's weight. For example,

```
(1, 2, 3, 2):   (zq)(zq^2)(zq^3)(zq^2) = z^4 q^8.
```

The 1-smooth rule says that a height-1 column can follow heights 1 or 2, a height-2 column can follow heights 1, 2 or 3, and a height-3 column can follow heights 2 or 3.

### 5.2 First count strips with ceiling 3

Let `X_j(z, q)` count anchored strips that end at height `j`, with all columns at most 3. These strips do **not** yet have to reach 3. Sorting them by their last column gives

```
X_1 = zq   (1 + X_1 + X_2),
X_2 = zq^2 (X_1 + X_2 + X_3),
X_3 = zq^3 (X_2 + X_3).
```

For the first equation, the final height-1 column is either the whole one-column strip, accounting for the `1`, or follows a strip ending at height 1 or 2. The other equations have no one-column case because the first column must be height 1.

The total ceiling-3 strip function is `S_3 = X_1 + X_2 + X_3`. Solving these three linear equations gives[^derivation]

```
D_3(z, q) = 1 - z(q + q^2 + q^3) + z^2 q^4 + z^3 q^6,
S_3(z, q) = zq(1 - zq^3) / D_3(z, q).
```

The denominator comes from solving the counting equations. Its individual terms need not be interpreted as individual castles; the coefficients of the expanded rational function are the counts.

### 5.3 Subtract the strips that never reach 3

A ceiling-3 strip that never reaches 3 is a strip on heights 1 and 2. Its first column is 1, and each later column can independently be 1 or 2. Therefore

```
D_2(z, q) = 1 - z(q + q^2),
S_2(z, q) = zq / D_2(z, q).
```

This is the initial height-1 column, of weight `zq`, followed by a sequence of columns of weights `zq` or `zq^2`.

Requiring exact height 3 now gives[^derivation]

```
C_3(z, q) = S_3(z, q) - S_2(z, q)
          = z^3 q^6 (1 - zq) / (D_2(z, q) D_3(z, q)).
```

This fraction is the compact form of the coefficient sum in Section 3. Its first term is `z^3 q^6`, the staircase `(1, 2, 3)`. Expanding it reproduces the width and area counts above.

### 5.4 Specialize the fraction

Setting `q = 1` gives

```
D_2(z, 1) = 1 - 2z,
D_3(z, 1) = (1 - z)(1 - 2z - z^2).
```

The numerator's `1 - z` cancels, leaving the known width function

```
C_3(z, 1) = z^3 / ((1 - 2z)(1 - 2z - z^2)).
```

Setting `z = 1` instead gives

```
D_2(1, q) = 1 - q - q^2,
D_3(1, q) = (1 - q)(1 - q^2 - 2q^3 - q^4 - q^5).
```

The numerator's `1 - q` cancels, leaving the area function[^specializations]

```
C_3(1, q) = q^6 / ((1 - q - q^2)(1 - q^2 - 2q^3 - q^4 - q^5)).
```

The two cancellations occur in different variables and leave different denominators.

### 5.5 Height-2 tie-in: Fibonacci counts, but a different castle rule

On heights `{1, 2}`, every pair of columns differs by at most 1. Thus **every height-2 castle is 1-smooth**: both adjacent 1s and adjacent 2s are allowed. To keep the same boundary condition as the Pell family, start at height 1 and require a visit to height 2. The joint generating function is

```
C_2(z, q) = S_2(z, q) - zq/(1 - zq)
          = z^2 q^3 / ((1 - zq)(1 - z(q + q^2))).
```

The subtracted term counts the strips that remain entirely at height 1. Setting `z = 1` gives[^height-two-area]

```
C_2(1, q) = q^3 / ((1 - q)(1 - q - q^2)),
area-n count = F_n - 1,
counts at n = 3, 4, ...:  1, 2, 4, 7, 12, 20, 33, 54, ... .
```

Here `F_0 = 0`, `F_1 = 1`, and `F_n = F_{n-1} + F_{n-2}`. After the initial height-1 column, the remaining cells form a composition of `n - 1` into 1s and 2s. There are `F_n` such compositions; removing the all-1 composition gives `F_n - 1`. Their area growth is the golden ratio `phi = (1 + sqrt(5))/2`. This is the same **height-2 area factor `1 - q - q^2`** that occurs in the Pell area denominator, through the ceiling-2 strips removed in Section 5.3.

The named Fibonacci and ridge castles use stricter neighbour rules:[^height-two-rules]

| exact-height-2 family | adjacent `(1, 1)` | adjacent `(2, 2)` |
|---|---|---|
| 1-smooth | allowed | allowed |
| [[fibonacci-castle](pages/fibonacci-castle.md)] | allowed | forbidden |
| [[ridge-castle](pages/ridge-castle.md)] | forbidden | allowed |

For example, `(1, 2, 2)` is 1-smooth but not a Fibonacci castle; `(1, 1, 2)` is 1-smooth but not a ridge castle. A Fibonacci **count** does not by itself identify the named Fibonacci **family**.

The Fibonacci page's "Counting by area" section already discusses **all** castles of exact height 2, with a free first column: their area-n count is `F_{n+1} - 1`. Our anchor accounts for the one-index shift to `F_n - 1`: removing the initial 1 is a bijection to a free-first-column height-2 castle with one fewer cell.[^height-two-area] The area refinement of the stricter, named Fibonacci family is instead [[q-fibonacci-castle](pages/q-fibonacci-castle.md)]. Exchanging heights 1 and 2 exchanges the Fibonacci and ridge neighbour rules, but changes area from `n` to `3w - n` at width `w`, so it is not an area-preserving identification.[^height-two-rules]

## 6. What growth by area means

Let `a_n` be the number of Pell castles with **exactly n cells**, including every allowed width. The area growth constant `alpha_3` describes how these counts increase for large `n`:

```
a_n ~ K alpha_3^n,       a_{n+1} / a_n -> alpha_3,
```

for a positive constant `K`. This is a statement about numbers of castles, not a procedure for adding one cell to a particular castle.

The growth constant is the reciprocal of the dominant pole of the area generating function. To see the reciprocal, if `a_n` behaves like `K alpha_3^n`, then `sum_n a_n q^n` behaves near its convergence boundary like the geometric sum `K sum_n (alpha_3 q)^n`. The boundary occurs at `alpha_3 q = 1`, or `q = 1/alpha_3`.

For the Pell area function, the factor `1 - q - q^2` has positive root about `0.618034`. The other factor vanishes sooner, at[^growth]

```
r = 0.600131331307574...,
1 = r^2 + 2r^3 + r^4 + r^5.
```

This is the unique positive root of the second factor. It is also the only root of that factor on its smallest-modulus circle: for `|q| < r`, the triangle inequality gives `|q^2 + 2q^3 + q^4 + q^5| < 1`; at `|q| = r`, equality with the real value 1 forces the powers `q^2` and `q^3` to have positive real phase, hence `q = r`. The pole is simple because the factor's derivative is negative at `r`. The numerator does not vanish there. Thus it gives the stated positive-constant asymptotic.

Consequently,

```
alpha_3 = 1/r = 1.666301937312933... .
```

Compare the two ways of measuring this same Pell family:

| grouping | size being increased | asymptotic growth |
|---|---|---|
| by width | number of columns `w` | a constant times `(1 + sqrt(2))^w`, base `2.414214...` |
| by area | number of cells `n` | a constant times `alpha_3^n`, base `1.666302...` |

A new column contains 1, 2 or 3 cells. One extra column and one extra cell are different units of size, so the two growth constants need not agree. There is also no single conversion factor: castles of a given width can have different areas, and castles of a given area can have different widths.

## Reproduce the Pell counts

The verification source is `raw/1-smooth-castles-by-area-verification.py`. Run it with Python 3 and SymPy:

```bash
python3 raw/1-smooth-castles-by-area-verification.py
```

Its Pell checks compare the joint generating function against direct enumeration through width 7, compare the area coefficients against an independent dynamic program through area 100, and compare the area-1000 consecutive-count ratio with the reciprocal pole.[^examples][^specializations][^growth]

For Pell castles, the area dynamic program remembers just the last column height and whether height 3 has been reached. Appending a height-`b` column, with `b` in `{1, 2, 3}`, adds `b` cells, moving a count at area `n` to area `n + b`. Use the source's `area_counts` function with its height argument set to 3.

## Related Concepts

- [[pell-castle](pages/pell-castle.md)] - the family counted here, with its width counts and block statistics.
- [[1-smooth-castles](pages/1-smooth-castles.md)] - the larger family containing Pell castles; the main count here stays at height 3.
- [[fibonacci-castle](pages/fibonacci-castle.md)] - distinguishes the named height-2 family from all height-2 castles counted by area.
- [[q-fibonacci-castle](pages/q-fibonacci-castle.md)] - area grading of that stricter Fibonacci family, not of every height-2 smooth castle.
- [[ridge-castle](pages/ridge-castle.md)] - the other height-2 neighbour rule, related to the Fibonacci rule by exchanging heights.
- [[pell-castle-strip](pages/pell-castle-strip.md)] - the ceiling-3 superset, from which the lower-ceiling strips are removed in Section 5.
- [[castle-strip](pages/castle-strip.md)] - column heights as the finite counting states.
- [[generating-functions](pages/generating-functions.md)] - coefficient bookkeeping and rational generating functions.
- [[exact-height-castle-by-area](pages/exact-height-castle-by-area.md)] - its height-3 row counts all castles by area, without the anchor or the smoothness restriction.
- [[area-growth-census](pages/area-growth-census.md)] - area counting for arbitrary fixed-height strip rules.

## Footnotes

[^definition]: `raw/1-smooth-castles-by-area-verification.py` §`is_castle` L1-L6,L17-L20 [synthesis] - with its height argument set to 3, fixes the Pell family, anchor, neighbour rule and inclusion of both block parities.
[^examples]: `raw/1-smooth-castles-by-area-verification.py` §`main`, joint coefficients L73-L94 [synthesis] - the listed width-4 and area-8 castles, the first width polynomials, and exhaustive comparison of every Pell joint coefficient through width 7. Executed 2026-10-07.
[^derivation]: `raw/1-smooth-castles-by-area-verification.py` §`strip_gf` and §`main`, last-column equations L23-L39,L96-L111 [synthesis] - independently constructs the weighted transfer matrix, solves the last-column equations, and verifies the ceiling-2, ceiling-3 and exact-height-3 rational functions as symbolic identities. Executed 2026-10-07.
[^specializations]: `raw/1-smooth-castles-by-area-verification.py` §`main`, specializations L113-L127 [synthesis] - verifies both Pell factorizations and variable specializations, the displayed width and area counts, and agreement with the separate area dynamic program through area 100. Executed 2026-10-07.
[^growth]: `raw/1-smooth-castles-by-area-verification.py` §`main`, dominant pole L129-L140 [synthesis] - computes the second factor's roots, checks the unique smallest modulus and its position below the first factor's positive root, and confirms the reciprocal against the area-1000 count ratio; `r = 0.600131331307573712987720337438`, `alpha_3 = 1.66630193731293346886105074154`. Executed 2026-10-07.
[^height-two-area]: `raw/pell-area-height-two-comparison.py` §`joint_gf` and §`main` L18-L24,L27-L50 [synthesis] - verifies the anchored and free exact-height-2 smooth generating functions, compares their joint coefficients with enumeration through width 8, and checks the area coefficients `F_n - 1` and `F_{n+1} - 1` through area 19. Executed 2026-10-07.
[^height-two-rules]: `raw/pell-area-height-two-comparison.py` §rule matrices and §`main` L12-L15,L35-L42,L51-L54 [synthesis] - the smooth rule allows every pair, Fibonacci forbids `(2, 2)`, ridge forbids `(1, 1)`, and exchanging heights conjugates the Fibonacci rule to the ridge rule. At each column the exchanged height is `3 - c_i`, giving the area identity `sum_i (3 - c_i) = 3w - n`. Executed 2026-10-07.
