---
title: Tone-castle catalogue - telephone signalling tones as exactly periodic castles
category: Analyses
summary: Every DTMF key, every R1 MF signal, the Bell precise-tone-plan call-progress tones and the 2600 Hz trunk tone, sampled 8000 times per second (the G.711 rate; the voice band is 300-3400 Hz, below the 4000 Hz Nyquist limit) and quantized to h = 256, as castles. A tone pair (f1, f2) in whole hertz has exact period w = 8000/gcd(8000, f1, f2), so every signal is a periodic castle of width w. All 15 MF signals have w = 80 (10 ms), shorter than the 27 ms minimum MF digit, so every MF burst holds at least two whole periods; DTMF keys have w = 8000 except 5 (4000) and 8 (2000), longer than the 45-55 ms DTMF burst, so a DTMF burst never holds a whole period and is only approximately periodic (best near-period phase error 0.006 to 0.035 cycles). The four nominal DFT atoms carry 99.997-99.999% of the mean-removed energy, but the exact support is a union of divisor classes: all w bins for 30 of the 35 castles. With the castle's tallest column first, blocks of r repeated periods = c_w + r·rise(c) with rise(c) odd for every signal, so the PE 502 parity of a burst alternates with the number of periods. Goertzel over a whole MF period is an exact DFT bin (off-tone response 0 before quantization, at least 49.6 dB down after); a DTMF detector's 136-sample block sits between bins, where the castle's area leaks in and moves the per-group margins by -2.9 to +3.9 dB until the mean is subtracted.
tags: [analysis, castle, audio, telephone, dtmf, mf-signaling, goertzel, dft, periodicity, sparse-spectrum, divisor-classes, block-parity, quantization, signal-processing]
sources: [project-euler-502-representations]
created: 2026-10-01
updated: 2026-10-01
---

# Tone-castle catalogue - telephone signalling tones as exactly periodic castles

Telephone signalling tones are sums of one or two sine waves at whole-hertz frequencies, and the digital telephone network takes 8000 samples per second. A sampled tone is therefore exactly periodic, and one period, quantized, is a castle. This page builds that castle for every DTMF key, every R1 MF signal, the Bell call-progress tones and the 2600 Hz trunk tone, and records for each one its period, its skyline DFT support, its block count, and what a Goertzel detector sees.

[[song-as-castle](pages/song-as-castle.md)] introduced the 2600 Hz tone (a width-40 castle) and the MF KP signal (width 80) as examples. [[spectral-analysis](pages/spectral-analysis.md)] §3 proves that the DFT support of a whole-number skyline is a union of divisor classes, which is why a quantized tone is sparse only approximately. This page runs both through the full set of signals.

## Sampling rate and bandwidth

Two different numbers describe the telephone channel. The **sampling rate** is 8000 samples per second, each stored as 8 bits (the 64 kbit/s of the G.711 standard). The **bandwidth** is the range of frequencies the channel passes, the voice band of about 300 to 3400 Hz.[^g711] The castle is built on the sampling rate: one column per sample, and the 8000 in every period formula below is a count of samples per second, not a frequency.

The Nyquist limit relates the two. Sampling 8000 times per second represents frequencies only up to half that rate, 4000 Hz. A tone at `f` above 4000 Hz is sampled as a tone at `8000 − f`, since `cos(2π(8000 − f)j/8000 + φ) = cos(2πfj/8000 − φ)` at every sample `j` (aliasing). The voice band stops at 3400 Hz, leaving the 600 Hz up to 4000 Hz for the filter in front of the sampler to cut off.

Every tone in the catalogue, 350 to 2600 Hz, lies inside the voice band and so below 4000 Hz. In the castle's DFT this is the statement that each atom `k_i = f_i w / 8000` lies below `w/2`: bin `w/2` is the 4000 Hz Nyquist frequency, and the mirror atom `w − k_i` is the alias of the same tone. With phase 0, `f` and `8000 − f` give the same castle.

## The construction

A signal of `a` tones (`a = 1` or `2`) at frequencies `f_1, f_2` (whole hertz) is sampled 8000 times per second and starts at phase 0:

