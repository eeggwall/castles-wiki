---
title: "Barry (2005) - A Catalan transform and related transformations on integer sequences"
category: Sources
summary: Paul Barry studies invertible transforms of integer sequences as Riordan arrays, the lower-triangular matrices (g, f) whose k-th column has generating function g·f^k. The Catalan transform A(x) → A(x c(x)), c(x) the Catalan generating function, has inverse A(x) → A(x(1 − x)) and the Catalan numbers as row sums; the generalized Ballot transform Cat ∘ Bin = (c(x), x c(x)²) has entries the ballot numbers (2k+1)/(n+k+1)·C(2n, n+k) (OEIS A039599). Tables of transform pairs cover powers, Fibonacci, Jacobsthal, Pell and Fine's sequence. A non-invertible companion, b_n = Σ_k C(n, 2k) a_k = Bin ∘ (1, x²) (aerate, then binomial transform), sends the Catalan numbers to the Motzkin numbers, 2^n to A001333 and 1^n to A011782. For castles this is the 1-smooth strip with both end columns pinned: the transfer matrix is I + A, the binomial transform inserts the flat steps, and the aeration is the even length of a closed skeleton walk. Checked here by execution, with the Pell strip on heights {1, 2, 3} split by its last column into Barry's two Pell sums.
tags: [source, paper, oeis, catalan, motzkin, pell, binomial-transform, riordan-array, ballot, 1-smooth, transfer-matrix, generating-functions]
sources: [barry-2005-catalan-transform]
created: 2026-10-08
updated: 2026-10-08
---

# Barry (2005) - A Catalan transform and related transformations on integer sequences

**Source:** `raw/barry-2005-catalan-transform.pdf` (text layer at `raw/barry-2005-catalan-transform.txt`, extracted with `pdftotext -layout`; the PDF is git-ignored, the text is tracked). P. Barry, "A Catalan Transform and Related Transformations on Integer Sequences", Journal of Integer Sequences 8 (2005), Article 05.4.4; PDF from https://cs.uwaterloo.ca/journals/JIS/VOL8/Barry/barry84.pdf.[^1]
**Date ingested:** 2026-10-08
**Type:** paper (PDF, 24 pp.)

## Notation used on this page

Several of the paper's symbols collide with the wiki's ([[castle-notation](pages/castle-notation.md)]), so they are renamed here. Footnote quotes keep the paper's symbols.

| paper | meaning | written here as |
|---|---|---|
| `c(x)` | Catalan generating function `(1 − √(1 − 4x))/(2x)` | `c(x)` (always with its argument; `c_i` stays a column height) |
| `(g, f)`, `R(g, f)` | Riordan array: column `k` has generating function `g(x) f(x)^k` | `(g, f)` |
| `Bin`, `Cat`, `Bal` | binomial, Catalan and generalized Ballot transforms | same |
| `B(n, k)` | generalized ballot number | `ballot(n, k)` (`B(x, y)` is the castle generating function) |
| `T(n, k)` | entry `(n, k)` of a matrix | "entry `(n, k)`" (`T(k, L)` is the tower count) |
| `F(n)`, `Pell(n)`, `J(n)` | Fibonacci, Pell, Jacobsthal numbers | `F_n`, `P⋆_n`, `J_n` (`F(w, h)` is the PE 502 count) |
| `M_n`, `C(n)` | Motzkin and Catalan numbers | `M_n`, `C_n` |

## Summary

**Riordan arrays.** A Riordan array `(g, f)`, with `g(x) = 1 + g_1 x + ⋯` and `f(x) = f_1 x + ⋯`, `f_1 ≠ 0`, is the lower-triangular matrix whose column `k` has generating function `g(x) f(x)^k`. It sends a sequence with generating function `A(x)` to the one with generating function `g(x) A(f(x))`; products are `(g, f) ∗ (h, l) = (g·(h ∘ f), l ∘ f)`, and the inverse uses the compositional inverse of `f`.[^2] The binomial transform `b_n = Σ_k C(n, k) a_k` is `Bin = (1/(1 − x), x/(1 − x))`, with inverse `(1/(1 + x), x/(1 + x))`.[^3]

