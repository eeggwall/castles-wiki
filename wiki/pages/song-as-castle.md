---
title: A Spotify song as a castle
category: Analyses
summary: How to encode a Spotify song as a castle, made concrete on three rungs with every number executed. Rung 0, the URL - the 22-character track id is a 128-bit integer, and an exact rank/unrank bijection (decompose by the first full-height column) turns it into a w=33, h=16 castle or a w=17, h=256 castle; the "some column reaches h" rule costs log2(h^w / A(w,h)) bits (0.18 at (33,16), 3.96 at (17,256)) and the even-block restriction costs exactly 1.000000 more, but block parity is a weak checksum (a single-column corruption flips it only 44% of the time). Rung 1, the API - a schema-faithful Track object is 3.6 KB minified, 1.0 KB zlib'd (570 B without the deprecated available_markets), so a w~1000, h=256 castle; audio-features is 130 bits of numbers, the same w=33, h=16 shape as the URL; relative to Spotify's own database every byte of it is redundant with the 128-bit id, so entropy is relative to the decoder. Rung 2, the audio - a castle with h=65536 is a peak-normalized 16-bit PCM waveform, one sample per column, and the castle rules are mastering rules (height exactly h = 0 dBFS positive peak, bottom row = the -32768 floor, block count = total upward variation). Measured on a real 2.16 s file: w=103846, 2,904,534 blocks, touch-cost 0.33 bits; the compression ladder WAV 100% / FLAC 26.6% / LPC-8+Rice 9.5% / AAC-160 2.4% is castle-compression's tier ladder run on a waveform. A 3:30 track is a w=18.5M castle at h=65536 or a w=8.4M castle at h=256 for the 320 kbps Vorbis stream. Finite fields - 16-bit samples are elements of F_65537 (a Fermat prime); Berlekamp-Massey on 400 samples returns linear complexity 200 = N/2 (Tier 2, no exact rule) against 5 for a 5-tap LFSR skyline, and the length-1024 NTT mod 65537 with root 3^64 is the skyline DFT with no rounding. Ends with a seminar seed, "The Wire, but castles" - the 2600 Hz tone at telephone rate is an exactly periodic w=40 castle with a two-atom DFT, the blue-box KP pair is a w=80 four-atom castle, Goertzel is one DFT bin, in-band signaling is block parity riding on the skyline, and the pager code "jump the 5" is a vertical reflection of the skyline.
tags: [analysis, castle, encoding, compression, audio, pcm, lpc, flac, finite-field, ntt, berlekamp-massey, entropy, spotify, json, phreaking, dtmf, seminar, pedagogy, implementation]
sources: [project-euler-502-representations, project-euler-502-solution]
created: 2026-09-19
updated: 2026-09-19
---

# A Spotify song as a castle

**The one idea:** a castle with `h = 65536` *is* a peak-normalized 16-bit waveform, one sample per column. Everything else on this page is either climbing down to that (the URL and the API response are small castles) or measuring how cheaply that big castle can be written (compression), and then asking what happens when the column heights are read as elements of a finite field.

This is the reverse direction of the S4 arc, "hear the shape of a castle" ([[spectral-analysis](pages/spectral-analysis.md)]). S4 starts from a castle and takes a spectrum - a lossy invariant, and the whole point is what collides ([[isospectral-castles](pages/isospectral-castles.md)]). This page starts from sound and builds a castle, and the map is a **bijection**: nothing is lost, the skyline is the waveform, and the skyline DFT of [[spectral-analysis](pages/spectral-analysis.md)] §3 is literally the audio spectrum. Same map, read the other way.

Every number below was produced by one script on 2026-09-19; the pinned outputs are quoted.[^exec] The encodings used are the skyline (integer tuple) of [[castle-representations](pages/castle-representations.md)], the exact codebook size `A(w,h) = h^w - (h-1)^w` of [[castle-counting-function](pages/castle-counting-function.md)], and the tier ladder of [[castle-compression](pages/castle-compression.md)].

