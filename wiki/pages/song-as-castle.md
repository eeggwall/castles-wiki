---
title: A song as a castle
category: Analyses
summary: How to encode a song as a castle, made concrete on three rungs with every number executed. Rung 0, the URL - a YouTube 11-character video id is a 66-bit integer, and an exact rank/unrank bijection (decompose by the first full-height column) turns it into a w=12, h=64 castle, a w=17, h=16 castle, or a w=67, h=2 castle; the "some column reaches h" rule costs log2(h^w/A(w,h)) bits (0.586 at (17,16), 2.538 at (12,64)) and the even-block restriction costs exactly 1.000 more, but block parity is a weak checksum. Rung 1, the metadata - a track's ID3-style label (title, artist, duration, sample rate, codec) is a few hundred bytes, a w~500 castle at h=256; entropy is relative to the decoder. Rung 2, the audio - a castle with h=65536 is a peak-normalized 16-bit PCM waveform, one sample per column, and the castle rules are mastering rules (height exactly h = 0 dBFS positive peak, bottom row = the -32768 floor, block count = total upward variation). Rick Astley's "Never Gonna Give You Up" (3:33 = 213 s) is a w=9,393,300 castle at h=65536 per channel; the compression ladder WAV 100% / FLAC / MP3 / AAC / Opus is castle-compression's tier ladder run on a waveform. Finite fields - 16-bit samples are elements of F_65537 (a Fermat prime); Berlekamp-Massey diagnoses linear-recurrence structure, and the length-1024 NTT mod 65537 with root 3^64 is the skyline DFT with no rounding. Seminar seed, "The Wire, but castles" - the 2600 Hz tone at telephone rate is an exactly periodic w=40 castle with a two-atom DFT, blue-box KP is a w=80 four-atom castle, Goertzel is one DFT bin, in-band signaling is block parity riding on the skyline, and the pager code "jump the 5" is a vertical reflection of the skyline. Finale - Beethoven's Ninth Symphony at the Red Book CD length (74 min, 782.8 MB) and the 78-min high-density variant; every tool from the page applied one at a time, from the opening open fifth on A and E (a two-tone sparse-spectrum castle) to the "Ode to Joy" phrase (a length-15 diatonic castle at h=5) to the whole symphony as one castle with w~391 million (74 min) or w~412 million (78 min).
tags: [analysis, castle, encoding, compression, audio, pcm, lpc, flac, mp3, aac, opus, finite-field, ntt, berlekamp-massey, entropy, youtube, beethoven, cd, red-book, phreaking, dtmf, seminar, pedagogy]
sources: [project-euler-502-representations, project-euler-502-solution]
created: 2026-09-19
updated: 2026-09-28
---

# A song as a castle

**The one idea:** a castle with `h = 65536` *is* a peak-normalized 16-bit waveform, one sample per column. Everything else on this page is either climbing down to that (the URL and the metadata are small castles) or measuring how cheaply that big castle can be written (compression), and then asking what happens when the column heights are read as elements of a finite field. The finale applies the whole page to one work, Beethoven's Ninth Symphony, at Compact Disc length.

This is the reverse direction of "hear the shape of a castle" ([[spectral-analysis](pages/spectral-analysis.md)]), which starts from a castle and takes a spectrum - a lossy invariant, and the whole point is what collides ([[isospectral-castles](pages/isospectral-castles.md)]). This page starts from sound and builds a castle, and the map is a **bijection**: nothing is lost, the skyline is the waveform, and the skyline DFT of [[spectral-analysis](pages/spectral-analysis.md)] §3 is literally the audio spectrum. Same map, read the other way.

The encodings used are the skyline (integer tuple) of [[castle-representations](pages/castle-representations.md)], the exact codebook size `A(w,h) = h^w - (h-1)^w` of [[castle-counting-function](pages/castle-counting-function.md)], and the tier ladder of [[castle-compression](pages/castle-compression.md)]. Every number below follows from those formulas plus one running example - Rick Astley's "Never Gonna Give You Up" for the rungs, Beethoven's Ninth for the finale.

---

## Rung 0 - the URL

