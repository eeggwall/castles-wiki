---
title: A song as a castle
category: Analyses
summary: How to encode a song as a castle, with every number computed. Rung 0, the URL - a YouTube video id is 11 base64url characters, a 66-bit integer, and a rank/unrank bijection (decomposing by the first column of height h) turns it into a castle of width 12 and height 64, width 17 and height 16, or width 67 and height 2; the condition that some column reaches h costs log2(h^w/A(w,h)) bits (0.586 at (17, 16), 2.538 at (12, 64)), and the even-block condition about one bit more, but block parity is a weak checksum (an edit of one column flips it with probability 0.427 at (17, 16)). Rung 1, the metadata - a 13-field JSON label is 233 bytes after zlib, a castle of width 234 at h = 256; a 128-bit fingerprint is width 17. Rung 2, the audio - a castle of height 65536 is a peak-normalized 16-bit PCM waveform, one sample per column; Never Gonna Give You Up (213 s) is a castle of width 9,393,300 per channel, and the codecs WAV, FLAC, MP3, AAC, Opus are castle-compression's tiers on a waveform. Finite fields - 16-bit samples are elements of F_65537; Berlekamp-Massey tests for exact linear recurrences, and the length-1024 NTT mod 65537 with root 3^64 is an exact skyline DFT. Telephone tones - the 2600 Hz tone at 8000 samples per second is a periodic castle of width 40 with a two-atom DFT, the MF KP tone a width-80 castle with four atoms. Finale - Beethoven's Ninth Symphony, about 65 minutes, from the opening open fifth (a two-tone castle) to the Ode to Joy phrase (a castle of width 15 and height 5) to the whole work as one castle of width about 344 million.
tags: [analysis, castle, encoding, compression, audio, pcm, lpc, flac, mp3, aac, opus, finite-field, ntt, berlekamp-massey, entropy, youtube, beethoven, cd, dtmf, seminar, pedagogy]
sources: [project-euler-502-representations, project-euler-502-solution]
created: 2026-09-19
updated: 2026-10-16
---

# A song as a castle

A castle with `h = 65536` is a peak-normalized 16-bit waveform, one sample per column. The page encodes a song at three sizes (the URL and the metadata are small castles, the audio a large one), compares how compactly the audio castle can be written, and reads its column heights as elements of a finite field. The finale applies the page to one work, Beethoven's Ninth Symphony.

The "hear the shape of a castle" direction ([[spectral-analysis](pages/spectral-analysis.md)]) starts from a castle and takes a spectrum, a lossy invariant ([[isospectral-castles](pages/isospectral-castles.md)]). Here the map goes from sound to a castle and is a **bijection** between peak-normalized 16-bit waveforms and castles of height 65536: the skyline is the waveform, and the skyline DFT of [[spectral-analysis](pages/spectral-analysis.md)] §3 is the audio spectrum.

The encodings used are the skyline (integer tuple) of [[castle-representations](pages/castle-representations.md)], the exact codebook size `A(w,h) = h^w - (h-1)^w` of [[castle-counting-function](pages/castle-counting-function.md)], and the tier ladder of [[castle-compression](pages/castle-compression.md)]. Every number on the page follows from those formulas plus one running example - Rick Astley's "Never Gonna Give You Up" for the rungs, Beethoven's Ninth for the finale.

---

## Rung 0 - the URL

A YouTube video URL is `https://www.youtube.com/watch?v=<id>` where `<id>` is 11 base64url characters (`A-Z`, `a-z`, `0-9`, `-`, `_`). Since `64^11 = 2^66`, the payload is **66 bits**. The canonical example on this page is `dQw4w9WgXcQ` - Rick Astley, "Never Gonna Give You Up", 3:33.[^rickroll] As a base-64 integer that id is `0x1d430e30f56817710` = 33,736,714,463,647,725,328. The table gives the castles that hold 66 bits.

The codebook is the set of all castles at `(w, h)`, of size `A(w,h) = h^w - (h-1)^w`; it holds `log2 A` bits. The rule "some column reaches `h`" costs

```
touch_cost(w,h) = log2( h^w / A(w,h) ) = -log2( 1 - ((h-1)/h)^w )   bits
```