```
x_j  =  Σ_i cos(2π f_i j / 8000),          j = 0, 1, 2, …
c_{j+1}  =  1 + floor( 255 · (x_j + a) / (2a)  +  1/2 )      heights 1..256, h = 256
```

Column `j + 1` holds sample `j`. The quantizer maps `[−a, a]` linearly onto `[1, 256]` and rounds halves up. Every tone is at its peak at `j = 0`, so `c_1 = 256 = h`: the touch rule holds on the first column, and every height is at least 1. The castle is the skyline encoding of [[castle-representations](pages/castle-representations.md)], 8 bits per column.

**Period.** `cos(2π f j / 8000)` repeats when `f j / 8000` is a whole number, first at `j = 8000 / gcd(8000, f)`. A sum of tones repeats at the least common multiple of those periods:

```
w  =  8000 / gcd(8000, f_1, f_2)            the castle width
k_i  =  f_i · w / 8000                       the DFT bin of tone i (a whole number)
```

The tone completes `k_i` cycles in `w` samples. Before quantization the DFT of one period is supported on `{0, k_1, k_2, w − k_1, w − k_2}`: bin 0 is the castle's area, the others are the four **atoms**.

Integer frequencies make every signal exactly periodic with period at most 8000 samples (one second). The catalogue's question is whether that period fits inside the signal as it is actually sent: a tone burst shorter than one period is, as a castle, only approximately periodic.

## Single tones

| tone | used in | `gcd(8000, f)` | period `w` (samples) | cycles `k` | period |
|---|---|---|---|---|---|
| 697 | DTMF row | 1 | 8000 | 697 | 1000 ms |
| 770 | DTMF row | 10 | 800 | 77 | 100 ms |
| 852 | DTMF row | 4 | 2000 | 213 | 250 ms |
| 941 | DTMF row | 1 | 8000 | 941 | 1000 ms |
| 1209 | DTMF column | 1 | 8000 | 1209 | 1000 ms |
| 1336 | DTMF column | 8 | 1000 | 167 | 125 ms |
| 1477 | DTMF column | 1 | 8000 | 1477 | 1000 ms |
| 1633 | DTMF column | 1 | 8000 | 1633 | 1000 ms |
| 700, 900, 1100, 1300, 1700 | MF | 100 | 80 | 7, 9, 11, 13, 17 | 10 ms |
| 1500 | MF | 500 | 16 | 3 | 2 ms |
| 2600 | trunk idle tone | 200 | 40 | 13 | 5 ms |
| 350 | dial tone | 50 | 160 | 7 | 20 ms |
| 440 | dial, ringback | 40 | 200 | 11 | 25 ms |
| 480 | ringback, busy | 160 | 50 | 3 | 6.25 ms |
| 620 | busy | 20 | 400 | 31 | 50 ms |

Five of the eight DTMF frequencies are coprime to 8000 and have the longest possible period, one second. Every MF frequency is a multiple of 100 Hz, so every MF tone repeats within 80 samples.[^exec]

## MF signals: all width 80

R1 multi-frequency signalling sends each of 15 codes as a pair from {700, 900, 1100, 1300, 1500, 1700} Hz.[^mf] The pair's gcd with 8000 is 100 in every case, so **every MF signal is a width-80 castle**, one period every 10 ms. The minimum MF timings are 27 ms per digit and 55 ms for KP,[^mf-timing] that is 216 and 440 samples: every MF burst holds at least 2.7 periods (KP at least 5.5).

