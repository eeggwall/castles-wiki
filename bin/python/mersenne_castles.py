# Mersenne castles: castles in which neighboring columns, read as strings whose lengths are the
# column heights, sound a perfect consonance: heights in ratio 1, 2, 3/2 or 4/3, or the inverse.
# Checks: the consonance rule and its matrix; the examples on the page; heights 2, 3 and 4 (all
# castles, the 1-smooth castles, the cubic x^3 - 4x^2 + 2x + 2) with generating functions; the
# classes m * 2^i 3^j and the reduction A(w, h) = A(w, h0); the triangular lattice of the heights
# 2^i 3^j and their number A071521; Perron roots, minimal polynomials and the bounds that give the
# limit 7; even-block and odd-block counts against brute-force enumeration.
# Page: wiki/pages/mersenne-castles.md.  OEIS data below: the data fields, read 2026-10-28.
import math
from fractions import Fraction as Fr
from itertools import product
import sympy as sp

A106514 = [1, 3, 9, 25, 67, 175, 449, 1137, 2851, 7095, 17553, 43225, 106051, 259423, 633089,
           1541985, 3749827, 9107175, 22095249, 53559817, 129739171, 314086735, 760009793,
           1838300625, 4444999651, 10745077143, 25968708369, 62749602745]          # offset 0
A071521 = [1, 2, 3, 4, 4, 5, 5, 6, 7, 7, 7, 8, 8, 8, 8, 9, 9, 10, 10, 10, 10, 10, 10, 11, 11, 11,
           12, 12, 12, 12, 12, 13, 13, 13, 13, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14,
           15, 15, 15, 15, 15, 15, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 17, 17, 17, 17, 17,
           17, 17, 17, 18, 18, 18, 18]                                              # offset 1

RATIOS = [Fr(1), Fr(2), Fr(1, 2), Fr(3, 2), Fr(2, 3), Fr(4, 3), Fr(3, 4)]
NAMES = {Fr(1): 'unison', Fr(2): 'octave', Fr(1, 2): 'octave', Fr(3, 2): 'fifth',
         Fr(2, 3): 'fifth', Fr(4, 3): 'fourth', Fr(3, 4): 'fourth'}


def cons(a, b):
    return Fr(b, a) in NAMES


def M_cons(h):
    return [[1 if cons(a, b) else 0 for b in range(1, h + 1)] for a in range(1, h + 1)]


def skylines(w, h, sign=False):
    """Skylines of width w on 1..h obeying the rule, reaching h or not; with sign, sum of (-1)^blocks."""
    if h <= 0 or w <= 0:
        return 0
    v = [(-1) ** a if sign else 1 for a in range(1, h + 1)]
    for _ in range(w - 1):
        v = [sum(v[a - 1] * ((-1) ** max(0, b - a) if sign else 1)
                 for a in range(1, h + 1) if cons(a, b)) for b in range(1, h + 1)]
    return sum(v)


def A(w, h):
    return skylines(w, h) - skylines(w, h - 1)


def S(w, h):
    return skylines(w, h, True) - skylines(w, h - 1, True)


def blocks(c):
    return c[0] + sum(max(0, b - a) for a, b in zip(c, c[1:]))


def brute(w, h):
    """Mersenne castles of width w and height h by depth-first search: (count, even, odd)."""
    tally = [0, 0, 0]

    def go(c, top, nb):
        if len(c) == w:
            if top == h:
                tally[0] += 1
                tally[1 + nb % 2] += 1
            return
        a = c[-1]
        for b in range(1, h + 1):
            if cons(a, b):
                c.append(b)
                go(c, max(top, b), nb + max(0, b - a))
                c.pop()
    for c1 in range(1, h + 1):
        go([c1], c1, c1)
    return tuple(tally)


def is_mersenne(c):
    return all(cons(a, b) for a, b in zip(c, c[1:]))


def part23(h):
    """h = m * h0 with h0 = 2^a 3^b and m prime to 6."""
    h0 = 1
    while h % 2 == 0:
        h, h0 = h // 2, h0 * 2
    while h % 3 == 0:
        h, h0 = h // 3, h0 * 3
    return h, h0


def vitry(n):
    """The heights 2^i 3^j <= n."""
    out, p = [], 1
    while p <= n:
        q = p
        while q <= n:
            out.append(q)
            q *= 3
        p *= 2
    return sorted(out)


def neighbors(n, V):
    return [int(n * r) for r in RATIOS if (n * r).denominator == 1 and int(n * r) in V]