relative to plain base-`h` digits, and it is the only thing separating a castle from a number written in base `h`:

| `h` | bits per column | smallest `w` with `A(w,h) >= 2^66` | `log2 A(w,h)` | touch cost | `log2 A(w-1,h)` |
|---|---|---|---|---|---|
| 2 | 1 | 67 | 67.000 | 0.000 | 66.000 (one short) |
| 16 | 4 | 17 | 67.414 | 0.586 | 63.365 (short) |
| 64 | 6 | 12 | 69.462 | 2.538 | 63.348 (short) |
| 256 | 8 | 9 | 67.147 | 4.853 | 58.980 (short) |

At `h = 64` the base matches the URL alphabet exactly, but the touch rule costs 2.5 bits, so a twelfth column carries the eleven base-64 characters plus a guaranteed peak. At `h = 16` the touch rule costs under a bit and the 17th hex-digit column is nearly free. At `h = 2` it is a plain 67-bit binary castle.

### The bijection: rank / unrank

Decompose by `j`, the position of the **first** column of height `h`: columns `1..j-1` lie in `{1..h-1}`, column `j` is `h`, columns `j+1..w` lie in `{1..h}`. The block for a given `j` has `(h-1)^(j-1) * h^(w-j)` castles, and summing over `j` telescopes to `h^w - (h-1)^w = A(w,h)` - the counting formula is the ranking scheme.

```python
def A(w, h): return h**w - (h-1)**w

def unrank(n, w, h):                      # integer in [0, A(w,h))  ->  skyline
    for j in range(1, w+1):
        cnt = (h-1)**(j-1) * h**(w-j)
        if n < cnt:
            left, right = divmod(n, h**(w-j))
            pre  = [];  post = []
            for _ in range(j-1): left,  r = divmod(left,  h-1); pre.append(r+1)
            for _ in range(w-j): right, r = divmod(right, h);   post.append(r+1)
            return tuple(pre[::-1]) + (h,) + tuple(post[::-1])
        n -= cnt

def rank(c, h):                           # skyline  ->  integer
    w = len(c); j = c.index(h) + 1
    n = sum((h-1)**(jj-1) * h**(w-jj) for jj in range(1, j))
    left = 0
    for x in c[:j-1]: left = left*(h-1) + (x-1)
    right = 0
    for x in c[j:]:   right = right*h + (x-1)
    return n + left * h**(w-j) + right
```

Applied to `dQw4w9WgXcQ` at `(17, 16)`:

```
skyline: (14, 16, 5, 4, 1, 15, 4, 1, 16, 6, 7, 9, 2, 8, 8, 2, 1)
blocks: 54    area: 119

.#......#........
.#...#..#........
##...#..#........
##...#..#........
##...#..#........
##...#..#........
##...#..#........
##...#..#..#.....
##...#..#..#.##..
##...#..#.##.##..
##...#..####.##..
###..#..####.##..
####.##.####.##..
####.##.####.##..
####.##.########.
#################
```

At `(12, 64)` the same id is the skyline `(64, 30, 17, 49, 57, 49, 62, 23, 33, 24, 29, 17)` - a full-height first column (the decomposition put the touch at `j = 1`), then eleven base-64 columns.

### The even-block codebook and a weak checksum

Project Euler 502 counts the even-block castles, `A^e(w, h)`. A dynamic program over (column, last height, whether `h` has been reached, block parity) counts completions and unranks into the even-block codebook. The parity costs `log2 A − log2 A^e` bits: `0.9999997` at `(17, 16)`, `0.999994` at `(12, 64)`, and `1.000000` to nine decimals at `(67, 2)`, which matches `log2 A^e = log2 A − 1 + log2(1 + S/A)` on [[castle-entropy](pages/castle-entropy.md)].

Block parity is not an error-detecting code. A parity bit detects every single-symbol error; block parity does not. Changing column `i` from height `a` to height `b` between neighbors `l` and `r` changes the block count by

```
Δ  =  max(0, b − l) − max(0, a − l)  +  max(0, r − b) − max(0, r − a)
```

