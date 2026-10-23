# New-sequence draft — `F(w,3)`, even-block castles of height 3

Status: DRAFT for Charles to submit. Searched 2026-10-23: no OEIS match for the terms, for the
odd-block companion `1, 5, 16, 44, 122, 358, 1082, 3274`, or for the signed difference
`1, 5, 13, 23, 33, 51, 105, 243` (even minus odd, negated).
Execution notes (field map, signature format, scope): see SUBMISSION-NOTES.md.

A standalone entry: the formulas below need no array. If the `F(w,h)` array is drafted later
(OEIS.md, stage 3), it says "Row 3 is A______"; if an editor asks for the array first, as
Michel Marcus asked on A001263, that item is the answer.

The sequence (index `n` = width `w`, so `a(n) = F(n,3)`), 50 terms:

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

## Fields

**NAME**

```
Number of castle polyominoes of width n and height 3 with an even number of blocks.
```

**DATA** (the first 30 terms, 255 characters):

```
0,0,3,21,89,307,977,3031,9321,28479,86505,261615,788969,2375119,7141769,21457999,64439145,193447887,580605705,1742342799,5228079593,15686337295,47063203337,141197992015,423610748265,1270865801295,3812664520713,11438127787791,34314651807209,102944492309647
```

**OFFSET** `1,3`. The leading zeros are counts: a castle of width 1 or 2 and height 3 has 3
blocks, the height of its tallest column.

**COMMENTS**

```
A castle (Project Euler, Problem 502: Counting Castles) is a stack of unit blocks on a grid, whose bottom row is a single block of length n, whose higher blocks have height 1 and rest on the blocks below without overhang, and in which two neighboring blocks of the same row are separated by a gap; its height is its number of rows. If the columns that reach height 2 form r runs and the columns that reach height 3 form s runs, the number of blocks is 1 + r + s, so an even number of blocks means r + s is odd.
The castles of width n and height 3 number A001047(n) = 3^n - 2^n, so A001047(n) - a(n) of them have an odd number of blocks.
```

**LINKS**

```
Project Euler, <a href="https://projecteuler.net/problem=502">Problem 502: Counting Castles</a>.
<a href="/index/Rec#order_06">Index entries for linear recurrences with constant coefficients</a>, signature (8,-27,54,-70,56,-24).
```

**FORMULA**

```
G.f.: x^3*(3 - 3*x + 2*x^2)/((1 - 2*x)*(1 - 3*x)*(1 - x + 2*x^2)*(1 - 2*x + 2*x^2)).
a(n) = 8*a(n-1) - 27*a(n-2) + 54*a(n-3) - 70*a(n-4) + 56*a(n-5) - 24*a(n-6) for n >= 7.
a(n) = (3^n - 2^(n+1) + A146559(n+1) + A107920(n))/2.
```

**EXAMPLE**

```
a(3) = 3: the castles of width 3 and height 3 with an even number of blocks have column heights (2,1,3), (3,1,2) and (3,2,3), each with 4 blocks.
```

**PROG** (rename `a` to the assigned A-number):

```
(Python)
def a(n):
    # states: (height of the last column, parity of the number of blocks, height 3 reached)
    d = {(h, h % 2, h == 3): 1 for h in (1, 2, 3)}
    for _ in range(n - 1):
        e = {}
        for (h, p, t), c in d.items():
            for g in (1, 2, 3):
                k = (g, (p + max(0, g - h)) % 2, t or g == 3)
                e[k] = e.get(k, 0) + c
        d = e
    return sum(c for (h, p, t), c in d.items() if t and p == 0) # _Chaz Reid_, Mon DD YYYY
```

**CROSSREFS**

```
Cf. A001047, A038505, A107920, A146559.
```

**KEYWORDS** `nonn,easy`

## Derivation (not for submission)

A castle of width `n` and height 3 is a column-height word `c(1), ..., c(n)` in `{1, 2, 3}` with
at least one 3, and its number of blocks is `c(1) + Sum_{i=2..n} max(0, c(i) - c(i-1))`. The
castle counting formula at `h = 3` gives

    a(n) = (3^n - 2^n - P(2,n) + P(1,n)) / 2,

with the signed tower counts `P(k,n) = Sum over (c_1..c_n) in {0..k}^n of
(-1)^(c_1 + Sum_{i=2..n} max(0, c_i - c_{i-1}))`. `P(1,n) = Re((1+i)^(n+1)) = A146559(n+1)`, and
`P(2,n)` satisfies `P(2,n) = 3*P(2,n-1) - 4*P(2,n-2) + 4*P(2,n-3)` with `P(2,1..3) = 1, 3, 9`
(characteristic polynomial `(x-2)(x^2-x+2)`); its partial fractions give
`P(2,n) = 2^n - A107920(n)`, with A107920 the Lucas and Lehmer numbers with parameters
`(1 +- sqrt(-7))/2`. The two together give the third FORMULA line. The characteristic polynomial of the sequence is
`(x-3)(x-2)(x^2-x+2)(x^2-2x+2)`, of degree 6 because `P(2,·)` and `2^n` share the root 2.

## Verification (2026-10-23)

Python 3.11, integer arithmetic: the 50 terms equal the g.f. expansion, the recurrence, the
closed form with A146559 and A107920 (live data and offsets checked 2026-10-23), and the program;
enumeration of all words `c` for `n <= 12` gives the first 12 terms and `1 + r + s` blocks for
every castle; `P(1,n)` and `P(2,n)` by their definitions equal `A146559(n+1)` and
`2^n - A107920(n)` for `n <= 11`.