def perron(n):
    """Perron root of the consonance rule on the heights 2^i 3^j <= n, by Collatz-Wielandt bounds."""
    V = vitry(n)
    idx = {a: k for k, a in enumerate(V)}
    nb = [[idx[b] for b in neighbors(a, idx)] for a in V]
    v = [1.0] * len(V)
    for _ in range(100000):
        u = [sum(v[j] for j in nb[k]) for k in range(len(V))]
        q = [u[k] / v[k] for k in range(len(V))]
        lo, hi = min(q), max(q)
        s = max(u)
        v = [t / s for t in u]
        if hi - lo < 1e-13:
            break
    return (lo + hi) / 2, V, nb


def charpoly_int(m):
    """Characteristic polynomial det(xI - m), coefficients from x^n down, by Faddeev-LeVerrier."""
    n = len(m)
    Am = [[Fr(x) for x in r] for r in m]
    c, Mk = [Fr(1)], [[Fr(0)] * n for _ in range(n)]
    for k in range(1, n + 1):
        AM = [[sum(Am[i][t] * Mk[t][j] for t in range(n)) for j in range(n)] for i in range(n)]
        Mk = [[AM[i][j] + (c[-1] if i == j else 0) for j in range(n)] for i in range(n)]
        AM = [[sum(Am[i][t] * Mk[t][j] for t in range(n)) for j in range(n)] for i in range(n)]
        c.append(-sum(AM[i][i] for i in range(n)) / k)
    return [int(x) for x in c]


def series(num, den, N):
    """Coefficients 0..N-1 of num/den, polynomials as coefficient lists from x^0, den[0] = 1."""
    out = []
    for n in range(N):
        t = (num[n] if n < len(num) else 0) - sum(den[k] * out[n - k] for k in range(1, min(n, len(den) - 1) + 1))
        out.append(t)
    return out


def pmul(p, q):
    r = [0] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            r[i + j] += a * b
    return r


# [1] the rule
print('[1] consonant ratios b/a:', ', '.join(f'{r} ({NAMES[r]})' for r in RATIOS))
print('[1] M_cons(4):', M_cons(4))
print('[1] M_cons symmetric for h <= 400:', all(cons(a, b) == cons(b, a) for a in range(1, 401) for b in range(1, 401)))
deg = [sum(cons(a, b) for b in range(1, 3 * a)) for a in range(1, 401)]
print('[1] consonant heights of a, over all heights b >= 1: at most', max(deg), 'for a <= 400;',
      '7 exactly when 12 | a:', all((deg[a - 1] == 7) == (a % 12 == 0) for a in range(1, 401)))
print('[1] the twelfth 3:1 and the major third 5:4 are not in the rule:', not cons(1, 3), not cons(4, 5))

# [2] examples
ex = (2, 3, 4, 2, 1)
print('[2]', ex, 'is a Mersenne castle of height 4:', is_mersenne(ex) and max(ex) == 4,
      '; steps:', [NAMES[Fr(b, a)] for a, b in zip(ex, ex[1:])], '; blocks', blocks(ex))
for row in range(4, 0, -1):
    print('     ', ' '.join('#' if c >= row else '.' for c in ex))
print('[2] the pairs (1, 3) and (4, 5) break the rule:', not is_mersenne((1, 3)), not is_mersenne((4, 5)))
w4 = [c for c in product(range(1, 5), repeat=3) if max(c) == 4 and is_mersenne(c)]
print('[2] the Mersenne castles of width 3 and height 4:', len(w4), w4)

# [3] small heights
print('[3] h = 1: A(w, 1) = 1 for w <= 30:', all(A(w, 1) == 1 for w in range(1, 31)))
print('[3] h = 2: every castle of height 2 obeys the rule (w <= 14):',
      all(is_mersenne(c) for w in range(1, 15) for c in product((1, 2), repeat=w)),
      '; A(w, 2) = 2^w - 1 for w <= 40:', all(A(w, 2) == 2 ** w - 1 for w in range(1, 41)))
print('[3] h = 3: the rule on {1, 2, 3} is |a - b| <= 1:',
      all(cons(a, b) == (abs(a - b) <= 1) for a in range(1, 4) for b in range(1, 4)),
      '; A(w, 3) = A106514(w - 1) for w = 1..28:', all(A(w, 3) == A106514[w - 1] for w in range(1, 29)))
