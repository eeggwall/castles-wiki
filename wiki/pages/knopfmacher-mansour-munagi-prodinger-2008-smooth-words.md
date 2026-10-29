---
title: "Knopfmacher, Mansour, Munagi & Prodinger (2008) - Smooth words and Chebyshev polynomials"
category: Sources
summary: A word over {1, ..., k} is smooth when neighboring letters differ by at most 1, and smooth cyclic when the last and first letters also do. The paper inverts the tridiagonal matrix of the smooth rule (Usmani's formula, with determinants θ_i = x^i U_i((1 − x)/(2x))), writes the generating function of smooth words with a given first letter and of all smooth words in Chebyshev polynomials of the second kind, and gives both counts as cosine sums, the cyclic one the trace Σ_j (1 + 2cos(jπ/(k + 1)))^n; it also counts smooth necklaces. In castle terms the smooth words over {1, ..., h} are the free 1-smooth skylines on h heights, the words starting with 1 are the anchored strips, and the cyclic words add the condition |c_w − c_1| ≤ 1. Every theorem and both tables were rechecked here by enumeration for k ≤ 8; the printed closed forms at k = 4 and 5 hold for n ≥ 1.
tags: [source, paper, 1-smooth, smooth-words, chebyshev, transfer-matrix, tridiagonal, necklaces, generating-functions]
sources: [knopfmacher-mansour-munagi-prodinger-2008-smooth-words]
created: 2026-10-22
updated: 2026-10-28
---

# Knopfmacher, Mansour, Munagi & Prodinger (2008) - Smooth words and Chebyshev polynomials

**Source:** `raw/knopfmacher-mansour-munagi-prodinger-2008-smooth-words.pdf` (text layer at `raw/knopfmacher-mansour-munagi-prodinger-2008-smooth-words.txt`, extracted with `pdftotext -layout`; the PDF is git-ignored, the text is tracked). A. Knopfmacher, T. Mansour, A. Munagi and H. Prodinger, "Smooth words and Chebyshev polynomials", arXiv:0809.0551v1 [math.CO], 3 September 2008, https://arxiv.org/abs/0809.0551.[^1]
**Date ingested:** 2026-10-22
**Type:** paper (PDF, 12 pp.)

## Notation used on this page

The wiki uses `h` for the castle height, `w` for the width, `θ_k = πk/(h+1)` for the eigenvalue angles and `χ_h` for the determinant `det(I − x(I + A_path))` ([[castle-notation](pages/castle-notation.md)]). The paper uses `θ` for both the determinants and the angles, so its symbols are renamed here. Footnote quotes keep the paper's symbols.

| paper | meaning | written here as |
|---|---|---|
| `k`, `[k]` | alphabet size, the letters `{1, …, k}` | `h`, the heights `{1, …, h}` |
| `n` | word length | `w` |
| `sw_{n,k}`, `scw_{n,k}`, `sn_{n,k}` | smooth words, smooth cyclic words, smooth necklaces | the same |
| `sw_k(x \| i)` | generating function of the smooth words with first letter `i` | the same |
| `θ_i` in §2 | `θ_i = (1 − x)θ_{i−1} − x²θ_{i−2}`, `θ_0 = 1`, `θ_1 = 1 − x` | `χ_i` |
| `θ_j` in the proofs of Theorems 2.4 and 3.3 | `jπ/(k + 1)` | `θ_j` |
| `t` | `(1 − x)/(2x)` | `t` |

## Summary

**Definitions.** A word over `[k]` is **smooth** if no two adjacent letters differ by more than 1, and **smooth cyclic** if in addition its last and first letters differ by at most 1. A **smooth necklace** is a class of smooth cyclic words under rotation.[^2]

**The matrix.** Reading off the second letter gives one linear equation per first letter, `sw_k(x | i) = x + x(sw_k(x | i − 1) + sw_k(x | i) + sw_k(x | i + 1))`. Its matrix has `1 − x` on the diagonal and `−x` on both off-diagonals, the matrix `I − x(I + A_path)` of the 1-smooth rule. The authors invert it entry by entry with a formula of Usmani for tridiagonal matrices: the entries are quotients of the determinants `θ_i`, and `θ_i = x^i U_i((1 − x)/(2x))`, with `U_i` the Chebyshev polynomials of the second kind. A footnote notes that equivalent results appeared earlier, for instance in Panny and Prodinger (1985).[^3]

**Smooth words.** With the identity for `Σ_{j≤p} U_j(t)` and a product formula for `U_i U_j`, the words with first letter `i` have generating function

```
sw_k(x | i)  =  (U_k(t) − U_{k−i}(t) − U_{i−1}(t)) / (2(t − 1) U_k(t)),        t = (1 − x)/(2x)        (2.5)
```

and summing over `i` gives Theorem 2.2, `sw_k(x) = 1 + x(k − (3k + 2)x)/(1 − 3x)² + 2x²(1 + U_{k−1}(t))/((1 − 3x)² U_k(t))`.[^4] At `k = 3, 4, 5` the paper prints `(1 + x)/(1 − 2x − x²)`, `(1 + x − x²)/(1 − 3x + x²)` and `(1 + 2x − 2x² − 2x³)/((1 − x)(1 − 2x − 2x²))`, with closed forms for the counts; the closed forms at `k = 4` (`2F_{2n+1}`) and `k = 5` give 2 at `n = 0`, so they hold for `n ≥ 1`.[^5][^exec] A partial-fraction lemma for `1/U_m` and `(1 + U_{m−1})/U_m` turns Theorem 2.2 into Theorem 2.4:[^6]

```
sw_{n,k}  =  (2/(k+1)) Σ_{j odd, j ≤ k} cot²(jπ/(2(k+1))) · (1 + 2cos(jπ/(k+1)))^{n−1}        (n ≥ 1),
```

so `sw_{n,k} ~ (2/(k+1)) cot²(π/(2(k+1))) (1 + 2cos(π/(k+1)))^{n−1}` (Corollary 2.5). For large `k` the constant is `8k/π² + O(1)`, against the bound `k·3^{n−1}` from `k` first letters and at most three choices for each later one.[^7]

**Smooth cyclic words.** The same matrix with the last letter tracked gives Theorem 3.2, and the partial fractions give Theorem 3.3, `scw_{n,k} = Σ_{j=1}^{k} (1 + 2cos(jπ/(k+1)))^n`, the trace of the `n`-th power of the transfer matrix. Smooth and smooth cyclic words have the same growth, and the fraction of smooth words that are cyclic tends to `½(k + 1)(2cos(π/(k+1)) + 1) tan²(π/(2(k+1)))` (Corollaries 3.4, 3.5).[^8]

**Smooth necklaces.** Theorem 3.2 and an exercise of Stanley's *Enumerative Combinatorics* (Vol. 2, 7.112(a)) give Theorem 4.1, `sn_{n,k} = (1/n) Σ_{j | n} φ(j) Σ_{i=1}^{k} (1 + 2cos(iπ/(k+1)))^{n/j}`, with `φ` Euler's totient.[^9]

## The castle reading

A smooth word over `[h]` of length `w` is a skyline `(c_1, …, c_w)` with `1 ≤ c_i ≤ h` and neighboring columns differing by at most 1: a free 1-smooth strip on `h` heights, which need not reach `h` ([[1-smooth-castles](pages/1-smooth-castles.md)]). So:

- **Anchored strips.** The words with first letter 1 are the anchored strips: `sw_h(x | 1) = Σ_w strips(w, h) x^w`, and (2.5) at `i = 1` is the cofactor formula of [[1-smooth-castles](pages/1-smooth-castles.md)] §3.1 written with Chebyshev polynomials. The paper's `θ_i` are the determinants `χ_i`.
- **Free castles.** The free 1-smooth castles of height `h` number `sw_{w,h} − sw_{w,h−1}`, and Theorem 2.4 is the free-first-column cosine sum of [[1-smooth-castles](pages/1-smooth-castles.md)], section *Other boundary conditions*. The row `k = 3` of Table 1 is the any-first-column Pell strip, `A001333(w + 1)` ([[pell-castle-strip](pages/pell-castle-strip.md)]).
- **Cyclic castles.** The smooth cyclic words are the 1-smooth skylines with `|c_w − c_1| ≤ 1`, a boundary condition the wiki had not used; their castles of height `h` are counted by the difference of two traces (section *Other boundary conditions* of [[1-smooth-castles](pages/1-smooth-castles.md)]).
- **Not covered.** The paper has no block count, so it does not see the parity split of Project Euler 502, and it treats only steps of size 1, not the m-smooth rule of [[m-smooth-castles](pages/m-smooth-castles.md)].

Every theorem of the paper, the three printed generating functions, and both tables were rechecked by enumeration.[^exec]

## Key Takeaways

- **The smooth rule is a tridiagonal matrix with Chebyshev determinants.** `θ_i = x^i U_i((1 − x)/(2x))`, and every entry of its inverse is a quotient of these.[^3]
- **Free and anchored strips in closed form.** (2.5) gives the strips with any fixed first letter; Theorem 2.4 gives the free count as a cotangent-weighted cosine sum over the odd indices.[^4][^6]
- **The cyclic count is a trace.** All `k` eigenvalues enter with coefficient 1.[^8]

## Entities & Concepts

- [[1-smooth-castles](pages/1-smooth-castles.md)] - the anchored, free, pinned and cyclic 1-smooth castles of every height; this paper's words are its strips.
- [[pell-castle-strip](pages/pell-castle-strip.md)] - the case `k = 3`.
- [[castle-strip](pages/castle-strip.md)] - the transfer matrix on column heights, of which the paper's matrix is the 1-smooth case.
- [[kernel-method](pages/kernel-method.md)] - the other closed-form route to bounded strips, for any step set.

## Relation to Other Wiki Pages

The wiki derived the anchored and free strip counts from the eigenvectors of `I + A_path` ([[1-smooth-castles](pages/1-smooth-castles.md)]); this paper reaches the same formulas through the inverse of the tridiagonal matrix and Chebyshev identities, and adds the cyclic words and necklaces. For larger steps the band matrix is no longer tridiagonal, and [[banderier-nicodeme-2010-bounded-discrete-walks](pages/banderier-nicodeme-2010-bounded-discrete-walks.md)] gives the strips through the roots of a kernel instead. The OEIS table of free smooth words by alphabet size, A188866, links this paper.[^10] The smooth words over `[h]` and the 2-disparate skylines, whose neighboring letters differ by at least 2, obey complementary rules, so by the Hilbert duality of [[hilbert-castles](pages/hilbert-castles.md)] the 2-disparate skylines on `h` heights have the series `1/sw_h(−x)`; at `k = 4` the smooth words are the Hilbert skylines on four heights with the letters relabeled, since the path on four vertices is its own complement.

## Footnotes

[^1]: [[knopfmacher-mansour-munagi-prodinger-2008-smooth-words](pages/knopfmacher-mansour-munagi-prodinger-2008-smooth-words.md)] p.1 L1-L9 [synthesis] - the title "SMOOTH WORDS AND CHEBYSHEV POLYNOMIALS", the four authors, and the arXiv stamp "arXiv:0809.0551v1 [math.CO] 3 Sep 2008".
[^2]: [[knopfmacher-mansour-munagi-prodinger-2008-smooth-words](pages/knopfmacher-mansour-munagi-prodinger-2008-smooth-words.md)] p.1 Abstract L10-L17 - "A word σ = σ1 · · · σn over the alphabet [k] = {1, 2, . . . , k} is said to be smooth if there are no two adjacent letters with difference greater than 1. A word σ is said to be smooth cyclic if it is a smooth word and in addition satisfies |σn − σ1 | ≤ 1." and "We also enumerate smooth necklaces, which are cyclic smooth words that are not equivalent up to rotation."
[^3]: [[knopfmacher-mansour-munagi-prodinger-2008-smooth-words](pages/knopfmacher-mansour-munagi-prodinger-2008-smooth-words.md)] §2 Lemma 2.1 and (2.1)-(2.2) L108-L137, L168 [synthesis] - the first-letter recursion; "A = (aij ) is a k × k matrix defined by aii = 1 − x, ai(i+1) = a(i+1)i = −x"; "Applying a result of Usmani [8] on the inversion of A"; "θi satisfies the recurrence relation θi = (1 − x)θi−1 − x2 θi−2 , with the initial conditions θ0 = 1 and θ1 = 1 − x. It follows from (1.1) that the solution is given by θi = x^i Ui((1−x)/2x)"; footnote "Equivalent results have been published earlier, for instance in [3]", reference [3] being Panny and Prodinger 1985 (L713-L714).
[^4]: [[knopfmacher-mansour-munagi-prodinger-2008-smooth-words](pages/knopfmacher-mansour-munagi-prodinger-2008-smooth-words.md)] §2 (2.3)-(2.5) and Theorem 2.2 L180-L222 [synthesis] - the sum identity (2.3), the product identity (2.4), "swk (x | i) = [Uk (t) − Uk−i (t) − Ui−1 (t)] / (2(t − 1)Uk (t))" (2.5), and Theorem 2.2's generating function of all smooth words.
[^5]: [[knopfmacher-mansour-munagi-prodinger-2008-smooth-words](pages/knopfmacher-mansour-munagi-prodinger-2008-smooth-words.md)] p.5 L233-L252 [synthesis] - the generating functions `sw_3`, `sw_4`, `sw_5` and the closed forms, "the number of smooth words in [4]^n is given by ... = 2F2n+1" and the `(1 ± √3)^{n+1}` form at `k = 5`, stated without a range of `n`.
[^6]: [[knopfmacher-mansour-munagi-prodinger-2008-smooth-words](pages/knopfmacher-mansour-munagi-prodinger-2008-smooth-words.md)] §2 Lemma 2.3 and Theorem 2.4 L255-L332 [synthesis] - the partial fractions of `1/U_m(x)` and `(1 + U_{m−1}(x))/U_m(x)` over the zeros `cos(jπ/(m+1))`, and "The number of smooth words of length n over the alphabet [k] is given by swn,k = (1/(k+1)) Σ_{j=1}^{k} (1 + (−1)^{j+1}) cot²(jπ/(2(k + 1))) (1 + 2 cos(jπ/(k+1)))^{n−1}", with the odd-index form.
[^7]: [[knopfmacher-mansour-munagi-prodinger-2008-smooth-words](pages/knopfmacher-mansour-munagi-prodinger-2008-smooth-words.md)] §2 Corollary 2.5 L439-L453 [synthesis] - the asymptotic `swn,k ∼ (2/(k+1)) cot²(π/(2(k+1))) (1 + 2 cos(π/(k+1)))^{n−1}` the upper bound from "k possible initial letters for a smooth word and at most three possibilities thereafter for each subsequent letter", and the expansion of `(2/(k+1)) cot²(π/(2(k+1)))` as `8k/π² + 8/π² + O(1/k)`.
[^8]: [[knopfmacher-mansour-munagi-prodinger-2008-smooth-words](pages/knopfmacher-mansour-munagi-prodinger-2008-smooth-words.md)] §3 Theorems 3.2-3.3, Corollaries 3.4-3.5 L499-L668 [synthesis] - the generating function of smooth cyclic words, "The number of smooth cyclic words of length n over the alphabet [k] is given by scwn,k = Σ_{j=1}^{k} (1 + 2 cos(jπ/(k+1)))^n", the equal growth, and the limiting proportion `½(k + 1)(2 cos(π/(k+1)) + 1) tan²(π/(2(k+1)))`.
[^9]: [[knopfmacher-mansour-munagi-prodinger-2008-smooth-words](pages/knopfmacher-mansour-munagi-prodinger-2008-smooth-words.md)] §4 Theorem 4.1 L682-L691 [synthesis] - "The number snn,k of smooth necklaces of length n over an alphabet of k letters is given by snn,k = (1/n) Σ_{j|n} Σ_{i=1}^{k} φ(j) (1 + 2 cos(iπ/(k+1)))^{n/j}", from Theorem 3.2 and Stanley's EC2 Exercise 7.112(a).
[^10]: https://oeis.org/A188866 (read 2026-10-22) - comment "Number of 0..n strings of length k and adjacent elements differing by one or less."; links "Arnold Knopfmacher, Toufik Mansour, Augustine Munagi and Helmut Prodinger, Smooth words and Chebyshev polynomials, arXiv:0809.0551v1 [math.CO], 2008."; offset 1,1, row `n` is the alphabet `{0, …, n}`.
[^exec]: Verified by execution (Python 3.11 with SymPy, 2026-10-22), by enumerating smooth, smooth cyclic and smooth necklace words: Theorems 2.2, 2.4, 3.2 and 3.3 and (2.5) for every first letter, for `k ≤ 8` and `n ≤ 11`; Theorem 4.1 against brute-force necklaces for `k ≤ 8`, `n ≤ 7`; Table 1 (`k = 3, …, 7`, `n ≤ 11`) and Table 2 (`k ≤ 7`, `1 ≤ n ≤ 11`, by Theorem 4.1 with the enumerated cyclic counts) entry by entry; the three printed generating functions at `k = 3, 4, 5` to 12 terms; the closed forms at `k = 3` for `n ≥ 0` and at `k = 4, 5` for `1 ≤ n ≤ 13`, both giving 2 at `n = 0`; Corollary 3.5 at `k = 3` and `k = 6` (`n = 300`); `sw_h(x | 1)` against the anchored strips of [[1-smooth-castles](pages/1-smooth-castles.md)] for `h ≤ 8`.
