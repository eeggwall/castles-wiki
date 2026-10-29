---
title: What survives a phone line - castles sent as frequency-stepping tones
category: Analyses
summary: The 512 row castles of the cameraman image, each sent as a tone whose frequency steps with the column heights (frequency-shift keying with 256 frequencies), through a simulated telephone line (300-3400 Hz band-pass, 8-bit mu-law encoding, Gaussian hiss) and read back from the phase step of the analytic signal. Over 125 to 1000 columns per second and three hiss levels, the block parity of a row is right in 41% to 58% of rows at every setting except 125 columns per second with hiss at most 30 dB, where 99.9% of heights arrive exact and the parity is right in 87.5% to 89.1% of rows; the lowest bit of each height fails at the off-by-one rate; the 16-bin height histogram and the 8 lowest Fourier modes of each row change by at most 4.8% and 1.6%. Since the line's errors are almost all off by one, hiding each bit as a height of residue 0 or 3 modulo 6 absorbs them: bit error rate 0.0007 at 250 columns per second and 30 dB, against 0.042 for the lowest bit, and the 56-character test message comes back exact in 20 of 20 trials from one 2-second row.
tags: [analysis, castle, steganography, audio, telephone, modem, frequency-shift-keying, error-profile, image, implementation]
sources: [project-euler-502-representations]
created: 2026-09-24
updated: 2026-10-16
---

# What survives a phone line - castles sent as frequency-stepping tones

## The experiment

[[castle-steganography](pages/castle-steganography.md)] hides a 56-character message in the 512 row castles of the cameraman image ([[image-as-castle](pages/image-as-castle.md)]) in two ways and tests them against PNG and JPEG. This page tests the castles and the hiding schemes against a telephone line: each row castle is turned into a tone, the tone is passed through a simulated line, and the received tone is turned back into a castle.

Each column's height selects a frequency, the tone holds that frequency for a fixed number of samples, and then steps to the next column's frequency, with no jump in the waveform. A row castle of width 512 becomes 512 tone segments. This is frequency-shift keying with 256 frequencies, one per height. The receiver measures frequency only.

## The line

A digital telephone line passes the band from about 300 Hz to 3400 Hz and takes 8000 samples per second, each stored as 8 bits on a logarithmic (mu-law) scale, for 64 kbit/s; this is the G.711 standard.[^g711] A signal sampled 8000 times per second represents frequencies only up to 4000 Hz: a tone at `f` above 4000 Hz gives the same samples as a tone at `8000 − f`, since `cos(2π(8000 − f)j/8000 + φ) = cos(2πfj/8000 − φ)` at every sample `j`. The tones here lie between 600 and 3000 Hz, inside the band.

The hiss level is the ratio of tone power to noise power in decibels: 30 dB means the noise has 1/1000 of the tone's power, 20 dB means 1/100. "None" means the encoding and the band-pass filter only.

```
sender:    frequency = 600 Hz + (height − 1) · 2400/255 Hz        heights 1..256 -> 600..3000 Hz
           tone = 0.5 cos(running sum of 2π·frequency/8000), each frequency held N samples
line:      8-bit mu-law encoding -> Gaussian hiss -> 300-3400 Hz band-pass, applied forward and backward
receiver:  frequency at each sample from the phase step of the analytic signal,
           averaged over the middle half of each column's N samples, rounded back to a height
```

With `N` samples per column, a row takes `512N/8000` seconds: `N = 32` is 250 columns per second and 2.05 seconds per row. Heights are `pixel + 1`, so each row is a castle at its own maximum `h`.[^exec]

## What comes out, statistic by statistic

Over every fourth row, 128 row castles:

| samples per column (columns per second) | hiss | heights exact | off by 1 | off by 2 or more | lowest bit wrong | block parity right | block count error | histogram drift | slow-trend error |
|---|---|---|---|---|---|---|---|---|---|
| 8 (1000) | none | 75.4% | 21.1% | 3.45% | 21.86% | 42.2% | 5.22% | 1.13% | 0.39% |
| 8 (1000) | 30 dB | 37.2% | 47.2% | 15.61% | 49.58% | 57.8% | 16.65% | 1.82% | 0.68% |
| 8 (1000) | 20 dB | 13.7% | 25.8% | 60.52% | 49.98% | 55.5% | 56.65% | 4.76% | 1.56% |
| 16 (500) | none | 96.7% | 2.9% | 0.39% | 3.07% | 52.3% | 0.63% | 0.26% | 0.18% |
| 16 (500) | 30 dB | 67.7% | 31.5% | 0.81% | 31.66% | 50.8% | 5.81% | 0.96% | 0.34% |
| 16 (500) | 20 dB | 26.4% | 42.3% | 31.28% | 50.00% | 48.4% | 23.71% | 2.40% | 0.86% |
| 32 (250) | none | 99.7% | 0.2% | 0.16% | 0.20% | 55.5% | 0.13% | 0.03% | 0.05% |
| 32 (250) | 30 dB | 95.8% | 4.0% | 0.16% | 4.08% | 52.3% | 0.83% | 0.20% | 0.12% |
| 32 (250) | 20 dB | 50.0% | 45.8% | 4.25% | 45.90% | 48.4% | 9.32% | 1.24% | 0.44% |
| 64 (125) | none | 99.9% | 0.1% | 0.00% | 0.06% | 89.1% | 0.01% | 0.00% | 0.00% |
| 64 (125) | 30 dB | 99.9% | 0.1% | 0.00% | 0.08% | 87.5% | 0.01% | 0.00% | 0.00% |
| 64 (125) | 20 dB | 82.5% | 17.5% | 0.00% | 17.53% | 41.4% | 3.14% | 0.57% | 0.22% |