---

## Rung 0 - the URL

A Spotify track URL is `https://open.spotify.com/track/<id>` where `<id>` is 22 base-62 characters. `62^22` is just over `2^131`, and the ids are 128-bit integers rendered in base 62 (the docs' running example, `11dFghVXANMlKmJXsNCbNl`, happens to be a 126-bit number, hex `21b8ea29b57de0be9f8de9e74970f265`).[^spot-track] So the payload is **128 bits**, and the question is: which `(w, h)` castle holds 128 bits?

The codebook is the set of all castles at `(w, h)`, of size `A(w,h) = h^w - (h-1)^w`; it holds `log2 A` bits. The rule "some column reaches `h`" costs

```
touch_cost(w,h) = log2( h^w / A(w,h) ) = -log2( 1 - ((h-1)/h)^w )   bits
```

relative to plain base-`h` digits, and it is the only thing separating a castle from a number written in base `h`:

| `h` | bits per column | smallest `w` with `A(w,h) > 2^128` | `log2 A(w,h)` | touch cost | `log2 A(w-1,h)` |
|---|---|---|---|---|---|
| 2 | 1 | 129 | 129.000 | 0.000 | 128.000 (one short) |
| 16 | 4 | 33 | 131.817 | 0.183 | 127.804 (one short) |
| 256 | 8 | 17 | 132.043 | 3.957 | 123.958 |

At `h = 256` sixteen columns *ought* to hold 16 bytes = 128 bits, but the touch rule eats almost 4 bits (a random 16-byte string fails to contain a 255 with probability `(255/256)^16 = 94%`), so a seventeenth column is needed. At `h = 16` the shortfall is 0.2 bits and the 33rd column is nearly free. Compression is a property of the encoding against the data, not of the encoding alone - the point [[castle-compression](pages/castle-compression.md)] makes about the U/R/D string, visible here at the scale of a single URL.

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

Checked as an exact bijection against the brute-force `all_castles` of [[castle-snippets](pages/castle-snippets.md)] at `(w,h) = (3,2), (4,3), (5,2), (3,4), (4,4)`. Applied to the example id at `(33, 16)`:

```
skyline: (16, 3, 2, 12, 9, 15, 11, 3, 10, 12, 6, 8, 14, 15, 1, 12, 15, 10, 16, 9, 14, 15, 10, 15, 8, 5, 10, 8, 1, 16, 3, 7, 6)
blocks: 105    area: 317

#.................#..........#...
#....#.......#..#.#..#.#.....#...
#....#......##..#.#.##.#.....#...
#....#......##..#.#.##.#.....#...
#..#.#...#..##.##.#.##.#.....#...
#..#.##..#..##.##.#.##.#.....#...
#..#.##.##..##.####.####..#..#...
#..####.##..##.#########..#..#...
#..####.##.###.##########.##.#...
#..####.##.###.##########.##.#.#.
#..####.######.##########.##.#.##
#..####.######.#############.#.##
#..####.######.#############.#.##
##.###########.#############.####
##############.#############.####
#################################
```

That picture is Carly Rae Jepsen's "Cut To The Feeling", or rather its address. At `(17, 256)` the same id is the skyline `(256, 34, 185, 235, 42, 182, 126, 225, 191, 160, 142, 234, 232, 74, 113, 243, 102)` - a full-height first column (the decomposition put the touch at `j = 1`), then the 16 bytes of the id, each plus one.

### The even-block codebook: exactly one bit, and a weak checksum

PE 502 counts only even-block castles, `F(w,h)`. Enumerative coding still works: a DP over `(column, last height, touched h yet, block parity)` counts completions and unranks directly into the even-block codebook (verified bijective at `(4,2), (4,3), (5,3)`). At `(34, 16)`:

```
log2 F(34,16) = 134.829548     log2 A(34,16) = 135.829548     difference = 1.000000 bits
```

The parity clause is worth one bit to six decimal places at this size - [[castle-entropy](pages/castle-entropy.md)]'s asymptotic `-1` is already exact for a URL-sized castle. But what does the bit *buy*? A true parity bit detects every single-symbol error. Block parity does not: corrupting one random column of a random `(33, 16)` castle flips the block parity in only **0.438** of 20,000 trials. The block count is the total upward variation `c_1 + sum max(0, c_i - c_{i-1})`, and a single-column edit changes two adjacent rises whose parities cancel more often than not. The one bit of [[castle-sign](pages/castle-sign.md)] is real information, but it is spent on a statistic of the *shape*, not on error detection - a fact for the S8 arc.

---

## Rung 1 - the API response

What Spotify's Web API will actually give you about a track, and how big it is:

- **`GET /v1/tracks/{id}`** - the Track object: album (with images and its own artist list), artists, `available_markets` (deprecated), `disc_number`, `duration_ms`, `explicit`, `external_ids` (ISRC), `external_urls`, `href`, `id`, `is_playable`, `name`, `popularity` (deprecated), `preview_url` (deprecated), `track_number`, `type`, `uri`, `is_local`.[^spot-track]
- **`GET /v1/audio-features/{id}`** (13 numbers: danceability, energy, key, loudness, mode, speechiness, acousticness, instrumentalness, liveness, valence, tempo, duration, time signature) and **`GET /v1/audio-analysis/{id}`** (per-segment pitch and timbre vectors) were **deprecated for new and development-mode apps on 2024-11-27**, along with 30-second `preview_url`s, Recommendations, and Related Artists. Apps that already held extended-quota access kept them.[^spot-deprec] So for a new app the API rungs are the Track object and nothing acoustic; the audio itself (rung 2) has to come from your own playback or your own files.

Sizes, measured on a schema-faithful reconstruction of the docs' example track (not a live response - the field list is the docs', the values are plausible fill):[^exec]

