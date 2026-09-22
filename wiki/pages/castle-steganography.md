---
title: Castle steganography - hiding a base64 string in a castle
category: Analyses
summary: Two ways to hide an arbitrary base64 string inside castles, both executed and round-tripped on the standard cameraman image read as 512 row castles. The payload is a 56-character base64 string (336 bits, decoding to "castles are skylines, skylines are numbers"); as its own castle it is one column per symbol at h=64. Channel A, least-significant bit of the column heights - one bit per column, never touching the peak column or the floor so the cover stays a castle at the same h; all 336 bits fit in one 512-wide row, 168 columns move by one cell, recovery exact; capacity 43,690 base64 characters per 512x512 image. Channel B, block parity - one bit per castle, set by a +/-1 change at a strict local extremum, which provably changes the block count by exactly one; 336 bits in 336 rows, 161 rows needed a change (175 already had the right parity), 161 pixels changed by one, PSNR 80.2 dB, recovery exact, 336/336 after a PNG round trip and 175/336 (chance) after JPEG q95; the block parity of untouched rows is a coin flip (249 odd / 263 even), so the embedding does not shift the distribution. Both are textbook LSB-style channels in castle clothing; the castle-specific fact is that channel B's capacity is exactly the one bit the even-block clause is worth on castle-entropy, and that its cost is provably one cell per flipped castle.
tags: [analysis, castle, steganography, base64, lsb, parity, block-parity, image, covert-channel, implementation, seminar]
sources: [project-euler-502-representations]
created: 2026-09-19
updated: 2026-09-19
---

# Castle steganography - hiding a base64 string in a castle

The question: given an arbitrary base64 string, hide it in a castle so that the castle still looks like a castle and the string comes back exactly. Two channels, both executed on 2026-09-19 with the standard 512x512 cameraman image ([[image-as-castle](pages/image-as-castle.md)]) read as 512 row castles of width 512.[^exec] Neither channel is new as steganography - both are least-significant-bit ideas; the castle content is in what the constraints cost and what the parity clause turns out to be worth.

## The payload

```
secret  = "Y2FzdGxlcyBhcmUgc2t5bGluZXMsIHNreWxpbmVzIGFyZSBudW1iZXJz"
          56 base64 characters = 336 bits  ->  b"castles are skylines, skylines are numbers"
```

A base64 string is already a castle: one column per character, height = alphabet index + 1, `h = 64`. The secret is the width-56 skyline `(25, 55, 6, 52, 30, 7, 50, 38, 29, 51, 2, 34, ...)`. It contains no `/` (index 63), so no column reaches 64; a leading sentinel column of height 64 makes it a valid castle at the cost of one column. (The exact rank/unrank of [[song-as-castle](pages/song-as-castle.md)] avoids even that column.) The bits to hide are the 6 bits of each symbol, most significant first.

## Channel A - the least significant bit of a column

Cover: one row of the image as a skyline `c`, heights `1..h` where `h` is the row's own maximum (row 100 has `h = 215`). Write one payload bit into the low bit of each column height, skipping three kinds of column so that the result is still a castle at the same `h`: the peak column (moving it could lower the maximum), the floor (height 1 could drop to 0), and any column at `h - 1` (which could rise to become a second peak). Extraction reads the low bits back at the same positions.

```
336 of 336 bits in one width-512 row castle (h = 215)
168 columns changed, each by one cell           still a castle at h = 215: True
recovered exactly: True
capacity: 1 bit per column -> 262,144 bits = 43,690 base64 characters per 512x512 image
```

Half the columns change (a random bit agrees with the existing low bit half the time), each by one grey level. This is ordinary LSB steganography with castle vocabulary; its one castle-specific feature is the skip rule, which keeps the touch rule and the bottom row intact.

## Channel B - the block parity

The even-block clause of PE 502 is one bit per castle ([[castle-entropy](pages/castle-entropy.md)] prices it at exactly one bit). Channel B spends that bit on a message: **one castle carries one bit, its block parity.**