(with `l = 0` at the first column and no `r` term at the last), and the parity flips exactly when `Δ` is odd. Over a uniform castle of width 17 and height 16, a uniform column and a uniform new height different from the old one, the parity flips with probability `0.4272`; restricted to edits after which some column still has height 16, `0.4236` (exact computation).[^song] The bit of [[castle-sign](pages/castle-sign.md)] is a statistic of the shape, and most single-column edits leave it unchanged.

---

## Rung 1 - the metadata

Between the URL and the audio there is a *label* for the track: an ID3v2 tag on an MP3, a Vorbis comment block on a FLAC or Ogg file, or an MP4 metadata atom, each a short block of key/value pairs. The table sizes a JSON label for "Never Gonna Give You Up" with 13 fields (title, artist, album, year, duration in milliseconds, sample rate, channels, bits per sample, codec, bitrate, genre, track number, a cover-art URL), and the same label with the four numeric fields only. A byte string of `n` bytes, read as an integer, fits a castle of height 256 and width `n + 1` by the rank/unrank bijection, since `A(n, 256) < 256^n ≤ A(n + 1, 256)` for these `n`:[^song]

| object | indented JSON | minified | zlib -9 | castle at `h = 256` |
|---|---|---|---|---|
| 13-field label | 366 B | 313 B | 233 B | `w = 234` |
| the 4 numeric fields | 92 B | 75 B | 74 B | `w = 75` |
| a 128-bit hash of the audio (fingerprint) | 16 B | 16 B | 16 B | `w = 17` |

**A fingerprint is a `(17, 256)` castle.** A 128-bit acoustic hash needs `w = 17` at `h = 256`, since `A(16,256) < 2^128 <= A(17,256)`. The 66-bit URL needs `w = 9` at the same height.

**The size depends on the decoder.** A decoder that holds a catalog of tracks (a music library, a fingerprint service) recovers the label from the URL, a castle of width 12 at height 64; a decoder without one needs the 233 bytes. In the terms of [[castle-compression](pages/castle-compression.md)], the label is parametric given the catalog and generic otherwise.

---

## Rung 2 - the audio itself

### The map

A 16-bit PCM sample is `s in [-32768, 32767]`. Set

```
c = s + 32769        so that   c in [1, 65536],    h = 65536
```

and scale the signal so its positive peak lands on `h`. Now every castle rule is a mastering rule:

| castle rule | waveform reading |
|---|---|
| column heights in `{1, ..., h}` | 16-bit quantization |
| **height `h`** (some column reaches `h`) | **peak-normalized**: the positive peak is at 0 dBFS |
| full-width bottom row (every `c_i >= 1`) | no sample below `-32768` - always true; the floor is the negative rail |
| block count `= c_1 + sum max(0, c_i - c_{i-1})` | **total upward variation** of the waveform |
| even number of blocks (PE 502) | total rise is even - one parity bit on the shape |
| digital silence | a plateau at height `32769`, mid-castle, not at the floor |

"Never Gonna Give You Up" runs 3 min 33 s = 213 s. At CD rate that is one channel of `213 x 44100 = 9,393,300` samples, so the mono waveform is a castle with

```
w = 9,393,300      h = 65536      raw skyline bits = w * 16 = 150,292,800
```

The stereo file, two skylines, is `w = 18,786,600` samples, or `37,573,200` bytes (37.6 MB) of raw PCM.

### Compression is the tier ladder

The **raster** of this castle, the `w x h` bit grid, would be `9,393,300 x 65536 = 615,599,308,800` bits, about 616 Gbit. The skyline is `150 Mbit`. That is the `w(h - log2 h)` gap of [[castle-compression](pages/castle-compression.md)]. Below the skyline, the audio codecs, sized from their bitrates on a 213-second track (the FLAC row is a typical ratio for pop music, not a measurement):

| codec | bytes for 213 s stereo | of WAV | castle at `h = 256` | tier |
|---|---|---|---|---|
| WAV 16-bit stereo (two skylines, raw) | 37,573,200 | 100.0% | `w = 37,573,200` | 2 - generic |
| FLAC (pop, ~60% typical) | ~22,500,000 | ~60% | `w ~ 22,500,000` | 1 - rule + residual |
| MP3 320 kbps | 8,520,000 | 22.7% | `w = 8,520,000` | lossy - spectral |
| Ogg Vorbis 160 kbps | 4,260,000 | 11.3% | `w = 4,260,000` | lossy - spectral |
| AAC 128 kbps | 3,408,000 | 9.1% | `w = 3,408,000` | lossy - spectral |
| Opus 96 kbps | 2,556,000 | 6.8% | `w = 2,556,000` | lossy - spectral |
| Opus 64 kbps | 1,704,000 | 4.5% | `w = 1,704,000` | lossy - spectral |

