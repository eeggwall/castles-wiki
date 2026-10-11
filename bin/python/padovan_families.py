# The five plastic castle families counted by Padovan numbers: generating functions and bijections.
# Pages: wiki/pages/padovan-families.md.  Needs sympy.
from itertools import product
import sympy as sp

def comps(n):
    if n == 0: yield (); return
    for k in range(1, n + 1):
        for r in comps(n - k): yield (k,) + r

def tower(t): return ''.join('1' if c == 2 else '0' for c in t)

def height2(w, max_end):  # height-2 columns isolated, gaps 1-2, end runs <= max_end
    out = []
    for t in product((1, 2), repeat=w):
        s = tower(t)
        if '1' not in s or '11' in s: continue
        r = s.split('1')
        if any(len(g) > 2 for g in r[1:-1]) or len(r[0]) > max_end or len(r[-1]) > max_end: continue
        out.append(t)
    return out

maximal = lambda w: height2(w, 1)
rll12 = lambda w: height2(w, 2)
ridge_area = lambda A: [c for c in comps(A) if set(c) <= {1, 2} and 2 in c and '11' not in ''.join(map(str, c))]
palin_tree = lambda A: [c for c in comps(A) if c == c[::-1] and all(min(a, b) < 2 for a, b in zip(c, c[1:]))]

def rule_from_1(w):  # 1 -> 2 -> 3 -> {1, 2}, first column 1, reaches 3
    nxt = {1: (2,), 2: (3,), 3: (1, 2)}; res = []
    def rec(c):
        if len(c) == w:
            if 3 in c: res.append(tuple(c))
            return
        for b in nxt[c[-1]]: rec(c + [b])
    rec([1]); return res

# bijections onto the maximal castles
def ridge_to_maximal(c):  # one column per cell, column by column, bottom up: 2 if a cell sits on it; drop the last
    return tuple((2 if j < h - 1 else 1) for h in c for j in range(h))[:-1]

def rule_to_maximal(c):  # 3s -> 2s, columns between 3s -> 1s, drop the leading 1 2, tail 1 / 2 / 1 2 -> end columns
    last3 = max(i for i, x in enumerate(c) if x == 3)
    body = tuple(2 if x == 3 else 1 for x in c[2:last3 + 1]); tail = c[last3 + 1:]
    lead, trail = {(): ((), ()), (1,): ((), (1,)), (2,): ((1,), ()), (1, 2): ((1,), (1,))}[tail]
    return lead + body + trail

def rll_to_maximal(t):  # one new column at each end: 1 beside an end 2, otherwise 2
    return ((1,) if t[0] == 2 else (2,)) + t + ((1,) if t[-1] == 2 else (2,))

def bijective(f, src, dst):
    img = [f(s) for s in src]
    return len(set(img)) == len(src) and set(img) == set(dst)

x = sp.symbols('x'); core = 1 / (1 - x**2 - x**3)
gf = {'maximal (width)': (x * (1 + x)**2 * core, maximal),
      'palindromic tree (area)': (x * (1 + x)**2 * core, palin_tree),
      'ridge, exact height 2 (area)': (x**2 * (1 + x)**2 * core, ridge_area),
      'rule from 1 (width)': (x**3 * (1 + x)**2 * core, rule_from_1),
      '(1, 2)-RLL (width)': (x * (1 + x + x**2)**2 * core, rll12)}
N = 18
for name, (F, fam) in gf.items():
    s = sp.series(F, x, 0, N + 1).removeO()
    print(f'{name:30s} GF matches counts n = 1..{N}:', all(s.coeff(x, n) == len(fam(n)) for n in range(1, N + 1)))
print('ridge area A -> maximal width A-1, A = 2..20:', all(bijective(ridge_to_maximal, ridge_area(A), maximal(A - 1)) for A in range(2, 21)))
print('rule width w -> maximal width w-2, w = 3..20:', all(bijective(rule_to_maximal, rule_from_1(w), maximal(w - 2)) for w in range(3, 21)))
print('(1,2)-RLL width w -> maximal width w+2, w = 3..18:', all(bijective(rll_to_maximal, rll12(w), maximal(w + 2)) for w in range(3, 19)))
y = sp.symbols('y')
print('tree-castle denominator at y = x^2:', sp.factor((y**3 - y**2 + 2*y - 1).subs(y, x**2)))
P = [1, 0, 0]
for _ in range(40): P.append(P[-2] + P[-3])
prime3 = lambda A: [c for c in comps(A) if min(c) >= 2 and max(c) == 3]
print('prime castles of exact height 3, area A = P(A+3) - [A even], A = 1..20:',
      all(len(prime3(A)) == P[A + 3] - (A % 2 == 0) for A in range(1, 21)))
print('examples:', ridge_to_maximal((2, 1, 2, 2, 1)), rule_to_maximal((1, 2, 3, 2, 3, 1, 2, 3, 1, 2)), rll_to_maximal((1, 1, 2, 1, 2)))