Setting the parity needs a single-cell edit that changes the block count by exactly one. With `blocks(c) = c_1 + sum_i max(0, c_i - c_{i-1})` ([[castle-sign](pages/castle-sign.md)]):

- **Raise a strict local maximum by one** (`c_{i-1} < c_i > c_{i+1}`): the rise into column `i` grows by one, the rise out of it stays zero. Block count `+1`.
- **Lower a strict local minimum by one** (`c_{i-1} > c_i < c_{i+1}`): the rise into `i` stays zero, the rise into `i+1` grows by one. Block count `+1`.

Either edit flips the parity with certainty and moves one cell; the constraints are only that a raised maximum stays below `h` and a lowered minimum stays at least 1. Compare the 44% flip rate of a *random* single-column edit measured on [[song-as-castle](pages/song-as-castle.md)] - the channel works because the edit is chosen, not random.

Embedding the 336 bits as the parities of rows 0..335:

```
161 rows needed a +/-1 change of one cell; 175 already had the right parity
pixels changed: 161 of 262,144, all by exactly 1        PSNR = 80.2 dB
recovered exactly: True
after a PNG round trip:      336 / 336 bits
after a JPEG q95 round trip: 175 / 336 bits   (chance is 168)
block parity of the 512 untouched rows: 249 odd, 263 even
```

Capacity is one bit per castle: 512 bits = 85 base64 characters per 512x512 image, about 1/512 of channel A. In exchange the edit count is minimal (about half the castles need one cell each), and the statistic being written is one a natural image already draws at random - untouched rows split 249/263 - so the embedding leaves no first-order trace in the parity distribution. Both channels survive lossless recoding (PNG) and neither survives JPEG, whose quantization re-randomizes low bits and block counts alike.

## Side by side

| | channel A - LSB of heights | channel B - block parity |
|---|---|---|
| capacity | 1 bit per **column** | 1 bit per **castle** |
| cells moved per bit | 0.5 on average | 0.5 on average, but per castle not per column |
| castle rules | kept by skipping peak, floor, `h-1` | kept by choosing an interior extremum |
| what the warden sees | low-bit statistics change | parity distribution unchanged (coin flip before and after) |
| survives PNG / JPEG | yes / no | yes / no |
| castle-specific content | the skip rule | the one bit of the parity clause, and the one-cell flip lemma |

## Where this sits

The S8 arc asks what the even-block bit *is*; here it is a covert channel of capacity exactly one bit per castle, written with one cell. The S12 seed on [[song-as-castle](pages/song-as-castle.md)] ("The Wire, but castles") gets its steganography from this page: a wiretap that reads skylines sees a picture, the receiver counting blocks sees a message. The next step is the obvious one - a warden that counts blocks: is there a second-order statistic (parity of adjacent rows, block count distribution) that channel B disturbs? That is open.

## Related Concepts

- [[image-as-castle](pages/image-as-castle.md)] - the cover: an image as 512 row castles.
- [[song-as-castle](pages/song-as-castle.md)] - the rank/unrank bijection, the 44% random-flip figure, and the S12 seminar seed.
- [[castle-entropy](pages/castle-entropy.md)] - the parity clause is one bit; channel B is that bit as capacity.
- [[castle-sign](pages/castle-sign.md)] - the block count formula the flip lemma is read off.
- [[castle-compression](pages/castle-compression.md)] - why lossless codecs preserve both channels and lossy ones destroy them.
- [[castle-conditional-entropy](pages/castle-conditional-entropy.md)] - the one bit this channel monetizes is the same bit that separates H(B) from H(N); the parity-clause thread.
- [[castle-snippets](pages/castle-snippets.md)] - the `blocks` predicate.

## Appearances in Sources

- [[project-euler-502-representations](pages/project-euler-502-representations.md)] - the block count as the sum of positive first differences, which makes the one-cell flip lemma a two-line check.

## Footnotes

[^exec]: Verified by execution (2026-09-19): Python 3 with numpy, scipy, Pillow and scikit-image under `uv`; the cover is `skimage.data.camera()`. Embedding and extraction were run and compared bit for bit; PNG and JPEG round trips used Pillow's encoders. All quoted numbers are the script's printed output.
