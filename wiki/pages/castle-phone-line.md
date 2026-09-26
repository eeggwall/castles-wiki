---
title: What survives a phone line - castles sent as pitch-stepping tones
category: Analyses
summary: The cameraman image's 512 row castles, each played as a tone whose pitch steps up and down with the column heights (like a dial-up modem, not FM radio), sent through a simulated telephone line (300-3400 Hz voice band, the phone system's 8-bit loudness encoding, background hiss), and read back by measuring the pitch in each column's time slot. Swept over 125 to 1000 columns per second and three hiss levels, then measured which castle statistics come out intact. Robustness runs opposite to capacity - the odd/even block count, the castle's own one-bit statistic, sits at a coin flip until the line is almost perfect (0.83 correct even when 99.9% of heights arrive exact), the lowest bit of each height is next most fragile, and the height histogram and the slow trends of the skyline survive every setting (at most 4.7% histogram drift and 1.4% slow-trend error at the worst setting, 0.2% and 0.1% at 250 columns per second with 30 dB hiss). Line errors are almost all off-by-one, so hiding each bit in heights 0 or 3 modulo 6 instead of in the lowest bit absorbs them - bit error rate 0.0016 at 250 columns per second with hiss 1000x weaker than the tone, and the 56-character test message came back exact in 20 of 20 trials from a single 2-second row.
tags: [analysis, castle, steganography, audio, telephone, modem, frequency-shift-keying, error-profile, image, implementation, seminar]
sources: [project-euler-502-representations]
created: 2026-09-24
updated: 2026-09-26
---

# What survives a phone line - castles sent as pitch-stepping tones

## What the experiment is

[[castle-steganography](pages/castle-steganography.md)] hid a 56-character message inside the 512 row castles of the cameraman image ([[image-as-castle](pages/image-as-castle.md)]) in two ways, and checked what survives PNG and JPEG. This page asks the same question for a telephone call: **turn each castle into sound, send the sound down a phone line, turn it back into a castle, and see which parts of the hidden message are still there.**

The sound is a single tone whose **pitch** carries the castle. Each column's height picks a pitch, the tone holds that pitch for a short fixed time, then steps to the next column's pitch. A width-512 row castle becomes a 512-note staircase melody. The receiver ignores loudness entirely and only measures pitch.

This is how dial-up modems and fax machines talk. It has nothing to do with broadcast FM radio: there is no radio signal anywhere, and everything happens at audio pitches a person could hear. Engineers call this family frequency modulation (FM), and this particular kind, with a fixed set of pitches each held for a fixed time, frequency-shift keying. Old modems used 2 pitches; this uses 256, one per possible height.

Pitch rather than loudness because a phone line damages loudness (it compresses and filters it) but leaves pitch mostly alone, as long as the pitch stays inside the band the line carries.

## Terms used on this page

- **Voice band** - telephone lines carry only pitches from about 300 Hz to 3400 Hz. Anything outside is cut off. All tones here sit inside it.
- **The phone system's loudness encoding** - digital phone lines store each sound sample as 8 bits on a logarithmic loudness scale (standard name: mu-law, from the ITU telephone standard G.711). Quiet sounds keep detail and loud sounds are coarse. It adds a small rounding distortion to every sample.
- **Hiss level, in decibels (dB)** - how much weaker the background noise is than the tone. 30 dB means the hiss carries 1000 times less power than the tone; 20 dB means 100 times less. "No hiss" below means only the loudness encoding and the band cutoff, with no added noise.
- **Samples per column** - the phone line carries 8000 sound samples per second. Holding each column's pitch for 32 samples means 4 ms per column, 250 columns per second, and 2 seconds for one row castle. Fewer samples per column is faster and harder to read.
- **Height error** - received height minus sent height, per column.
- **Bit error rate** - the fraction of hidden bits that come out wrong.

## The setup

```
sender:    pitch = 600 Hz + (height - 1) * 9.41 Hz        heights 1..256 -> 600..3000 Hz
           tone  = cos(running sum of pitch), each pitch held N samples, no jumps in the wave
line:      8-bit phone loudness encoding -> optional hiss -> cut everything outside 300-3400 Hz
receiver:  measure how fast the wave's phase turns at each sample (that is the pitch),
           average over the middle half of each column's time slot, round back to a height
```

The line's band cutoff was applied with a filter that does not delay the signal. A real line does delay it; see the open questions below. Heights are `pixel + 1`, so every row is a castle at `h = 256` or its own lower maximum.[^exec]

## What comes out, statistic by statistic

Measured on every fourth row (128 row castles):