| code | tones (Hz) | atoms `k_1, k_2` | atom classes `d` | nonzero bins | blocks (one period) | `c_w` | even-block bursts of `r` periods |
|---|---|---|---|---|---|---|---|
| 1 | 700 + 900 | 7, 9 | 1, 1 | 80 | 1546 | 231 | `r` odd |
| 2 | 700 + 1100 | 7, 11 | 1, 1 | 80 | 1749 | 224 | `r` even |
| 3 | 900 + 1100 | 9, 11 | 1, 1 | 80 | 1859 | 218 | `r` even |
| 4 | 700 + 1300 | 7, 13 | 1, 1 | 80 | 1945 | 216 | `r` even |
| 5 | 900 + 1300 | 9, 13 | 1, 1 | 80 | 1991 | 210 | `r` even |
| 6 | 1100 + 1300 | 11, 13 | 1, 1 | 80 | 2106 | 203 | `r` odd |
| 7 | 700 + 1500 | 7, 15 | 1, 5 | 80 | 2130 | 207 | `r` odd |
| 8 | 900 + 1500 | 9, 15 | 1, 5 | 80 | 2190 | 201 | `r` odd |
| 9 | 1100 + 1500 | 11, 15 | 1, 5 | 80 | 2225 | 194 | `r` even |
| 0 | 1300 + 1500 | 13, 15 | 1, 5 | 80 | 2363 | 186 | `r` even |
| 11/ST3 | 700 + 1700 | 7, 17 | 1, 1 | 56 | 2305 | 198 | `r` even |
| 12/ST2 | 900 + 1700 | 9, 17 | 1, 1 | 80 | 2369 | 192 | `r` even |
| KP | 1100 + 1700 | 11, 17 | 1, 1 | 80 | 2456 | 185 | `r` odd |
| KP2 | 1300 + 1700 | 13, 17 | 1, 1 | 64 | 2510 | 177 | `r` odd |
| ST | 1500 + 1700 | 15, 17 | 5, 1 | 80 | 2559 | 168 | `r` even |

Columns: the **atom class** of `k` is `d = gcd(k, w)`, the class `D_d` of [[spectral-analysis](pages/spectral-analysis.md)] §3, which has `φ(w/d)` bins (32 for `d = 1`, 8 for `d = 5` at `w = 80`). **Nonzero bins** counts the support of the quantized castle, bin 0 included. `c_w` is the last column's height; the last column fixes the block parity of repeated bursts (below).

MF code 1 at `h = 9` (same quantizer with 8 in place of 255) shows the two tones beating: their difference, 200 Hz, gives an envelope that repeats every 40 columns.

```
(9, 8, 6, 4, 2, 1, 2, 4, 6, 7, 8, 7, 6, 4, 4, 3, 4, 5, 5, 5, 5, 5, 5, 5, 6, 7, 6, 6, 4, 3, 2, 3, 4, 6, 8, 9, 8, 6, 4, 2,
 1, 2, 4, 6, 8, 9, 8, 6, 4, 3, 2, 3, 4, 6, 6, 7, 6, 5, 5, 5, 5, 5, 5, 5, 4, 3, 4, 4, 6, 7, 8, 7, 6, 4, 2, 1, 2, 4, 6, 8)

#..................................#.........#..................................
##........#.......................###.......###.......................#........#
##.......###.............#........###.......###........#.............###.......#
###.....#####...........####.....#####.....#####.....####...........#####.....##
###.....#####....###########.....#####.....#####.....###########....#####.....##
####...########.#############...#######...#######...#############.########...###
####...#######################.########...########.#######################...###
#####.##################################.##################################.####
################################################################################
```

52 blocks. The skyline is symmetric about its first column (`c_{j+1} = c_{w−j+1}`), because both tones are cosines started at phase 0.

## DTMF keys: periods of 2000 to 8000 samples

Each DTMF key sends one row tone from {697, 770, 852, 941} Hz and one column tone from {1209, 1336, 1477, 1633} Hz.[^dtmf] Thirteen of the sixteen pairs have gcd 1 with 8000 and so have period 8000 samples (one second). Key 5 (770 + 1336, gcd 2) has period 4000 and key 8 (852 + 1336, gcd 4) has period 2000.

