---
title: An image as a castle
category: Analyses
summary: Three readings of the 512 x 512 grayscale cameraman image as castles, with heights pixel + 1. (1) Raster - the bytes in row order as one skyline of width 262,144 and height 256. (2) Row castles - each row a skyline of width 512; 163 rows reach height 256, and the others are castles at their own maxima, 176 to 255. (3) Height field - a castle with a two-dimensional base, whose block count is defined as the sum over levels k of the number of 4-connected components of {heights >= k}, the two-dimensional form of the identity blocks(c) = sum_k #(runs of columns with c_i >= k); the cameraman has 171,687 blocks, odd, and area 34,094,639, and the block count is the total length of the 0-dimensional persistence bars of the superlevel-set filtration. A silhouette (topmost dark pixel per column) is a castle of width 512 with heights 290 to 448. Sizes: zlib 64.4%, PNG 53.2%, JPEG quality 90 22.6%, quality 50 8.4% of the raw bytes; the height field takes 2.1 Mbit against 67 Mbit for the 512 x 512 x 256 voxel raster, a factor h/log2 h = 32.
tags: [analysis, castle, encoding, image, png, jpeg, height-field, higher-dimensional, compression, persistence, implementation]
sources: [project-euler-502-representations]
created: 2026-09-19
updated: 2026-10-16
---

# An image as a castle

[[song-as-castle](pages/song-as-castle.md)] reads a sound recording as one skyline. A grayscale image is a stack of skylines, or one castle with a two-dimensional base. Every number below is computed on the standard 512 x 512 grayscale "cameraman" test image with heights `pixel + 1`, from 1 to 256.[^exec]

## Three readings

**1. Raster.** Read the pixels in row order and add one: the image is a single skyline of width `w = 262,144` and height `h = 256`, since the image contains a pixel of value 255. This reading uses no structure of the picture.

**2. Row castles.** Each row is a skyline of width 512. Of the 512 rows, 163 contain a pixel of value 255 and are castles of height 256; the others reach heights 176 to 255 and are castles of their own maximum height. Any statistic of a castle, such as the block count ([[castle-sign](pages/castle-sign.md)]) or the skyline DFT ([[spectral-analysis](pages/spectral-analysis.md)]), becomes a statistic of a row. [[castle-steganography](pages/castle-steganography.md)] and [[castle-phone-line](pages/castle-phone-line.md)] use this reading.

**3. Height field.** The heights over the 512 x 512 base form a **two-dimensional castle**: a stack of unit cubes with no overhangs, every base cell covered, and some column at height 256. Its block count comes from the one-dimensional identity

```
blocks(c)  =  c_1 + Σ_{i≥2} max(0, c_i − c_{i−1})  =  Σ_{k=1}^{h} #(maximal runs of columns with c_i ≥ k),
```

which holds because the blocks in row `k` of a castle are, by definition, the maximal runs of columns with `c_i ≥ k`. The right-hand side uses only connectivity, so it defines the block count of a two-dimensional castle with heights `g`:

```
blocks(g)  =  Σ_{k=1}^{256}  #(4-connected components of {(x, y) : g(x, y) ≥ k}).
```

The cameraman has 171,687 blocks, an odd number, and area 34,094,639 cells. The number of components of `{g ≥ k}` is the number of 0-dimensional persistence bars of the superlevel-set filtration alive at level `k`, so the block count is the total length of those bars, measured in levels.[^ph]

## The silhouette

Threshold the image at its median pixel value, 152, and for each column take the topmost dark pixel; its distance from the bottom edge, `512 − row`, is the column's height. The result is a castle of width 512 with heights from 290 to 448, the top of the photographer and the tripod against the sky. Every 16th column, starting at column 0, with heights scaled by `10/448` and rounded:

```
skyline (7, 7, 7, 7, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 10, 9, 8, 7, 8, 8, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7)

...........#####................
.......##########...............
....##############.##...........
################################
################################
################################
################################
################################
################################
################################
```

The silhouette keeps one number per column of the image.

## Compression

