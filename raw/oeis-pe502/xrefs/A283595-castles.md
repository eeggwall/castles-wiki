# Comment and formula draft - A283595, the castle reading, the column g.f. over R(2k+2) and the trinomial form

Status: DRAFT for Chaz to submit.
Execution notes (field map, signature format, scope): see ../SUBMISSION-NOTES.md.
Checked against the live entries 2026-11-01 (A283595 revision #45, Oct 31 2026; A027907, the
trinomial triangle, offset 0, row `n` is `k = 0..2n`).

## The facts (verified)

A283595 = "Triangle read by rows: T(n,k) is the number of Motzkin prefixes (i.e., left factors
of Motzkin paths) of length n and height k" (Steven Finch, Mar 13 2017), offset 0, rows
`k = 0..n`. Its approved formula block (Chaz Reid, Oct 23 2026, A283595 #45) gives the column
g.f. `z^k/(R(k)*R(k+1))`, with `R(2*j) = P(j) - z*P(j-1)`, `R(2*j+1) = P(j+1) - z^2*P(j-1)` and
`P(k)` of A097862, and the product form of `R(k)`. It has no comment beyond "Row n has n+1
entries." and no castle reading. Source: `wiki/pages/1-smooth-castles.md`, where the
anchored 1-smooth castles of width `w` and height `h` number `smooth(w, h) = T(w-1, h-1)`.

1. **Castles.** `T(n,k)` is the number of castles of width `n+1` and height `k+1` whose first
   column has height 1 and whose neighboring columns differ in height by at most 1, of any
   number of blocks. The column heights `c(1) = 1, c(2), ..., c(n+1)` are the prefix's heights
   plus 1: step `i` goes up, level or down as `c(i+1) - c(i)` is 1, 0 or -1, the prefix stays
   at height 0 or more since every `c(i) >= 1`, and its height is `k` exactly when the
   castle's is `k+1`.
2. **`R(k)*R(k+1) = R(2*k+2) + z^(k+1)`** for every `k >= 0`, so the g.f. of column `k` is
   `z^k/(R(2*k+2) + z^(k+1))`. Proof (wiki §3.3, with `R(k+1)` its `η_h` at `h = k+1`): from
   the Chebyshev forms of `R`, at `h = 2m` the identity is `2V_m T_m = V_{2m} + 1` and at
   `h = 2m+1` it is `2T_{m+1} V_m = V_{2m+1} + 1` (first and third kinds), and both follow
   from `2cos(aφ)cos(bφ) = cos((a+b)φ) + cos((a-b)φ)` with `a - b = 1/2`.
3. **`T(n,k) = A027907(n,n+k) + A027907(n,n+k+1) - A027907(n,n+k+2) - A027907(n,n+k+3)` for
   `k <= n <= 2*k`.** Proof (wiki §3.7): `A027907(n, n+d)` counts the step sequences in
   `{-1, 0, 1}^n` with sum `d`; the prefixes with height at most `k` are the walks from 0 that
   avoid -1 and `k+1`, counted by the reflection principle at both walls, and for `n <= 2*k`
   only one reflection in the ceiling contributes to the difference of the cases `k` and
   `k-1`. The range is sharp: at `n = 2*k+1` the right side is `T(n,k) + 1`.

Verified 2026-11-01: the castles by brute force for `n <= 11`; the identity for `k <= 70`; the
column g.f. and the trinomial form against the counts for rows `0..140`, whose program matches
the live DATA here and all 10011 terms of the b-file in `bin/python/a283595_column_gf.py`;
script below. Bounded-height path g.f.s are classical, so the formulas go in without a
novelty claim.

## Edits (lines to add)

**COMMENTS** (append after "Row n has n+1 entries."):

```
T(n,k) is also the number of castle polyominoes of width n+1 and height k+1 whose first column has height 1 and whose neighboring columns differ in height by at most 1, of any number of blocks (Project Euler, Problem 502: Counting Castles, without the rule that the number of blocks is even): columns of heights c(1) = 1, c(2), ..., c(n+1) >= 1 with |c(i+1) - c(i)| <= 1 and maximum k+1. The Motzkin prefix whose height after i steps is c(i+1) - 1 gives the bijection. - _Chaz Reid_, Mon DD YYYY
```

**LINKS** (append after Steven R. Finch's link, in alphabetical order by author):

```
Project Euler, <a href="https://projecteuler.net/problem=502">Problem 502: Counting Castles</a>.
```

**FORMULA** (append after the existing block):

```
From _Chaz Reid_, Mon DD YYYY: (Start)
R(k)*R(k+1) = R(2*k+2) + z^(k+1), with R(k) as above.
G.f. of column k: z^k/(R(2*k+2) + z^(k+1)).
T(n,k) = A027907(n,n+k) + A027907(n,n+k+1) - A027907(n,n+k+2) - A027907(n,n+k+3) for k <= n <= 2*k. (End)
```

**CROSSREFS** (insert into the existing line, in numeric order):

```
Cf. A000225, A027907, A097862, A282869.
```

## Notes

- The formula lines are bare and the proofs stay in this draft, as on the column g.f. edit
  (#45), and the subscripts are arguments, `R(2*k+2)`.
- The comment gives no name to the castles; the entry's "Column k=2 gives A094706(n-1)."
  already covers height 3.

## Verification script

```python
from itertools import product

A283595 = [1, 1, 1, 1, 3, 1, 1, 7, 4, 1, 1, 15, 13, 5, 1, 1, 31, 38, 19, 6, 1, 1, 63, 105, 64,
           26, 7, 1, 1, 127, 280, 202, 97, 34, 8, 1, 1, 255, 729, 612, 334, 139, 43, 9, 1, 1,
           511, 1866, 1803, 1094, 516, 191, 53, 10, 1, 1, 1023, 4717, 5205, 3465, 1802, 760,
           254, 64, 11, 1]                                                 # live, offset 0
M = 140
H = [[0] * (M + 1)]                              # H[k+1][n]: prefixes of length n, height <= k
for k in range(M + 1):
    v, row = [1] + [0] * k, []
    for n in range(M + 1):
        row.append(sum(v))
        v = [(v[j-1] if j else 0) + v[j] + (v[j+1] if j < k else 0) for j in range(k + 1)]
    H.append(row)
T = lambda n, k: H[k+1][n] - H[k][n]
assert [T(n, k) for n in range(11) for k in range(n + 1)] == A283595

for n in range(12):                              # castles: c(1) = 1, steps in {-1, 0, 1}
    count = [0] * (n + 2)
    for steps in product((-1, 0, 1), repeat=n):
        c = [1]
        for s in steps:
            c.append(c[-1] + s)
        if min(c) >= 1:
            count[max(c) - 1] += 1
    assert all(count[k] == T(n, k) for k in range(n + 1))

def mul(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out

def add(a, b):
    out = [0] * max(len(a), len(b))
    for i, x in enumerate(a): out[i] += x
    for i, x in enumerate(b): out[i] += x
    while len(out) > 1 and out[-1] == 0: out.pop()
    return out

shift = lambda a, s, c=1: [0] * s + [c * x for x in a]          # c * z^s * a
P = [[1], [1, -1]]                                              # A097862's P(k)
while len(P) < M + 3:
    P.append(add(mul([1, -1], P[-1]), shift(P[-2], 2, -1)))
p = lambda j: P[j] if j >= 0 else [0]
R = lambda k: add(p(k//2), shift(p(k//2 - 1), 1, -1)) if k % 2 == 0 \
    else add(p(k//2 + 1), shift(p(k//2 - 1), 2, -1))
for k in range(71):
    assert mul(R(k), R(k + 1)) == add(R(2*k + 2), shift([1], k + 1))

for k in range(M + 1):                           # z^k / D(z), D = R(2k+2) + z^(k+1), D(0) = 1
    D, a = add(R(2*k + 2), shift([1], k + 1)), []
    for n in range(M + 1):
        a.append((n == k) - sum(D[i] * a[n - i] for i in range(1, min(n, len(D) - 1) + 1)))
    assert all(a[n] == T(n, k) for n in range(M + 1))

tri_rows = [[1]]                                 # A027907, rows 0..M
for n in range(M):
    r = tri_rows[-1]
    tri_rows.append([(r[j] if j < len(r) else 0) + (r[j-1] if 0 <= j-1 < len(r) else 0)
                     + (r[j-2] if 0 <= j-2 < len(r) else 0) for j in range(len(r) + 2)])
A027907 = lambda n, j: tri_rows[n][j] if 0 <= j <= 2*n else 0
F = lambda n, k: (A027907(n, n+k) + A027907(n, n+k+1)
                  - A027907(n, n+k+2) - A027907(n, n+k+3))
assert all(F(n, k) == T(n, k) for k in range(M + 1) for n in range(k, min(2*k, M) + 1))
assert all(F(2*k + 1, k) == T(2*k + 1, k) + 1 for k in range((M - 1)//2 + 1))
print("ok")
```