**Tier 1 is linear prediction.** For each block of a few thousand samples, FLAC fits an approximate linear recurrence `c_i ≈ Σ a_k c_{i−k}` of order up to 32, quantizes the coefficients, and codes the integer residual with a Rice code.[^flac] [[berlekamp-massey](pages/berlekamp-massey.md)] finds the shortest exact linear recurrence over a field; linear prediction fits an approximate one by least squares, and its compression ratio depends on how well a low-order recurrence predicts the material.

**Lossy codecs are spectral.** MP3, AAC, Vorbis and Opus keep quantized coefficients of a windowed modified discrete cosine transform, a relative of the skyline DFT of [[spectral-analysis](pages/spectral-analysis.md)] §3, with the quantization set by a model of hearing. Their output is a bitstream, a castle of height 256 with one column per byte, and the waveform is not recovered exactly.

---

## Finite fields on the waveform

`65537 = 2^16 + 1` is prime, the largest known Fermat prime, so the column heights `1, …, 65536` are elements of `F_65537`, all but `0`.

1. **Berlekamp-Massey detects exact linear rules.** Over `F_65537`, [[berlekamp-massey](pages/berlekamp-massey.md)] gives linear complexity 200 on 400 uniform random symbols, 200 on 400 samples of a quantized two-tone signal (440 Hz plus 329.628 Hz at 44.1 kHz), and 5 on 400 terms of a sequence generated by a linear recurrence of order 5.[^song] The quantized tone satisfies no exact linear recurrence of low order, although linear prediction compresses such signals; Berlekamp-Massey sees exact recurrences only.
2. **The NTT is an exact skyline DFT.** `3` generates the multiplicative group `F_65537^*`, of order `2^16`, so `ω = 3^64` has order 1024, and the number-theoretic transform of a block of 1024 columns, `Σ_j c_j ω^{jk}`, is computed exactly: the inverse transform recovers all 1024 samples.[^song] It is the DFT of [[spectral-analysis](pages/spectral-analysis.md)] §3 over `F_65537` instead of the complex numbers ([[finite-fields](pages/finite-fields.md)]); over the complex numbers its bins have the frequency reading.
3. **Encryption by a ring element.** The [[castle-cryptography](pages/castle-cryptography.md)] pages work in `F_p[x]/(Q)` with `Q` the characteristic polynomial of a castle count. Multiplying a waveform, block by block, by a fixed element of such a ring is a linear cipher; that ring and the attacks on it are on [[castle-cryptography-round-two](pages/castle-cryptography-round-two.md)].

The compact disc's error correction (CIRC) is a pair of Reed-Solomon codes over `GF(2^8)`, so a CD already stores a song as a stream of `h = 256` field symbols with parity.[^circ]

---

## Telephone signals as castles

Telephone tones and their detection are castle operations.

**Tones are Tier-0 castles.** At the telephone sampling rate of 8000 samples per second, a 2600 Hz tone has period `8000 / gcd(8000, 2600) = 40` samples (13 cycles), so it is a **castle of width 40, repeated**: a period and a repeat count, the parametric tier. Quantized to `h = 9` as `c_j = 5 + round(4 sin(2π · 13j/40))`, `j = 0, …, 39`:

```
(5, 9, 2, 4, 9, 2, 4, 9, 3, 3, 9, 3, 3, 9, 4, 2, 9, 4, 2, 9, 5, 1, 8, 6, 1, 8, 6, 1, 7, 7, 1, 7, 7, 1, 6, 8, 1, 6, 8, 1)

.#..#..#..#..#..#..#....................
.#..#..#..#..#..#..#..#..#.........#..#.
.#..#..#..#..#..#..#..#..#..##.##..#..#.
.#..#..#..#..#..#..#..##.##.##.##.##.##.
##..#..#..#..#..#..##.##.##.##.##.##.##.
##.##.##..#..##.##.##.##.##.##.##.##.##.
##.##.#########.##.##.##.##.##.##.##.##.
#####################.##.##.##.##.##.##.
########################################
```

