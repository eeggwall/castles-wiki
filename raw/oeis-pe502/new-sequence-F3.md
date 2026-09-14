# New-sequence draft — `F(w,3)`, even-block castles of height 3

Status: **DRAFT for Charles to reword and submit.** OEIS requires human authorship; the
text below is a checked, correct starting point, not final prose. Verify the exact
field syntax against the [Style Sheet](https://oeis.org/wiki/Style_Sheet) before pasting.
Execution notes (field map, signature format, scope): see SUBMISSION-NOTES.md.

The sequence (index `n` = width `w`, so `a(n) = F(n,3)`):

```
0, 0, 3, 21, 89, 307, 977, 3031, 9321, 28479, 86505, 261615, 788969,
2375119, 7141769, 21457999, 64439145, 193447887, 580605705, 1742342799,
5228079593, 15686337295, 47063203337, 141197992015, 423610748265,
1270865801295, 3812664520713, 11438127787791, 34314651807209,
102944492309647, 308834550687497, 926505799512271, 2779521693371241,
8338573669884879, 25015738189560585, 75047248928849295,
225141815506642409, 675425583959033359, 2026277026754186249,
6078831630016984399, 18236495989561785705, 54709490167709021007,
164128474901174524425, 492385433499617777679, 1477156318091042853353,
4431468989457508051855, 13294407038741272978697, 39883221256961292936655,
119649664052358815097705, 358948992720026361835215
```

## Name (proposed)

> Number of castles (Project Euler Problem 502, "Counting Castles") of width n and
> height exactly 3 having an even number of blocks.

## Data & offset

- `offset` **1** (a(n) = F(n,3), n = 1,2,3,...).  **Default: submit with the two leading
  zeros** a(1) = a(2) = 0 — they are meaningful, not padding: a width-1 or width-2 castle
  of height 3 always has max(c) = 3 blocks (odd), so none has an even block count.
- (Fallback if an editor objects to the leading zeros: trim to `3, 21, 89, ...` with
  `offset 3`.)

## Keywords

`nonn, easy` (all terms nonnegative; linear recurrence).

## Comment (definition, plain English)

> A castle is a stack of unit-height blocks on a grid, in which blocks snap to the grid,
> each block rests on the grid or on a block below (nothing floats), the bottom row is a
> single block spanning the full width n, the maximum height is exactly 3, no two
> neighbouring blocks in the same row touch, and the number of blocks is even. Such a
> castle is determined by its column heights c(1),...,c(n) in {1,2,3} with at least one
> 3; the number of blocks is c(1) + Sum_{i=2..n} max(0, c(i)-c(i-1)). Equivalently, with
> r2 = number of runs of columns of height >= 2 and r3 = number of runs of columns of
> height 3, the number of blocks is 1 + r2 + r3, so it is even iff r2 + r3 is odd.

## Formula

Closed form (with P(k,w) = Sum over (c_1..c_w) in {0..k}^w of (-1)^(c_1 + Sum_{i=2..w} max(0, c_i-c_{i-1}))):

    a(n) = (3^n - 2^n - P(2,n) + P(1,n)) / 2,
    where P(1,n) = Re((1+i)^(n+1)) = A146559(n+1).

P(2,n) is the signed tower count (castle.py: p_signed(2,n)); it satisfies the order-3
recurrence P(2,n) = 3*P(2,n-1) - 4*P(2,n-2) + 4*P(2,n-3), with
P(2,1)=1, P(2,2)=3, P(2,3)=9 (characteristic polynomial (x-2)(x^2-x+2)).

Linear recurrence (holds for n >= 7):

    a(n) = 8*a(n-1) - 27*a(n-2) + 54*a(n-3) - 70*a(n-4) + 56*a(n-5) - 24*a(n-6),
    with a(1)=0, a(2)=0, a(3)=3, a(4)=21, a(5)=89, a(6)=307.

Characteristic polynomial `(x-3)(x-2)(x^2-x+2)(x^2-2x+2)`.

Generating function:

    A(x) = (3*x^3 - 3*x^4 + 2*x^5) / (1 - 8*x + 27*x^2 - 54*x^3 + 70*x^4 - 56*x^5 + 24*x^6).

Complementary relation (with odd(n,3) = odd-block castles of height 3, also new):

    a(n) + odd(n,3) = 3^n - 2^n = A001047(n).

## Program (Python)

Efficient (linear recurrence; reproduces all 50 terms):

```python
def a(n):
    # castles of width n, height 3, even number of blocks (Project Euler 502)
    if n < 3:
        return 0
    v = [0, 0, 3, 21, 89, 307]          # a(1)..a(6)
    while len(v) < n:
        v.append(8*v[-1] - 27*v[-2] + 54*v[-3] - 70*v[-4] + 56*v[-5] - 24*v[-6])
    return v[n-1]

print([a(n) for n in range(1, 21)])
```

Self-contained brute-force check (VERIFICATION ONLY — do not submit; exponential in n),
from the definition:

```python
from itertools import product
def a_brute(n):
    t = 0
    for c in product((1,2,3), repeat=n):
        if 3 not in c:
            continue
        b = c[0] + sum(max(0, c[i]-c[i-1]) for i in range(1, n))
        if b % 2 == 0:
            t += 1
    return t
```

## Crossrefs (Cf.)

- `A038505` (the h=2 analogue: `F(w,2) = A038505(w+1)`).
- `A038503` (`odd(w,2) = A038503(w+1) - 1`).
- `A000225` (total height-2 castles, `2^w - 1`).
- `A001047` (`3^n - 2^n`, total height-3 castles of any parity).
- `A146559` (`Re((1+i)^n)`), `A009545` (`Im((1+i)^n)`).
- The odd-block companion `odd(n,3)` and the taller analogues `F(n,4)`, `F(n,5)`,
  `odd(n,4)`, `odd(n,5)` are (as yet unallocated) sibling sequences.

## Flags for Charles before submitting

1. Rewrite the Name and Comment in your own words and sign
   `- _Firstname Lastname_, Mon D YYYY` (replace the placeholder `_Charles Reid_,
   Sep 05 2026` with the actual account name and date; OEIS forbids AI-authored text).
2. OEIS Style Sheet: use `Sum_{i=2..n}`, `binomial(n,k)`, plain ASCII — never TeX/`\sum`/
   `\binom`, no Mathematica.
3. Confirm the Project Euler link form:
   `Project Euler, <a href="https://projecteuler.net/problem=502">Problem 502: Counting
   castles</a>` (title confirmed "Counting Castles").
4. Offset: default `offset 1` with the two leading zeros (see "Data & offset").
5. New contributors are throttled to a few open drafts — submit the A038505/A038503
   cross-reference first (lower-risk interlinking), then this new sequence.
