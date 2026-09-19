---
title: An image as a castle
category: Analyses
summary: JPG and PNG to castle, three readings executed on the standard 512x512 cameraman test image (skimage.data.camera). (1) Raster - the bytes as one h=256 skyline, w=262144. (2) Row castles - each of the 512 rows is a width-512 skyline; 163 rows already have a 255 and are castles at h=256 as they stand, the rest need a peak-normalize or their own h, exactly as a waveform does. (3) Height field - the grayscale image is a two-dimensional castle, heights 1..256 over a 512x512 base, and the block count generalizes: in 1D, blocks(c) equals the sum over levels k of the number of runs of columns with c >= k (verified on 200 random skylines), so in 2D blocks = sum over 256 levels of the number of 4-connected components of the superlevel set; the cameraman has 171,687 blocks, odd. This is a concrete definition for the open "higher-dimensional castles" item and coincides with total 0-dimensional superlevel-set persistence. A silhouette reading (top dark pixel per column against the bright sky) gives a PE 502 castle of width 512 with heights 290..448 - a picture of a shape is a castle. Compression ladder measured: PNG 53.2%, JPEG q90 22.6%, JPEG q50 8.4% of raw; PNG's filters are order-1 predictors (Tier 1), JPEG's DCT is the spectral tier; the height-field skyline is 32x smaller than the voxel raster (2.1 Mbit vs 67 Mbit).
tags: [analysis, castle, encoding, image, png, jpeg, height-field, higher-dimensional, compression, persistence, implementation]
sources: [project-euler-502-representations]
created: 2026-09-19
updated: 2026-09-19
---

# An image as a castle

Companion to [[song-as-castle](pages/song-as-castle.md)], which does the same for audio. An audio signal is one skyline; an image is a stack of them, or one two-dimensional castle. All numbers below were executed on the standard 512x512 grayscale "cameraman" test image, `skimage.data.camera()`, on 2026-09-19.[^exec]

## Three readings

**1. Raster.** Read the pixel bytes in row-major order, add one, and the image is a single skyline: `w = 262144`, `h = 256`. The cameraman contains a 255, so the touch rule holds as it stands. This is the generic reading, Tier 2 on [[castle-compression](pages/castle-compression.md)]'s ladder, and it says nothing about the picture.

