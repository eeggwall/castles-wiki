"""Fixed-height 1-smooth castles by width and area, verified 2026-10-07.

Original computation supporting wiki/pages/1-smooth-castles-by-area.md.
Run with Python 3 and SymPy. This source is immutable once cited.
All counts use first column 1, free last column, exact maximum h,
and adjacent height differences at most 1. Both block parities are included.
"""

from collections import defaultdict
from itertools import product

import sympy as sp

z, q = sp.symbols("z q")


def is_castle(c, h):
    """The anchored 1-smooth family at exact height h."""
    return (c[0] == 1 and max(c) == h
            and all(abs(a - b) <= 1 for a, b in zip(c, c[1:])))


def strip_gf(h):
    """Ceiling h, starting at height 1; no requirement to reach h.

    T[a,b] = z*q**b when |a-b| <= 1, with physical heights 1..h.
    The initial column has weight z*q; the last column is free.
    """
    if h == 0:
        return sp.Integer(0)
    transfer = sp.Matrix(h, h, lambda a, b:
                         z * q**(b + 1) if abs(a - b) <= 1 else 0)
    continuations = (sp.eye(h) - transfer).inv() * sp.ones(h, 1)
    return sp.cancel(z * q * continuations[0])


def exact_gf(h):
    """Exact height h means ceiling h minus ceiling h-1."""
    return sp.cancel(strip_gf(h) - strip_gf(h - 1))


def area_counts(h, n_max):
    """Exact-height area counts by DP over (last height, reached h).

    Appending height b adds b cells, so it moves from area n to n+b.
    """
    dp = [defaultdict(int) for _ in range(n_max + 1)]
    if n_max >= 1:
        dp[1][(1, h == 1)] = 1
    for n in range(1, n_max + 1):
        for (a, reached), count in dp[n].items():
            for b in (a - 1, a, a + 1):
                if 1 <= b <= h and n + b <= n_max:
                    dp[n + b][(b, reached or b == h)] += count
    return [sum(v for (a, reached), v in states.items() if reached)
            for states in dp]


def coefficients(f, variable, n_max):
    """Expand a rational GF by matching numerator/denominator coefficients."""
    numerator, denominator = (sp.Poly(p, variable)
                              for p in sp.fraction(sp.cancel(f)))
    out = []
    for n in range(n_max + 1):
        value = numerator.nth(n) - sum(
            denominator.nth(k) * out[n - k]
            for k in range(1, min(n, denominator.degree()) + 1))
        out.append(sp.cancel(value / denominator.nth(0)))
    return out


def main():
    # The explicit castles and the joint width/area coefficients.
    pell_width_four = [(1, 1, 2, 3), (1, 2, 2, 3),
                       (1, 2, 3, 2), (1, 2, 3, 3)]
    pell_area_eight = [(1, 2, 2, 3), (1, 2, 3, 2), (1, 1, 1, 2, 3)]
    assert all(is_castle(c, 3) for c in pell_width_four + pell_area_eight)
    assert all(sum(c) == 8 for c in pell_area_eight)
    for h in range(1, 5):
        joint = coefficients(exact_gf(h), z, 7)
        for w in range(1, 8):
            castles = [(1,) + tail
                       for tail in product(range(1, h + 1), repeat=w - 1)
                       if is_castle((1,) + tail, h)]
            polynomial = sp.expand(sum(q**sum(c) for c in castles))
            assert sp.expand(joint[w] - polynomial) == 0
            if h == 3 and w == 4:
                assert castles == pell_width_four
    pell_joint = coefficients(exact_gf(3), z, 5)
    assert pell_joint[3] == q**6
    assert sp.expand(pell_joint[4] - (q**7 + 2*q**8 + q**9)) == 0
    assert sp.expand(pell_joint[5] -
                     (q**8 + 4*q**9 + 4*q**10 + 3*q**11 + q**12)) == 0
    print("Joint GF versus enumeration: h=1..4, width<=7 PASS")

    # Last-column equations and the Pell joint rational function.
    x1, x2, x3 = sp.symbols("X1 X2 X3")
    solution = sp.solve((x1 - z*q*(1 + x1 + x2),
                         x2 - z*q**2*(x1 + x2 + x3),
                         x3 - z*q**3*(x2 + x3)), (x1, x2, x3))
    d2 = 1 - z*(q + q**2)
    d3 = 1 - z*(q + q**2 + q**3) + z**2*q**4 + z**3*q**6
    s2 = z*q/d2
    s3 = z*q*(1 - z*q**3)/d3
    pell = z**3*q**6*(1 - z*q)/(d2*d3)
    assert sp.cancel(sum(solution.values()) - s3) == 0
    assert sp.cancel(strip_gf(2) - s2) == 0
    assert sp.cancel(strip_gf(3) - s3) == 0
    assert sp.cancel(s3 - s2 - pell) == 0
    assert sp.cancel(exact_gf(3) - pell) == 0
    print("Last-column equations and exact-height subtraction PASS")

    # Forgetting area or width produces the stated one-variable functions.
    width_gf = z**3/((1 - 2*z)*(1 - 2*z - z**2))
    p = 1 - q**2 - 2*q**3 - q**4 - q**5
    area_gf = q**6/((1 - q - q**2)*p)
    assert sp.expand(d3.subs(q, 1) - (1-z)*(1-2*z-z**2)) == 0
    assert sp.expand(d3.subs(z, 1) - (1-q)*p) == 0
    assert sp.cancel(pell.subs(q, 1) - width_gf) == 0
    assert sp.cancel(pell.subs(z, 1) - area_gf) == 0
    assert coefficients(width_gf, z, 8)[3:] == [1, 4, 13, 38, 105, 280]
    area = area_counts(3, 1000)
    assert area[6:18] == [1, 1, 3, 6, 11, 22, 40, 74, 135, 242, 434, 770]
    assert coefficients(area_gf, q, 100) == area[:101]
    for h in range(1, 5):
        assert coefficients(exact_gf(h).subs(z, 1), q, 100) == area_counts(h, 100)
    print("Width and area specializations; area DP through 100 PASS")

    # Positive dominant area pole and its reciprocal growth constant.
    roots = sp.nroots(p, n=30, maxsteps=100)
    r = next(sp.re(root) for root in roots
             if abs(sp.im(root)) < sp.Float("1e-25") and sp.re(root) > 0)
    alpha = 1/r
    assert all(abs(complex(root)) > float(r) for root in roots if root != r)
    assert r < (sp.sqrt(5) - 1)/2
    assert abs(area[-1]/area[-2] - float(alpha)) < 1e-12
    print("Area pole r =", r)
    print("Area growth alpha =", alpha)
    print("Area-1000 consecutive-count ratio =", area[-1]/area[-2])
    print("All fixed-height checks PASS")


if __name__ == "__main__":
    main()