| samples per column (columns per second) | hiss | heights exact | height off by 1 | off by 2 or more | lowest bit wrong | odd/even block count correct | block count error | histogram drift | slow-trend error |
|---|---|---|---|---|---|---|---|---|---|
| 8 (1000) | none | 75.5% | 21.0% | 3.54% | 21.9% | 50.8% | 3.7% | 1.1% | 0.5% |
| 8 (1000) | 30 dB | 36.8% | 47.2% | 15.9% | 49.7% | 57.8% | 15.0% | 1.9% | 0.7% |
| 8 (1000) | 20 dB | 13.8% | 25.7% | 60.5% | 50.0% | 46.9% | 55.3% | 4.7% | 1.4% |
| 16 (500) | none | 97.8% | 1.9% | 0.40% | 2.0% | 50.8% | 0.7% | 0.2% | 0.1% |
| 16 (500) | 30 dB | 67.8% | 31.5% | 0.75% | 31.6% | 48.4% | 6.2% | 0.9% | 0.3% |
| 16 (500) | 20 dB | 26.0% | 42.3% | 31.7% | 50.0% | 50.0% | 24.3% | 2.4% | 0.8% |
| 32 (250) | none | 99.6% | 0.2% | 0.18% | 0.2% | 54.7% | 0.1% | 0.03% | 0.06% |
| 32 (250) | 30 dB | 95.3% | 4.6% | 0.18% | 4.6% | 49.2% | 0.9% | 0.2% | 0.1% |
| 32 (250) | 20 dB | 49.8% | 45.7% | 4.47% | 45.9% | 48.4% | 9.5% | 1.3% | 0.4% |
| 64 (125) | none | 99.9% | 0.1% | 0% | 0.07% | 85.9% | 0.01% | 0% | 0% |
| 64 (125) | 30 dB | 99.9% | 0.1% | 0% | 0.08% | 82.8% | 0.01% | 0% | 0% |
| 64 (125) | 20 dB | 82.2% | 17.8% | 0% | 17.8% | 57.8% | 3.3% | 0.6% | 0.2% |

Column meanings: **block count error** is the average relative change in the castle's block count ([[castle-sign](pages/castle-sign.md)]). **Histogram drift** is the share of columns that would have to move to a different bin to turn the received 16-bin height histogram back into the sent one. **Slow-trend error** is the median relative error in the 8 smoothest up-and-down waves that fit across the row (the lowest Fourier modes of [[spectral-analysis](pages/spectral-analysis.md)]).

Four readings:

- **The odd/even block count is the most fragile statistic.** It sits at a coin flip (about 50%) until the line is nearly perfect, and even when 99.9% of heights arrive exact it is right only 83-86% of the time. The block count is `c_1 + sum of every upward step`, so its odd/even value depends on every column's error at once; a single stray off-by-one anywhere in the row can flip it. This is the one-bit statistic [[castle-entropy](pages/castle-entropy.md)] prices the even-block rule at, and the one the block-parity scheme of [[castle-steganography](pages/castle-steganography.md)] writes its message into. It dies on a phone line the same way it died under JPEG.
- **The histogram and the slow trends survive everything.** Both average over the whole row, so single-column errors wash out: under 5% histogram drift and under 1.5% slow-trend error even at 1000 columns per second with the loudest hiss. They carry very little information, but what they carry arrives.
- **The lowest bit of each height is in between**, and its failure has a single shape: the line's errors are almost all off-by-one. At 250 columns per second and 30 dB hiss, 4.6% of columns are off by one and only 0.18% by two or more. An off-by-one error flips the lowest bit every time, so the lowest-bit error rate tracks the off-by-one rate.
- **At the fastest rate, the big errors sit at cliffs.** At 1000 columns per second with no hiss, 69% of the errors of two or more fall on columns next to a height jump of 16 or more, though such columns are only 20% of all columns: the band cutoff smears a sudden pitch jump across the neighbouring column's time slot. The effect fades as columns get longer (17% at 500 columns per second, 8% at 250, both with 30 dB hiss).

## Redesigning the height-bit scheme for this line

The height-bit scheme of [[castle-steganography](pages/castle-steganography.md)] puts one hidden bit in the lowest bit of each column height. On this line that is the wrong bit to use, because the line's typical error (off by one) always flips it.

The fix is to space the two meanings of a bit far enough apart that an off-by-one error cannot turn one into the other. **To hide a 0, move the column to the nearest height that is a multiple of 6; to hide a 1, move it to the nearest height that is 3 more than a multiple of 6.** The receiver reads the height, finds which of the two families it is closer to, and reads off the bit. A 0 sent as height 12 and received as 11 or 13 is still closest to 12, so an off-by-one error does no harm; only an error of 2 or more can flip the bit. A spacing of 4 would not work: with spacing 4 an off-by-one error lands exactly halfway between the two families, where the receiver cannot tell them apart (measured bit error rate 2.4% at 250 columns per second and 30 dB hiss). A spacing of 10 absorbs errors up to 2. (The standard name for this family of schemes is quantization index modulation.)

The skip rule that keeps each row a castle changes with it: use only columns with height from 5 to `h - 5` and at least 3 below the row's peak, so no move reaches the floor, the ceiling, or creates a second peak. That leaves 509 of 512 columns usable per row. Each hidden bit moves its column by 1.5 cells on average with spacing 6, and 2.5 with spacing 10.