| key | tones (Hz) | `w` | atoms `k_1, k_2` | atom classes `d` | nonzero bins | blocks (one period) | `c_w` |
|---|---|---|---|---|---|---|---|
| 1 | 697 + 1209 | 8000 | 697, 1209 | 1, 1 | 8000 | 161955 | 220 |
| 2 | 697 + 1336 | 8000 | 697, 1336 | 1, 8 | 8000 | 174936 | 215 |
| 3 | 697 + 1477 | 8000 | 697, 1477 | 1, 1 | 8000 | 189133 | 208 |
| A | 697 + 1633 | 8000 | 697, 1633 | 1, 1 | 5600 | 204464 | 201 |
| 4 | 770 + 1209 | 8000 | 770, 1209 | 10, 1 | 8000 | 164853 | 218 |
| 5 | 770 + 1336 | 4000 | 385, 668 | 5, 4 | 4000 | 88888 | 213 |
| 6 | 770 + 1477 | 8000 | 770, 1477 | 10, 1 | 8000 | 191531 | 206 |
| B | 770 + 1633 | 8000 | 770, 1633 | 10, 1 | 8000 | 206650 | 199 |
| 7 | 852 + 1209 | 8000 | 852, 1209 | 4, 1 | 7996 | 168489 | 216 |
| 8 | 852 + 1336 | 2000 | 213, 334 | 1, 2 | 2000 | 45361 | 210 |
| 9 | 852 + 1477 | 8000 | 852, 1477 | 4, 1 | 8000 | 194503 | 204 |
| C | 852 + 1633 | 8000 | 852, 1633 | 4, 1 | 8000 | 209360 | 197 |
| * | 941 + 1209 | 8000 | 941, 1209 | 1, 1 | 6080 | 172916 | 213 |
| 0 | 941 + 1336 | 8000 | 941, 1336 | 1, 8 | 8000 | 184812 | 207 |
| # | 941 + 1477 | 8000 | 941, 1477 | 1, 1 | 8000 | 198122 | 201 |
| D | 941 + 1633 | 8000 | 941, 1633 | 1, 1 | 8000 | 212555 | 194 |

**No DTMF burst holds a whole period.** The AT&T timing puts each DTMF tone in a 100 ms slot, sounding for at least 45 ms and at most 55 ms,[^att] that is 360 to 440 samples. The shortest DTMF period is 2000 samples. A transmitted DTMF key is therefore a castle of width 360 to 440 cut from a periodic castle of width 2000 to 8000, and it does not repeat within itself.

**Approximate periods.** A shift `P` is a near-period when `P f_i / 8000` is close to a whole number for both tones. The table gives, for each key, the shift `P ≤ 440` with the smallest worst-case phase error (in cycles, the larger of the two distances to a whole number), and the largest height difference `|c_{j+P+1} − c_{j+1}|` over the first 440 columns at `h = 256`:

| key | best `P ≤ 440` | phase error (cycles) | max height mismatch | key | best `P ≤ 440` | phase error (cycles) | max height mismatch |
|---|---|---|---|---|---|---|---|
| 1 | 172 | 0.0145 | 9 | 7 | 291 | 0.0226 | 13 |
| 2 | 425 | 0.0281 | 21 | 8 | 413 | 0.0290 | 18 |
| 3 | 195 | 0.0106 | 5 | 9 | 103 | 0.0305 | 19 |
| A | 436 | 0.0135 | 7 | C | 338 | 0.0058 | 4 |
| 4 | 291 | 0.0226 | 13 | * | 119 | 0.0161 | 8 |
| 5 | 395 | 0.0350 | 22 | 0 | 425 | 0.0250 | 14 |
| 6 | 260 | 0.0250 | 11 | # | 119 | 0.0296 | 13 |
| B | 343 | 0.0149 | 12 | D | 289 | 0.0079 | 6 |

Key C comes closest to repeating inside a burst (shift 338, heights within 4 of 256); key 5 is furthest (best shift 395, heights off by up to 22).[^exec]

## Call-progress tones and the 2600 Hz tone

The Bell precise tone plan builds its call-progress tones from 350, 440, 480 and 620 Hz: dial tone 350 + 440 Hz, continuous; ringback 440 + 480 Hz, 2 s on and 4 s off; busy 480 + 620 Hz, 0.5 s on and off; reorder the same pair, 0.25 s on and off.[^ptp]