| object | pretty JSON | minified | zlib -9 | castle `h=256` (zlib bytes as columns) |
|---|---|---|---|---|
| Track object, with 185 `available_markets` codes | 6325 B | 3597 B | 1027 B | `w = 1027` |
| Track object, markets stripped | 2249 B | 1749 B | 570 B | `w = 570` |
| audio-features object | 559 B | 486 B | 280 B | `w = 280` |
| audio-features, numbers only, 3-decimal precision | | | **130 bits** | `w = 33, h = 16` |

Two things to notice.

**The audio-features vector is the same castle shape as the URL.** Seven unit-interval floats at three decimals (10 bits each), tempo (18), loudness (12), key (4), mode (1), time signature (3), duration (22) - 130 bits, a `(33, 16)` castle, indistinguishable in size from the 128-bit id. A song's "vibe" as Spotify quantifies it and a song's *address* cost the same number of columns.

**Entropy is relative to the decoder.** The Track object is ~1 KB compressed, but every byte of it is a deterministic function of the 128-bit id *given Spotify's database*. To a decoder with that oracle, the JSON is worth exactly the 17-column castle of rung 0; to a decoder without it, ~1000 columns. This is [[castle-compression](pages/castle-compression.md)]'s Tier 0 / Tier 2 split with the "program" being an HTTP call: parametric relative to the API, generic relative to the bytes. The mixed-radix and even-block codebooks of rung 0 do the JSON just as well - `zlib(track)` starts `(121, 219, 238, 88, 94, 116, 163, 73, ...)` as an `h = 256` skyline, bytes plus one, with the touch rule satisfied or not by luck (a 1027-byte stream fails to contain a 255 with probability `(255/256)^1027 = 1.8%`; the rank/unrank above handles it exactly either way).

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

Measured on a real file, macOS's `Funk.aiff` (2 ch, 48 kHz; converted to 16-bit, left channel used):[^exec]

