---
title: "On the Discrete Logarithm Problem on Algebraic Tori (Granger-Vercauteren, 2005)"
category: Sources
summary: Granger and Vercauteren give an index calculus algorithm that works directly in the algebraic tori T_2(F_{q^m}) and T_6(F_{q^m}), following Gaudry and using the rational (compressed) representation of the torus. It is faster than Pollard rho in the full torus T_6(F_{q^m}) from m = 3. They state that LUC, XTR and CEILIDH over prime fields are not affected, and Table 2 shows the T_6 algorithm slower than Pollard rho at m = 1 in every row. Over extension fields the attack matters: T_30(F_p) embeds in T_6(F_{p^5}), the DLP there is feasible for p of about 20 bits, and the security of fields F_{q^30} "should be completely reassessed". §2 defines the torus T_n(F_q) as the elements whose norms to every proper subfield are 1 (the order-Φ_n(q) subgroup), shows that norms to subfields recover the discrete log only modulo the subfield orders, and gives the compression factor n/φ(n), 3 for T_6. The castle torus of round three is T_6(F_p), the prime-field case. Summarized: §§1-2, the comparisons of §§4.5 and 5.5, Table 2 with Remark 2, §6; not the decomposition and Gröbner-basis details of §§3-5.
tags: [paper, source, cryptography, cryptanalysis, discrete-logarithm, index-calculus, algebraic-torus, torus, xtr, ceilidh, luc, pollard-rho, finite-field, cyclotomic, compression]
sources: [granger-vercauteren-2005-dlp-algebraic-tori]
created: 2026-10-09
updated: 2026-10-25
---

# On the Discrete Logarithm Problem on Algebraic Tori (Granger-Vercauteren, 2005)

**Source:** `raw/granger-vercauteren-2005-dlp-algebraic-tori.pdf` (text layer at `raw/granger-vercauteren-2005-dlp-algebraic-tori.txt`, extracted with `pdftotext -layout`; the PDF is git-ignored, the text is tracked). The IACR archive copy of the CRYPTO 2005 paper (`iacr.org/archive/crypto2005/36210065/36210065.pdf`), 20 pp.; published in V. Shoup (ed.), *Advances in Cryptology - CRYPTO 2005*, LNCS 3621, Springer, 2005, pp. 66-85, doi:10.1007/11535218_5. Page numbers below are LNCS pages (PDF page 1 = p.66).[^1]
**Authors:** R. Granger (University of Bristol) and F. Vercauteren (University of Leuven).[^1]
**Date ingested:** 2026-10-09
**Type:** paper (PDF, 20 pp., conference paper)