**2. Row castles.** Each row is a width-512 skyline with heights `pixel + 1`. Of the 512 rows, 163 contain a 255 and are castles at `h = 256` as they stand; the others have maxima from 175 to 254 and are castles only at their own `h`, or after a per-row peak-normalize - the same bookkeeping [[song-as-castle](pages/song-as-castle.md)] does for a waveform that does not reach full scale. A grayscale image is 512 castles of width 512, and any per-castle statistic ([[castle-sign](pages/castle-sign.md)]'s block count, the skyline DFT of [[spectral-analysis](pages/spectral-analysis.md)]) becomes a per-row feature. [[castle-steganography](pages/castle-steganography.md)] uses this reading.

**3. Height field - the two-dimensional castle.** Take heights `1..256` over the 512x512 base. The bottom layer is full, the maximum is reached, and the object is a stack of unit cubes with no overhangs - a castle with a 2D base. The open item "higher-dimensional castles" on IDEAS (S11) asks what the block count should be. The 1D count answers it. On a skyline,

```
blocks(c) = c_1 + sum_i max(0, c_i - c_{i-1})  =  sum_{k=1}^{h}  #(maximal runs of columns with c_i >= k)
```

because each block is a unit-height horizontal run at some level `k`, and the runs at level `k` are exactly the connected components of `{i : c_i >= k}`. Verified on 200 random skylines against the `blocks` predicate of [[castle-snippets](pages/castle-snippets.md)]. The right-hand side needs no ordering of the base, so it *is* the 2D definition:

```
blocks(image) = sum_{k=1}^{256}  #(4-connected components of {(x,y) : g(x,y) + 1 >= k})
```

For the cameraman: **171,687 blocks, odd**, area 34,094,639 cells. In the language of topological data analysis this is the total 0-dimensional persistence of the superlevel-set filtration - every block is one unit of one bar's length - so the PE 502 parity of an image is the parity of its total persistence.[^ph] A one-line `scipy.ndimage.label` per level computes it.

## The silhouette: a picture of a shape is a castle

Threshold at the median, and for each column take the topmost dark pixel (the cameraman and his tripod are dark against a bright sky). The result is a width-512 skyline with heights from 290 to 448 - a PE 502 castle read off a photograph. Downsampled to 32 columns:

```
skyline (8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 9, 8, 9, 9, 8, 7, 7, 7, 7, 7, 8, 7, 8, 8, 8)

..........#######...............
.....#############.##...........
######################.....#.###
################################
################################
################################
################################
################################
################################
################################
```

Head and shoulders, then the ground. This reading is lossy (it keeps one number per column) and it is the one that makes "castle" literal: any skyline photograph, any city or mountain silhouette, is a castle in exactly the PE 502 sense, and its rank under the bijection of [[song-as-castle](pages/song-as-castle.md)] is a number.

## Compression: the same ladder as audio

| form | bytes | of raw | castle at `h = 256` | tier |
|---|---|---|---|---|
| raw 512x512 grayscale | 262,144 | 100.0% | `w = 262,144` | 2 - generic |
| zlib -9 of the raw bytes | 168,858 | 64.4% | `w = 168,858` | 2 - byte statistics |
| PNG (optimized) | 139,500 | 53.2% | `w = 139,500` | 1 - predict + entropy-code |
| JPEG quality 90 | 59,366 | 22.6% | `w = 59,366` | lossy - spectral |
| JPEG quality 50 | 22,050 | 8.4% | `w = 22,050` | lossy - spectral |

PNG beats zlib on the same bytes because of its per-row filters - Sub, Up, Average, Paeth - which predict each byte from its left and upper neighbours before DEFLATE runs.[^png] Those are order-1 linear predictors in two directions: the image version of FLAC's LPC on [[song-as-castle](pages/song-as-castle.md)], Tier 1 on the ladder. JPEG replaces the residual with quantized 8x8 DCT coefficients, the spectral tier.[^jpeg] And the raster gap of [[castle-compression](pages/castle-compression.md)] is again the biggest step of all: the height-field skyline is 2.1 Mbit, the `512 x 512 x 256` voxel raster of the same 2D castle would be 67 Mbit, a factor of 32 = `h / log2 h`.

## Related Concepts

- [[song-as-castle](pages/song-as-castle.md)] - the audio version; same map, one skyline instead of a stack.
- [[castle-steganography](pages/castle-steganography.md)] - hiding a string in the row castles of this image.
- [[castle-compression](pages/castle-compression.md)] - the tier ladder the codecs instantiate.
- [[castle-sign](pages/castle-sign.md)] - the block count whose level-sum form generalizes to 2D.
- [[castle-representations](pages/castle-representations.md)] - the skyline encoding.
- [[castle-snippets](pages/castle-snippets.md)] - the `blocks` predicate used for the 1D verification.
- [[spectral-analysis](pages/spectral-analysis.md)] - the skyline DFT, per row.

## Appearances in Sources

- [[project-euler-502-representations](pages/project-euler-502-representations.md)] - the integer-tuple encoding and the block count as a sum of positive differences, which the level-sum identity rewrites.

## Footnotes

[^exec]: Verified by execution (2026-09-19): Python 3 with numpy, scipy 1.15 (`ndimage.label`), Pillow 11 (PNG and JPEG encoders), scikit-image (`data.camera()`), run under `uv`. All quoted numbers are the script's printed output.
[^ph]: https://en.wikipedia.org/wiki/Persistent_homology §"Definition" [synthesis] - persistent homology tracks the homology classes of a filtration (a nested sequence of spaces, here the superlevel sets `{g >= k}` as `k` decreases); the 0-dimensional classes are connected components, and each component's lifetime across the filtration is one bar of the barcode. The sum over levels of the component count is the sum of the bar lengths.
[^png]: https://www.w3.org/TR/png/#9Filters §"9. Filtering" [synthesis] - PNG filter type 0 to 4 are None, Sub, Up, Average, Paeth; each predicts a byte from the corresponding byte to the left, above, their average, or the Paeth predictor of the three neighbours, and the filtered bytes are what DEFLATE compresses.
[^jpeg]: https://en.wikipedia.org/wiki/JPEG §"JPEG codec example" [synthesis] - the encoder splits the image into 8x8 blocks, applies the discrete cosine transform, quantizes the coefficients with a quality-dependent table, and entropy-codes the result.