```
w = 103846 columns (2.163 s)      h = 65536
left channel peaks at +8623 -> peak-normalize gain x3.8000 so that max(c) = 65536
blocks (total rise) = 2,904,534  -> even        area = 3,402,919,201 cells
raw bits w*16 = 1,661,536       log2 A(w,h) = 1,661,535.669       touch cost = 0.33 bits
first 16 columns: 32769 x 16   (the file opens with digital silence: a plateau at mid-height)
```

The castle has 2.9 million blocks in 104 thousand columns - 28 blocks per column, because the waveform's rises are tens of thousands of cells tall. On [[castle-classification-shape](pages/castle-classification-shape.md)]'s axes it is as far from convex, unimodal or symmetric as a castle gets; on [[castle-compression](pages/castle-compression.md)]'s compressibility axis it is where the interesting question lives.

### Compression is the tier ladder

The **raster** of this castle - the `w x h` bit grid - would be `103846 x 65536 = 6.8 Gbit`. The skyline is `1.66 Mbit`. That is the `w(h - log2 h)` gap of [[castle-compression](pages/castle-compression.md)] made physical: the reason audio is stored as samples and not as a picture of the waveform is the castle rules. Below the skyline, the measured ladder on the same file:

| description | bytes | of WAV | castle at `h = 256` | tier |
|---|---|---|---|---|
| WAV 16-bit stereo (two skylines, raw) | 419,480 | 100.0% | `w = 419,480` | 2 - generic |
| gzip -9 of the WAV | 115,880 | 27.6% | `w = 115,880` | 2 - generic, byte statistics only |
| FLAC via `afconvert` | 111,685 | 26.6% | `w = 111,685` | 1 - rule + residual |
| LPC order 8 + Rice residual, own 30-line coder, both channels | 39,827 | 9.5% | `w = 39,827` | 1 - rule + residual |
| AAC 320 kbps | 18,418 | 4.4% | `w = 18,418` | lossy - spectral |
| AAC 160 kbps (Spotify "high" is Vorbis at this rate) | 10,261 | 2.4% | `w = 10,261` | lossy - spectral |

**Tier 1 is linear prediction.** FLAC's core is exactly the wiki's "rule-generated skyline": per block of 4096 samples, fit a linear recurrence `c_i ~ sum a_k c_{i-k}` of order up to 32, quantize the taps, and entropy-code the integer residual with a Rice code.[^flac] That is the least-squares, real-valued cousin of what [[berlekamp-massey](pages/berlekamp-massey.md)] does exactly over a field: find the shortest linear rule that explains the skyline. The own coder in the script does only this (order 8, Q12 taps, per-block optimal Rice parameter, no framing or sync) and reaches 9.5%; order 1 alone reaches 16.8%, order 2 reaches 10.7%, order 12 gains nothing over 8. The measured `afconvert` FLAC at 26.6% sits near gzip and is not explained here; the estimate counts payload bits only.

**Lossy is spectral.** AAC and Vorbis discard the residual altogether and keep quantized MDCT coefficients - the skyline DFT of [[spectral-analysis](pages/spectral-analysis.md)] §3, windowed, with the small bins zeroed by a hearing model. Their output is a bitstream, so as a castle it is again `h = 256`, `w =` bytes; the waveform castle is gone and only a *spectral* description survives. Spotify's stream is Ogg Vorbis at 96, 160 or 320 kbps depending on the quality setting.[^spot-quality]

**A 3:30 track (210 s), as castles:**

| form | size | castle at `h = 256` | castle at `h = 65536` |
|---|---|---|---|
| PCM 44.1 kHz, 16-bit, stereo | 37.04 MB | `w = 37,044,000` | `w = 18,522,000` (two of 9.26M) |
| Ogg Vorbis 320 kbps | 8.40 MB | `w = 8,400,000` | `w = 4,200,000` |
| Ogg Vorbis 160 kbps | 4.20 MB | `w = 4,200,000` | `w = 2,100,000` |
| Ogg Vorbis 96 kbps | 2.52 MB | `w = 2,520,000` | `w = 1,260,000` |
| the URL (rung 0) | 16 B | `w = 17` | `w = 33` at `h = 16` |