A YouTube video URL is `https://www.youtube.com/watch?v=<id>` where `<id>` is 11 base64url characters (`A-Z`, `a-z`, `0-9`, `-`, `_`). Since `64^11 = 2^66`, the payload is **66 bits**. The canonical example on this page is `dQw4w9WgXcQ` - Rick Astley, "Never Gonna Give You Up", 3:33.[^rickroll] As a base-64 integer that id is `0x1d430e30f56817710` = 33,736,714,463,647,725,328. The question is: which `(w, h)` castle holds 66 bits?

The codebook is the set of all castles at `(w, h)`, of size `A(w,h) = h^w - (h-1)^w`; it holds `log2 A` bits. The rule "some column reaches `h`" costs

```
touch_cost(w,h) = log2( h^w / A(w,h) ) = -log2( 1 - ((h-1)/h)^w )   bits
```

relative to plain base-`h` digits, and it is the only thing separating a castle from a number written in base `h`:

| `h` | bits per column | smallest `w` with `A(w,h) >= 2^66` | `log2 A(w,h)` | touch cost | `log2 A(w-1,h)` |
|---|---|---|---|---|---|
| 2 | 1 | 67 | 67.000 | 0.000 | 66.000 (one short) |
| 16 | 4 | 17 | 67.414 | 0.586 | 63.457 (one short) |
| 64 | 6 | 12 | 69.462 | 2.538 | 63.483 (short) |
| 256 | 8 | 9 | 67.147 | 4.853 | 59.294 |

At `h = 64` the base matches the URL alphabet exactly, but the touch rule eats 2.5 bits, so a twelfth column carries the eleven base-64 characters plus a guaranteed peak. At `h = 16` the shortfall is under a bit and the 17th hex-digit column is nearly free. At `h = 2` a plain 67-bit binary castle. Compression is a property of the encoding against the data, not of the encoding alone - the point [[castle-compression](pages/castle-compression.md)] makes about the U/R/D string, visible here at the scale of a single URL.

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

### The even-block codebook: exactly one bit, and a weak checksum

PE 502 counts only even-block castles, `F(w,h)`. Enumerative coding still works: a DP over `(column, last height, touched h yet, block parity)` counts completions and unranks directly into the even-block codebook. At `(w,h)` sizes of this order the difference `log2 A - log2 F` is one bit to six decimal places - [[castle-entropy](pages/castle-entropy.md)]'s asymptotic `-1` is already exact for a URL-sized castle. The bit is not an error-detecting code. A true parity bit detects every single-symbol error. Block parity does not: corrupting one random column flips the block parity only about 44% of the time on random `h=16` castles. The block count is the total upward variation `c_1 + sum max(0, c_i - c_{i-1})`, and a single-column edit changes two adjacent rises whose parities cancel more often than not. The one bit of [[castle-sign](pages/castle-sign.md)] is real information, but it is spent on a statistic of the *shape*, not on error detection.

---

## Rung 1 - the metadata

Between the URL and the audio there is a *label* for the track. In the general audio ecosystem this is an ID3 v2 tag frame on an MP3, a Vorbis comment block on a FLAC or Ogg, or the equivalent Xiph / MP4 metadata atom - a short block of UTF-8 key/value pairs. A minimal but recognizable frame carries title, artist, album, year, duration in milliseconds, sample rate, channel count, codec name, and bitrate. Written naively it runs a few hundred bytes; zlib'd, well under two hundred:

| object | pretty | minified | zlib -9 | castle `h=256` (zlib bytes as columns) |
|---|---|---|---|---|
| generous ID3-equivalent JSON (13 fields, cover-art URL) | ~500 B | ~380 B | ~200 B | `w ~ 200` |
| the same, numbers only (duration, rate, channels, bitrate) | ~80 B | ~60 B | ~40 B | `w ~ 40` |
| a 128-bit hash of the audio (fingerprint) | 16 B | 16 B | 16 B | `w = 17, h = 256` |

Two things to notice.

**A fingerprint is a `(17, 256)` castle.** A 128-bit acoustic hash needs `w = 17` at `h = 256`, since `A(16,256) < 2^128 <= A(17,256)`. The 66-bit URL needs `w = 9` at the same height.

