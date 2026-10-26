---
title: "Systematic Enumeration of Fundamental Quantities Involving Runs in Binary Strings (Balado-Silvestre, 2026)"
category: Sources
summary: Balado and Silvestre count binary strings by their runs of 1s, with recurrences, generating functions and explicit formulas in one framework that includes runs of length 0 (null runs), a fixed number of 1s, runs of 0s and 1s together, compositions, and the total number of runs over all strings. A binary string of length L is the row of blocks above a block of length L, its runs of 1s the blocks, so the paper is a census of one row of a castle, the castles of height 2, and through its link between runs and compositions, of the castles by area. Its counts give the Fibonacci castles (longest run of length 1), the height-2 row of the tower-spacing table (no run shorter than g), the castles of height h with every column 1 or h by semi-perimeter (every run at least h long, after lengthening each upper run by h − 1), the castles of area n by exact height (A000100, A000102, A006979, A006980, the triangle A048004), and the total numbers of blocks and of height-j columns. Summarized: §1.2, §§2.1-2.7 (the counts used here and their OEIS lists), §4.2, §5 through Theorem 5.1 and Remark 30, §8.1; not the run-parity, Bernoulli, other fixed-weight or joint-run sections.
tags: [paper, source, runs, binary-strings, generating-functions, compositions, fibonacci, n-nacci, tower-spacing, semiperimeter, oeis]
sources: [balado-silvestre-2026-runs-binary-strings]
created: 2026-10-25
updated: 2026-10-25
---

# Systematic Enumeration of Fundamental Quantities Involving Runs in Binary Strings (Balado-Silvestre, 2026)

**Source:** `raw/balado-silvestre-2026-runs-binary-strings.pdf` (text layer at `raw/balado-silvestre-2026-runs-binary-strings.txt`, extracted with `pdftotext -layout`; the PDF is git-ignored, the text is tracked). arXiv:2602.10005v2 [math.CO], 11 February 2026, CC BY-NC-ND 4.0, from `arxiv.org/pdf/2602.10005v2`.[^1]
**Authors:** Félix Balado and Guénolé C. M. Silvestre (School of Computer Science, University College Dublin).[^1]
**Date ingested:** 2026-10-25
**Type:** paper (PDF, 120 pp.)

> **Scope.** Summarized here: §1.2 (definitions), §2.1 (strings with `m` runs whose lengths lie in a window, and their generating function), the results and OEIS lists of §§2.2-2.7 used below (no short runs, nonnull runs, the longest run, the shortest nonnull run), §4.2 (nonnull runs at a fixed number of 1s), §5 through Theorem 5.1 and Remark 30 (runs of 0s and 1s, and compositions), and §8.1 (the total number of runs over all strings). Not summarized: §2.8 and its sequels §3.5, §4.4, §5.5 and §7.4 (runs of odd or even length), §3 and §6 (strings of independent Bernoulli bits), §4.1, §4.3 and §4.5, §§5.2-5.4, §7, §§8.2-8.4 and §9.

## Summary