**The Catalan transform.** `Cat` sends `A(x)` to `A(x c(x))`, so `Cat = (1, x c(x))`. Its inverse is `A(x) → A(x(1 − x))`, entry `(n, k)` of the inverse is `C(k, n − k)(−1)^{n−k}`, and the row sums of `Cat` are the Catalan numbers.[^4] In terms of the sequence, `b_n = Σ_k (k/(2n − k)) C(2n − k, n − k) a_k`, with inverse `a_n = Σ_k C(k, n − k)(−1)^{n−k} b_k`.[^5] Table 1 pairs classical sequences: `1^n → C_n`, `2^n → C(2n, n)`, `0^n − (−1)^n →` Fine's sequence (A000957), `F_n →` the generating function `x c(x)/(x + √(1 − 4x))`, the Jacobsthal numbers to sums of central binomials (A014300), and others.[^6] §4 extends the Jacobsthal case to the family `x(1 − x)/((1 − kx²)(1 − 2x))`, whose Catalan transform is `x/√(1 − 4x(1 − k(x c(x))²))`.[^7]

**The generalized Ballot transform.** `Bal = Cat ∘ Bin = (c(x), x c(x)²)`, with inverse `(1/(1 + x), x/(1 + x)²)`.[^8] Its entries are the generalized ballot numbers

```
ballot(n, k)  =  (2k + 1)/(n + k + 1) · C(2n, n + k)  =  C(2n, n − k) − C(2n, n − k − 1),
```

which count Dyck paths of semilength `n + k + 1` whose first peak has height `2k + 1`, and lattice paths from `(0, −2k)` to `(n − k, n − k)` that do not cross the diagonal.[^9] The inverse transform is `b_n = Σ_k (−1)^{n−k} C(n + k, 2k) a_k`. The matrix of `Bal` is A039599 and the absolute value of its inverse is A085478.[^10] Table 2 lists pairs (`1^n → C(2n, n)`, `0^n → C_n`, `2n + 1 → 4^n`, and others).[^11] §6 treats the signed version `(c(−x), x c(−x)²)`, whose inverse matrix is the DFF triangle `C(n + k, 2k)` of the Fibonacci literature.[^12]

**The aerated binomial transform.** §7 studies a non-invertible companion,

```
b_n  =  Σ_{k ≤ n/2} C(n, 2k) a_k,         generating function  (1/(1 − x)) · A(x²/(1 − x)²),
```

and opens with `M_n = Σ_k C(n, 2k) C_k`.[^13] Powers go to a two-term recurrence, `k^n → (1 − x)/(1 − 2x − (k − 1)x²)`; at `k = 2` this gives the Pell-Lucas numbers `Σ_k C(n, 2k) 2^k = 1, 1, 3, 7, 17, …` (A001333), and alongside it `Σ_k C(n, 2k + 1) 2^k = P⋆_n` (A000129). The central binomials go to the central trinomials A002426.[^14] The transform factors as `Bin ∘ (1, x²)`: `(1, x²)` "aerates" the sequence with zeros at the odd places and `Bin` follows.[^15] A left inverse recovers `a_n` as every second term of the inverse binomial transform of `b_n`.[^16] Table 3 lists pairs, among them `1^n → A011782`, `2^n → A001333` and `C_n → M_n`.[^17]

**Combined transforms.** §8 applies `Bin ∘ Cat`, `Bin⁻¹ ∘ Cat` and their inverses to the Fibonacci numbers. `Cat⁻¹ ∘ Bin` gives `0, 1, 2, 2, 0, −5, −13, −21, −21, 0, 55, 144, 233, 233, 0, −610, −1597, …`, with generating function `x(1 − x)/(1 − 3x + 4x² − 2x³ + x⁴)`, whose terms the paper notes "would appear to be Fibonacci numbers".[^18]

## The castle reading