**Entropy is relative to the decoder.** The metadata block is ~200 bytes compressed, but every byte of it is a deterministic function of the audio *given a catalog*. To a decoder with that oracle (a music library, a fingerprint service), the label is worth exactly the URL-sized castle; to a decoder without it, ~200 columns. This is [[castle-compression](pages/castle-compression.md)]'s Tier 0 / Tier 2 split with the "program" being a lookup: parametric relative to the catalog, generic relative to the bytes.

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
| **height exactly `h`** (some column reaches `h`) | **peak-normalized**: the positive peak hits 0 dBFS |
| full-width bottom row (every `c_i >= 1`) | no sample below `-32768` - always true; the floor is the negative rail |
| block count `= c_1 + sum max(0, c_i - c_{i-1})` | **total upward variation** of the waveform |
| even number of blocks (PE 502) | total rise is even - one parity bit on the shape |
| digital silence | a plateau at height `32769`, mid-castle, not at the floor |

"Never Gonna Give You Up" runs 3 min 33 s = 213 s. At CD rate that is one channel of `213 x 44100 = 9,393,300` samples, so the mono waveform is a castle with

```
w = 9,393,300      h = 65536      raw skyline bits = w * 16 = 150,292,800
```

The full stereo file, two skylines, is `w = 18,786,600` or `bytes = 37,573,200` (~37.6 MB) as raw PCM. The castle is as far from convex, unimodal or symmetric as a castle gets ([[castle-classification-shape](pages/castle-classification-shape.md)]).

### Compression is the tier ladder

The **raster** of this castle - the `w x h` bit grid - would be `9,393,300 x 65536 = 616 Gbit`. The skyline is `150 Mbit`. That is the `w(h - log2 h)` gap of [[castle-compression](pages/castle-compression.md)]. Below the skyline, the general audio codec ladder, sized directly from bitrate on a 213-second track:

| codec | bytes for 213 s stereo | of WAV | castle at `h = 256` | tier |
|---|---|---|---|---|
| WAV 16-bit stereo (two skylines, raw) | 37,573,200 | 100.0% | `w = 37,573,200` | 2 - generic |
| FLAC (pop, ~60% typical) | ~22,500,000 | ~60% | `w ~ 22,500,000` | 1 - rule + residual |
| MP3 320 kbps | 8,520,000 | 22.7% | `w = 8,520,000` | lossy - spectral |
| Ogg Vorbis 160 kbps | 4,260,000 | 11.3% | `w = 4,260,000` | lossy - spectral |
| AAC 128 kbps | 3,408,000 | 9.1% | `w = 3,408,000` | lossy - spectral |
| Opus 96 kbps | 2,556,000 | 6.8% | `w = 2,556,000` | lossy - spectral |
| Opus 64 kbps | 1,704,000 | 4.5% | `w = 1,704,000` | lossy - spectral |

**Tier 1 is linear prediction.** FLAC's core is exactly the wiki's "rule-generated skyline": per block of a few thousand samples, fit a linear recurrence `c_i ~ sum a_k c_{i-k}` of order up to 32, quantize the taps, and entropy-code the integer residual with a Rice code.[^flac] That is the least-squares, real-valued cousin of what [[berlekamp-massey](pages/berlekamp-massey.md)] does exactly over a field: find the shortest linear rule that explains the skyline. The same coder gives different ratios on different material: the ratio measures how well a low-order linear rule predicts the skyline.

**Lossy is spectral.** MP3, AAC, Vorbis, and Opus discard the residual altogether and keep quantized MDCT coefficients - the skyline DFT of [[spectral-analysis](pages/spectral-analysis.md)] §3, windowed, with the small bins zeroed by a hearing model. Their output is a bitstream, so as a castle it is again `h = 256`, `w =` bytes; the waveform castle is gone and only a *spectral* description survives.

---

## Finite fields on the waveform

`65537 = 2^16 + 1` is prime (the largest known Fermat prime), so 16-bit samples are, as they stand, elements of `F_65537` - no reduction, no wasted symbols, one spare element. Three things follow.

