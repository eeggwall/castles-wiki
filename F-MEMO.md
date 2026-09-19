# F Division memo: tie-ins with compression, encryption, encoding

Running memo kept alongside the F Division pages. Every entry is a place where a fractional-order idea touches compression, encryption, or encoding (the R Division / S5 / S12 territory). Entries are dated, name the F item they came out of, and say what is verified versus conjectured. Plain hyphens. Repo-root file like `TODO.md`, not a wiki page.

Legend: `[v]` verified by execution, `[c]` conjecture or reading, `[q]` open question.

## 2026-09-19 - while building fractional-block-count

### Compression

- `[v]` **The fractional difference is a prediction residual.** For `0 < alpha < 1` every Grunwald-Letnikov weight past the first is negative and they sum to `-1`, so `Delta^alpha c_i = c_i - (power-law weighted mean of the columns to the left)`. The fractional block count is the positive part of the residual of a fixed linear predictor. `sum_i |Delta^alpha c_i|` is the L1 cost of coding the skyline through a `(1 - B)^alpha` whitening filter, which is the ARFIMA fractional-differencing filter. Minimizing it over `alpha` recovers the skyline's integration order `d` (see the argmin table in `scratch-fractional-block-count.py`).
- `[c]` **The castle-compression tier ladder gets a continuous rung.** Tier 2 (skyline) codes `c_i` raw (`alpha = 0`); Tier 3 (run-length / blocks) codes the first difference (`alpha = 1`). A fractional-order predictor sits between them and the best `alpha` for a skyline is a one-number description of how much memory it has. Candidate third axis for the rule-generated-castle detector.
- `[q]` Does the Rice / Golomb coder on the rounded fractional residual beat LPC-8 on the song-as-castle waveform? The song page's 9.5% vs 26.6% FLAC gap is the target.

### Encoding

- `[v]` **`B_alpha` at a fixed irrational `alpha` is close to an injective real-valued encoding of a castle.** `(4,2)`: 15 of 15 castles separated at `alpha = sqrt(2) - 1`; `(6,3)`: 657 of 665; `(6,4)`: 2866 of 3367. The map castle -> real number is a lossy-but-nearly-lossless hash with the castle's left-to-right position information baked in (the small-`alpha` expansion weights column `j` by the harmonic number `H_{w-j}`).
- `[v]` **`B_{1/2}` is exactly representable in binary.** The half-order weights are `1, -1/2, -1/8, -1/16, -5/128, ...`, so `B_{1/2}` of a width-`w` castle is an integer multiple of `2^{-(2w-2)}`: a fixed-point number with `2w - 2` fractional bits, no rounding. Half-order is the order to use if the statistic has to be stored or transmitted exactly.
- `[v]` **The residual collisions are tail-blind pairs.** For `alpha` near 1 the statistic cannot see how a castle descends after its last positive-residual column (`(1,1,1,4,1)` and `(1,1,1,4,2)` agree on all of `[0.5, 1)`), because the block count is the total ascent and never saw the descent either. An encoder that wants injectivity should use a small `alpha` or a two-sided difference; an encoder that wants to ignore trailing detail on purpose has a knob for exactly that.
- `[c]` **Position-aware, unlike area and blocks.** Area and block count are both invariant under reversing the skyline; `B_alpha` is not (in `(5,3)` only the 19 palindromes match their reversal). It is the first single-number castle statistic on the wiki that knows which end is which. For an encoding that is what you want; for a shape invariant it is a defect.

### Encryption

- `[v]` **Area parity is a trivial clause; block parity is not.** `sum_C (-1)^{area} = (-1)^{w+h+1}` in every cell, so an even-area PE 502 would have answer `(A +- 1)/2`. The one-bit parity check that makes PE 502 hard (and that castle-steganography channel B and the in-band-signaling item exploit) is hard only because it sits at `alpha = 1`; at `alpha = 0` the same construction leaks nothing.
- `[v]` **The fractional sign `e^{i pi B_alpha}` is a keyed phase, and it is not a simple dephasing.** With `alpha` as a secret, the phase is a check value only the key holder computes. The cell-wide phase sum `|P_alpha|` stays near zero to `alpha = 0.25`, then grows and *exceeds* `|P_1|` inside `(0.5, 1)` (`(6,4)`: 157 at `alpha = 0.9` against `|P_1| = 91`). So the fractional phases of a uniform cell are more aligned at three-quarter order than the integer signs are: a keyed check at `alpha = 0.9` has a larger bias than the parity bit itself. For a check value you want the flat region, `alpha <= 0.25`.
- `[q]` **Steganography channel B under a fractional warden.** The block-parity channel flips one bit per row castle by a one-cell edit at a strict local extremum. That edit changes `B_alpha` for every `alpha`, by a position-dependent amount (a cell in column `j` moves `B_alpha` by about `1 - alpha H_{w-j}` at small `alpha`). A warden computing `B_alpha` at several `alpha` sees more than the parity; whether the edit's fingerprint is detectable against the natural distribution of `B_alpha` (variance minimum near `alpha = 0.75`) is the question the block-counting-warden item should add to its list.

## 2026-09-19 - while building fractional-width-and-height

### Encoding

- `[v]` **A half-column rule is a rate-2 recoding of a strip.** If `R^2 = M` with `R` a 0/1 rule, every width-`w` strip under `M` is a width-`2w` strip under `R` read at even columns: the castle language is re-encoded at twice the column rate with the same count. 8 of the 16 height-2 rules and 88 of the 512 height-3 rules admit such a recoding. The free strip `J` admits a weighted one, `J / sqrt h`; the metallic strips (1-smooth, ceiling exception) admit none, because a simple negative eigenvalue forbids any real square root. So the metallic-growth castle languages are the ones that cannot be split into finer columns: they are already at their finest encoding rate.
- `[c]` **The imaginary part as a checksum of the parity clause.** `Im F(w, m + 1/2) = (-1)^m (A_w(h-1) + A_w(h-2)) / 2` is an exact polynomial in `h` that measures how much of the count is due to the parity clause. It is a number one can attach to a `(w, h)` cell as a parity-load figure, independent of the actual castles.

### Encryption

- `[c]` **Square roots of the transfer matrix are the ring's root-extraction problem, seen over the reals.** Over `R` the question "does `M^{1/2}` exist" is answered by the sign of the eigenvalues (Higham). Over `F_p[x] / (char)` the same question becomes "is `x^w` a square in the ring", which is the quadratic-residuosity cousin of the castle DLP on castle-cryptography-ring. The real answer is a hint for the finite one: the `-1` eigenvalue that blocks the real half-column is, mod `p`, the element whose square root exists iff `p = 1 (mod 4)`. The F Division ring item should start there.

### Compression

- `[c]` **`log_2 F(w, h)` at fractional width is the bit cost per half column.** castle-entropy has `log_2 F ~ w log_2 h - 1`; the real interpolant makes `log_2 F(w, h)` a smooth function of `w`, and its derivative in `w` is the marginal cost of a column in bits, `log_2 h` in the limit with the parity bit's `-1` a constant offset. The oscillating cosine in `F(w, 2)` says the marginal cost of a column at height 2 wobbles with period 8 around `1` bit. Whether that wobble is visible in a real arithmetic coder over castles is a measurable question.
