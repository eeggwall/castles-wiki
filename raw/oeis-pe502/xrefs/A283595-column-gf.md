# Formula draft — A283595 (Motzkin prefixes by length and height), the column generating functions

Status: DRAFT for Charles to submit.
Execution notes (field map, signature format, scope): see ../SUBMISSION-NOTES.md.
Checked against the live entry 2026-10-23 (A283595 revision #41, Mar 26 2018).

## Edits (lines to add)

**FORMULA** (the entry has no formula section):

```
From _Chaz Reid_, Oct 23 2026: (Start)
G.f. of column k: z^k/(R_k*R_{k+1}), where R_{2j} = P_j - z*P_{j-1}, R_{2j+1} = P_{j+1} - z^2*P_{j-1}, P_{-1} = 0, and P_k are the polynomials of A097862: P_0 = 1, P_1 = 1-z, P_k = (1-z)*P_{k-1} - z^2*P_{k-2}.
R_k = Product_{i=1..k, i odd} (1 - (1 + 2*cos(i*Pi/(k+1)))*z).
Proof: Motzkin prefixes of height at most k are walks from 0 on {0..k}, so by the eigenvalues of the walk's transfer matrix their g.f. is Sum_{i=1..k+1} c_i/(1 - (1 + 2*cos(i*Pi/(k+2)))*z) for constants c_i, and c_i = 0 for even i, since the eigenvector (sin(i*j*Pi/(k+2)))_{j=1..k+1} sums to 0, so this is a proper fraction over R_{k+1}. Column k is the difference of the cases k and k-1, a fraction over R_k*R_{k+1} whose numerator has degree at most k; it is z^k since T(n,k) = 0 for n < k and T(k,k) = 1. The two forms of R_k agree since P_k(z) = z^k*U_k((1-z)/(2*z)), U_{2j+1} = U_j*(U_{j+1} - U_{j-1}) and U_{2j} = (U_j - U_{j-1})*(U_j + U_{j-1}), with U the Chebyshev polynomials of the second kind. (End)
```

**CROSSREFS** (add one line, after "T(2n,n) gives A283667."):

```
Column k=2 gives A094706(n-1).
```

## Proof

Write `λ_i = 1 + 2cos(iπ/(k+2))`. A Motzkin prefix of height at most `k` is a walk on
`{0, ..., k}` from 0 with steps `-1, 0, 1`, so the prefixes of length `n` number
`e_0ᵀ M^n 𝟙`, where `M = I + A` and `A` is the adjacency matrix of the path on `k + 1`
vertices. `M` has eigenvalues `λ_1 > ... > λ_{k+1}` with eigenvectors
`v_i(j) = sin(ijπ/(k+2))`, `j = 1, ..., k+1`, so

    F_k(z) = Sum_n e_0ᵀ M^n 𝟙 z^n = Sum_i c_i/(1 - λ_i z),   c_i = v_i(1) Sum_j v_i(j) / |v_i|^2.

The sum `Sum_j sin(ijπ/(k+2))` is 0 for even `i` (the terms pair off under `j -> k+2-j`) and
`cot(iπ/(2(k+2)))` for odd `i`. No odd `i` has `λ_i = 0`, since that needs
`i = 2(k+2)/3`, which is even. So `F_k = N_k/R_{k+1}` with `deg N_k < deg R_{k+1}`,
where `R_{k+1}` is the product of `1 - λ_i z` over odd `i`.

Column `k` of the triangle is `F_k - F_{k-1}` (with `F_{-1} = 0`), which equals
`(N_k R_k - N_{k-1} R_{k+1})/(R_k R_{k+1})`. The numerator has degree at most
`⌈k/2⌉ + ⌈(k+1)/2⌉ - 1 = k`. A prefix of height `k` has length at least `k`, and the only one of
length `k` is `U^k`, so the column starts `z^k + ...`; since `R_k R_{k+1}` has constant term 1,
the numerator is `z^k`.

The P-form of `R_k`: `P_k(z) = z^k U_k((1-z)/(2z))` (same recurrence and initial values), and
the zeros of `U_k` are `cos(iπ/(k+1))`, so `P_k` is the product of `1 - (1 + 2cos(iπ/(k+1)))z`
over all `i = 1..k`. The Chebyshev factorizations give `P_{2j+1} = P_j (P_{j+1} - z^2 P_{j-1})`
and `P_{2j} = (P_j - z P_{j-1})(P_j + z P_{j-1})`. At `k = 2j+1` the even-`i` factors are those of
`P_j` (`cos(2iπ/(2j+2)) = cos(iπ/(j+1))`), so the odd-`i` product is `P_{j+1} - z^2 P_{j-1}`; at
`k = 2j` the zeros of `U_j - U_{j-1}` are `cos((2i-1)π/(2j+1))`, the odd-`i` angles, so the
odd-`i` product is `P_j - z P_{j-1}`.

On the wiki this is the anchored 1-smooth castle count `smooth(w, h) = T(w-1, h-1)`
(`wiki/pages/1-smooth-castles.md` §3.2-3.3), with `η_h = R_h`.

## Verification

`bin/python/a283595_column_gf.py` (log `bin/python/a283595_column_gf-run.log`, 2026-10-23),
with the b-file `b283595.txt` as argument: the b-file (rows 0..140, 10011 terms) equals a
brute-force count of Motzkin prefixes by length and height; the column g.f. reproduces every
column `k = 0..140` up to row 140, and `deg R_k = ⌈k/2⌉`; for `k <= 40`, the height-at-most-`k`
g.f. reduces to a proper fraction over `R_{k+1}`, the two factorizations of `P` hold, both
product forms agree with `R_k` and `P_k` to 35 digits, and the eigenvector sums vanish
exactly at even `i`; column 2 equals `A094706(n-1)` for `n = 2..140`.

## Already there (do NOT duplicate)

The name, "Row n has n+1 entries", Heinz's b-file, the Finch link (arXiv:1802.04615, which
cites A283595 for the counts and gives no column g.f.), the examples, the Maple and
Mathematica programs, and the Cf. lines (row sums A005773, `T(2n,n)` A283667, A000225,
A097862, A282869). No formula section.

## Flags

1. No novelty claim: bounded-height path g.f.s are classical. The line gives the formula and
   its proof only.
2. The variable is `z`, as in A097862's column g.f. `z^(2k)/[P_k*P_{k+1}]`, so that its `P_k`
   carry over unchanged.
3. If the editors find the proof line too long, the line can go and the first two lines
   stand.