1. **Berlekamp-Massey as a Tier-1 detector.** Run [[berlekamp-massey](pages/berlekamp-massey.md)] over `F_65537` on 400 consecutive waveform columns from any real recording: linear complexity reliably lands near **200**, the maximum `N/2` a length-400 sequence can have. A recorded waveform satisfies no exact linear recurrence - it is Tier 2 in the exact sense even though LPC compresses it 10x in the approximate sense. Run the same test on a 5-tap LFSR skyline of the same length and BM returns complexity **5**. This is the "detector for rule-generated castles" that [[castle-compression](pages/castle-compression.md)] asks for, answered for exact linear rules; LPC measures least-squares linear structure, which BM does not see.
2. **The NTT is the skyline DFT with no rounding.** `3` generates `F_65537^*`, so `omega = 3^64` is a primitive 1024th root of unity and the number-theoretic transform of a 1024-column block is exact: forward then inverse recovers all 1024 samples bit for bit. [[spectral-analysis](pages/spectral-analysis.md)] §3 and [[finite-fields](pages/finite-fields.md)] are the same transform over two different fields; over `F_p` it is a bijection with no floating point, over `C` it has the frequency reading.
3. **Encryption is a change of ring.** The [[castle-cryptography](pages/castle-cryptography.md)] series works in `F_p[x]/(Q)` with `Q` a castle's characteristic polynomial. A waveform castle is a very long vector over `F_65537`; multiplying it, block by block, by a fixed element of such a ring is a stream cipher whose key is a castle - and a small one, since `Q` has degree `k+1`. The [[castle-cryptography-round-two](pages/castle-cryptography-round-two.md)] attacks apply verbatim.

Also worth knowing: the compact disc's error correction (CIRC) is a pair of Reed-Solomon codes over `GF(2^8)`, so a CD already stores a song as a stream of `h = 256` field symbols with parity.[^circ]

---

## Seminar seed: "The Wire, but castles"

Every object of a telephone network gets a toy castle, and the network's operations become maps between castles.

**Tones are Tier-0 castles.** At the telephone sampling rate of 8000 Hz, a 2600 Hz tone has exact period `8000 / gcd(8000, 2600) = 40` samples (13 cycles), so it is a **width-40 castle repeated** - period plus repeat count, the parametric tier. Quantized to `h = 9`:

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

Its skyline DFT has **two atoms**, bins 13 and 27 = 40 - 13, carrying over 99% of the energy - the [[castle-classification-spectrum](pages/castle-classification-spectrum.md)] sparse-spectrum predicate, with the crenellated castle of [[castle-classification-shape](pages/castle-classification-shape.md)] Axis 7 as the special case of a tone at the Nyquist frequency. 2600 Hz is the tone a long-distance trunk read as "line idle".[^bluebox]

**Blue-box digits are four-atom castles.** The trunk's own MF signaling used pairs from {700, 900, 1100, 1300, 1500, 1700} Hz; KP (key pulse, "start of number") is 1100 + 1700.[^mf] Both have period 80 samples at 8 kHz, so KP is a width-80 castle whose DFT support is exactly `{11, 17, 63, 69}`. Every MF digit is a castle with a four-atom spectrum.

**Detection is one DFT bin.** The Goertzel algorithm evaluates the DFT at a single bin, so a tone detector is a linear functional on the skyline.

**In-band signaling and block parity.** In-band signaling puts control (tones) and content (voice) on the same channel. The PE 502 parity clause is likewise a control bit computed from the same skyline that carries the data, and by the 44% flip rate above, most single-column edits change the data without changing that bit.

**The pager code is a skyline reflection.** In *The Wire*, the Barksdale crew's pager messages are seven-digit numbers that do not dial; the cipher Prez cracks on screen ("jump the 5") replaces each digit by its opposite across the 5 on a phone keypad, `d -> 10 - d`, with `5 <-> 0`.[^wire] Write a pager number as a castle with `h = 10` (digit `d` is height `d`, digit 0 is height 10) and the cipher is a **vertical reflection of the skyline about height 5**, with the two special heights swapping:

```
5550134  ->  0005976

...#...          ###....
...#...          ###.#..
...#...          ###.#..
...#...          ###.##.
...#...          ###.###
####...          #######
####..#          #######
####.##          #######
####.##          #######
#######          #######
```

Phone numbers are `(7, 10)` or `(10, 10)` castles; a contact network is a graph whose vertices are small castles; an organization chart is the cycle-forest form of [[castle-representations](pages/castle-representations.md)]; the wiretap is the intercepted skyline stream of rung 2; and the encryption is the [[castle-cryptography](pages/castle-cryptography.md)] ring with a castle of large `k` as the key.

---

## Beethoven's Ninth - the whole page in one work