The 1-smooth strip of height `h`, skylines on heights `{1, …, h}` with `|c_{i+1} − c_i| ≤ 1`, has transfer matrix `I + A`, `A` the adjacency matrix of the path on `h` vertices ([[castle-notation](pages/castle-notation.md)], [[motzkin-castles](pages/motzkin-castles.md)] §4). Expanding `(I + A)^{w−1} = Σ_j C(w − 1, j) A^j` splits a strip of width `w` into the set of `j` column boundaries where the height changes and a **skeleton**, a walk of `j` steps `±1` with no flat steps. So every 1-smooth strip count is the binomial transform of its skeleton count ([[binomial-transform](pages/binomial-transform.md)]). When both end columns are pinned at the same height the skeleton is a closed walk on a path, of even length `2k`, and the count is Barry's aerated transform with `n = w − 1`:

```
#{1-smooth strips of width w, c_1 = c_w}  =  Σ_k C(w − 1, 2k) · #{closed skeletons of 2k steps}.
```

Barry's factorization `Bin ∘ (1, x²)` is this split: `(1, x²)` keeps the even skeleton lengths, `Bin` inserts the flat steps. Checks, by execution:[^exec]

- **No ceiling, pinned at height 1.** The closed skeletons are the Dyck paths, `C_k`, and the transform gives the Motzkin-path castles, `M_{w−1}` ([[motzkin-castles](pages/motzkin-castles.md)] §2). This is Barry's identity `M_n = Σ_k C(n, 2k) C_k`.
- **Ceiling `h`, pinned at height 1.** The closed skeletons are the Dyck paths of height `≤ h − 1`. At `h = 2` there is one of each length and the strip count is `1, 1, 2, 4, 8, …` = A011782(`w − 1`), Barry's `1^n → A011782`. At `h = 3` the skeleton counts are `1, 1, 2, 4, 8, …` = A011782(`k`) again, so the pinned Pell strip `1, 1, 2, 4, 9, 21, 50, 120, …` = A171842(`w − 1`) is the aerated transform applied twice to `1^n`; the OEIS name of A171842 is "Binomial transform of 1,0,1,0,2,0,4,0,8,0,16,...", the aerated A011782. Checked for `h ∈ {2, 3, 4, 5, 8}` and no ceiling, `w ≤ 14`.
- **The Pell strip, by last column.** On heights `{1, 2, 3}` a skeleton step away from height 2 has two choices (to 1 or 3) and a step back to 2 has one. A skeleton from 2 back to 2 with `2k` steps makes `k` free choices, so the strips with `c_1 = c_w = 2` number `Σ_k C(w − 1, 2k) 2^k = A001333(w − 1)`, Barry's Pell-Lucas sum. An anchored strip (`c_1 = 1`) ending at height 2 has an odd skeleton whose first step is forced, so these number `Σ_k C(w − 1, 2k + 1) 2^k = P⋆_{w−1}`, Barry's Pell sum; the anchored strips ending at 1 or 3 number `A001333(w − 1)`. Together they give the anchored Pell strip `P⋆_{w−1} + A001333(w − 1) = P⋆_w` of [[pell-castle-strip](pages/pell-castle-strip.md)]. Adding a column of height 2 at each end is a bijection from the free strips of width `w` to the strips of width `w + 2` with both ends at 2, so the free strip count is `A001333(w + 1)`, the Pell-Lucas row of [[pell-castle-strip](pages/pell-castle-strip.md)].
- **No floor, no ceiling.** Closed `±1` walks on the integers number `C(2k, k)`, and the aerated transform gives the central trinomials A002426, the unconstrained `U/R/D` words returning to their start ([[aocp-multinomial-coefficients](pages/aocp-multinomial-coefficients.md)]); Barry's `C(2n, n) → A002426`.

## Key Takeaways

- **Transforms as Riordan arrays.** The binomial, Catalan and generalized Ballot transforms and their inverses are each one Riordan array `(g, f)`, and composing transforms multiplies arrays.[^2][^8]
- **The Catalan and Ballot transforms.** `Cat = (1, x c(x))` has the Catalan row sums; `Bal = Cat ∘ Bin` has the ballot numbers as entries (A039599), and both come with tables of classical pairs.[^4][^9][^10]
- **Aerate, then insert flat steps.** `Σ_k C(n, 2k) a_k` sends Catalan to Motzkin, `2^n` to Pell-Lucas and `1^n` to A011782.[^13][^14][^17] On castles it is the 1-smooth strip with pinned ends, built from its closed skeleton (verified).[^exec]
- **Both Pell sums are one strip.** Barry's `Σ C(n, 2k + 1) 2^k = P⋆_n` and `Σ C(n, 2k) 2^k = A001333(n)` count the anchored Pell strip by whether its last column is at height 2 (verified).[^exec]