The columns: **block parity right** is the share of rows whose received block count has the parity of the sent one, and **block count error** the mean of `|blocks(received) − blocks(sent)| / blocks(sent)` ([[castle-sign](pages/castle-sign.md)]). **Histogram drift** is the share of columns that would have to change bin to turn the received 16-bin height histogram into the sent one. **Slow-trend error** is the median, over rows and over `k = 1, …, 8`, of the relative error `|ĉ'_k − ĉ_k| / |ĉ_k|` of the skyline DFT coefficients ([[spectral-analysis](pages/spectral-analysis.md)]).

- **The block parity.** It is right in 41% to 58% of the 128 rows at every setting except 125 columns per second with hiss at most 30 dB, where it is right in 87.5% to 89.1% of rows although 99.9% of heights arrive exact; for 128 independent fair coins the standard deviation of the share is 4.4%. A change of one column's height by one changes the block count by −1, 0 or 1 ([[one-bit-seminar](pages/one-bit-seminar.md)], the section *Stop 3*), so the parity of a row depends on the errors at all its columns together. JPEG destroys it too ([[castle-steganography](pages/castle-steganography.md)]).
- **The histogram and the slow trends.** Both average over the row: at most 4.76% histogram drift and 1.56% slow-trend error at every setting.
- **The lowest bit of each height.** The line's errors are almost all off by one (at 250 columns per second and 30 dB, 4.0% of columns are off by one and 0.16% by two or more), and the lowest bit changes exactly when the error is odd, so the lowest-bit error rate is the off-by-one rate plus the share of odd errors of three or more.
- **Errors at height jumps.** At 1000 columns per second without hiss, 71% of the errors of two or more fall on columns next to a height jump of 16 or more, which are 20% of all columns: the band-pass filter spreads a frequency step into the neighboring column's samples. With 30 dB hiss the share is 31% at 500 columns per second and 5% at 250.

## A height code that absorbs off-by-one errors

The height-bit channel of [[castle-steganography](pages/castle-steganography.md)] puts each hidden bit in the lowest bit of a column height, which every off-by-one error changes. A code with spacing `s` (even) puts the two values of a bit in the residues 0 and `s/2` modulo `s`: to hide a 0, move the column to the nearest height divisible by `s`; to hide a 1, to the nearest height congruent to `s/2` modulo `s` (ties broken downward). The receiver reads the bit as the residue class nearer to the received height, and counts an equidistant height as an error.

- With `s = 6`, a 0 sent as height 12 and received as 11 or 13 is nearer to 12 than to 9 or 15, so an error of 1 is absorbed and an error of 2 changes the bit.
- With `s = 4`, an error of 1 lands halfway between the classes, so `s = 4` fails at the off-by-one rate, like the lowest bit.
- With `s = 10`, errors up to 2 are absorbed.

A move is at most `s/2`, and the columns used are those with height between `s/2 + 1` and `h − s/2`, so every move keeps the height between 1 and `h` and the row a castle at `h`. The payload's 336 bits go into the first 336 such columns, and the receiver is given these positions. The mean move is 1.5 cells for `s = 6` and 2.5 for `s = 10` (the mean distance from a uniform residue to the nearer class), and in row 100 (`h = 215`), 385 of the 512 columns are usable for `s = 6`.

Bit error rate, 336 bits per row over rows 100, 104, …, 352 (21,504 bits per entry):

| samples per column (columns per second) | hiss | lowest bit | `s = 4` | `s = 6` | `s = 10` | `s = 6`, cliff columns skipped |
|---|---|---|---|---|---|---|
| 16 (500) | none | 0.0308 | 0.0332 | 0.0027 | 0.0009 | 0.0015 |
| 16 (500) | 30 dB | 0.3181 | 0.3264 | 0.0069 | 0.0011 | 0.0040 |
| 32 (250) | 30 dB | 0.0420 | 0.0437 | 0.0007 | 0 | 0.0007 |
| 32 (250) | 20 dB | 0.4565 | 0.4976 | 0.0426 | 0.0008 | 0.0440 |
| 64 (125) | 20 dB | 0.1709 | 0.1772 | 0 | 0 | 0 |