**CD length.** The Red Book Compact Disc specification fixed a 12 cm disc with about 74 minutes of playing time. A widely repeated but disputed story attributes the length to Sony's Norio Ohga requiring that the disc hold Furtwängler's 1951 Bayreuth recording of the Ninth.[^cd-history] Later high-density variants reach 78 or 80 minutes by reducing the track pitch.

**Rung 0 - the URL of a Ninth video.** Any full YouTube upload of the symphony is an 11-character base-64 castle - `w = 12, h = 64` after the touch rule, exactly the shape "Never Gonna Give You Up" landed on above.

**Rung 1 - the metadata.** An ID3-equivalent label for a movement of the Ninth carries roughly: `composer = "Ludwig van Beethoven"` (20 B), `work = "Symphony No. 9 in D minor, Op. 125"` (34 B), `movement = "IV. Presto - Allegro assai (Ode to Joy)"` (~40 B), `performer` / `conductor` / `year` (~50 B), plus `duration_ms` and `sample_rate` (~30 B). A generous frame is `~500 B` before compression, a few hundred after - a `w ~ 200` castle at `h = 256`. An acoustic fingerprint is 16 bytes, `w = 17` at `h = 256`. The score itself, in a symbolic representation like MusicXML, is a few tens of kilobytes - larger than the label, smaller than the audio by four orders of magnitude.

**Rung 2 - the whole symphony as one castle.** The exact CD-DA payload of a 74-min disc is

```
74 min x 60 s x 44,100 samples/s x 2 channels x 2 bytes = 782,784,000 bytes  (782.8 MB)
samples per channel: 195,804,000            total samples: 391,608,000
```

so the two-channel castle at `h = 65536` has `w = 391,608,000`, and its raw skyline is `6.27 Gbit` (the audio payload of the disc). The 78-minute high-density variant is `78 min x 176,400 B/s = 825,552,000 bytes (825.6 MB)`, `w = 412,776,000` at `h = 65536`. Peak normalization satisfies the touch rule by construction. The block count is the total upward variation of the waveform, and PE 502's parity clause keeps one bit of it.

**Compression tier ladder, applied.** The FLAC figure is a typical ratio for classical material, not a measurement:

| form | 74 min (Red Book, 1980) | 78 min (high-density variant) | of WAV |
|---|---|---|---|
| WAV / CD-DA payload | 782,784,000 B (782.8 MB) | 825,552,000 B (825.6 MB) | 100% |
| FLAC (classical, ~50%) | ~390 MB | ~413 MB | ~50% |
| MP3 320 kbps | 177,600,000 B (177.6 MB) | 187,200,000 B (187.2 MB) | 22.7% |
| MP3 128 kbps | 71,040,000 B (71.0 MB) | 74,880,000 B (74.9 MB) | 9.1% |
| AAC 96 kbps | 53,280,000 B (53.3 MB) | 56,160,000 B (56.2 MB) | 6.8% |
| Opus 64 kbps | 35,520,000 B (35.5 MB) | 37,440,000 B (37.4 MB) | 4.5% |
| YouTube video URL | 11 characters (66 bits) | 11 characters (66 bits) | ~10^-8 |
| an acoustic fingerprint of the work | 16 B | 16 B | ~10^-8 |

The last two rows identify the recording; they do not encode it.

**The opening as a two-tone castle.** The Ninth begins *pianissimo* with an open fifth, A and E, in the second violins and cellos. At standard tuning, A = 440 Hz and E = 329.628 Hz. At 44.1 kHz the two component periods are

```
A: 44100 / 440     = 100.227 samples
E: 44100 / 329.628 = 133.787 samples
```

The frequency ratio is `2^(7/12)` in equal temperament, which is irrational, so the two-tone skyline has no exact period. Its DFT is concentrated at two bins (and their mirrors), plus the harmonics of the string tone: the [[castle-classification-spectrum](pages/castle-classification-spectrum.md)] sparse-spectrum predicate, as for the 2600 Hz tone above. Because neither period is a whole number of samples, a finite window leaks energy into neighbouring bins, so the two atoms are only approximate.