Six orders of magnitude between the address and the sound, with the API response in between at `w ~ 10^3`.

---

## Finite fields on the waveform

`65537 = 2^16 + 1` is prime (the largest known Fermat prime), so 16-bit samples are, as they stand, elements of `F_65537` - no reduction, no wasted symbols, one spare element. Three things follow, each executed:[^exec]

1. **Berlekamp-Massey as a Tier-1 detector.** Run [[berlekamp-massey](pages/berlekamp-massey.md)] over `F_65537` on 400 consecutive waveform columns: linear complexity **200**, the maximum `N/2` a length-400 sequence can have. The waveform satisfies no exact linear recurrence - it is Tier 2 in the exact sense even though LPC compresses it 10x in the approximate sense. Run it on a 5-tap LFSR skyline of the same length: complexity **5**. This is the "detector for rule-generated castles" that [[castle-compression](pages/castle-compression.md)] asks for, answered for linear rules, and the gap between 200 and the LPC result is the gap between *exact* and *least-squares* structure.
2. **The NTT is the skyline DFT with no rounding.** `3` generates `F_65537^*`, so `omega = 3^64` is a primitive 1024th root of unity and the number-theoretic transform of a 1024-column block is exact: forward then inverse recovers all 1024 samples bit for bit (verified). The real DFT of the same block peaks at bin 7, about 328 Hz - the bass note. [[spectral-analysis](pages/spectral-analysis.md)] §3 and [[finite-fields](pages/finite-fields.md)] are the same transform over two different fields; over `F_p` it is a bijection with no floating point, over `C` it has the frequency reading.
3. **Encryption is a change of ring.** The [[castle-cryptography](pages/castle-cryptography.md)] series works in `F_p[x]/(Q)` with `Q` a castle's characteristic polynomial. A waveform castle is a very long vector over `F_65537`; multiplying it, block by block, by a fixed element of such a ring is a stream cipher whose key is a castle - and a small one, since `Q` has degree `k+1`. The [[castle-cryptography-round-two](pages/castle-cryptography-round-two.md)] attacks apply verbatim, which is the point of building it.

Also worth knowing: the compact disc's error correction (CIRC) is a pair of Reed-Solomon codes over `GF(2^8)`, so a CD already stores a song as a stream of `h = 256` field symbols with parity - the PE 502 parity bit's serious cousin.[^circ]

---

## Seminar seed: "The Wire, but castles"

A castle universe: every object of a telephone network gets a toy castle, the real-world operations become maps between castles, and the maps compose. Toy versions make the structure visible the way a diagram does - same homomorphisms, different glasses. The pieces below are computed; the seminar would be the walk through them.[^exec]

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

Its skyline DFT has **two atoms**, bins 13 and 27 = 40 - 13, carrying over 99% of the energy - the [[castle-classification-spectrum](pages/castle-classification-spectrum.md)] sparse-spectrum predicate, with the crenellated castle of [[castle-classification-shape](pages/castle-classification-shape.md)] Axis 7 as the special case of a tone at the Nyquist frequency. This is the 2600 Hz that a Cap'n Crunch whistle produced, the tone a long-distance trunk read as "the call has ended, the line is free."[^bluebox]

**Blue-box digits are four-atom castles.** The trunk's own MF signaling used pairs from {700, 900, 1100, 1300, 1500, 1700} Hz; KP (key pulse, "start of number") is 1100 + 1700.[^mf] Both have period 80 samples at 8 kHz, so KP is a width-80 castle whose DFT support is exactly `{11, 17, 63, 69}`. Every MF digit is a castle with a four-atom spectrum; a blue box is a castle generator.