At 250 columns per second with 30 dB hiss, spacing 6 has 1/60 of the error rate of the lowest bit. Skipping the columns next to a height jump of 16 or more lowers the spacing-6 error rate at 500 columns per second and leaves it unchanged at 250.

**End to end.** The 56-character message (336 bits) was hidden in row 100 with `s = 6` (with three copies, in rows 100, 101 and 102, decoded by majority vote), sent down the line and decoded, 20 times with fresh hiss each time:

| samples per column | hiss | copies of each bit | audio | message exact |
|---|---|---|---|---|
| 32 | none | 1 | 2.05 s | 20 / 20 |
| 32 | 30 dB | 1 | 2.05 s | 20 / 20 |
| 32 | 30 dB | 3 | 6.14 s | 20 / 20 |
| 16 | 30 dB | 1 | 1.02 s | 5 / 20 |
| 16 | 30 dB | 3 | 3.07 s | 19 / 20 |

At 250 columns per second with 30 dB hiss one row castle, 2.05 seconds of audio, carries the whole message, with 535 cells moved in row 100. At 500 columns per second one copy fails in most trials and three copies recover the message in 19 of 20.

## Side by side

| statistic | information carried | survives the line |
|---|---|---|
| each column's height, exactly | `log₂ h` bits per column | at 125 columns per second with hiss at most 30 dB |
| lowest bit of each height | 1 bit per column | no: every off-by-one error changes it |
| height residue 0 or 3 modulo 6 | 1 bit per column | yes at 250 columns per second, 30 dB hiss |
| block parity | 1 bit per castle | only at 125 columns per second with hiss at most 30 dB, in 87.5% to 89.1% of rows |
| 16-bin height histogram | 16 numbers per castle | yes, at every setting |
| 8 lowest Fourier modes | 8 numbers per castle | yes, at every setting |

## Related Concepts

- [[castle-steganography](pages/castle-steganography.md)] - the two hiding channels and the message this page sends down the line.
- [[image-as-castle](pages/image-as-castle.md)] - the cover image as 512 row castles.
- [[song-as-castle](pages/song-as-castle.md)] - the other direction: a sound recording read as a castle.
- [[castle-sign](pages/castle-sign.md)] - the block count, total ascent of the skyline.
- [[castle-entropy](pages/castle-entropy.md)] - the even-block condition costs one bit up to `log₂(1 + S/A)`; that bit is the block parity, which this line does not carry.
- [[spectral-analysis](pages/spectral-analysis.md)] - the skyline DFT, whose lowest modes survive the line.
- [[one-bit-seminar](pages/one-bit-seminar.md)] - Stop 3, the change of the block count under a one-cell edit, and Stop 4, the parity as a fragile statistic.
- [[tone-castle-catalog](pages/tone-castle-catalog.md)] - the telephone network's own signaling tones (DTMF, MF, call progress), sampled 8000 times per second, as periodic castles.

## Appearances in Sources

- [[project-euler-502-representations](pages/project-euler-502-representations.md)] - the block count read from the differences of consecutive column heights.

## Footnotes

[^exec]: Verified by execution (Python 3.14 with NumPy 2.4 and SciPy 1.17, 2026-10-16), on the cameraman image of scikit-image's data files (`camera.png`, which `skimage.data.camera()` returns). Tone at 8000 samples per second and amplitude 0.5; mu-law at `mu = 255`, the companded value quantized uniformly to 8 bits; Gaussian hiss of variance `0.125 / 10^(SNR/10)` added after the encoding; band-pass `scipy.signal.butter(4, [300, 3400], btype='bandpass', fs=8000)` (order 8) applied by `sosfiltfilt`; frequency from the phase step of `scipy.signal.hilbert`. Seeds: `numpy.random.default_rng(1000N + i)` for the statistics table (`i = 0, 1, 2` for no hiss, 30 dB, 20 dB), `100j + s` for the bit-error table (`j = 1, …, 5` by row, with `s = 1` for the lowest bit and `s = 7` for the cliff-skipping column), `7000 + 10N + copies + SNR` for the end-to-end table. Statistics over rows 0, 4, …, 508; hiding schemes over rows 100, 104, …, 352.
[^g711]: https://en.wikipedia.org/wiki/G.711 (lead) and §"Features" - "G.711 passes audio signals in the frequency band of 300–3400 Hz and samples them at the rate of 8000 Hz"; "64 kbit/s bit rate (8 kHz sampling frequency × 8 bits per sample)".