**The "Ode to Joy" phrase as a diatonic castle.** The first sung phrase of *Freude, schöner Götterfunken* is stepwise, in D major, and covers scale degrees 1-5. Written as a castle over `h = 5` with each note occupying one column and the height equal to its scale degree, the phrase `(3, 3, 4, 5, 5, 4, 3, 2, 1, 1, 2, 3, 3, 2, 2)` is:

```
scale degree
5      ...##..........
4      ..####.........
3      #######....##..
2      ########..#####
1      ###############
       Freu-de,  schö-ner Göt-ter- fun-ken
```

Length 15, blocks = 7. The mean block count over all `(15, 5)` castles is about 14.3.

**Berlekamp-Massey on the phrase.** Read those 15 note-heights as elements of `F_65537`. [[berlekamp-massey](pages/berlekamp-massey.md)] returns linear complexity 8 = `ceil(15/2)`, the generic value for a length-15 sequence: no linear recurrence shorter than the phrase itself explains it. The 5-tap LFSR of the phreaking seminar returns complexity 5 in a length-30 window.

**NTT on 1024 samples.** Take any 1024 consecutive samples from the opening, read them as elements of `F_65537`, and run the NTT with `omega = 3^64`. Forward then inverse recovers the samples bit for bit. Over `C`, the DFT of the same block has bin width `44100 / 1024 = 43.1 Hz`, so A lies near bin 10.2 and E near bin 7.7, with further peaks at the harmonics.

**Every tool from the page, one row per movement:**

| movement | ~duration | rung/tool it exemplifies best |
|---|---|---|
| I. Allegro ma non troppo | ~15 min | the opening two-tone castle - sparse spectrum |
| II. Molto vivace (Scherzo) | ~11 min | tutti peak that pins the touch row - the rung-2 mastering rule |
| III. Adagio molto e cantabile | ~15 min | linear prediction (Tier 1) |
| IV. Presto / Ode to Joy | ~24 min | the diatonic castle above, Berlekamp-Massey complexity 8 of 15 |
| whole work | ~74 min | `w = 391,608,000`, `h = 65536`, block-parity 1 bit |

---

## Related Concepts

- [[castle-representations](pages/castle-representations.md)] - the skyline is the encoding used throughout; the cycle-forest form is the org chart.
- [[castle-counting-function](pages/castle-counting-function.md)] - `A(w,h) = h^w - (h-1)^w`, the codebook size and the rank/unrank decomposition.
- [[castle-compression](pages/castle-compression.md)] - the tier ladder that the audio codecs instantiate; the rule-detector question answered for linear rules.
- [[castle-entropy](pages/castle-entropy.md)] - the one-bit parity cost, exact here to six decimals.
- [[castle-sign](pages/castle-sign.md)] - the block count as total upward variation.
- [[berlekamp-massey](pages/berlekamp-massey.md)] - exact linear complexity over `F_65537`; the finite-field cousin of LPC.
- [[finite-fields](pages/finite-fields.md)] - `F_p` and roots of unity; the NTT lives here.
- [[spectral-analysis](pages/spectral-analysis.md)] - the skyline DFT, read as an audio spectrum; the "hear the shape" direction this page reverses.
- [[castle-classification-spectrum](pages/castle-classification-spectrum.md)], [[castle-classification-shape](pages/castle-classification-shape.md)] - sparse-spectrum and crenellated castles; the tones and the Ninth's opening chord.
- [[castle-cryptography](pages/castle-cryptography.md)], [[castle-cryptography-round-two](pages/castle-cryptography-round-two.md)] - the ring the toy network encrypts with, and what breaks it.
- [[castle-snippets](pages/castle-snippets.md)] - `all_castles` and `blocks`, used to verify the bijections.
- [[isospectral-castles](pages/isospectral-castles.md)] - where the "hear the shape" direction loses information; the lossless direction here does not.
- [[image-as-castle](pages/image-as-castle.md)] - the same map for JPG and PNG: an image as a stack of row castles or one two-dimensional castle.
- [[castle-steganography](pages/castle-steganography.md)] - hiding a base64 string in castles; the block-parity channel is the covert channel of "The Wire, but castles".
- [[castle-entropy](pages/castle-entropy.md)] - the `log_2 A(w,h)` budget and the `-1` bit even-block price used throughout Rung 0/1; the "castle-entropy asymptotic -1" this page invokes.
- [[hear-the-shape-seminar](pages/hear-the-shape-seminar.md)] / [[one-bit-seminar](pages/one-bit-seminar.md)] / [[hardin-identity-seminar](pages/hardin-identity-seminar.md)] / [[oeis-mining-seminar](pages/oeis-mining-seminar.md)] / [[sandcastle-seminar](pages/sandcastle-seminar.md)] / [[castle-fibers-char-2-walkthrough](pages/castle-fibers-char-2-walkthrough.md)] / [[tower-recursion-master-class](pages/tower-recursion-master-class.md)] / [[pell-castle-strip](pages/pell-castle-strip.md)] - the other seminar pages.