cp3, cp4 = charpoly_int(M_cons(3)), charpoly_int(M_cons(4))
print('[3] char poly h = 3:', cp3, '= (x - 1)(x^2 - 2x - 1):', cp3 == pmul([1, -1], [1, -2, -1]))
print('[3] char poly h = 4:', cp4, '= x(x^3 - 4x^2 + 2x + 2):', cp4 == pmul([1, 0], [1, -4, 2, 2]))
for h in (2, 3, 4):
    print(f'[3] A(w, {h}), w = 1..12:', [A(w, h) for w in range(1, 13)])
den4 = pmul([1, -2, -1], [1, -4, 2, 2])
print('[3] sum_w A(w, 4) x^w = x(1 - x)/((1 - 2x - x^2)(1 - 4x + 2x^2 + 2x^3)), w <= 60:',
      series([0, 1, -1], den4, 61)[1:] == [A(w, 4) for w in range(1, 61)])
print('[3] A(401, h)/A(400, h): h = 3 %.12f vs 1 + sqrt 2 = %.12f; h = 4 %.12f'
      % (A(401, 3) / A(400, 3), 1 + math.sqrt(2), A(401, 4) / A(400, 4)))

# [4] the classes
ok = True
for h in range(1, 301):
    comp, seen = [], set()
    for s in range(1, h + 1):
        if s in seen:
            continue
        stack, cl = [s], {s}
        while stack:
            a = stack.pop()
            for b in range(1, h + 1):
                if b not in cl and cons(a, b):
                    cl.add(b)
                    stack.append(b)
        seen |= cl
        comp.append(cl)
    want = [{m * t for t in vitry(h // m)} for m in range(1, h + 1) if math.gcd(m, 6) == 1]
    ok &= sorted(map(sorted, comp)) == sorted(map(sorted, want))
print('[4] for h <= 300 the classes of {1..h} under chains of consonances are m * {2^i 3^j <= h/m}, m prime to 6:', ok)
ok = True
for h in range(1, 73):
    m, h0 = part23(h)
    for w in range(1, 9):
        ok &= (A(w, h), S(w, h)) == (A(w, h0), S(w, h0))
print('[4] A(w, h) = A(w, h0) and S(w, h) = S(w, h0), h <= 72, w <= 8:', ok)
print('[4] h = 5:', [A(w, 5) for w in range(1, 9)], '; h = 10:', [A(w, 10) for w in range(1, 9)],
      '; h = 12 vs 60:', [A(w, 12) for w in range(1, 6)], [A(w, 60) for w in range(1, 6)])
print('[4] blocks(m c) = m blocks(c) on the Mersenne castles of height 6, w <= 6, m = 5, 7:',
      all(blocks(tuple(m * x for x in c)) == m * blocks(c)
          for w in range(1, 7) for c in product(range(1, 7), repeat=w) if max(c) == 6 and is_mersenne(c)
          for m in (5, 7)))

# [5] the lattice
def exps(n):
    """(i, j) with n = 2^i 3^j times a part prime to 6."""
    i = j = 0
    while n % 2 == 0:
        n, i = n // 2, i + 1
    while n % 3 == 0:
        n, j = n // 3, j + 1
    return i, j


steps = {}
for r in RATIOS:
    (a, b), (c, d) = exps(r.numerator), exps(r.denominator)
    steps[NAMES[r] + (' up' if r > 1 else ' down' if r < 1 else '')] = (a - c, b - d)
print('[5] exponent steps (i, j) of 2^i 3^j:', steps)
print('[5] fourth up = octave up - fifth up:', steps['fourth up'] == tuple(x - y for x, y in zip(steps['octave up'], steps['fifth up'])))
print('[5] |{2^i 3^j <= h}| = A071521(h) for h = 1..75:', all(len(vitry(h)) == A071521[h - 1] for h in range(1, 76)))
V32 = vitry(32)
pos = {n: (2 * exps(n)[0] + 3 * exps(n)[1], exps(n)[1]) for n in V32}
grid = {}
for n, (x, y) in pos.items():
    grid[(3 * x, 2 * y)] = str(n)
for n, (x, y) in pos.items():
    for b in neighbors(n, set(V32)):
        bx, by = pos[b]
        if (bx, by) == (x + 2, y):
            grid[(3 * x + 3, 2 * y)] = '--'
        elif (bx, by) == (x + 1, y + 1):
            grid[(3 * x + 1, 2 * y + 1)] = '/'
        elif (bx, by) == (x + 1, y - 1):
            grid[(3 * x + 1, 2 * y - 1)] = '\\'
print('[5] the heights 2^i 3^j <= 32 (octave --, fifth /, fourth \\):')
for row in range(6, -1, -1):
    line = ''
    for col in range(0, 36):
        if (col, row) in grid:
            line = line.ljust(col) + grid[(col, row)]
    print('     ', line.rstrip())
ok = True
for n in [h for h in vitry(2 ** 20)]:
    V = set(vitry(n))
    for a in V:
        i, j = exps(a)
        ok &= (len(neighbors(a, V)) == 7) == (i >= 2 and j >= 1 and 2 * a <= n)
print('[5] 2^i 3^j <= h has all 7 consonant heights in the set exactly when i >= 2, j >= 1, 2^(i+1) 3^j <= h, for 3-smooth h <= 2^20:', ok)

# [6] spectrum and growth
x = sp.symbols('x')
print('[6] characteristic polynomials of the rule on the heights 2^i 3^j <= h:')
for h in [2, 3, 4, 6, 8, 9, 12, 16, 18, 24, 27, 32]:
    lam, V, nb = perron(h)
    idx = {a: k for k, a in enumerate(V)}
    Mx = sp.Matrix(len(V), len(V), lambda r, c: 1 if c in nb[r] else 0)
    cp = Mx.charpoly(x).as_expr()
    fl = sp.factor_list(cp)[1]
    top = [g for g, e in fl if abs(complex(g.subs(x, lam))) < 1e-7]
    print(f'     h = {h:2d}, {len(V):2d} heights, rho = {lam:.10f}, factor of rho: {top[0]} (degree {sp.degree(top[0], x)}), char poly {sp.factor(cp)}')
print('[6] rho(h), average consonant heights dbar(h), (7 - rho)(ln h)^2, and the bound 12(log2 h + 3 log3 h + 4)/(log2 h log3 h):')
ok = True
for e in [5, 7, 10, 16, 20, 30, 40]:
    h = 2 ** e
    lam, V, nb = perron(h)
    dbar = sum(len(r) for r in nb) / len(V)
    D = sum(1 for r in nb if len(r) < 7)
    l2, l3 = math.log2(h), math.log(h, 3)
    bound = 12 * (l2 + 3 * l3 + 4) / (l2 * l3)
    ok &= dbar <= lam < 7 and D <= l2 + 3 * l3 + 4 and len(V) >= l2 * l3 / 2 and 7 - lam <= 6 * D / len(V) <= bound
    print(f'     h = 2^{e:<2d} |V| = {len(V):3d}  |D| = {D:3d}  dbar = {dbar:.4f}  rho = {lam:.6f}  (7 - rho)(ln h)^2 = {(7 - lam) * math.log(h) ** 2:.2f}  bound {bound:.3f}')
for h in vitry(10 ** 6)[1:]:
    lam, V, nb = perron(h)
    D = sum(1 for r in nb if len(r) < 7)
    l2, l3 = math.log2(h), math.log(h, 3)
    ok &= sum(len(r) for r in nb) / len(V) <= lam < 7 and D <= l2 + 3 * l3 + 4 and len(V) >= l2 * l3 / 2
print('[6] dbar <= rho < 7, |D| <= log2 h + 3 log3 h + 4, |V| >= log2 h log3 h / 2: all 3-smooth h <= 10^6 and the rows above:', ok)
for h in [4, 5, 6, 10, 12, 24, 30, 36]:
    m, h0 = part23(h)
    print(f'[6] h = {h:2d} = {m} * {h0}: A(1001, h)/A(1000, h) = {A(1001, h) / A(1000, h):.10f}, rho(h0) = {perron(h0)[0]:.10f}')

# [7] blocks
print('[7] even-block and odd-block Mersenne castles, w = 1..10, against brute-force enumeration:')
ok = True
for h in [1, 2, 3, 4, 6, 8, 9, 12]:
    cnt, ev, od = [], [], []
    for w in range(1, 11):
        n, e, o = brute(w, h)
        ok &= n == A(w, h) and e - o == S(w, h)
        cnt.append(n)
        ev.append(e)
        od.append(o)
    print(f'     h = {h}: A   {cnt}')
    print(f'            A^e {ev}')
    print(f'            A^o {od}')
small = all(brute(w, h)[0] == sum(1 for c in product(range(1, h + 1), repeat=w) if max(c) == h and is_mersenne(c))
            for h in range(1, 9) for w in range(1, 7) if h ** w <= 300000)
print('[7] transfer counts agree with the search:', ok, '; the search agrees with all of {1..h}^w where h^w <= 300000:', small)