| signal | tones (Hz) | `w` | period | atoms `k_1, k_2` | atom classes `d` | nonzero bins | blocks (one period) | `c_w` | shortest burst, in periods |
|---|---|---|---|---|---|---|---|---|---|
| dial tone | 350 + 440 | 800 | 100 ms | 35, 44 | 5, 4 | 800 | 6763 | 250 | continuous |
| ringback | 440 + 480 | 200 | 25 ms | 11, 12 | 1, 4 | 200 | 2113 | 248 | 80 |
| busy / reorder | 480 + 620 | 400 | 50 ms | 24, 31 | 8, 1 | 400 | 4779 | 244 | 10 / 5 |
| trunk idle | 2600 | 40 | 5 ms | 13 | 1 | 40 | 2842 | 71 | - |

The 2600 Hz castle at `h = 9` is drawn on [[song-as-castle](pages/song-as-castle.md)].

## Which signals are exactly periodic

| family | exact period | shortest burst | whole periods per burst |
|---|---|---|---|
| MF (all 15 codes) | 80 samples, 10 ms | 27 ms (digits), 55 ms (KP) | at least 2.7 (KP 5.5) |
| call progress | 200 to 800 samples, 25 to 100 ms | 250 ms (reorder) | at least 5 |
| 2600 Hz | 40 samples, 5 ms | - | - |
| DTMF keys 5 and 8 | 4000 and 2000 samples | 45 ms | 0.09 and 0.18 |
| other DTMF keys | 8000 samples, 1 s | 45 ms | 0.045 |

As sent, the MF signals, the call-progress tones and the 2600 Hz tone are castles repeated several times over; DTMF keys are fragments of a much longer castle. These periods are for the nominal frequencies. Equipment holds the precise-tone-plan frequencies to ±0.5%,[^ptp] and DTMF receivers must accept tones up to ±1.5% off nominal;[^ti-n] a frequency that is not a whole number of hertz has a different exact period (a rational `f = p/q` Hz gives `8000q / gcd(8000q, p)`), or none at all.

## Spectrum: sparse only approximately

Before quantization each castle's mean-removed energy sits entirely in its atoms. After quantization the atoms carry between 99.997% and 99.999% of it, for every signal in the catalogue. That matches the rounding error: rounding adds about `1/12` of power per column, against `2 · 63.75² / 2 = 4064` for two tones of amplitude `255/4`, a fraction `2.05 · 10⁻⁵`.[^exec]

The exact support is a different matter. Heights are whole numbers, so by [[spectral-analysis](pages/spectral-analysis.md)] §3 the support is bin 0 plus a union of the classes `D_d = {k : gcd(k, w) = d}`, and it contains the full class of every atom. MF KP's atoms 11 and 17 are coprime to 80, so all 32 bins of `D_1` are nonzero; DTMF key 1's atoms are coprime to 8000, so all 3200 bins of `D_1` are. In practice the rounding error fills every class:

- **30 of the 35 castles have all `w` bins nonzero.**
- Five lose whole classes: DTMF A (`D_2`, `D_4`: 5600 of 8000 bins), DTMF 7 (`D_1600`, the four bins `1600, 3200, 4800, 6400`: 7996 bins), DTMF * (`D_2`, `D_10`: 6080 bins), MF 11/ST3 (`D_2`, `D_4`: 56 of 80 bins) and MF KP2 (`D_2`: 64 bins).

The zero classes were confirmed in exact integer arithmetic: `ĉ_k = 0` for `k ∈ D_d` exactly when the cyclotomic polynomial `Φ_{w/d}(x)` divides `Σ c_{j+1} x^j`. The floating-point supports agree class by class, and no class is part zero and part nonzero.[^exec] So no tone castle is a sparse-spectrum castle in the exact sense of [[castle-classification-spectrum](pages/castle-classification-spectrum.md)]; each is approximately sparse, which is the regime [[spectral-analysis](pages/spectral-analysis.md)] §3 assigns to compressed sensing.

## Block parity of a tone burst

The block count is `blocks(c) = c_1 + Σ max(0, c_{i+1} − c_i)` ([[castle-sign](pages/castle-sign.md)]). Let `rise(c)` be the **cyclic rise**, the same sum taken around the cycle, including the step from `c_w` back to `c_1`. A burst of `r` whole periods is the skyline `c` written `r` times, and since `c_1 = h` is the tallest column,

```
blocks(c repeated r times)  =  c_w  +  r · rise(c)
```