**Detection is one DFT bin.** The Goertzel algorithm - evaluate the DFT at a single bin - is how a switch hears a tone. On the 2600 castle, bin 13 reads 2.042; on a random `(40, 9)` castle, 0.107. A tone detector is a linear functional on the skyline.

**In-band signaling is block parity.** The phreaking vulnerability was that control (tones) and content (voice) travel on the same channel, so content can impersonate control. The castle already has this: the PE 502 parity clause is control information (does this castle count?) computed *from the same skyline* that carries the data. The 0.438 flip rate above is the toy version of the exploit - shape edits that change the data without disturbing the control bit, or the reverse.

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

Phone numbers are `(7, 10)` or `(10, 10)` castles; a contact network is a graph whose vertices are small castles; an organization chart is the cycle-forest form of [[castle-representations](pages/castle-representations.md)] (blocks nested inside blocks, roots on the base); the wiretap is the intercepted skyline stream of rung 2; and the encryption that the toy network runs on is the [[castle-cryptography](pages/castle-cryptography.md)] ring with a castle of large `k` as the key. Small castles for numbers, medium castles for messages, huge castles for the cipher - one object at every scale.

---

## Related Concepts

- [[castle-representations](pages/castle-representations.md)] - the skyline is the encoding used throughout; the cycle-forest form is the org chart.
- [[castle-counting-function](pages/castle-counting-function.md)] - `A(w,h) = h^w - (h-1)^w`, the codebook size and the rank/unrank decomposition.
- [[castle-compression](pages/castle-compression.md)] - the tier ladder that the audio codecs instantiate; the rule-detector question answered for linear rules.
- [[castle-entropy](pages/castle-entropy.md)] - the one-bit parity cost, exact here to six decimals.
- [[castle-sign](pages/castle-sign.md)] - the block count as total upward variation.
- [[berlekamp-massey](pages/berlekamp-massey.md)] - exact linear complexity over `F_65537`; the finite-field cousin of LPC.
- [[finite-fields](pages/finite-fields.md)] - `F_p` and roots of unity; the NTT lives here.
- [[spectral-analysis](pages/spectral-analysis.md)] - the skyline DFT, read as an audio spectrum; the S4 arc this page reverses.
- [[castle-classification-spectrum](pages/castle-classification-spectrum.md)], [[castle-classification-shape](pages/castle-classification-shape.md)] - sparse-spectrum and crenellated castles; the tones.
- [[castle-cryptography](pages/castle-cryptography.md)], [[castle-cryptography-round-two](pages/castle-cryptography-round-two.md)] - the ring the toy network encrypts with, and what breaks it.
- [[castle-snippets](pages/castle-snippets.md)] - `all_castles` and `blocks`, used to verify the bijections.
- [[isospectral-castles](pages/isospectral-castles.md)] - where the S4 direction loses information; the lossless direction here does not.
- [[image-as-castle](pages/image-as-castle.md)] - the same map for JPG and PNG: an image as a stack of row castles or one two-dimensional castle.
- [[castle-steganography](pages/castle-steganography.md)] - hiding a base64 string in castles; the block-parity channel is the S12 covert channel.

## Appearances in Sources

- [[project-euler-502-representations](pages/project-euler-502-representations.md)] - the integer-tuple (skyline) encoding and the block count as a sum of differences, the two facts every rung uses.
- [[project-euler-502-solution](pages/project-euler-502-solution.md)] - the count `A(w,h)` whose decomposition by first full-height column is the ranking scheme.

## Footnotes