Bit error rate, 336 bits per row over 64 rows:

| samples per column (columns per second) | hiss | spacing 6 | spacing 10 |
|---|---|---|---|
| 16 (500) | none | 0.0019 | 0.0001 |
| 16 (500) | 30 dB | 0.0050 | 0.0004 |
| 32 (250) | 30 dB | 0.0016 | 0.0002 |
| 32 (250) | 20 dB | 0.043 | 0.0017 |
| 64 (125) | 20 dB | 0.0001 | 0.0000 |

For comparison, the plain lowest-bit scheme at 250 columns per second and 30 dB hiss has an error rate of 0.046, about 30 times worse than spacing 6. Skipping the columns next to cliffs made no difference once the spacing was in place.

**End to end.** The 56-character message (336 bits, `castles are skylines, skylines are numbers` in base64) was hidden in row 100 with spacing 6, sent down the line, and decoded, 20 times with fresh hiss each time:

| samples per column | hiss | copies of each bit | rows used | audio | message exact |
|---|---|---|---|---|---|
| 32 | none | 1 | 1 | 2.0 s | 20 / 20 |
| 32 | 30 dB | 1 | 1 | 2.0 s | 20 / 20 |
| 32 | 30 dB | 3, majority vote | 3 | 6.1 s | 20 / 20 |
| 16 | 30 dB | 1 | 1 | 1.0 s | 2 / 20 |
| 16 | 30 dB | 3, majority vote | 3 | 3.1 s | 15 / 20 |

At 250 columns per second with 30 dB hiss, one row castle is 2 seconds of audio and carries the whole message, 484 cells moved out of 512 columns. Going twice as fast breaks it; sending three copies of each bit recovers most of it.

## Side by side

| statistic | information carried | survives the phone line |
|---|---|---|
| each column's height, exactly | most | only on a slow, quiet line |
| lowest bit of each height | 1 bit per column | no - every off-by-one error flips it |
| height modulo 6 (0 or 3) | 1 bit per column | yes at 250 columns per second, 30 dB hiss |
| odd/even block count | 1 bit per castle | no, even at 99.9% exact heights |
| 16-bin height histogram | a few numbers per castle | yes, everywhere tested |
| 8 slowest up-and-down waves | a few numbers per castle | yes, everywhere tested |

The statistics that carry the most information are not the ones that survive best, and the castle's own statistic, the odd/even block count, survives worst of all.

## Open questions

- **A real line's delay.** The band cutoff here was applied without delaying the signal. A real line delays it by a few samples, which shifts where each column's time slot starts; does the receiver need to find the column boundaries itself?
- **An eavesdropper who listens.** [[castle-steganography](pages/castle-steganography.md)] asks whether a warden counting blocks can detect the hidden message. Here the warden hears the tone: does moving columns to multiples of 3 leave an audible or measurable trace in the tone's pitch statistics?
- **The speed limit.** At fixed hiss, what is the largest number of columns per second at which some spacing plus copies still delivers the message exactly, and how close is that to the phone line's theoretical capacity?

## Related Concepts

- [[castle-steganography](pages/castle-steganography.md)] - the two hiding schemes and the message this page sends down the line.
- [[image-as-castle](pages/image-as-castle.md)] - the cover image as 512 row castles.
- [[song-as-castle](pages/song-as-castle.md)] - the other direction: a sound recording read as a castle.
- [[castle-sign](pages/castle-sign.md)] - the block count formula behind the odd/even fragility.
- [[castle-entropy](pages/castle-entropy.md)] - the even-block rule is worth one bit; this page shows that bit does not survive a phone line.
- [[castle-compression](pages/castle-compression.md)] - lossless and lossy recoding, the other damage models the hiding schemes were tested against.
- [[spectral-analysis](pages/spectral-analysis.md)] - the skyline's Fourier modes, whose slowest members survive the line.
- [[one-bit-seminar](pages/one-bit-seminar.md)] - Stop 4 of the one-bit seminar: why the parity is the first statistic to go.


## Appearances in Sources

- [[project-euler-502-representations](pages/project-euler-502-representations.md)] - the block count as the first column plus the sum of upward steps, which makes the odd/even value depend on every column.

## Footnotes

[^exec]: Verified by execution (2026-09-24): Python 3 with numpy, scipy and scikit-image under `uv`; the cover is `skimage.data.camera()`. Tone at 8000 samples per second and half full-scale amplitude; 8-bit mu-law encoding at mu = 255; Gaussian hiss scaled to the tone's power; 8th-order Butterworth band-pass 300-3400 Hz applied forward and backward (no delay); pitch read from the phase step of the Hilbert analytic signal. Statistics table over rows 0, 4, ..., 508; hiding-scheme table over rows 100, 104, ..., 352; end-to-end table over 20 hiss draws. All quoted numbers are the script's printed output.