(checked for `r = 1, 2, 3, 5`). For every castle in the catalogue `rise(c)` is **odd**:

- The skyline is symmetric, `c_{j+1} = c_{w−j+1}`, so the walk from column 1 to column `w/2 + 1` and the walk back are mirror images, and the rises on the way back are the falls on the way out. Hence `rise(c) = 2 · (falls on the way out) + c_{w/2+1} − c_1 ≡ c_{w/2+1} (mod 2)`, as `c_1 = 256` is even.
- Every period in the catalogue is even. At `j = w/2` each tone is at `cos(π k_i) = ±1`. Both atoms even would make `w/2` a period, contradicting minimality, so at least one is odd: `x_{w/2} = −2` (both odd), `0` (one odd) or `−1` (a single odd tone), and the quantizer gives `c_{w/2+1} = 1, 129, 1`. Each is odd.

So the Project Euler 502 parity of a tone burst alternates with the number of whole periods: a burst of `r` periods has an even number of blocks exactly when `r ≡ c_w (mod 2)`. The MF table lists which. The odd cyclic rise depends on the quantizer: rounding the midpoint `127.5` down instead of up gives `c_{w/2+1} = 128` for the 13 pairs with exactly one odd atom, and their cyclic rise becomes even; the 21 pairs with two odd atoms keep it odd.[^exec]

## Goertzel: one DFT bin, or a point between bins

The Goertzel algorithm computes one DFT term with a two-term recursion and a single real coefficient:[^goertzel]

```
s_n  =  c_{n+1} + 2 cos(2π f / 8000) · s_{n−1} − s_{n−2},       s_{−1} = s_{−2} = 0,   n = 0 … N−1
power(f)  =  s_{N−1}² + s_{N−2}² − 2 cos(2π f / 8000) · s_{N−1} s_{N−2}
```

Run over a whole period (`N = w`) at a tone's own frequency, `power(f_i) = |ĉ_{k_i}|²` exactly: one Goertzel filter is one bin of the skyline DFT, a linear functional of the castle followed by a squared magnitude (checked on MF KP at bins 7, 11 and 17).

**MF at `N = 80`.** The six MF frequencies sit on bins 7, 9, 11, 13, 15 and 17 of an 80-sample block, and the castle repeats exactly in that block. Before quantization the response at the four frequencies not in the signal is exactly zero (the DFT bins are orthogonal); computed in floating point it is 291 dB below the signal's own. On the quantized castle the worst case over all 15 codes is 49.6 dB down.

**DTMF at `N = 136`.** A published DTMF detector uses blocks of `N = 136` samples (main lobe about 58 Hz), set by the Bellcore recognition bandwidth, and places two bins 9 Hz either side of each column frequency.[^ti-n] At `N = 136` the eight DTMF frequencies fall between bins: `k = f · 136 / 8000 = 11.85, 13.09, 14.48, 16.00, 20.55, 22.71, 25.11, 27.76`. The Goertzel recursion still runs at a fractional `k`; it then samples the transform of the block between two DFT bins. The table gives, for each key at its nominal frequencies (one bin per frequency, not the dual bins), the detector's margin in each group: the power at the key's own frequency over the largest power at another frequency of the same group, in dB, over the first 136 columns.

| key | ideal tone: row, column | castle: row, column | key | ideal tone: row, column | castle: row, column |
|---|---|---|---|---|---|
| 1 | 15.4, 21.3 | 13.9, 19.4 | 7 | 12.4, 19.3 | 12.3, 18.3 |
| 2 | 16.1, 16.8 | 14.5, 16.5 | 8 | 13.1, 16.0 | 12.9, 15.8 |
| 3 | 15.0, 18.6 | 13.7, 16.6 | 9 | 13.3, 18.1 | 13.3, 16.9 |
| A | 15.7, 21.1 | 14.3, 20.7 | C | 13.4, 23.0 | 13.2, 22.2 |
| 4 | 12.9, 20.9 | 10.3, 18.4 | * | 13.8, 21.2 | 17.7, 18.4 |
| 5 | 12.9, 17.7 | 10.3, 17.4 | 0 | 13.0, 17.3 | 16.4, 16.9 |
| 6 | 13.7, 17.7 | 10.8, 15.9 | # | 13.2, 17.7 | 16.9, 15.9 |
| B | 12.9, 19.8 | 10.2, 18.6 | D | 13.3, 20.1 | 16.8, 17.4 |