[^exec]: Verified by execution (2026-09-19): one Python 3.11 / numpy 1.26 script implementing rank/unrank, the even-block DP, the JSON sizing, the waveform map on `/System/Library/Sounds/Funk.aiff` (converted with `afconvert` to 16-bit WAV, FLAC, and AAC at 160 and 320 kbps), the LPC + Rice estimator, Berlekamp-Massey and the NTT over `F_65537`, and the tone castles. All quoted numbers are the script's printed output. The JSON is a schema-faithful reconstruction of the documented Track object, not a live API response.
[^spot-track]: https://developer.spotify.com/documentation/web-api/reference/get-track §"Get Track" - request example id `11dFghVXANMlKmJXsNCbNl`; response fields album, artists, available_markets (deprecated), disc_number, duration_ms, explicit, external_ids, external_urls, href, id, is_playable, linked_from (deprecated), restrictions, name, popularity (deprecated), preview_url (deprecated, nullable), track_number, type, uri, is_local.
[^spot-deprec]: https://developer.spotify.com/blog/2024-11-27-changes-to-the-web-api (2024-11-27) - "Effective today, new Web API use cases will no longer be able to access or use the following endpoints and functionality": Related Artists, Recommendations, Audio Features, Audio Analysis, Get Featured Playlists, Get Category's Playlists, 30-second preview URLs, and algorithmic / Spotify-owned editorial playlists; "Applications with existing extended mode Web API access that were relying on these endpoints remain unaffected."
[^spot-quality]: https://en.wikipedia.org/wiki/Spotify §"Technical information" [synthesis] - the audio-quality table lists Vorbis 96 kbit/s and 160 kbit/s as standard options and Vorbis 320 kbit/s as a Premium option for the native apps, AAC 128 / 256 kbit/s for the web player, HE-AAC v2 24 kbit/s for the low setting, and FLAC (24-bit / 44.1 kHz) lossless for Premium since September 2025. Spotify's own support page (https://support.spotify.com/us/article/audio-quality/) gives the same tiers as "equivalent to approximately" 24 / 96 / 160 / 320 kbit/s without naming the codec.
[^flac]: https://xiph.org/flac/format.html §"Overview" and §"Subframe" [synthesis] - a FLAC stream is blocks of typically 4096 samples; each subframe is coded as constant, verbatim, fixed predictor, or LPC of order 1-32 with quantized coefficients, followed by the prediction residual encoded with Rice codes in partitions.
[^circ]: https://en.wikipedia.org/wiki/Cross-interleaved_Reed%E2%80%93Solomon_coding §"Overview" [synthesis] - CIRC, the CD's error-correction scheme, is two concatenated Reed-Solomon codes over GF(2^8), (32,28) and (28,24), with interleaving between them.
[^bluebox]: https://en.wikipedia.org/wiki/Blue_box §"Discovery and early use", §"Blue boxing" - "The basic protocol for finding a free line worked by playing a 2600 Hz tone into the line whenever it was not being used"; a phreaker's 2600 Hz tone meant "The called office interpreted this tone as the caller hanging up before the call completed"; Cap'n Crunch cereal boxes included "a small whistle that, by coincidence, generated a 2600 Hz tone when one of the whistle's two holes was covered", and "The phreaker John Draper adopted his nickname 'Captain Crunch' from this whistle."
[^mf]: https://en.wikipedia.org/wiki/Multi-frequency_signaling §"Multi-frequency signals" and the tone table transcluded from https://en.wikipedia.org/wiki/Template:Multi-frequency_signaling_tones [synthesis] - "electronic signals that consist of a combination of two audible frequencies, usually selected from a set of six frequencies"; the table's columns are 700, 900, 1100, 1300, 1500, 1700 Hz, the KP row is marked at 1100 and 1700 Hz, the ST row at 1500 and 1700 Hz; "In R1 MF signaling this address information normally is a KP tone, the numeric digits of the destination number, and an ST tone to indicate the end of the address."
[^wire]: https://en.wikipedia.org/wiki/The_Pager §"Plot summary" - "each pager message consists of a seven-digit phone number and a two-digit identifying tag"; the numbers do not work as dialed, so a masking scheme is suspected, and "The code is ultimately cracked by Prez." The article does not spell out the substitution; the rule stated above (each digit to its opposite across the 5 on the keypad, with 5 and 0 trading places) is the one Prez works out on screen in the episode.
