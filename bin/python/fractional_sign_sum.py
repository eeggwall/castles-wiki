# The fractional sign sum S_alpha(w, h) = sum over castles of exp(i pi B_alpha(C)), with B_alpha the
# fractional block count, on the four rows of the table on fractional-block-count.
# Checks: the tabulated abs(S_alpha) at alpha = 0.1, 0.25, 0.5, 0.75, 0.9 and S_1 = S(w, h); the largest
# abs(S_alpha) on (0.5, 1), on a grid of step 0.001, against abs(S_1).
# Page: wiki/pages/fractional-block-count.md.
from itertools import product

import numpy as np

ok_all = True


def check(label, cond):
    global ok_all
    ok_all &= bool(cond)
    print(label, bool(cond))


def castles(w, h):
    return np.array([c for c in product(range(1, h + 1), repeat=w) if max(c) == h], dtype=float)


def S(cs, alpha):                          # sum_C exp(i pi B_alpha(C)), B_alpha = sum_i max(0, nabla^alpha c_i)
    w = cs.shape[1]
    wt = [1.0]
    for k in range(1, w):
        wt.append(wt[-1] * (k - 1 - alpha) / k)
    res = np.stack([sum(wt[k] * cs[:, i - k] for k in range(i + 1)) for i in range(w)], axis=1)
    return np.exp(1j * np.pi * np.clip(res, 0, None).sum(axis=1)).sum()


TABLE = {(8, 2): ([1.00, 1.01, 35.5, 49.2, 24.4], -15), (6, 3): ([0.19, 0.31, 8.57, 29.8, 41.0], -51),
         (5, 4): ([0.33, 1.11, 6.35, 47.1, 98.0], 97), (6, 4): ([0.19, 0.99, 10.5, 104.2, 157.0], 91)}
ORDERS = [0.1, 0.25, 0.5, 0.75, 0.9]
GRID = np.arange(501, 1000) / 1000

ok1, ok2 = True, True
for (w, h), (tab, s1) in TABLE.items():
    cs = castles(w, h)
    vals = [abs(S(cs, a)) for a in ORDERS]
    S1 = S(cs, 1.0)
    ok1 &= all(abs(v - t) <= 0.006 * max(1, t) for v, t in zip(vals, tab)) and abs(S1 - s1) < 1e-9
    m = [abs(S(cs, a)) for a in GRID]
    i = int(np.argmax(m))
    exceeds = m[i] > abs(s1)
    ok2 &= exceeds == ((w, h) != (6, 3))
    print(f'    ({w}, {h}): {len(cs)} castles; abs(S_alpha) at {ORDERS} = {[round(float(v), 2) for v in vals]}; S_1 = {S1.real:.0f}; '
          f'max on (0.5, 1) = {m[i]:.3f} at alpha = {GRID[i]:.3f}, {"above" if exceeds else "below"} abs(S_1) = {abs(s1)}')
check('[1] the tabulated abs(S_alpha) and S_1 of the four rows:', ok1)
check('[2] on (0.5, 1), abs(S_alpha) exceeds abs(S_1) at (8, 2), (5, 4) and (6, 4), and stays below it at (6, 3):', ok2)

print('all checks passed:', ok_all)