| form | bytes | of raw | as a castle at `h = 256` | method |
|---|---|---|---|---|
| raw 512 x 512 grayscale | 262,144 | 100.0% | `w = 262,144` | none |
| zlib level 9 of the raw bytes | 168,858 | 64.4% | `w = 168,858` | DEFLATE |
| PNG (optimized) | 139,500 | 53.2% | `w = 139,500` | row filters, then DEFLATE |
| JPEG quality 90 | 59,366 | 22.6% | `w = 59,366` | DCT and quantization (lossy) |
| JPEG quality 50 | 22,050 | 8.4% | `w = 22,050` | DCT and quantization (lossy) |

PNG filters each row before compressing it with DEFLATE, the algorithm zlib implements: the filters Sub, Up, Average and Paeth predict each byte from the byte to its left, the byte above, their average, or whichever of left, above and upper-left the Paeth rule picks, and DEFLATE compresses the prediction errors.[^png] FLAC's linear prediction plays the same part for audio on [[song-as-castle](pages/song-as-castle.md)]. JPEG applies the discrete cosine transform to 8 x 8 blocks and quantizes the coefficients.[^jpeg]

The height field takes `512 · 512 · log₂ 256 = 2,097,152` bits, 2.1 Mbit; the voxel raster of the same two-dimensional castle, one bit per cell of the `512 x 512 x 256` box, takes 67,108,864 bits, 67 Mbit, a factor `256 / log₂ 256 = 32`. [[castle-compression](pages/castle-compression.md)] makes the same comparison for one-dimensional castles: `log₂ A(w, h) ≤ w log₂ h` bits against `w h` for the raster.

## Related Concepts

- [[song-as-castle](pages/song-as-castle.md)] - the same readings for audio: one skyline instead of a stack.
- [[castle-steganography](pages/castle-steganography.md)] - a message hidden in the row castles of this image.
- [[castle-phone-line](pages/castle-phone-line.md)] - the row castles sent over a simulated telephone line.
- [[castle-compression](pages/castle-compression.md)] - the description tiers of a castle and the comparison of `log₂ A(w, h)` bits with the `w h` bits of the raster.
- [[castle-sign](pages/castle-sign.md)] - the block count as total ascent.
- [[castle-representations](pages/castle-representations.md)] - the skyline encoding.
- [[castle-snippets](pages/castle-snippets.md)] - the `blocks` predicate.
- [[spectral-analysis](pages/spectral-analysis.md)] - the skyline DFT, applied row by row.
- [[castle-entropy](pages/castle-entropy.md)] - `log₂ A(w, h) ≈ w log₂ h` bits per castle of width `w` and height `h`.

## Appearances in Sources

- [[project-euler-502-representations](pages/project-euler-502-representations.md)] - the integer-tuple encoding and the block count from the differences of consecutive heights, which the level sum rewrites.

## Footnotes

[^exec]: Verified by execution (2026-10-16), on the cameraman image of scikit-image's data files (`camera.png`, which `skimage.data.camera()` returns): row maxima, the two-dimensional block count with `scipy.ndimage.label` (4-connectivity) at each of the 256 levels, the one-dimensional identity on 200 random skylines, the silhouette and its sampled skyline, zlib level 9, and PNG (optimized) and JPEG sizes from Pillow 11.3; Python 3.11 with NumPy 1.26 and Pillow, and Python 3.14 with SciPy 1.17 for `ndimage`.
[^ph]: https://en.wikipedia.org/wiki/Persistent_homology §"Definition" [synthesis] - persistent homology tracks the homology classes of a filtration (a nested sequence of spaces, here the superlevel sets `{g >= k}` as `k` decreases); the 0-dimensional classes are connected components, and each component's lifetime across the filtration is one bar of the barcode. The sum over levels of the component count is the sum of the bar lengths.
[^png]: https://www.w3.org/TR/png/#9Filters §"9. Filtering" [synthesis] - PNG filter type 0 to 4 are None, Sub, Up, Average, Paeth; each predicts a byte from the corresponding byte to the left, above, their average, or the Paeth predictor of the three neighbors, and the filtered bytes are what DEFLATE compresses.
[^jpeg]: https://en.wikipedia.org/wiki/JPEG §"JPEG codec example" [synthesis] - the encoder splits the image into 8x8 blocks, applies the discrete cosine transform, quantizes the coefficients with a quality-dependent table, and entropy-codes the result.