**Runs.** A run is "an uninterrupted sequence of bits of the same kind, flanked on each side either by the opposite bit or by the start/end of the string" (Mood's counting criterion), and its length is its number of bits. Unqualified, "run" means a run of 1s. A `k`-run has length `k ≥ 0`. The paper counts **null runs**, runs of 1s of length 0, wherever a 0 follows a 0 and wherever the string starts or ends with 0, so `0010` has three null runs and `0000` has five; a nonnull run has length at least 1. An `n`-string is a binary string of length `n`.[^2]

**The window count.** The paper writes `w_{k̲≤k̄}(n, m)` for the number of `n`-strings with exactly `m` runs whose lengths lie between `k̲` and `k̄`; this page writes `w_{a≤b}(n, m)`. Other runs may occur. Splitting off the first run gives a recurrence, and its generating function is

```
W_{a≤b}(x, y)  =  Σ_{n,m} w_{a≤b}(n, m) x^n y^m  =  (1 − x) / ( x (1 − 2x + (1 − y)(x^{a+1} − x^{b+2})) ).        (16)
```

Its term `x^{−1}` is the value `w(−1, m) = [m = 0]` at the length `n = −1` that starts the recurrences (Remark 4). The other counts of §2 are special cases.[^3]

**Nonnull runs.** The `n`-strings with exactly `m` nonnull runs number

```
w(n, m)  =  C(n + 1, 2m),        (69)
```

which Goulden and Jackson found from a different generating function (Remark 12); the paper also sums over the number of 1s to derive it combinatorially. The strings with at least `m` nonnull runs number `2^n − Σ_{t=0}^{2(m−1)} C(n, t)`, A000225, A002662 and A002664 for `m = 1, 2, 3`.[^4] With the number of 1s fixed at `r`, the `n`-strings with `m ≥ 1` nonnull runs number

```
w(n, m, r)  =  C(r − 1, m − 1) C(n − r + 1, m),        (201)
```

given before by Stevens, Mood and others.[^5]

**The longest run.** The `n`-strings whose longest run has length at most `k` are the strings with no run of length at least `k + 1` (eq. 73), and they number `F^{(k+1)}_{n+k+1}` (eq. 83). Here `F^{(j)}` is the `j`-step Fibonacci sequence, `F^{(j)}_i = F^{(j)}_{i−1} + ⋯ + F^{(j)}_{i−j}` from `j − 1` zeros and a 1 (eq. 48), so `F^{(2)}` is Fibonacci and `F^{(3)}` is A000073 at its OEIS offset. The case `k = 1`, `F_{n+2}`, is Schilling's, and the strings whose longest run has length exactly 1 number `F_{n+2} − 1` (eq. 84).[^6] By §2.6.4, those whose longest run has length exactly `j` form the column `j` of A048004; at length `n − 1` they are A000100, A000102, A006979 and A006980 for `j = 2, 3, 4, 5`, "number of compositions of n in which the maximal part is j + 1", and at length `n − 2` with `j = 1` they are A000071.[^7]

**Short runs.** The `n`-strings with at least one 1 whose nonnull runs all have length at least `k` number `w_{≤(k−1)}(n, 0) − 1` for `k > 1`, the strings with no nonnull run of length at most `k − 1` less the all-zero string (eq. 87), and `2^n − 1` at `k = 1` (eq. 88). The paper finds them in the OEIS as `w_{≥2}(n + 2) = A077855(n)`, `w_{≥3}(n) = A130578(n)` and `w_{≥4}(n) = A209231(n)`.[^8] The strings with no nonnull run of length at most `k` are A005251, A005252, A005253, A005689, A098574 and A217838 for `k = 1, …, 6`, at shifts, and the strings with no run of length at least `k` are the `k`-step Fibonacci numbers (eq. 47).[^9]

**Compositions.** The parts of a composition of `n` are the lengths of the alternating runs of 0s and 1s of an `n`-string, and of its complement. Theorem 5.1 relates the counts by runs of 0s and 1s to the counts by runs of 1s with null runs included, `S_{a≤b}(x, y) = 2x W_{(a−1)≤(b−1)}(x, y)`, and Remark 30 turns it into compositions: the compositions of `n` with exactly `m` parts in `[a, b]` have generating function `x W_{(a−1)≤(b−1)}(x, y)` (eq. 273). Two of its examples are Riordan's. The compositions with no part above `k` have generating function `(x − x^{k+1})/(1 − 2x + x^{k+1})` (eq. 274), and those with largest part exactly `k` have `x^k (1 − x)² / ((1 − 2x + x^k)(1 − 2x + x^{k+1}))` (eq. 275), which the paper reads as a bijection between the compositions of `n + 1` with largest part `k` and the `n`-strings whose longest run has length `k − 1`.[^10]

**Totals.** Over all `n`-strings there are `ρ(n) = (n + 1) 2^{n−2}` nonnull runs (eq. 368), and `ρ_k(n) = (n − k + 3) 2^{n−k−2}` runs of length `k` for `k < n`, with `ρ_n(n) = 1` (eq. 367); the paper credits eq. (367) first to Gold, studying two-state meteorological series. `ρ_k(n + k)` is A045623 for every `k`, and `ρ(n + 1)` is A001792.[^11]

## The castle reading

**One row of blocks.** By the [[binary-string-bijection](pages/binary-string-bijection.md)], the row of blocks directly above a block of length `L` is a binary string of length `L`, a 1 for each covered column, and its blocks are the nonnull runs of 1s. So the paper counts the towers of height at most 1 on a base of length `L`, and the castles of height 2: a castle of width `w` and height 2 stands on a nonzero string of length `w` and has one block more than the string has runs.

| paper | castle |
|---|---|
| `n`-string | the row above a block of length `n` (a tower of height at most 1) |
| nonnull run of 1s | an upper block |
| run of 0s with 1s on both sides | a gap between two upper blocks |
| number of 1s `r` | the covered cells of the row; a castle of height 2 has area `w + r` |
| longest run at most `k`, shortest nonnull run at least `k` | every upper block at most, or at least, `k` long |
| a composition of `n` | a castle of area `n`, by its column heights |
| null run, in the composition reading | a column of height 1 |

Towers of height 2 and more are outside the paper: it never weights a run by the towers standing on it, as the recursions for `T(k, L)` and `P(k, L)` on [[binary-string-bijection](pages/binary-string-bijection.md)] do.

Each statement below was rechecked here by enumeration.[^exec]

- **Blocks and covered cells.** Eq. (69) is the count `C(L + 1, 2r)` of rows with `r` blocks on [[binary-string-bijection](pages/binary-string-bijection.md)] and [[block-count-constraints](pages/block-count-constraints.md)]. Eq. (201) refines it by the covered cells: the rows above a block of length `L` with `m ≥ 1` blocks covering `r` cells number `C(r − 1, m − 1) C(L − r + 1, m)`, and so do the castles of width `L`, height 2, `m + 1` blocks and area `L + r`. The rows with at least `m` blocks number `Σ_{t ≥ 2m−1} C(L, t)`.
- **Fibonacci castles.** A Fibonacci castle is a castle of height 2 whose upper blocks all have length 1 ([[fibonacci-castle](pages/fibonacci-castle.md)]), so `A_Fib(w) = F_{w+2} − 1` is eq. (84). The skylines of height at most 2 whose upper blocks are at most `k` long are eq. (83), `F^{(k+1)}_{w+k+1}` of width `w`, a `(k + 1)`-step Fibonacci count by width ([[n-nacci-disambiguation](pages/n-nacci-disambiguation.md)]).
- **Tower spacing at height 2.** [[tower-spacing-castles](pages/tower-spacing-castles.md)] proves that the skylines of height at most 2 and width `w` whose gaps are at least `g` correspond to the binary words of length `w + g − 1` whose runs of 1s are all at least `g` long, the paper's strings with no nonnull run of length at most `g − 1`. The paper's list for those strings, A005251, A005252, A005253, A005689, A098574 and A217838, is that page's row `h = 2` for `g = 2, …, 7`.
- **Semi-perimeter.** A castle of height `h` with every column 1 or `h` (at `h = 2`, any castle of height 2) with `r` runs of height-`h` columns has `1 + (h − 1)r` blocks, so semi-perimeter `s = w + 1 + (h − 1)r`. Delete the bottom row and lengthen each of the `r` runs by `h − 1` columns: the result is a nonzero string of length `s − 1` whose runs all have length at least `h`, and shortening each run by `h − 1` undoes it. So these castles are the paper's shortest-run count at `k = h`: `A077855(s − 3)` at `h = 2` and `A130578(s − 1)` at `h = 3`, the counts on [[golden-silver-bronze-plastic-castles](pages/golden-silver-bronze-plastic-castles.md)], and `A209231(s − 1)` at `h = 4`. By the tower-spacing identity they number `spacing_h(s − h, 2) − 1`, which matches the denominator `(1 − x)² − x^{h+1}` that [[semi-perimeter-growth-census](pages/semi-perimeter-growth-census.md)] gives for the two heights 1 and `h`.
- **Castles by area.** The map of [[castles-of-height-h-by-area](pages/castles-of-height-h-by-area.md)] sends a castle `(c_1, …, c_w)` of area `n` to the string `1^{c_1−1} 0 1^{c_2−1} 0 ⋯ 0 1^{c_w−1}` of length `n − 1`, so a column of height `c` becomes a run of `c − 1` 1s, null when `c = 1`. Then eq. (273) counts the castles of area `n` with `m` columns of height in `[a, b]`, and eqs. (274) and (275) are the castles of area `n` and height at most `k`, and exactly `k`. The rows `h = 3, …, 6` of that page are A000100, A000102, A006979 and A006980, and the whole table is the triangle A048004.
- **Totals.** The towers of height at most 1 on a base of length `L` have `(L + 1) 2^{L−2} = A001792(L − 1)` blocks in all, `(L + 1)/4` per tower on average. Through the composition map, eq. (367) counts the columns of height `j` over all castles of area `n`: `ρ_{j−1}(n − 1) = A045623(n − j)`, equal to `(n − j + 3) 2^{n−j−2}` for `j < n`. At `j = 1` this is the total of [[prime-castles](pages/prime-castles.md)].

## Key Takeaways

- One binary string is one row of blocks, so the paper is a census of the castles of height 2 by their upper blocks, and through compositions, of the castles by area by their column heights.
- The Fibonacci castles, the height-2 row of the tower-spacing table and the castles of height 2 by semi-perimeter are the paper's longest-run, no-short-run and shortest-run counts.
- The castles of height `h` with every column 1 or `h` and semi-perimeter `s` correspond to the nonzero strings of length `s − 1` with every run at least `h` long, by lengthening each run of height-`h` columns by `h − 1` (checked for `h ≤ 9`).
- The castles of area `n` and height exactly `h` are the column `h − 1` of A048004, and A000100, A000102, A006979, A006980 for `h = 3, …, 6`.
- The columns of height `j` over all castles of area `n` total A045623(n − j).

## Entities & Concepts

- One row of blocks as a binary string - [[binary-string-bijection](pages/binary-string-bijection.md)].
- Block-count generating functions at height at most 1 - [[block-count-constraints](pages/block-count-constraints.md)].
- Fibonacci castles - [[fibonacci-castle](pages/fibonacci-castle.md)]; the n-nacci mechanisms - [[n-nacci-disambiguation](pages/n-nacci-disambiguation.md)].
- Tower spacing - [[tower-spacing-castles](pages/tower-spacing-castles.md)].
- Castles by semi-perimeter - [[golden-silver-bronze-plastic-castles](pages/golden-silver-bronze-plastic-castles.md)], [[semi-perimeter-growth-census](pages/semi-perimeter-growth-census.md)], [[castle-classification-growth](pages/castle-classification-growth.md)].
- Castles by area as compositions - [[castles-of-height-h-by-area](pages/castles-of-height-h-by-area.md)], [[prime-castles](pages/prime-castles.md)].

## Relation to Other Wiki Pages

The pages listed above cite this paper for the counts in *The castle reading*. [[a005251-bijection](pages/a005251-bijection.md)] and [[tree-castle-by-area](pages/tree-castle-by-area.md)] carry the strings with no isolated 1, the paper's first no-short-run count, which it lists as A005251.

## Footnotes

[^1]: [[balado-silvestre-2026-runs-binary-strings](pages/balado-silvestre-2026-runs-binary-strings.md)] p.1 L1-15 and p.120 L6219 - "Systematic Enumeration of Fundamental Quantities Involving Runs in Binary Strings", "Félix Balado and Guénolé C.M. Silvestre", "arXiv:2602.10005v2 [math.CO] 11 Feb 2026", "School of Computer Science University College Dublin"; "2020 Mathematics Subject Classification: Primary 05A15". https://arxiv.org/html/2602.10005v2 (read 2026-10-25) - "License: CC BY-NC-ND 4.0".
[^2]: [[balado-silvestre-2026-runs-binary-strings](pages/balado-silvestre-2026-runs-binary-strings.md)] §1.2 p.3 L105-116, L118-126 and §1.3 p.6 L228-233 [synthesis] - Definition 1.1, "A run in a binary string is an uninterrupted sequence of bits of the same kind, flanked on each side either by the opposite bit or by the start/end of the string (Mood’s counting criterion [44]). The number of bits of the same kind in a run is its length."; Definitions 1.2-1.4, "A k-run means a run of length k, where k ≥ 0", "A null run is defined to be a 0-run, i.e., a zero-length run, whereas a nonnull run is a k-run with k ≥ 1"; Remark 1, the examples `0010` with three null runs of 1s, `0101` with one and `0000` with five; Remark 3, "the unqualified term “run” always implicitly refers to a run of ones unless explicitly specified otherwise".
[^3]: [[balado-silvestre-2026-runs-binary-strings](pages/balado-silvestre-2026-runs-binary-strings.md)] §2.1 p.6 L245-248, Remark 4 p.7 L281-288 and §2.1.2 pp.9-10 L402-438 [synthesis] - the definition of `w_{k̲≤k̄}(n, m)`, "Notice that such n-strings may also contain other runs longer than k or shorter than k"; the cases `n = −1` and `n = 0`, whose values start all the recurrences of §§2-4; the extended recurrence (15) and the generating function (16).
[^4]: [[balado-silvestre-2026-runs-binary-strings](pages/balado-silvestre-2026-runs-binary-strings.md)] §2.5 pp.24-26 L1188-1192, L1226-1300 and §2.5.4 pp.26-27 L1315-1340 [synthesis] - "the number of n-strings that contain exactly m nonnull runs", the generating functions (65) and (66) and eq. (69); Remark 12, "Goulden and Jackson [26, Sec. 2.4.4] found (69) using the following alternative ogf", and the combinatorial derivation through eq. (70); "w≥1 (n) = 2n − 1 is A000225", "w≥2 (n) is A002662", "w≥3 (n) is A002664", and `w^{≥m}(n) = 2^n − Σ_{t=0}^{2(m−1)} C(n, t)`.
[^5]: [[balado-silvestre-2026-runs-binary-strings](pages/balado-silvestre-2026-runs-binary-strings.md)] §4.2 pp.56-57 L2877-2950 [synthesis] - `w(n, m, r)`, "the number of n-strings of Hamming weight r that contain exactly m nonnull runs", the generating function (198) and eq. (201); "expression (201) was previously given by Stevens [63, Eq. (3.05)], Mood [44, Eq. (2.11)], Charalambides [10, p. 97], Gibbons and Chakraborti [22, Cor. 3.2.1] Schuster [56, Cor. 3.5] and others".
[^6]: [[balado-silvestre-2026-runs-binary-strings](pages/balado-silvestre-2026-runs-binary-strings.md)] §2.3 Remark 9 pp.18-19 L872-890, §2.6 p.27 L1378-1382 and §2.6.3 pp.29-30 L1477-1492 [synthesis] - "F_i^{(j)} are the jth order Fibonacci numbers, also called Fibonacci j-step numbers, j-nacci numbers", eq. (48), started from `F^{(j)}_{j−1} = 1` and `F^{(j)}_i = 0` for `0 ≤ i < j − 1`; eq. (73); eq. (83); "Schilling observed already the special case w≤1 (n) = F_{n+2}"; eq. (84), "w1 (n) = F_{n+2} − 1".
[^7]: [[balado-silvestre-2026-runs-binary-strings](pages/balado-silvestre-2026-runs-binary-strings.md)] §2.6.4 p.30 L1518-1523 - "w1 (n − 2) is A000071 (Fibonacci numbers minus one) for n ≥ 2", "wj (n − 1) for j = 2, 3 and 4 are A000100, A000102 and A006979, respectively (number of compositions of n in which the maximal part is j + 1) for n ≥ 1", "w5 (n − 1) is A006980 for n ≥ 6", "wk (n) is the kth column of A048004".
[^8]: [[balado-silvestre-2026-runs-binary-strings](pages/balado-silvestre-2026-runs-binary-strings.md)] §2.7 pp.30-31 L1529-1554 and §2.7.4 p.33 L1664-1670 [synthesis] - "the number of n-strings whose shortest run is a (≥ k)-run", eqs. (87) and (88), "We subtract one both in (87) and in (88) to discount the all-zeros n-string"; "w≥2 (n + 2) is A077855", "w≥3 (n) is A130578", "w≥4 (n) is A209231".
[^9]: [[balado-silvestre-2026-runs-binary-strings](pages/balado-silvestre-2026-runs-binary-strings.md)] §2.4.4 p.24 L1169-1176 and §2.3 p.18 L872-874, §2.3.4 p.19 L921-925 [synthesis] - "w≤1 (n − 2, 0) = w1 (n − 2, 0) is A005251 for n ≥ 2", "w≤2 (n − 1, 0) is A005252 for n ≥ 1", "w≤3 (n, 0) is A005253", "w≤4 (n − 2, 0) is A005689 (number of Twopins positions) for n ≥ 6", "w≤5 (n − 1, 0) is A098574 for n ≥ 1", "w≤6 (n + 6, 0) is A217838"; eq. (47), `w_{≥k}(n, 0) = F^{(k)}_{n+k}`, with A000045, A000073, A000078 and A001591 for `k = 2, …, 5`.
[^10]: [[balado-silvestre-2026-runs-binary-strings](pages/balado-silvestre-2026-runs-binary-strings.md)] §5 p.63 L3238-3243, Theorem 5.1 p.66 L3358-3360 and Remark 30 pp.74-75 L3785-3828 [synthesis] - the parts of a composition of `n` as "the ordered lengths of an alternating series of runs of ones and zeros in an n-string, and in its ones’ complement"; eq. (235); eq. (273); eq. (274), "which was also given by Riordan [53, Eq. (40)]"; eq. (275), "which was given by Riordan as well [53, p. 155]. Expression (275) can be read as a bijection between the compositions of n + 1 with largest part equal to k and the n-strings with longest run (of ones) a (k − 1)-run."
[^11]: [[balado-silvestre-2026-runs-binary-strings](pages/balado-silvestre-2026-runs-binary-strings.md)] §8.1.1 p.97 L5066-5075, Remark 35 p.98 L5087-5089 and §8.1.2 p.100 L5213-5215 [synthesis] - "We denote the number of k-runs over all n-strings by ρk (n), and the number of nonnull runs (of arbitrary lengths, all strictly greater than zero) over all n-strings by ρ(n)", eqs. (367) and (368); "the first author who produced (367) was Gold [24, 14], in his analysis of the predictability of two-state meteorological series"; "ρk (n + k) is A045623 (number of 1’s in all compositions of n + 1)", "ρ≥k (n + k) and ρ(n + 1) are A001792".
[^exec]: Verified by execution (Python 3.11 with SymPy, 2026-10-25), by brute force over binary strings, compositions and skylines, with the null runs of a string read off by splitting it at its 0s: eq. (16) for the windows `[0, 0]`, `[0, 2]`, `[1, 1]`, `[1, 3]`, `[2, 2]`, `[2, 4]`, `[1, 9]` and `n ≤ 9`; eq. (69) for `n ≤ 12`; eq. (201) for `n ≤ 12`, `m ≥ 1`; the strings with at least `m` nonnull runs for `n ≤ 12`, `m ≤ 5`, and their terms against A000225, A002662 and A002664; eq. (368) for `n ≤ 14` and eq. (367) for `n ≤ 13`, `0 ≤ k ≤ n`; eq. (83) for `k ≤ 4`, `n ≤ 13` and eq. (84) for `n ≤ 14`; the tower-spacing correspondence for `2 ≤ g ≤ 6`, `w ≤ 11`, and `spacing_7(w, 2) = A217838(w)` for `w ≤ 16`; the lengthening map, a bijection from the castles of height `h` with every column 1 or `h` and semi-perimeter `s` onto the nonzero strings of length `s − 1` with every run at least `h` long, for `h ≤ 5`, `s ≤ 14`, the count `spacing_h(s − h, 2) − 1` for `h ≤ 9`, `s ≤ h + 11`, and `A209231(s − 1)` at `h = 4` for `s ≤ 14`; the composition map, a bijection onto the strings of length `n − 1` sending the height to the longest run plus 1 and the columns of height `j` to the runs of length `j − 1`, for `n ≤ 14`; the castles of area `n ≤ 14` and exact height 3, 4, 5, 6 against A000100, A000102, A006979 and A006980; the totals of height-`j` columns against A045623 for `n ≤ 14`; eqs. (274) and (275) against Equation (2) of [[castles-of-height-h-by-area](pages/castles-of-height-h-by-area.md)], symbolically for `k ≤ 9`. OEIS names and offsets read at https://oeis.org on 2026-10-25 (see the citing pages).