Its skyline DFT has **two atoms**: bins 13 and 27 = 40 − 13 carry 99.2% of the energy once the mean is removed.[^song] A tone at the Nyquist frequency, 4000 Hz, has period 2, which gives the crenellated castles of [[castle-classification-shape](pages/castle-classification-shape.md)]; the sparse-spectrum castles of [[castle-classification-spectrum](pages/castle-classification-spectrum.md)] are defined from the exact DFT support.

**MF digits are four-atom castles.** Multi-frequency signaling uses pairs from {700, 900, 1100, 1300, 1500, 1700} Hz; KP (key pulse, the start of a number) is 1100 + 1700 Hz.[^mf] All 15 pairs have period 80 samples at 8000 samples per second, so KP is a castle of width 80; before quantization its DFT support is `{11, 17, 63, 69}`.[^song]

**Detection is one DFT bin.** The Goertzel algorithm evaluates the DFT at a single bin, so a tone detector is a linear functional on the skyline.

**The catalogue.** [[tone-castle-catalog](pages/tone-castle-catalog.md)] builds the castle for every DTMF key, every MF code and the call-progress tones. The DTMF keys have periods of 2000, 4000 or 8000 samples, longer than a DTMF burst, so a sent DTMF key is not a whole number of periods.[^song]

---

## Beethoven's Ninth - the whole page in one work

**Length.** The castle below is sized for a performance of about 65 minutes, the sum of the approximate movement timings in the table at the end of this section; performances differ by several minutes.

**Rung 0 - the URL of a Ninth video.** The id of any YouTube upload of the symphony is 11 base64url characters, a castle of width 12 and height 64, as for "Never Gonna Give You Up" in Rung 0.

**Rung 1 - the metadata.** A label for a movement of the Ninth carries fields such as `composer = "Ludwig van Beethoven"` (20 B), `work = "Symphony No. 9 in D minor, Op. 125"` (34 B) and `movement = "IV. Presto - Allegro assai (Ode to Joy)"` (39 B), with the performers, the year and the numeric fields of the Rung 1 table; it is a castle of a few hundred columns at `h = 256`. An acoustic fingerprint is 16 bytes, width 17 at `h = 256`.

**Rung 2 - the whole symphony as one castle.** At CD rate, 65 minutes of stereo audio is

```
65 min x 60 s x 44,100 samples/s x 2 channels x 2 bytes = 687,960,000 bytes  (688.0 MB)
samples per channel: 171,990,000            total samples: 343,980,000
```

so the two-channel castle at `h = 65536` has `w = 343,980,000`, and its raw skyline is `5,503,680,000` bits (5.5 Gbit). Peak normalization puts a column at height `h`. The block count is the total upward variation of the waveform, and the parity clause of Project Euler 502 keeps one bit of it.

**The tiers, applied.** The sizes of 65 minutes of stereo audio; the FLAC figure is a typical ratio for classical material, not a measurement:

| form | 65 min | of WAV |
|---|---|---|
| WAV, 16-bit stereo | 687,960,000 B (688.0 MB) | 100% |
| FLAC (classical, ~50%) | ~344 MB | ~50% |
| MP3 320 kbps | 156,000,000 B (156.0 MB) | 22.7% |
| MP3 128 kbps | 62,400,000 B (62.4 MB) | 9.1% |
| AAC 96 kbps | 46,800,000 B (46.8 MB) | 6.8% |
| Opus 64 kbps | 31,200,000 B (31.2 MB) | 4.5% |
| YouTube video URL | 11 characters (66 bits) | 1.2 × 10^-8 |
| an acoustic fingerprint of the recording | 16 B | 2.3 × 10^-8 |

The last two rows identify the recording; they do not encode it.

**The opening as a two-tone castle.** The Ninth begins with the open fifth A–E. Take the fifth A3–E4 in equal temperament with A4 = 440 Hz, so A3 = 220 Hz and E4 = 329.628 Hz. At 44.1 kHz the two periods are

