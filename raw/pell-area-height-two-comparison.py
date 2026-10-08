"""Height-2 comparison for the Pell area page, verified 2026-10-07.

Original verification source; immutable once cited.
Smooth, Fibonacci and ridge are different height-2 neighbour rules.
Only the smooth family with first column 1 matches the Pell anchor.
"""

from itertools import product

import sympy as sp

z, q = sp.symbols("z q")
smooth = sp.Matrix([[1, 1], [1, 1]])
fibonacci = sp.Matrix([[1, 1], [1, 0]])
ridge = sp.Matrix([[0, 1], [1, 1]])


def joint_gf(rule, anchored=False):
    weights = sp.diag(z*q, z*q**2)
    initial = sp.Matrix([[z*q, 0 if anchored else z*q**2]])
    total = (initial * (sp.eye(2) - rule*weights).inv() * sp.ones(2, 1))[0]
    # Remove every allowed skyline that stays entirely at height 1.
    flat = z*q/(1-z*q) if rule[0, 0] else z*q
    return sp.cancel(total - flat)


def main():
    anchored = z**2*q**3/((1-z*q)*(1-z*(q+q**2)))
    free = z*q**2/((1-z*q)*(1-z*(q+q**2)))
    assert sp.cancel(joint_gf(smooth, True) - anchored) == 0
    assert sp.cancel(joint_gf(smooth) - free) == 0
    assert sp.cancel(anchored.subs(z, 1) - q**3/((1-q)*(1-q-q**2))) == 0
    assert sp.cancel(free.subs(z, 1) - q**2/((1-q)*(1-q-q**2))) == 0

    for rule, pin_first in ((smooth, True), (smooth, False),
                            (fibonacci, False), (ridge, False)):
        series = sp.series(joint_gf(rule, pin_first), z, 0, 9).removeO().expand()
        for w in range(1, 9):
            castles = [c for c in product((1, 2), repeat=w)
                       if max(c) == 2 and (not pin_first or c[0] == 1)
                       and all(rule[a-1, b-1] for a, b in zip(c, c[1:]))]
            assert sp.expand(series.coeff(z, w) - sum(q**sum(c) for c in castles)) == 0

    fib = [0, 1]
    for _ in range(30):
        fib.append(fib[-1] + fib[-2])
    anchored_area = sp.series(anchored.subs(z, 1), q, 0, 20).removeO().expand()
    free_area = sp.series(free.subs(z, 1), q, 0, 20).removeO().expand()
    assert all(anchored_area.coeff(q, n) == fib[n]-1 for n in range(1, 20))
    assert all(free_area.coeff(q, n) == fib[n+1]-1 for n in range(1, 20))
    assert (fibonacci*sp.Matrix([[0, 1], [1, 0]])) != smooth
    assert sp.Matrix([[0, 1], [1, 0]])*fibonacci*sp.Matrix([[0, 1], [1, 0]]) == ridge
    assert (1, 2, 2) not in [c for c in product((1, 2), repeat=3)
                             if all(fibonacci[a-1, b-1] for a, b in zip(c, c[1:]))]
    print("Height-2 rule matrices and joint GFs versus enumeration: PASS")
    print("Anchored smooth area counts, n=3..10:", [fib[n]-1 for n in range(3, 11)])
    print("Free smooth area counts, n=2..9:", [fib[n+1]-1 for n in range(2, 10)])


if __name__ == "__main__":
    main()