## Entities & Concepts

- [[binomial-transform](pages/binomial-transform.md)] - the transform `Σ C(n, k) a_k` and its aerated version, read on castle strips.
- [[1-smooth-castles](pages/1-smooth-castles.md)] - the strips whose transfer matrix is `I + A`; the pinned boundary condition is the aerated transform.
- [[pell-castle-strip](pages/pell-castle-strip.md)] - the height-3 strip, where Barry's two Pell sums are the two kinds of last column.
- [[motzkin-castles](pages/motzkin-castles.md)] - the Motzkin-path castles, `M_{w−1} = Σ C(w − 1, 2k) C_k`.
- [[catalan-numbers](pages/catalan-numbers.md)] / [[motzkin-numbers](pages/motzkin-numbers.md)] / [[pell-numbers](pages/pell-numbers.md)] - the sequences paired by the transforms.

## Relation to Other Wiki Pages

The wiki counts 1-smooth strips with the transfer matrix `I + A` and its eigenvalues `1 + 2cos θ_k` ([[1-smooth-castles](pages/1-smooth-castles.md)]) or with the kernel method ([[kernel-method](pages/kernel-method.md)]). Barry's §7 is the combinatorial reading of the `I`: the flat steps are chosen freely, and only the skeleton depends on the walls. The Catalan and generalized Ballot transforms of §§3-6 are recorded here as source material; no castle count on the wiki is identified as one of them yet. The Dyck-path readings of the ballot numbers sit beside [[dyck-words](pages/dyck-words.md)] and [[deutsch-elizalde-2017-bargraphs-dyck-paths](pages/deutsch-elizalde-2017-bargraphs-dyck-paths.md)].

## Footnotes