```
A3: 44100 / 220     = 200.455 samples
E4: 44100 / 329.628 = 133.787 samples
```

The ratio of the frequencies is `2^(7/12)`, irrational, so the two-tone skyline has no exact period. Its DFT is concentrated near two bins and their mirrors, with further peaks at the harmonics of the instruments. Neither period is a whole number of samples, so a finite window spreads energy into neighboring bins, and the two atoms are approximate, unlike those of the 2600 Hz tone.

**The "Ode to Joy" phrase as a diatonic castle.** The phrase "Freude, schöner Götterfunken, Tochter aus Elysium" is stepwise, in D major, and covers the scale degrees 1 to 5. Written with one column per note and the height equal to the scale degree, it is the castle `(3, 3, 4, 5, 5, 4, 3, 2, 1, 1, 2, 3, 3, 2, 2)` of width 15 and height 5:

```
scale degree
5      ...##..........
4      ..####.........
3      #######....##..
2      ########..#####
1      ###############
       Freu-de schö-ner Göt-ter-fun-ken Toch-ter aus E-ly-si-um
```

It has 7 blocks; the mean block count over all castles of width 15 and height 5 is 14.31.[^song]

**Berlekamp-Massey on the phrase.** Over `F_65537`, [[berlekamp-massey](pages/berlekamp-massey.md)] gives the 15 heights linear complexity 8 = `⌈15/2⌉`, the value expected for 15 random symbols; 30 terms of a recurrence of order 5 give complexity 5.[^song]

**The transform of 1024 samples.** The NTT with `ω = 3^64` on 1024 consecutive samples of the opening is exact, as in the section on finite fields. Over the complex numbers, the DFT of the same block has bins `44100 / 1024 = 43.07 Hz` wide, so A3 lies at bin 5.11 and E4 at bin 7.65.

**Every tool from the page, one row per movement:**

| movement | ~duration | rung/tool it exemplifies best |
|---|---|---|
| I. Allegro ma non troppo | ~15 min | the opening two-tone castle - sparse spectrum |
| II. Molto vivace (Scherzo) | ~11 min | the loudest passage sets the column of height `h`, the peak normalization of Rung 2 |
| III. Adagio molto e cantabile | ~15 min | linear prediction (Tier 1) |
| IV. Presto / Ode to Joy | ~24 min | the diatonic castle, Berlekamp-Massey complexity 8 of 15 |
| whole work | ~65 min | `w = 343,980,000`, `h = 65536`, block parity one bit |

---

## Related Concepts

- [[castle-representations](pages/castle-representations.md)] - the skyline encoding used throughout.
- [[castle-counting-function](pages/castle-counting-function.md)] - `A(w, h) = h^w − (h−1)^w`, the size of the codebook.
- [[castle-compression](pages/castle-compression.md)] - the tiers of description that the audio codecs fall into.
- [[castle-entropy](pages/castle-entropy.md)] - `log2 A(w, h)` and the parity cost `log2 A − log2 A^e = 1 − log2(1 + S/A)`.
- [[castle-sign](pages/castle-sign.md)] - the block count as total upward variation.
- [[berlekamp-massey](pages/berlekamp-massey.md)] - the shortest exact linear recurrence of a sequence over a field.
- [[finite-fields](pages/finite-fields.md)] - finite fields and the orders of their elements, as for `ω = 3^64` in `F_65537`.
- [[spectral-analysis](pages/spectral-analysis.md)] - the skyline DFT and the spectra of castle graphs.
- [[castle-classification-spectrum](pages/castle-classification-spectrum.md)], [[castle-classification-shape](pages/castle-classification-shape.md)] - sparse-spectrum and crenellated castles.
- [[castle-cryptography](pages/castle-cryptography.md)], [[castle-cryptography-round-two](pages/castle-cryptography-round-two.md)] - the rings `F_p[x]/(Q)` used for encryption, and the attacks on them.
- [[castle-snippets](pages/castle-snippets.md)] - `all_castles` and `blocks`, used to verify the bijections.
- [[isospectral-castles](pages/isospectral-castles.md)] - non-isomorphic castle graphs with the same spectrum.
- [[image-as-castle](pages/image-as-castle.md)] - the same map for JPG and PNG: an image as a stack of row castles or one two-dimensional castle.
- [[castle-steganography](pages/castle-steganography.md)] - hiding a base64 string in castles; block parity as a covert channel.
- [[tone-castle-catalog](pages/tone-castle-catalog.md)] - every DTMF, MF and call-progress signal as a castle.
- [[hear-the-shape-seminar](pages/hear-the-shape-seminar.md)] / [[one-bit-seminar](pages/one-bit-seminar.md)] / [[hardin-identity-seminar](pages/hardin-identity-seminar.md)] / [[oeis-mining-seminar](pages/oeis-mining-seminar.md)] / [[sandcastle-seminar](pages/sandcastle-seminar.md)] / [[castle-fibers-char-2-walkthrough](pages/castle-fibers-char-2-walkthrough.md)] / [[tower-recursion-master-class](pages/tower-recursion-master-class.md)] / [[pell-castle-strip](pages/pell-castle-strip.md)] - the other seminar pages.