## Appearances in Sources

- [[project-euler-502-representations](pages/project-euler-502-representations.md)] - the integer-tuple (skyline) encoding and the block count as a sum of differences, the two facts every rung uses.
- [[project-euler-502-solution](pages/project-euler-502-solution.md)] - the count `A(w,h)` whose decomposition by first full-height column is the ranking scheme.

## Footnotes

[^rickroll]: https://www.youtube.com/watch?v=dQw4w9WgXcQ - "Rick Astley - Never Gonna Give You Up (Official Music Video)", 3 min 33 s runtime. YouTube video ids are 11 characters from the base64url alphabet `A-Z a-z 0-9 - _`, so the id namespace has size `64^11 = 2^66` and every id is a 66-bit integer.
[^flac]: https://xiph.org/flac/format.html §"Overview" and §"Subframe" [synthesis] - a FLAC stream is blocks of typically 4096 samples; each subframe is coded as constant, verbatim, fixed predictor, or LPC of order 1-32 with quantized coefficients, followed by the prediction residual encoded with Rice codes in partitions.
[^circ]: https://en.wikipedia.org/wiki/Cross-interleaved_Reed%E2%80%93Solomon_coding §"Overview" [synthesis] - CIRC, the CD's error-correction scheme, is two concatenated Reed-Solomon codes over GF(2^8), (32,28) and (28,24), with interleaving between them.
[^bluebox]: https://en.wikipedia.org/wiki/Blue_box §"Discovery and early use", §"Blue boxing" - "The basic protocol for finding a free line worked by playing a 2600 Hz tone into the line whenever it was not being used"; a phreaker's 2600 Hz tone meant "The called office interpreted this tone as the caller hanging up before the call completed"; Cap'n Crunch cereal boxes included "a small whistle that, by coincidence, generated a 2600 Hz tone when one of the whistle's two holes was covered", and "The phreaker John Draper adopted his nickname 'Captain Crunch' from this whistle."
[^mf]: https://en.wikipedia.org/wiki/Multi-frequency_signaling §"Multi-frequency signals" and the tone table transcluded from https://en.wikipedia.org/wiki/Template:Multi-frequency_signaling_tones [synthesis] - "electronic signals that consist of a combination of two audible frequencies, usually selected from a set of six frequencies"; the table's columns are 700, 900, 1100, 1300, 1500, 1700 Hz, the KP row is marked at 1100 and 1700 Hz, the ST row at 1500 and 1700 Hz; "In R1 MF signaling this address information normally is a KP tone, the numeric digits of the destination number, and an ST tone to indicate the end of the address."
[^wire]: https://en.wikipedia.org/wiki/The_Pager §"Plot summary" - "each pager message consists of a seven-digit phone number and a two-digit identifying tag"; the numbers do not work as dialed, so a masking scheme is suspected, and "The code is ultimately cracked by Prez." The article does not spell out the substitution; the rule stated above (each digit to its opposite across the 5 on the keypad, with 5 and 0 trading places) is the one Prez works out on screen in the episode.
[^cd-history]: https://en.wikipedia.org/wiki/Compact_disc §"History" [synthesis] - the Red Book Compact Disc specification adopted a 12 cm disc with roughly 74 minutes of playing time; a widely repeated origin story is that Sony vice-president Norio Ohga, a trained baritone, required that the disc hold Wilhelm Furtwängler's 1951 Bayreuth Festival recording of Beethoven's Symphony No. 9 (about 74 minutes) in a single sitting, over Philips's proposed shorter format. The story has been questioned in interviews with the Philips engineers involved but remains the canonical account and is repeated by Sony in its own histories. Later Red Book variants extended nominal playing time to about 80 minutes by decreasing track pitch.