[^1]: [[barry-2005-catalan-transform](pages/barry-2005-catalan-transform.md)] p.1 L2-L18, p.24 L1495-L1496 [synthesis] - the running header "Journal of Integer Sequences, Vol. 8 (2005), Article 05.4.4", the title "A Catalan Transform and Related Transformations on Integer Sequences", the author Paul Barry (Waterford Institute of Technology), and "Received December 21 2004; revised version received September 20 2005. Published in Journal of Integer Sequences, September 20 2005."
[^2]: [[barry-2005-catalan-transform](pages/barry-2005-catalan-transform.md)] §2 L177-L188 - "The associated matrix is the matrix whose k-th column is generated by g(x)f (x)k"; "The group law is then given by (g, f ) ∗ (h, l) = (g(h ◦ f ), l ◦ f )"; "the inverse of (g, f ) is (g, f ) −1 = (1/(g ◦ f¯), f¯) where f¯ is the compositional inverse of f"; "the sequence Ma has ordinary generating function g(x)A(f (x))".
[^3]: [[barry-2005-catalan-transform](pages/barry-2005-catalan-transform.md)] §2 L116-L151, L189-L192 [synthesis] - the binomial transform `b_n = Σ_k C(n, k) a_k` and its inverse with signs `(−1)^{n−k}`; "the Binomial matrix Bin is the element (1/(1−x), x/(1−x)) of the Riordan group, while its inverse is the element (1/(1+x), x/(1+x))".
[^4]: [[barry-2005-catalan-transform](pages/barry-2005-catalan-transform.md)] §3 L218-L231, L259-L280, L299-L303 [synthesis] - "The Catalan transform of that sequence is defined to be the sequence whose generating function is A(xc(x))", "the element of the Riordan group given by (1, xc(x))"; Proposition 1, "The inverse of the Catalan transformation is given by A(x) → A(x(1 − x))"; "the matrix Cat has the Catalan numbers as row sums"; the general term of `(1, x(1 − x))` is `C(k, n − k)(−1)^{n−k}`.
[^5]: [[barry-2005-catalan-transform](pages/barry-2005-catalan-transform.md)] §3 Proposition 3 L368-L394 [synthesis] - the Catalan transform `b_n = Σ_k (k/(2n − k)) C(2n − k, n − k) a_k = Σ_k (k/n) C(2n − k − 1, n − k) a_k`, and the inverse `a_n = Σ_k C(n − k, k)(−1)^k b_{n−k} = Σ_k C(k, n − k)(−1)^{n−k} b_k`.
[^6]: [[barry-2005-catalan-transform](pages/barry-2005-catalan-transform.md)] §3 Table 1 L443-L505 [synthesis] - the Catalan pairs `1^n → C(n)` (A000108), `2^n → C(2n, n)` (A000984), `0^n − (−1)^n →` Fine's sequence A000957, `F(n) →` "G.f. xc(x)/(x+√1−4x)", `J(n) → A014300`, and the generating function of Fine's sequence `x/(1 − (xc(x))²)`.
[^7]: [[barry-2005-catalan-transform](pages/barry-2005-catalan-transform.md)] §4 Proposition 4 L550-L567 [synthesis] - the Catalan transform of `x(1 − x)/((1 − kx²)(1 − 2x))` has generating function `x/√(1 − 4x(1 − k(xc(x))²))` and general term `Σ_j C(2n − 2j − 2, n − 1) k^j`.
[^8]: [[barry-2005-catalan-transform](pages/barry-2005-catalan-transform.md)] §5 L647-L683 [synthesis] - "we define a new transformation Bal as the composition of the Catalan transform and the Binomial transform: Bal = Cat ◦ Bin", computed as `(c(x), c(x) − 1) = (c(x), xc(x)²)`, and `Bal⁻¹ = Bin⁻¹ ∘ Cat⁻¹ = (1/(1 + x), x/(1 + x)²)`.
[^9]: [[barry-2005-catalan-transform](pages/barry-2005-catalan-transform.md)] §5 L725-L735, Proposition 6 L749-L753, L817-L823 [synthesis] - the generalized Ballot numbers `B(n, k) = C(2n, n + k)(2k + 1)/(n + k + 1) = C(2n, n − k) − C(2n, n − k − 1)` are the general term of `(c(x), c(x) − 1)`; "B(n, k) = D(n + k + 1, 2k + 1) where D(n, k) is the number of Dyck paths of semi-length n having height of the first peak equal to k"; "B(n, k) also counts the number of paths from (0, −2k) to (n − k, n − k) with permissible steps (0, 1) and (1, 0) that don't cross the diagonal y = x".
[^10]: [[barry-2005-catalan-transform](pages/barry-2005-catalan-transform.md)] §5 Proposition 7 L845-L854, L919-L961 [synthesis] - the inverse generalized Ballot transform `b_n = Σ_k (−1)^{n−k} C(n + k, 2k) a_k`; the two matrices printed, and "The first matrix is A039599, while the absolute value of the second matrix is A085478."
[^11]: [[barry-2005-catalan-transform](pages/barry-2005-catalan-transform.md)] §5 Table 2 L880-L917 [synthesis] - Ballot transform pairs including `0^n → C(n)`, `1^n → C(2n, n)` (A000984), `2n + 1 → 4^n` (A000302), `F(n) → A026674`.
[^12]: [[barry-2005-catalan-transform](pages/barry-2005-catalan-transform.md)] §6 L964-L1000 [synthesis] - the signed generalized Ballot transform `(c(−x), 1 − c(−x)) = (c(−x), xc(−x)²)`, with inverse `b_n = Σ_k C(n + k, 2k) a_k`; "The latter matrix has a growing literature in which it is known as the DFF triangle", the element `(1/(1−x), x/(1−x)²)`.
[^13]: [[barry-2005-catalan-transform](pages/barry-2005-catalan-transform.md)] §7 L1100-L1130 [synthesis] - "Unlike other transformations in this study, this is not invertible"; "Mn = Σ_{k=0}^{⌊n/2⌋} C(n, 2k) C(k) where Mn is the nth Motzkin number A001006"; the general transform `b_n = Σ_k C(n, 2k) a_k` with generating function `(1/(1 − x)) A(x²/(1 − x)²)`.
[^14]: [[barry-2005-catalan-transform](pages/barry-2005-catalan-transform.md)] §7 L1131-L1172 [synthesis] - `1/(1 − kx) → (1 − x)/(1 − 2x − (k − 1)x²)`; "Σ C(n, 2k) 2^k = 1, 1, 3, 7, 17, . . . = ((1 + √2)^n + (1 − √2)^n)/2 which is the sequence A001333"; "the following formula for the Pell numbers A000129, Σ C(n, 2k + 1) 2^k = Pell(n)"; the central binomial numbers "are mapped to the central trinomial numbers A002426".
[^15]: [[barry-2005-catalan-transform](pages/barry-2005-catalan-transform.md)] §7 L1174-L1197 [synthesis] - the "generalized" Riordan array `(1/(1 − x), x²/(1 − x)²) = (1/(1 − x), x/(1 − x)) (1, x²) = Bin ◦ (1, x²)`; "Thus the effect of this transform is to 'aerate' a sequence with interpolated zeros and then follow this with a binomial transform."
[^16]: [[barry-2005-catalan-transform](pages/barry-2005-catalan-transform.md)] §7 L1205-L1206, L1280-L1282 - "this transformation possesses a left inverse"; "we can recover the original sequence an by taking every second element of the inverse binomial transform of the transformed sequence bn".
[^17]: [[barry-2005-catalan-transform](pages/barry-2005-catalan-transform.md)] §7 Table 3 L1285-L1311 [synthesis] - transform pairs including `1^n → A011782`, `2^n → A001333`, `C(2n, n) → A002426` and `C(n) →` Motzkin A001006.
[^18]: [[barry-2005-catalan-transform](pages/barry-2005-catalan-transform.md)] §8 L1411-L1420 - "we apply the combined transformation Cat−1 ◦ Bin to the Fibonacci numbers. We obtain the sequence 0, 1, 2, 2, 0, −5, −13, −21, −21, 0, 55, 144, 233, 233, 0, −610, −1597, . . . whose elements would appear to be Fibonacci numbers", with generating function `x(1 − x)/(1 − 3x + 4x² − 2x³ + x⁴)`.
[^exec]: Verified by execution (Python 3, SymPy, 2026-10-08). The paper's side: Proposition 3 (both forms) gives `1^n → C_n` and `2^n → C(2n, n)`, its inverse undoes it on the Fibonacci numbers, the Jacobsthal formula of Table 1 holds for `n < 14`, `0^n − (−1)^n` goes to `0, 1, 0, 1, 2, 6, 18, 57, …` (A000957), the matrix of `Bal` has rows `1; 1, 1; 2, 3, 1; 5, 9, 5, 1; 14, 28, 20, 7, 1; 42, 90, 75, 35, 9, 1` (A039599), `Bal⁻¹` undoes `Bal`, `2n + 1 → 4^n`, the aerated transform sends `C_k`, `2^k`, `C(2k, k)`, `1^k` to `M_n`, A001333, A002426, A011782, `Σ C(n, 2k + 1) 2^k = P⋆_n`, and the three §8 Fibonacci sequences match the printed terms. The castle side: 1-smooth skylines were counted by dynamic program on heights `{1, …, h}` (cross-checked against brute force for `w ≤ 7`). With `c_1 = c_w = 1`, the count equals `Σ_k C(w − 1, 2k)` times the number of flat-free closed walks of length `2k` for `h ∈ {2, 3, 4, 5, 8, 40}` and `w ≤ 14`; the closed-skeleton counts are `1, 1, 1, …` at `h = 2` and `1, 1, 2, 4, 8, 16, 32` at `h = 3`. On `{1, 2, 3}`, for `w ≤ 13`: strips from 2 to 2 number `A001333(w − 1)`, from 1 to 2 `P⋆_{w−1}`, from 1 to `{1, 3}` `A001333(w − 1)`, all anchored strips `P⋆_w`, and free strips of width `w` as many as strips from 2 to 2 of width `w + 2`. Closed walks on the integers with flat steps number `1, 1, 3, 7, 19, 51, 141, …`. OEIS data for A000957, A000984, A039599, A085478 and A171842 checked on oeis.org 2026-10-08.