> **Scope.** Summarized here: §1 (introduction and results), §2 (discrete logs in extension fields, the algebraic torus, rationality), the comparisons with other methods (§4.5 for `T_2`, §5.5 for `T_6`), Table 2 and Remark 2, and §6. Not summarized: §3 (Gaudry's method against classical index calculus) and the setup, decomposition base, relation finding and complexity analysis of §§4.1-4.4 and 5.1-5.4.

## Summary

**The torus.** Let `K = F_{q^n}` over `k = F_q`. The algebraic torus is[^2]

```
T_n(F_q) = { α ∈ K : N_{K/k_d}(α) = 1 for every subfield k ⊆ k_d ⊊ K }
```

By Lemma 1 (from Rubin and Silverberg) it is isomorphic to the subgroup of `F_{q^n}^×` of order `Φ_n(q)`, the `n`-th cyclotomic polynomial at `q`. An element of `T_n(F_q)` of prime order not dividing `n` lies in no proper subfield.[^3] XTR and CEILIDH work in the subgroup of `F_{q^6}^×` with order dividing `Φ_6(q) = q² − q + 1`, and an element there can be represented by two `F_q`-elements instead of six.[^4] When `T_n` is rational, its elements are represented by `φ(n)` elements of `F_q`, a compression factor of `n/φ(n)`, which is optimal. `T_n` is rational when `n` is a prime power or a product of two prime powers. CEILIDH uses `T_6`, with compression factor three.[^5]

**Why the torus is what is left.** Applying the norm maps to every intermediate subfield and solving the discrete logs there determines the exponent `s` only modulo `lcm{Φ_d(q) : d | n, d ≠ n}`. Up to a negligible factor, the rest of the discrete log comes from the order-`Φ_n(q)` subgroup, which is `T_n(F_q)`.[^6] The paper opens §2 with Odlyzko's 1984 remark that fields of composite extension degree "may be very weak", and says its main result shows the concern "may indeed be valid".[^7]

**The algorithm and its reach.** Following Gaudry, the algorithm is an index calculus that works directly in the torus, through its compressed representation. It is faster than Pollard rho in the full torus `T_2(F_{q^m})` from `m = 5` and in `T_6(F_{q^m})` from `m = 3`. In a prime-order subgroup of about `2^160` it is faster only for larger `m`.[^8] The authors state that over prime fields `F_p` the security of LUC, XTR, CEILIDH and MNT curves is not affected, and that over extension fields "this is not always the case".[^9] The compact representation that lowers the communication cost of the tori "may also be exploited by the cryptanalyst".[^14] §§4.5 and 5.5 repeat the conclusion after the complexity analysis. Neither algorithm improves on the existing attacks on LUC, XTR or CEILIDH over `F_p`, while XTR over extension fields and the `T_30(F_p)` system "need to be reassessed".[^10]

**Table 2 and `T_30`.** Table 2 gives the log₂ of the expected running time in seconds for the `T_6` algorithm at `m = 1, …, 5`, against Pollard rho in a subgroup of size `2^160`, for fields `F_{p^{6m}}` of 200 to 1000 bits:[^11]

| `log₂ |F_{p^{6m}}|` | Pollard rho | `m = 1` | `m = 2` | `m = 3` | `m = 4` | `m = 5` |
|---|---|---|---|---|---|---|
| 200 | 18 | 25 | 18 | 14 | 20 | 29 |
| 400 | 52 | 59 | 54 | 32 | 29 | 36 |
| 600 | 66 | 93 | 88 | 55 | 40 | 42 |
| 800 | 66 | 127 | 122 | 78 | 57 | 51 |
| 1000 | 69 | 161 | 156 | 101 | 74 | 60 |

(Five of the nine rows.) Remark 2: since `T_30(F_q)` embeds in `T_6(F_{q^5})`, the `m = 5` column bounds the DLP in `T_30`. The proposed `T_30` keys have 960 bits (`q` of 32 bits); the table shows the DLP in `T_30(F_p)` feasible "with p a prime of around 20 bits", and "the security offered by the DLP in finite fields of the form F_{q^30} should be completely reassessed".[^12] The conclusion says the techniques, made practical, "may weaken the security of practical systems based on T30".[^13]

## The castle reading

The castle torus of [[castle-cryptography-round-three](pages/castle-cryptography-round-three.md)] is the order-`p² − p + 1` subgroup of `F_{p^6}`, the castle ring `F_p[x]/(char_5)` with `char_5` irreducible mod `p`, which holds for a density `1/6` of primes, all with `p ≡ 3 (mod 4)` (round three, *Choosing p*). In this paper's notation it is `T_6(F_p)`, the case `q = p` prime and `m = 1`.

- **The attack does not apply.** This is the prime-field case the paper exempts.[^9][^10] In Table 2 the `m = 1` column is slower than Pollard rho in every row, and the gap grows with the field (25 against 18 bits of time at 200-bit fields, 161 against 69 at 1000 bits).[^11] Round three's full-size field has 3072 bits, beyond the table.
- **The subfield reduction.** Round three raises a torus element to `p^4 + p^2 + 1` and to `p^3 + 1`, the norm maps to `F_{p^2}` and `F_{p^3}`, and gets 1, since both exponents are multiples of `p² − p + 1`. That step is the norm-map reduction of §2.1: the subfields give the discrete log only modulo their orders, and the torus part remains.[^6] By Lemma 1, a torus element of prime order does not lie in a proper subfield.[^3]
- **Definition and compression.** Round three's torus (norms to `F_{p^2}` and `F_{p^3}` both 1, size `p² − p + 1`) is Definition 1 with `n = 6`. Its 3-to-1 trace compression is the compression factor `6/φ(6) = 3`.[^2][^4][^5]

## Entities & Concepts

- The castle torus, XTR and the trace compression - [[castle-cryptography-round-three](pages/castle-cryptography-round-three.md)].
- Subfield structure of `F_{p^n}` and the cyclotomic factors `Φ_d` - [[finite-fields](pages/finite-fields.md)].
- XTR, CEILIDH, LUC, DLP - [[acronyms](pages/acronyms.md)].

## Relation to Other Wiki Pages

[[castle-cryptography-round-three](pages/castle-cryptography-round-three.md)] cites this paper for the attacks that do not apply, for the subfield reduction and for its torus definition. [[castle-cryptography-round-two](pages/castle-cryptography-round-two.md)] prescribed the torus (Fix 4), with `p` chosen so that `Φ_d(p)` has a large prime factor, after its Attack 4 carried a key into a proper subfield.

## Footnotes

[^1]: [[granger-vercauteren-2005-dlp-algebraic-tori](pages/granger-vercauteren-2005-dlp-algebraic-tori.md)] p.66 L1-14 - title "On the Discrete Logarithm Problem on Algebraic Tori", "R. Granger and F. Vercauteren", "University of Bristol", "University of Leuven"; publication data from https://link.springer.com/doi/10.1007/11535218_5 (search-result excerpt 2026-10-09) - "Advances in Cryptology – CRYPTO 2005 ... Lecture Notes in Computer Science, vol 3621", "pp 66–85".
[^2]: [[granger-vercauteren-2005-dlp-algebraic-tori](pages/granger-vercauteren-2005-dlp-algebraic-tori.md)] §2.2 p.69 L152-155 - "Definition 1. Let k = Fq and let K = Fqn be an extension of k of degree n > 1. We define the algebraic torus Tn(Fq) as Tn(Fq) = {α ∈ K | NK/kd(α) = 1 for all subfields k ⊆ kd ⊊ K}."
[^3]: [[granger-vercauteren-2005-dlp-algebraic-tori](pages/granger-vercauteren-2005-dlp-algebraic-tori.md)] §2.2 p.69 L164-170 - "Lemma 1. 1. Tn(Fq) ≅ Gq,n and hence #Tn(Fq) = Φn(q). 2. If h ∈ Tn(Fq) is an element of prime order not dividing n, then h does not lie in a proper subfield of Fqn/Fq."
[^4]: [[granger-vercauteren-2005-dlp-algebraic-tori](pages/granger-vercauteren-2005-dlp-algebraic-tori.md)] §1 p.67 L59-65 - "LUC [25], XTR [16] and CEILIDH [22] ... the latter two working in a subgroup G ⊂ F×q6 with |G| | Φ6(q) = q² − q + 1"; "representing elements in G using only two Fq-elements, instead of six, effectively reducing the communication cost by a factor of three."
[^5]: [[granger-vercauteren-2005-dlp-algebraic-tori](pages/granger-vercauteren-2005-dlp-algebraic-tori.md)] §2.3 p.70 L188-194, L205-206 [synthesis] - rationality gives a representation by φ(n) elements of `F_q`, "an effective compression factor of n/φ(n) ... this compression factor is optimal. Tn is known to be rational when n is either a prime power, or is a product of two prime powers"; "CEILIDH [22] is based on the algebraic torus T6, which achieves a compression factor of three".
[^6]: [[granger-vercauteren-2005-dlp-algebraic-tori](pages/granger-vercauteren-2005-dlp-algebraic-tori.md)] §2.1 p.68 L133-140 - "by applying to g and h the norm maps NK/kd with respect to each intermediate subfield kd of K, and solving the resulting discrete logarithms in these subfields, a simple argument shows that one can determine s mod lcm{Φd(q)}d|n,d≠n"; "the remaining modular information required to determine the full discrete logarithm comes from the order Φn(q) subgroup of K×. As observed by Rubin and Silverberg [22], this subgroup is precisely the algebraic torus Tn(Fq)."
[^7]: [[granger-vercauteren-2005-dlp-algebraic-tori](pages/granger-vercauteren-2005-dlp-algebraic-tori.md)] §2 p.68 L118-123 - "in 1984 Odlyzko stated that fields with a composite extension degree 'may be very weak' [21]. The main result of this paper shows that these concerns may indeed be valid."
[^8]: [[granger-vercauteren-2005-dlp-algebraic-tori](pages/granger-vercauteren-2005-dlp-algebraic-tori.md)] §1 pp.67-68 L72-75, L93-97 - "The algorithm is based on the purely algebraic index calculus approach by Gaudry [10] and exploits the compact representation of elements of rational tori"; "faster than Pollard-Rho in the full torus T2(Fqm) for m ≥ 5 and in the full torus T6(Fqm) for m ≥ 3. However, in cryptographic applications one would work in a prime order subgroup of Tn(Fqm) of order around 2^160; in this case, our algorithm is only faster than Pollard-Rho for larger m."
[^9]: [[granger-vercauteren-2005-dlp-algebraic-tori](pages/granger-vercauteren-2005-dlp-algebraic-tori.md)] abstract p.66 L22-24 and §1 p.67 L78-81 - "Our results do not affect the security of the cryptosystems LUC, XTR, or CEILIDH over prime fields"; "We stress that when defined over prime fields Fp, the security of these cryptosystems is not affected by our algorithm. Over extension fields however, this is not always the case."
[^10]: [[granger-vercauteren-2005-dlp-algebraic-tori](pages/granger-vercauteren-2005-dlp-algebraic-tori.md)] §4.5 p.77 L532-535 and §5.5 p.82 L805-814 - "the T2 algorithm does not lead to an improvement over existing attacks on LUC [25], XTR [16] or CEILIDH [22] over Fp"; "the T6 algorithm does not lead to an improvement over the existing attacks on LUC [25], XTR [16], CEILIDH [22] or MNT curves [19] as long as these systems are defined over Fp. However, the security of XTR over extension fields, as proposed in [17] or of the recent proposal that works in T30(Fp) [27], needs to be reassessed".
[^11]: [[granger-vercauteren-2005-dlp-algebraic-tori](pages/granger-vercauteren-2005-dlp-algebraic-tori.md)] §5.4 p.82 Table 2 L766-779 - "log2 of expected running times (s) of the T6-algorithm and Pollard-Rho in a subgroup of size 2^160", columns `log₂|F_{p^{6m}}|`, `log₂|T_6(F_{p^m})|`, ρ and m = 1..5; rows 200, 400, 600, 800 and 1000 reproduced here.
[^12]: [[granger-vercauteren-2005-dlp-algebraic-tori](pages/granger-vercauteren-2005-dlp-algebraic-tori.md)] Remark 2 p.82 L784-792 - "the column for m = 5 provides an upper bound for the hardness of the DLP in T30(Fq), since this can be embedded in T6(Fq5)"; "keys of length 960 bits were recommended, i.e., with q of length 32 bits"; "it would be feasible to compute discrete logarithms in T30(Fp) with p a prime of around 20 bits"; "the security offered by the DLP in finite fields of the form Fq30 should be completely reassessed."
[^13]: [[granger-vercauteren-2005-dlp-algebraic-tori](pages/granger-vercauteren-2005-dlp-algebraic-tori.md)] §6 p.83 L848-850 - "These upper bounds indicate that if the techniques in this paper can be made fully practical and optimized, then they may weaken the security of practical systems based on T30."
[^14]: [[granger-vercauteren-2005-dlp-algebraic-tori](pages/granger-vercauteren-2005-dlp-algebraic-tori.md)] §1 p.67 L75-77 - "The very existence of such an algorithm shows that the lower communication cost offered by these tori, may also be exploited by the cryptanalyst."