## Appearances in Sources

- [[project-euler-502-representations](pages/project-euler-502-representations.md)] - the integer-tuple (skyline) encoding and the block count as a sum of differences, the two facts every rung uses.
- [[project-euler-502-solution](pages/project-euler-502-solution.md)] - the count `A(w, h)`.

## Footnotes

[^rickroll]: https://www.youtube.com/watch?v=dQw4w9WgXcQ - "Rick Astley - Never Gonna Give You Up (Official Music Video)", 3 min 33 s runtime. YouTube video ids are 11 characters from the base64url alphabet `A-Z a-z 0-9 - _`, so the id namespace has size `64^11 = 2^66` and every id is a 66-bit integer.
[^flac]: https://xiph.org/flac/format.html §"Overview" and §"Subframe" [synthesis] - a FLAC stream is blocks of typically 4096 samples; each subframe is coded as constant, verbatim, fixed predictor, or LPC of order 1-32 with quantized coefficients, followed by the prediction residual encoded with Rice codes in partitions.
[^circ]: https://en.wikipedia.org/wiki/Cross-interleaved_Reed%E2%80%93Solomon_coding §"Overview" [synthesis] - CIRC, the CD's error-correction scheme, is two concatenated Reed-Solomon codes over GF(2^8), (32,28) and (28,24), with interleaving between them.
[^mf]: https://en.wikipedia.org/wiki/Multi-frequency_signaling §"Multi-frequency signals" and the tone table transcluded from https://en.wikipedia.org/wiki/Template:Multi-frequency_signaling_tones [synthesis] - "electronic signals that consist of a combination of two audible frequencies, usually selected from a set of six frequencies"; the table's columns are 700, 900, 1100, 1300, 1500, 1700 Hz, the KP row is marked at 1100 and 1700 Hz, the ST row at 1500 and 1700 Hz; "In R1 MF signaling this address information normally is a KP tone, the numeric digits of the destination number, and an ST tone to indicate the end of the address."
[^song]: Verified by execution (Python 3.11 with NumPy, 2026-10-16): the id `dQw4w9WgXcQ` as the integer `0x1d430e30f56817710`; the table of smallest widths and the skylines at `(17, 16)` (54 blocks, area 119) and `(12, 64)`, with `rank(unrank(n)) = n`, and the bijection checked on all castles of width 4 and height 3; `log2 A − log2 A^e` at `(17, 16)`, `(12, 64)`, `(67, 2)`; the flip probabilities at `(17, 16)` by exact summation over the neighbors of the edited column; the JSON labels (sizes from `json.dumps` and `zlib.compress(..., 9)`) and `A(n, 256) < 256^n ≤ A(n + 1, 256)`; 3 a generator of `F_65537^*`, `3^64` of order 1024, and the round trip of the length-1024 NTT on random samples; Berlekamp-Massey over `F_65537` on 400 random symbols, the quantized two-tone signal and an order-5 recurrence, and on the phrase; the 2600 Hz skyline and its 99.2% energy share; the KP support; the DTMF and MF periods; the phrase's 7 blocks and the mean 14.31; the 65-minute sizes.
