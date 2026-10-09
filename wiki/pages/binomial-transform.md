---
title: Binomial transform
category: Concepts
summary: The binomial transform sends a sequence a_k to b_n = Σ_k C(n, k) a_k, generating function (1/(1 − x))·A(x/(1 − x)); as a Riordan array it is (1/(1 − x), x/(1 − x)). Barry's aerated version b_n = Σ_k C(n, 2k) a_k = Bin ∘ (1, x²) puts zeros at the odd places first. On castles, a neighbour rule that allows equal neighbours has transfer matrix I + N, so a strip count is the binomial transform of its skeleton count (the walks with no flat steps); for the 1-smooth strip with both ends pinned the skeleton has even length and the count is the aerated transform: Catalan to the Motzkin-path castles M_{w−1}, and on heights {1, 2, 3} Barry's Pell and Pell-Lucas sums.
tags: [concept, binomial-transform, riordan-array, transfer-matrix, 1-smooth, motzkin, pell, generating-functions, technique]
sources: [barry-2005-catalan-transform]
created: 2026-10-08
updated: 2026-10-08
---

# Binomial transform

## Description

The **binomial transform** of a sequence `a_0, a_1, …` is

```
b_n  =  Σ_{k=0}^{n} C(n, k) a_k,          generating function  (1/(1 − x)) · A(x/(1 − x)),
```

with inverse `a_n = Σ_k C(n, k)(−1)^{n−k} b_k`. Its matrix is Pascal's triangle, and as a Riordan array, the lower-triangular matrix `(g, f)` whose column `k` has generating function `g·f^k`, it is `Bin = (1/(1 − x), x/(1 − x))`.[^1]

**The aerated version.** Barry studies `b_n = Σ_k C(n, 2k) a_k`, which first spreads `a_k` onto the even places (`a_0, 0, a_1, 0, a_2, …`, the array `(1, x²)`) and then applies `Bin`, so it is `Bin ∘ (1, x²)` with generating function `(1/(1 − x)) A(x²/(1 − x)²)`. It is not invertible, but `a_n` is every second term of the inverse binomial transform of `b_n`. It sends the Catalan numbers to the Motzkin numbers, `2^n` to the Pell-Lucas numbers A001333, `1^n` to A011782 and the central binomials to the central trinomials.[^2]

## For castles

A castle strip is a walk on column heights, counted by a transfer matrix `M` ([[castle-strip](pages/castle-strip.md)]). If the neighbour rule allows two equal neighbours, `M = I + N` with `N` the rule without its flat step, and `(I + N)^{w−1} = Σ_j C(w − 1, j) N^j`. A strip of width `w` is then a choice of the `j` column boundaries where the height changes, and a **skeleton**, a walk of `j` steps under `N`. So the strip count is the binomial transform of the skeleton count.

For the 1-smooth rule `N = A` is the adjacency matrix of a path, so a skeleton is a walk of `±1` steps ([[1-smooth-castles](pages/1-smooth-castles.md)]). With both end columns at the same height the skeleton is closed and has even length, and the count is the aerated transform ([[barry-2005-catalan-transform](pages/barry-2005-catalan-transform.md)], "The castle reading"):

| strip, 1-smooth | closed skeletons of length `2k` | strips of width `w` |
|---|---|---|
| `c_1 = c_w = 1`, no ceiling | Dyck paths, `C_k` | `M_{w−1}`, the Motzkin-path castles ([[motzkin-castles](pages/motzkin-castles.md)] §2) |
| `c_1 = c_w = 1`, ceiling 2 | 1 | `2^{w−2}` (`w ≥ 2`), A011782(`w − 1`) |
| `c_1 = c_w = 1`, ceiling 3 | `1, 1, 2, 4, 8, …` = A011782(`k`) | A171842(`w − 1`), the Motzkin paths of height `≤ 2` |
| `c_1 = c_w = 2`, ceiling 3 | `2^k` | A001333(`w − 1`), Pell-Lucas ([[pell-castle-strip](pages/pell-castle-strip.md)]) |
| no floor, no ceiling (walks on the integers) | `C(2k, k)` | central trinomials A002426 |

On heights `{1, 2, 3}` a skeleton step away from height 2 has two choices and a step back has one, which gives the `2^k`. The anchored strips (`c_1 = 1`) ending at height 2 have odd skeletons with a forced first step, and number `Σ_k C(w − 1, 2k + 1) 2^k = P⋆_{w−1}`, Barry's Pell sum ([[pell-numbers](pages/pell-numbers.md)]). The ceiling enters only through the skeleton; the flat steps are free.

## Appearances in Sources

- [[barry-2005-catalan-transform](pages/barry-2005-catalan-transform.md)] - the binomial transform as a Riordan array, its composition with the Catalan transform (the generalized Ballot transform), and the aerated version `Bin ∘ (1, x²)` with its table of pairs.

## Related Concepts

- [[1-smooth-castles](pages/1-smooth-castles.md)] - the strips with transfer matrix `I + A`.
- [[pell-castle-strip](pages/pell-castle-strip.md)] - the height-3 strip, where Barry's Pell and Pell-Lucas sums are the strips by last column.
- [[motzkin-castles](pages/motzkin-castles.md)] - `M_{w−1} = Σ_k C(w − 1, 2k) C_k`.
- [[castle-strip](pages/castle-strip.md)] - the transfer-matrix picture.
- [[kernel-method](pages/kernel-method.md)] - the other way the wiki counts the same strips in closed form.
- [[generating-functions](pages/generating-functions.md)] - the wider method.

## Footnotes

[^1]: [[barry-2005-catalan-transform](pages/barry-2005-catalan-transform.md)] §2 L116-L151, L175-L192 [synthesis] - the binomial transform `b_n = Σ_k C(n, k) a_k`, its inverse with signs `(−1)^{n−k}`, the matrix `Bin` "corresponds to Pascal's triangle", the transformed generating function "(1/(1 − x))A(x/(1 − x))", the definition of the Riordan array by "the matrix whose k-th column is generated by g(x)f (x)k", and "the Binomial matrix Bin is the element (1/(1−x), x/(1−x)) of the Riordan group".
[^2]: [[barry-2005-catalan-transform](pages/barry-2005-catalan-transform.md)] §7 L1100-L1197, L1280-L1282, Table 3 L1285-L1311 [synthesis] - the transform `b_n = Σ_k C(n, 2k) a_k` with generating function `(1/(1 − x))A(x²/(1 − x)²)`, "not invertible", factored as `Bin ◦ (1, x²)` ("'aerate' a sequence with interpolated zeros and then follow this with a binomial transform"), recoverable "by taking every second element of the inverse binomial transform", and the pairs Catalan → Motzkin, `2^n → A001333`, `1^n → A011782`, central binomial → central trinomial A002426.
