# Catalan number — cached facts from Wikipedia

Source: https://en.wikipedia.org/wiki/Catalan_number (fetched 2026-09-13 via WebFetch;
this is a cached extract of the facts used, not the full article).

## Definition and closed forms
- C_n = (1/(n+1)) * binomial(2n, n) = (2n)! / ((n+1)! * n!)
- C_n = binomial(2n, n) - binomial(2n, n+1)   (shows integrality)

## First values (n = 0..10)
1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862, 16796

## Recurrences
- Convolution:  C_0 = 1,  C_{n+1} = sum_{i=0..n} C_i * C_{n-i}
- Ratio:        C_0 = 1,  C_n = (2(2n-1)/(n+1)) * C_{n-1}

## Generating function
c(x) = sum_n C_n x^n  satisfies  c(x) = 1 + x*c(x)^2,  so  c(x) = (1 - sqrt(1-4x)) / (2x).

## Asymptotics
C_n ~ 4^n / (n^(3/2) * sqrt(pi))  as n -> infinity.

## Canonical interpretations (a selection)
- Dyck words of length 2n (n X's, n Y's, no prefix with more Y than X)
- Balanced parentheses with n pairs
- Full binary trees with n+1 leaves
- Non-crossing partitions of {1..n}
- Monotonic lattice paths in an n x n grid not passing above the diagonal
- Triangulations of a convex (n+2)-gon
- Stack-sortable / 123-avoiding permutations of {1..n}

## Related sequences (castle-relevant, verified separately, not all from WP)
- Narayana row sum:  sum_k N(n,k) = C_n   (N = A001263)
- q-Catalan numbers: polynomial q-analogs, C_n(q) -> C_n at q=1
- Motzkin numbers: up/flat/down lattice-path cousin