Every key is detected correctly in both versions. The castle's margins differ from the ideal tone's by between about −2.9 and +3.9 dB, and the difference is not rounding: subtracting the castle's mean before the recursion restores every ideal margin to within 0.1 dB.[^exec] The castle's heights run from 1 to 256, so it carries a constant of about 128 (its area, bin 0). A constant is orthogonal to every whole-number bin of the block, but not to a fractional one, and it leaks most into the bin furthest from a whole number, 852 Hz at `k = 14.48`. Rows 770 Hz (keys 4, 5, 6, B), whose strongest competitor is 852 Hz, lose the most. At `N = 80` the MF bins are whole numbers and the area leaks nowhere.

## Open problems

- **Zero classes.** Five castles lose whole divisor classes (DTMF A, 7, *, MF 11/ST3, KP2) and the other thirty lose none. Which symmetry of the sampled pair and the rounding rule forces each zero class?
- **Other quantizers.** The odd cyclic rise uses the linear quantizer with halves rounded up. Under the telephone network's 8-bit logarithmic encoding (mu-law, [[castle-phone-line](pages/castle-phone-line.md)]) the castle is still symmetric, so the parity of `rise(c)` is still the parity of the middle column; which signals keep an odd cyclic rise?
- **Off-nominal tones.** Over the ±1.5% DTMF acceptance band, how does the best near-period inside a 45 ms burst vary with the frequency offset, and does any offset make a DTMF key exactly periodic within a burst?

## Related Concepts

- [[song-as-castle](pages/song-as-castle.md)] - the 2600 Hz and KP examples this page extends, and the waveform-as-castle map at `h = 65536`.
- [[spectral-analysis](pages/spectral-analysis.md)] - §3: the skyline DFT, the divisor-class theorem on supports, and the cyclic difference whose eigenbasis the Goertzel bins are.
- [[castle-classification-spectrum](pages/castle-classification-spectrum.md)] - the sparse-spectrum predicate; tone castles are approximately sparse, not members.
- [[castle-phone-line](pages/castle-phone-line.md)] - the same voice-band channel, sampled 8000 times per second, carrying castles as pitch-stepping tones, and its 8-bit logarithmic encoding.
- [[castle-representations](pages/castle-representations.md)] - the skyline (integer tuple) encoding used for every castle here.
- [[castle-sign](pages/castle-sign.md)] - the block count as first column plus total rise, behind the burst-parity formula.
- [[castle-compression](pages/castle-compression.md)] - a periodic castle is described by one period and a repeat count, the parametric tier.
- [[finite-fields](pages/finite-fields.md)] - cyclotomic polynomials and roots of unity, used for the exact zero-class check.

## Appearances in Sources

- [[project-euler-502-representations](pages/project-euler-502-representations.md)] - the integer-tuple encoding and the block count from the differences of the column heights, the two facts the block-parity section uses.

## Footnotes

