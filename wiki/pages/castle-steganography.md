---
title: Castle steganography - hiding a base64 string in a castle
category: Analyses
summary: Two channels that hide a base64 string in castles, run on the cameraman image read as 512 row castles. The payload is a 56-character base64 string (336 bits). Channel A writes one bit into the lowest bit of each usable column height, skipping the heights whose low-bit pair contains 1 or the row's maximum h, so the row stays a castle at h and the extractor finds the same columns; all 336 bits fit in row 100, 168 columns move by one, and the image holds 257,919 bits. Channel B writes one bit per castle, its block parity, by raising a strict interior local maximum below h or lowering a strict interior local minimum above 1, which changes the block count by exactly one; 161 of rows 0 to 335 need one changed pixel, PSNR 80.2 dB, recovery exact, 336 of 336 bits after PNG and 175 after JPEG quality 95. The untouched rows have 249 odd and 263 even block counts.
tags: [analysis, castle, steganography, base64, lsb, parity, block-parity, image, implementation]
sources: [project-euler-502-representations]
created: 2026-09-19
updated: 2026-10-16
---

# Castle steganography - hiding a base64 string in a castle

Given a base64 string, hide it in castles so that every castle stays a castle and the string comes back exactly. The cover is the 512 x 512 grayscale cameraman image read as 512 row castles of width 512, with heights `pixel + 1` and each row a castle at its own maximum `h` ([[image-as-castle](pages/image-as-castle.md)]).[^exec] Channel A writes one bit per column, channel B one bit per castle.

## The payload

```
secret  = "Y2FzdGxlcyBhcmUgc2t5bGluZXMsIHNreWxpbmVzIGFyZSBudW1iZXJz"
          56 base64 characters = 336 bits  ->  b"castles are skylines, skylines are numbers"
```

The bits to hide are the 6 bits of each character's index in the base64 alphabet, most significant first; 164 of the 336 bits are 1. The string is itself a skyline of width 56 with heights `index + 1`: `(25, 55, 6, 52, 30, 7, 50, 38, 29, 51, 2, 34, …)`, of height 58, since it contains no character of index above 57.

## Channel A - the lowest bit of a column height

Write a payload bit `b` into a column of height `c` by setting the lowest bit of `c` to `b`, which moves `c` by at most one, within its low-bit pair `{2m, 2m + 1}`. Two kinds of column are skipped:

- columns of height 1, which could drop to 0, and
- columns in the low-bit pair of the row's maximum `h`, which could move to `h + 1` or remove the only column of height `h`. For odd `h` that pair is `{h − 1, h}`; for even `h` it is `{h, h + 1}`, so only the columns of height `h` are skipped.

A written column stays in its low-bit pair, so the set of skipped columns is the same before and after writing, the row keeps the maximum `h`, and the extractor finds the same columns and reads their lowest bits.

In row 100, `h = 215`, odd, so the skipped heights are 1, 214 and 215, and 455 of the 512 columns are usable:

```
336 of 336 bits in row 100 (h = 215)
168 columns changed, each by one cell           still a castle at h = 215: True
recovered exactly: True
usable columns in the whole image: 257,919 -> 42,986 base64 characters
```

A column changes when its lowest bit differs from the payload bit, here in 168 of 336 columns.

## Channel B - the block parity

The block count of a skyline is `blocks(c) = Σ_i max(0, c_i − c_{i−1})` with `c_0 = 0` ([[castle-sign](pages/castle-sign.md)]). Channel B writes one bit into each castle, the parity of its block count. When the parity is already the payload bit, nothing changes; otherwise one cell is moved:

- **Raise a strict local maximum by one** (`c_{i−1} < c_i > c_{i+1}`, `1 < i < w`, `c_i < h`): the rise into column `i` grows by one and the rise out of it stays zero, so the block count grows by one.
- **Lower a strict local minimum by one** (`c_{i−1} > c_i < c_{i+1}`, `1 < i < w`, `c_i ≥ 2`): the rise into column `i` stays zero and the rise into column `i + 1` grows by one, so the block count grows by one.

Either edit changes the parity, keeps the heights between 1 and `h`, and moves one cell ([[one-bit-seminar](pages/one-bit-seminar.md)], the section *Stop 3*). The edit is chosen: a uniform one-column edit of a uniform castle of width 17 and height 16 changes the parity with probability 0.4272 ([[song-as-castle](pages/song-as-castle.md)]). The extractor reads each row's block parity.

The 336 bits written as the parities of rows 0 to 335, at the first strict interior local extremum of each row that needs a change:

```
161 rows needed a change of one cell; 175 already had the right parity
pixels changed: 161 of 262,144, each by 1        PSNR = 80.2 dB
recovered exactly: True
after a PNG round trip:          336 / 336 bits
after a JPEG quality-95 round trip: 175 / 336 bits
block parity of the 512 rows before writing: 249 odd, 263 even
```

The capacity is one bit per castle, 512 bits or 85 base64 characters per 512 x 512 image. After writing, the row parities are the payload bits. PNG reproduces every pixel, so both channels survive it; JPEG changes low bits and block counts, and channel B keeps 175 of 336 bits.

## Side by side

| | channel A - lowest bit of a height | channel B - block parity |
|---|---|---|
| capacity | 1 bit per usable column (257,919 in the image) | 1 bit per castle (512 in the image) |
| cells moved | 168 for 336 bits in row 100 | 161 for 336 bits in rows 0 to 335 |
| how the castle is kept | skip height 1 and the low-bit pair of `h` | edit a strict interior local extremum |
| PNG / JPEG quality 95 | survives / does not | 336 of 336 / 175 of 336 |

## Related Concepts

- [[image-as-castle](pages/image-as-castle.md)] - the cover image as 512 row castles.
- [[castle-phone-line](pages/castle-phone-line.md)] - the two channels sent over a simulated telephone line; the block parity does not survive it, and a height code with spacing 6 does.
- [[song-as-castle](pages/song-as-castle.md)] - the rank/unrank bijection of castles and the parity-change probability of a uniform one-column edit.
- [[castle-entropy](pages/castle-entropy.md)] - the even-block condition costs one bit up to `log₂(1 + S/A)`; channel B writes that bit.
- [[castle-sign](pages/castle-sign.md)] - the block count as total ascent.
- [[castle-conditional-entropy](pages/castle-conditional-entropy.md)] - the entropies of the block count and the area of the even-block castles; on that ensemble the block count is even, so the parity that channel B writes is fixed.
- [[castle-snippets](pages/castle-snippets.md)] - the `blocks` predicate.
- [[one-bit-seminar](pages/one-bit-seminar.md)] - Stop 3, the one-cell edits that change the parity, and Stop 5, the parity as a channel.

## Appearances in Sources

- [[project-euler-502-representations](pages/project-euler-502-representations.md)] - the block count read from the differences of consecutive column heights.

## Footnotes

[^exec]: Verified by execution (Python 3.11 with NumPy 1.26 and Pillow 11.3, 2026-10-16), on the cameraman image of scikit-image's data files (`camera.png`, which `skimage.data.camera()` returns). Both channels written and read back bit for bit; the image-wide capacity of channel A counted over all 512 rows with the skip rule above; PSNR from the mean squared pixel change; PNG and JPEG round trips with Pillow's encoders.
