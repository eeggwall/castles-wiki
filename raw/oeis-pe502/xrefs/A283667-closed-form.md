# Formula draft - A283667, the closed form in trinomial coefficients

Status: DRAFT for Chaz to submit.
Execution notes (field map, signature format, scope): see ../SUBMISSION-NOTES.md.
Checked against the live entry 2026-11-01 (A283667 revision #13, May 11 2020).

## The facts (verified)

A283667 = "Number of Motzkin prefixes of length 2n and height n" (Alois P. Heinz, Mar 13
2017), offset 0, 24 terms: `1, 3, 13, 64, 334, 1802, 9933, …, 100703275233924096`, b-file
`n = 0..1279`. Its formulas are "Recursion: see Maple program.", `a(n) = A283595(2n,n)` and
Vaclav Kotesovec's asymptotic (Mar 13 2017); there is no explicit formula. Its Cf. is
`A283595, A283799`.

Write `tri(m, d) = A027907(m, m+d)`, the number of step sequences in `{-1, 0, 1}^m` with sum
`d` (A027907 is the trinomial triangle, row `m` is `k = 0..2m`), and `S(m, k)` for the Motzkin
prefixes of length `m` and height at most `k`.

1. **`a(n) = A027907(2n,3n) + A027907(2n,3n+1) - A027907(2n,3n+2) - A027907(2n,3n+3)`**, for
   all 1280 terms of the b-file.
2. **Proof.** A prefix of height at most `k` is a walk from 0 that never visits -1 or `k+1`, and
   a step of size at most 1 cannot pass a height without landing on it, so the reflection
   principle applies at both walls (`wiki/pages/1-smooth-castles.md` §3.7, at `h = k+1`):
   `S(m, k) = Sum_{j in Z} [tri(m, 2j(k+2)) + tri(m, 2j(k+2)+1) - tri(m, 2j(k+2)+k+1) -
   tri(m, 2j(k+2)+k+2)]`. Since `tri(m, d) = tri(m, -d)` and `tri(m, d) = 0` for `|d| > m`,
   for `m <= 2k+2` only `j = 0` and `j = -1` contribute:
   `S(m, k) = tri(m,0) + tri(m,1) - tri(m,k+1) - 2*tri(m,k+2) - tri(m,k+3)`. Taking this at
   `k` and `k-1` with `m = 2k`, `a(k) = S(2k, k) - S(2k, k-1) = tri(2k,k) + tri(2k,k+1) -
   tri(2k,k+2) - tri(2k,k+3)`.

Verified 2026-11-01: the 24 DATA terms and, with the b-file, all 1280 terms; the reduced form
of `S(m, k)` against the direct count for `k <= 40`, `m <= 2k+2`; script below. The same
reasoning gives A283595's `T(n,k)` for `k <= n <= 2k` (`A283595-castles.md`), whose diagonal
`T(2n,n)` this is; the two edits are independent.

## Edit - A283667 closed form

All additions, except that A027907 joins the existing Cf. line in numeric order, as A226274
and A226275 joined A226136's (A226136 #21).

**FORMULA** (append after Vaclav Kotesovec's line):

```
a(n) = A027907(2*n,3*n) + A027907(2*n,3*n+1) - A027907(2*n,3*n+2) - A027907(2*n,3*n+3). - _Chaz Reid_, Mon DD YYYY
```

**CROSSREFS** (insert into the existing line):

```
Cf. A027907, A283595, A283799.
```

No comment, no proof line and no program: the formula line is bare, as on the A283595
column g.f. edit (#45).

## Verification script

Run as `python3 check.py [b283667.txt]`; with the b-file path it checks all 1280 terms.

```python
import sys
from math import comb

A283667 = [1, 3, 13, 64, 334, 1802, 9933, 55575, 314362, 1793126, 10295625, 59430043,
           344559826, 2005026610, 11703965955, 68503652100, 401892122682, 2362629703214,
           13914547415998, 82081163986020, 484893156220356, 2868234297838092,
           16986185485228431, 100703275233924096]                          # live, offset 0

def tri(m, d):                   # A027907(m, m+d) = Sum_j m!/(j! (j+d)! (m-2j-d)!)
    d = abs(d)
    t, s, j = (comb(m, d) if d <= m else 0), 0, 0
    while 2*j + d <= m:
        s += t
        t = t * (m - 2*j - d) * (m - 2*j - d - 1) // ((j + 1) * (j + d + 1))
        j += 1
    return s

a = lambda n: tri(2*n, n) + tri(2*n, n + 1) - tri(2*n, n + 2) - tri(2*n, n + 3)

def S(m, k):                     # Motzkin prefixes of length m, height <= k, counted directly
    v = [1] + [0] * k
    for _ in range(m):
        v = [(v[j-1] if j else 0) + v[j] + (v[j+1] if j < k else 0) for j in range(k + 1)]
    return sum(v)

assert [a(n) for n in range(len(A283667))] == A283667
assert all(S(m, k) == tri(m, 0) + tri(m, 1) - tri(m, k+1) - 2*tri(m, k+2) - tri(m, k+3)
           for k in range(41) for m in range(2*k + 3))
assert all(a(n) == S(2*n, n) - S(2*n, n - 1) for n in range(1, 41))
if len(sys.argv) > 1:
    b = [tuple(map(int, line.split())) for line in open(sys.argv[1])
         if line.strip() and not line.startswith('#')]
    assert all(a(n) == x for n, x in b)
    print(f"b-file: all {len(b)} terms")
print("ok")
```