[^exec]: Verified by execution (2026-10-01): Python 3 with NumPy and python-flint under `uv`. Castles built with the quantizer above (`floor(v + 1/2 + 10⁻⁹)`, so exact zero crossings `x_j = 0` round up to 129). Periods from `gcd`; every castle checked to have minimum height at least 1 and maximum 256. Supports from the FFT of one period, grouped by divisor class: no class is mixed, and the zero classes were confirmed exactly by divisibility of the integer polynomial `Σ c_{j+1} x^j` by `Φ_{w/d}` (python-flint `fmpz_poly`). Atom energy is `Σ_atoms |ĉ_k|² / Σ_{k≠0} |ĉ_k|²`. The identity `blocks(c repeated r times) = c_w + r · rise(c)` was checked on MF KP, DTMF 5 and busy for `r = 1, 2, 3, 5`. Replacing each frequency `f` by `8000 − f` gives the identical castle (checked on 2600 Hz, MF KP and DTMF 1). With halves rounded down instead, the middle column and the parity of `rise(c)` were recomputed for all 34 two-tone castles. Near-periods: exhaustive over `P = 1 … 440`. Goertzel: the recursion above in float64; the full-period Goertzel power matches `|ĉ_k|²` to 10 significant figures on MF KP. DTMF margins over the first 136 columns at the eight nominal frequencies, for the unquantized two-cosine signal, the castle, and the castle minus its block mean; MF margins over 80 columns at the six MF frequencies.
[^mf]: https://en.wikipedia.org/wiki/Template:Multi-frequency_signaling_tones [synthesis] - the table "Multifrequency signals" marks two of the columns 700, 900, 1100, 1300, 1500, 1700 Hz for each code: 1 = 700+900, 2 = 700+1100, 3 = 900+1100, 4 = 700+1300, 5 = 900+1300, 6 = 1100+1300, 7 = 700+1500, 8 = 900+1500, 9 = 1100+1500, 0/10 = 1300+1500, 11/ST3 = 700+1700, 12/ST2 = 900+1700, KP = 1100+1700, KP2 = 1300+1700, ST = 1500+1700.
[^mf-timing]: https://en.wikipedia.org/wiki/Multi-frequency_signaling §"Multi-frequency signals" - "The minimum timings of signals were initially at least 27 milliseconds per digit with 20 millisecond spacing. KP required at least 55 milliseconds as a precaution against activation of the sender by transients mimicking the KP signal."
[^dtmf]: https://en.wikipedia.org/wiki/DTMF_signaling §"Keypad" - "each row represents the low-frequency component and each column represents the high-frequency component of the DTMF signal ... Pressing a key sends a combination of the row and column frequencies"; https://www.ti.com/lit/an/spra096a/spra096a.pdf p.2 Figure 1 [synthesis] - rows 697, 770, 852, 941 Hz carry keys `1 2 3 A`, `4 5 6 B`, `7 8 9 C`, `* 0 # D`; columns 1209, 1336, 1477, 1633 Hz.
[^att]: https://www.ti.com/lit/an/spra096a/spra096a.pdf p.3 - "Tone duration specifications by AT&T state the following: 10 digits/sec are the maximum data rate for touch tone signals. For a 100 msec time slot the duration for the actual tone is at least 45 msec and not longer than 55 msec."
[^ti-n]: https://www.ti.com/lit/an/spra096a/spra096a.pdf p.7 - "the Bellcore recognition bandwidth requirements necessitate the setting for N=136, which corresponds to a mainlobe width of ~58Hz ... Guaranteed recognition of tones deviating +/−1.5% from center frequency"; p.6 - "Each column frequency has two frequency bins attached, which deviate +/−9Hz from center".
[^ptp]: https://en.wikipedia.org/wiki/Precise_tone_plan (lead) - "All signals in the specification use combination (by addition) of audible tones of four frequencies: 350 Hz, 440 Hz, 480 Hz, and 620 Hz. Equipment is required to maintain tolerances within ± 0.5% in frequency"; "Dial tone is a continuous tone of the addition of the frequencies 350 and 440 Hz"; ringing tone "440 and 480 Hz ... a cadence of 2 seconds ON and 4 seconds OFF"; busy tone "480 and 620 Hz ... a cadence of one half second ON and one half second OFF"; reorder tone "the same tone, but with a cadence of 0.25 of a second ON and 0.25 of a second OFF".
[^g711]: https://en.wikipedia.org/wiki/G.711 (lead) and §"Features" - "G.711 passes audio signals in the frequency band of 300–3400 Hz and samples them at the rate of 8000 Hz"; "64 kbit/s bit rate (8 kHz sampling frequency × 8 bits per sample)".
[^goertzel]: https://en.wikipedia.org/wiki/Goertzel_algorithm (lead) and §"Power-spectrum terms" [synthesis] - the algorithm evaluates individual DFT terms with "a single real-valued coefficient at each iteration" and is "useful in ... recognition of dual-tone multi-frequency signaling (DTMF) tones"; the power is "sprev^2 + sprev2^2 - (coeff × sprev × sprev2)" with `coeff = 2 cos(2πk/N)`.
