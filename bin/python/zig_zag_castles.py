# Zig-zag castles: castles in which neighboring columns differ by exactly 1, the 1-smooth rule
# |c_{i+1} - c_i| <= 1 combined with the plateau-free rule c_{i+1} != c_i.
# Checks: the combined rule matrix is A_path, with characteristic polynomial U_h(x/2) and eigenvalues
# 2cos(pi k/(h+1)); the examples on the page; the zig-zag strips against the zig-zag path entries of
# the OEIS; the castles of height h against the (h-1)-balanced strings, by count and by bijection;
# the block formula and the even-block and odd-block counts; the growth by width.
# Page: wiki/pages/zig-zag-castles.md.  OEIS data below: the data fields, read 2026-10-27.
import math
from itertools import product
import numpy as np
import sympy as sp

OEIS = {
    'A090992': (1, [7, 13, 24, 45, 84, 158, 296, 557, 1045, 1966, 3691, 6942, 13038, 24516, 46055, 86585,
                    162680, 305809, 574624, 1080106, 2029680, 3814941, 7169145, 13474502, 25322375, 47592650,
                    89441626, 168100324, 315917527, 593742597, 1115852904, 2097145317]),
    'A090993': (1, [8, 14, 24, 42, 72, 126, 216, 378, 648, 1134, 1944, 3402, 5832, 10206, 17496, 30618, 52488,
                    91854, 157464, 275562, 472392, 826686, 1417176, 2480058, 4251528, 7440174, 12754584,
                    22320522, 38263752, 66961566, 114791256, 200884698]),
    'A090994': (1, [9, 17, 32, 61, 116, 222, 424, 813, 1556, 2986, 5721, 10982, 21053, 40416, 77505, 148785,
                    285380, 547810, 1050876, 2017126, 3869845, 7427671, 14250855, 27351502, 52479500,
                    100719775, 193258375, 370895324, 711682501, 1365808847, 2620797529]),
    'A090995': (1, [10, 18, 32, 58, 104, 188, 338, 610, 1098, 1980, 3566, 6428, 11580, 20870, 37602, 67762,
                    122096, 220018, 396448, 714388, 1287266, 2319594, 4179738, 7531660, 13571542, 24455124,
                    44066548, 79405254, 143083226, 257827186, 464588384]),
    'A030435': (0, [2, 2, 4, 6, 12, 20, 40, 68, 136, 232, 464, 792, 1584, 2704, 5408, 9232, 18464, 31520,
                    63040, 107616, 215232, 367424, 734848, 1254464, 2508928, 4283008, 8566016, 14623104,
                    29246208, 49926400, 99852800, 170459392, 340918784, 581984768, 1163969536, 1987020288]),
    'A030436': (0, [1, 1, 2, 3, 6, 10, 20, 34, 68, 116, 232, 396, 792, 1352, 2704, 4616, 9232, 15760, 31520,
                    53808, 107616, 183712, 367424, 627232, 1254464, 2141504, 4283008, 7311552, 14623104,
                    24963200, 49926400, 85229696, 170459392, 290992384, 581984768, 993510144, 1987020288,
                    3392055808]),
    'A153334': (1, [1, 1, 4, 8, 24, 52, 136, 296, 720, 1556, 3624, 7768, 17584, 37416, 83024, 175568, 383904,
                    807604, 1746280, 3657464, 7839216, 16357496, 34812144, 72407728, 153204064, 317777032,
                    669108496, 1384524656, 2903267040, 5994736336]),
    'A153335': (1, [0, 1, 2, 8, 18, 52, 116, 296, 650, 1556, 3372, 7768, 16660, 37416, 79592, 175568, 371034,
                    807604, 1697660, 3657464, 7654460, 16357496, 34106712, 72407728, 150499908, 317777032,
                    658707896, 1384524656, 2863150440, 5994736336]),
    'A153336': (1, [1, 8, 52, 296, 1556, 7768, 37416, 175568, 807604, 3657464, 16357496, 72407728, 317777032,
                    1384524656, 5994736336, 25816193952, 110652549620, 472302724408, 2008499580504,
                    8513063608304, 35975584631128, 151621915797840]),
    'A153337': (1, [1, 4, 24, 136, 720, 3624, 17584, 83024, 383904, 1746280, 7839216, 34812144, 153204064,
                    669108496, 2903267040, 12526343584, 53779871552, 229895033832, 978965187184,
                    4154438114480, 17575883030496, 74150192517808]),
    'A153338': (1, [0, 2, 18, 116, 650, 3372, 16660, 79592, 371034, 1697660, 7654460, 34106712, 150499908,
                    658707896, 2863150440, 12371226064, 53178791162, 227561427612, 969890051884,
                    4119092850680, 17438036501676, 73611934643368, 309935825654168, 1301878616066736]),
    'A153339': (1, [3, 4, 8, 12, 24, 36, 72, 108, 216, 324, 648, 972, 1944, 2916, 5832, 8748, 17496, 26244,
                    52488, 78732, 157464, 236196, 472392, 708588, 1417176, 2125764, 4251528, 6377292,
                    12754584, 19131876, 38263752, 57395628, 114791256, 172186884]),
    'A153340': (1, [8, 14, 26, 48, 90, 168, 316, 592, 1114, 2090, 3932, 7382, 13884, 26076, 49032, 92110,
                    173170, 325360, 611618, 1149248, 2160212, 4059360, 7629882, 14338290, 26949004, 50644750,
                    95185300, 178883252, 336200648, 631835054, 1187485194, 2231705808]),
    'A153360': (1, [10, 18, 34, 64, 122, 232, 444, 848, 1626, 3112, 5972, 11442, 21964, 42106, 80832, 155010,
                    297570, 570760, 1095620, 2101752, 4034252, 7739690, 14855342, 28501710, 54703004,
                    104959000, 201439550, 386516750, 741790648, 1423365002, 2731617694]),
    'A153361': (1, [12, 22, 42, 80, 154, 296, 572, 1104, 2138, 4136, 8020, 15536, 30148, 58450, 113472,
                    220110, 427410, 829352, 1610628, 3125954, 6071028, 11784514, 22887536, 44431506, 86293452,
                    167532792, 325373382, 631721620, 1226878704, 2382108386]),
    'A153362': (1, [9, 16, 30, 56, 106, 200, 380, 720, 1370, 2600, 4950, 9400, 17900, 34000, 64750, 123000,
                    234250, 445000, 847500, 1610000, 3066250, 5825000, 11093750, 21075000, 40137500, 76250000,
                    145218750, 275875000, 525406250, 998125000, 1900937500]),
    'A153363': (1, [5, 8, 16, 28, 56, 100, 200, 360, 720, 1300, 2600, 4700, 9400, 17000, 34000, 61500, 123000,
                    222500, 445000, 805000, 1610000, 2912500, 5825000, 10537500, 21075000, 38125000, 76250000,
                    137937500, 275875000, 499062500, 998125000, 1805625000]),
    'A153364': (1, [4, 8, 14, 28, 50, 100, 180, 360, 650, 1300, 2350, 4700, 8500, 17000, 30750, 61500, 111250,
                    222500, 402500, 805000, 1456250, 2912500, 5268750, 10537500, 19062500, 38125000, 68968750,
                    137937500, 249531250, 499062500, 902812500, 1805625000]),
    'A153365': (1, [8, 28, 100, 360, 1300, 4700, 17000, 61500, 222500, 805000, 2912500, 10537500, 38125000,
                    137937500, 499062500, 1805625000, 6532812500, 23635937500, 85515625000, 309398437500,
                    1119414062500, 4050078125000, 14653320312500]),
    'A153366': (1, [5, 16, 56, 200, 720, 2600, 9400, 34000, 123000, 445000, 1610000, 5825000, 21075000,
                    76250000, 275875000, 998125000, 3611250000, 13065625000, 47271875000, 171031250000,
                    618796875000, 2238828125000, 8100156250000, 29306640625000]),
    'A153367': (1, [4, 14, 50, 180, 650, 2350, 8500, 30750, 111250, 402500, 1456250, 5268750, 19062500,
                    68968750, 249531250, 902812500, 3266406250, 11817968750, 42757812500, 154699218750,
                    559707031250, 2025039062500, 7326660156250, 26508105468750]),
    'A153368': (1, [11, 20, 38, 72, 138, 264, 508, 976, 1882, 3624, 6996, 13488, 26054, 50264, 97124, 187440,
                    362250, 699240, 1351492, 2609008, 5042950, 9735768, 18818772, 36332016, 70229066,
                    135588200, 262091348, 506012592, 978124038, 1888445784, 3650380228]),
    'A153369': (1, [6, 10, 20, 36, 72, 132, 264, 488, 976, 1812, 3624, 6744, 13488, 25132, 50264, 93720,
                    187440, 349620, 699240, 1304504, 2609008, 4867884, 9735768, 18166008, 36332016, 67794100,
                    135588200, 253006296, 506012592, 944222892, 1888445784, 3523868888]),
    'A153370': (1, [5, 10, 18, 36, 66, 132, 244, 488, 906, 1812, 3372, 6744, 12566, 25132, 46860, 93720,
                    174810, 349620, 652252, 1304504, 2433942, 4867884, 9083004, 18166008, 33897050, 67794100,
                    126503148, 253006296, 472111446, 944222892, 1761934444, 3523868888]),
    'A153371': (1, [10, 36, 132, 488, 1812, 6744, 25132, 93720, 349620, 1304504, 4867884, 18166008, 67794100,
                    253006296, 944222892, 3523868888, 13151219892, 49080945144, 183172429612, 683608511160,
                    2551261090740, 9521434803224, 35534476025004]),
    'A153372': (1, [6, 20, 72, 264, 976, 3624, 13488, 50264, 187440, 699240, 2609008, 9735768, 36332016,
                    135588200, 506012592, 1888445784, 7047737776, 26302439784, 98161890288, 366344859224,
                    1367217022320, 5102522181480, 19042869606448]),
    'A153373': (1, [5, 18, 66, 244, 906, 3372, 12566, 46860, 174810, 652252, 2433942, 9083004, 33897050,
                    126503148, 472111446, 1761934444, 6575609946, 24540472572, 91586214806, 341804255580,
                    1275630545370, 4760717401612, 17767238012502]),
    'A027383': (0, [1, 2, 4, 6, 10, 14, 22, 30, 46, 62, 94, 126, 190, 254, 382, 510, 766, 1022, 1534, 2046,
                    3070, 4094, 6142, 8190, 12286, 16382, 24574, 32766, 49150, 65534, 98302, 131070, 196606,
                    262142, 393214, 524286, 786430, 1048574, 1572862, 2097150, 3145726, 4194302, 6291454]),
    'A027557': (0, [1, 2, 4, 8, 14, 26, 44, 78, 130, 224, 370, 626, 1028, 1718, 2810, 4656, 7594, 12506,
                    20356, 33374, 54242, 88640, 143906, 234594, 380548, 619238, 1003882, 1631312, 2643386,
                    4291082, 6950852, 11274702, 18258322, 29598560]),
    'A027559': (0, [1, 2, 4, 8, 16, 30, 58, 106, 200, 360, 668, 1190, 2182, 3858, 7012, 12328, 22256, 38958,
                    69962, 122042, 218248, 379656, 676636, 1174390, 2087222, 3615906, 6411716, 11090504,
                    19627984, 33907134, 59912410, 103385482, 182429768]),
    'A027560': (0, [1, 2, 4, 8, 16, 32, 62, 122, 232, 450, 846, 1622, 3026, 5748, 10664, 20106, 37144, 69608,
                    128164, 238984, 438826, 814874, 1492908, 2762562, 5051602, 9320014, 17014950, 31311964,
                    57084732, 104819474, 190865620, 349797128, 636274832]),
}


def A_path(h):
    return [[1 if abs(a - b) == 1 else 0 for b in range(h)] for a in range(h)]


def zstrips(w, h, keep=lambda c1: True):
    """Zig-zag strips of width w on the heights 1..h whose first column c1 passes keep."""
    if h <= 0 or w <= 0:
        return 0
    v = [1 if keep(c) else 0 for c in range(1, h + 1)]
    for _ in range(w - 1):
        v = [(v[i - 1] if i > 0 else 0) + (v[i + 1] if i < h - 1 else 0) for i in range(h)]
    return sum(v)


def A_zigzag(w, h):
    return zstrips(w, h) - zstrips(w, h - 1)


def skylines(w, h):
    """All zig-zag strips of width w on the heights 1..h, as tuples."""
    out = []
    def rec(s):
        if len(s) == w:
            out.append(tuple(s)); return
        for c in ([s[-1] - 1, s[-1] + 1] if s else range(1, h + 1)):
            if 1 <= c <= h:
                rec(s + [c])
    rec([])
    return out


def castles(w, h):
    return [c for c in skylines(w, h) if max(c) == h]


def blocks(c):
    return sum(max(0, b - a) for a, b in zip((0,) + tuple(c), c))


def check(a, f):
    off, data = OEIS[a]
    return all(f(off + i) == x for i, x in enumerate(data) if f(off + i) is not None), len(data)


# [1] the combined rule is A_path; its characteristic polynomial and eigenvalues
ok1 = True
for h in range(2, 13):
    I = np.eye(h, dtype=int); J = np.ones((h, h), dtype=int); A = np.array(A_path(h))
    ok1 &= bool(((I + A) * (J - I) == A).all())
print("[1] (I + A_path) (.) (J - I) = A_path, entrywise, for h = 2..12:", ok1)
print("[1] h = 3: 1-smooth", (np.eye(3, dtype=int) + np.array(A_path(3))).tolist(),
      " plateau-free", (np.ones((3, 3), dtype=int) - np.eye(3, dtype=int)).tolist(), " product", A_path(3))
x = sp.symbols('x')
ok1b = all(sp.expand(sp.Matrix(A_path(h)).charpoly(x).as_expr() - sp.chebyshevu(h, x / 2)) == 0 for h in range(1, 13))
print("[1] characteristic polynomial of A_path on h heights = U_h(x/2), h = 1..12:", ok1b)
ok1c = all(np.allclose(sorted(np.linalg.eigvalsh(np.array(A_path(h), dtype=float))),
                       sorted(2 * math.cos(math.pi * k / (h + 1)) for k in range(1, h + 1))) for h in range(1, 13))
print("[1] eigenvalues 2cos(pi k/(h+1)), k = 1..h, h = 1..12:", ok1c)

# [2] the examples on the page
ex = castles(4, 3)
print("[2] the zig-zag castles of width 4 and height 3:", ex, "count", len(ex), "blocks", [blocks(c) for c in ex])
for c in ex:
    print("    ", c, " ".join("".join("#" if c[i] >= r else "." for i in range(4)) for r in (3, 2, 1)))
ok2 = (1, 2, 2, 3) not in skylines(4, 3) and (1, 3, 2) not in skylines(3, 3)
print("[2] (1, 2, 2, 3) and (1, 3, 2) are not zig-zag:", ok2, "; blocks(1, 2, 3, 2) =", blocks((1, 2, 3, 2)))

# [3] zig-zag strips against the zig-zag path entries; same/opp: c_1 has the parity of h / the other parity
same = lambda h: (lambda c1: c1 % 2 == h % 2)
opp = lambda h: (lambda c1: c1 % 2 != h % 2)
first1 = lambda c1: c1 == 1
table = [  # (entry, h, which strips, width of term n, width label, factor, first n)
    ('A153340', 8, 'all', lambda n: n, 'n', 1, 1), ('A153362', 9, 'all', lambda n: n, 'n', 1, 1),
    ('A153360', 10, 'all', lambda n: n, 'n', 1, 1), ('A153368', 11, 'all', lambda n: n, 'n', 1, 1),
    ('A153361', 12, 'all', lambda n: n, 'n', 1, 1),
    ('A090993', 5, 'all', lambda n: n + 1, 'n + 1', 1, 1), ('A090995', 6, 'all', lambda n: n + 1, 'n + 1', 1, 1),
    ('A153339', 5, 'same', lambda n: n, 'n', 1, 1), ('A090992', 8, 'same', lambda n: n + 1, 'n + 1', 1, 1),
    ('A090994', 10, 'same', lambda n: n + 1, 'n + 1', 1, 1),
    ('A153363', 9, 'same', lambda n: n, 'n', 1, 1), ('A153364', 9, 'opp', lambda n: n, 'n', 1, 1),
    ('A153365', 9, 'same', lambda n: 2 * n, '2n', 1, 1), ('A153366', 9, 'same', lambda n: 2 * n - 1, '2n - 1', 1, 1),
    ('A153367', 9, 'opp', lambda n: 2 * n - 1, '2n - 1', 1, 1),
    ('A153369', 11, 'same', lambda n: n, 'n', 1, 1), ('A153370', 11, 'opp', lambda n: n, 'n', 1, 1),
    ('A153371', 11, 'same', lambda n: 2 * n, '2n', 1, 1), ('A153372', 11, 'same', lambda n: 2 * n - 1, '2n - 1', 1, 1),
    ('A153373', 11, 'opp', lambda n: 2 * n - 1, '2n - 1', 1, 1),
    ('A030435', 7, 'same', lambda n: n - 1, 'n - 1', 1, 2), ('A030436', 7, 'opp', lambda n: n - 2, 'n - 2', 1, 3),
    ('A030436', 7, 'first1', lambda n: n + 1, 'n + 1', 1, 0), ('A030435', 7, 'first1', lambda n: n + 1, 'n + 1', 2, 0),
]
keepers = {'all': lambda h: (lambda c1: True), 'same': same, 'opp': opp, 'first1': lambda h: first1}
names = {'all': 'all', 'same': 'c_1 with the parity of h', 'opp': 'c_1 with the other parity', 'first1': 'c_1 = 1'}
ok3 = True
for a, h, kind, wf, wl, k, n0 in table:
    r, m = check(a, lambda n: k * zstrips(wf(n), h, keepers[kind](h)) if n >= n0 else None)
    ok3 &= r
    print("[3] %s(n) = %szig-zag strips of width %s on heights 1..%d, %s, n >= %d: %s, %d terms"
          % (a, '' if k == 1 else '%d x ' % k, wl, h, names[kind], n0, r, m))
for a, side, sl, kind in [('A153334', lambda n: n, 'n', same), ('A153335', lambda n: n, 'n', opp),
                          ('A153336', lambda n: 2 * n, '2n', same), ('A153337', lambda n: 2 * n - 1, '2n - 1', same),
                          ('A153338', lambda n: 2 * n - 1, '2n - 1', opp)]:
    r, m = check(a, lambda n: zstrips(side(n), side(n), kind(side(n))))
    ok3 &= r
    print("[3] %s(n) = zig-zag strips of width s on heights 1..s, s = %s, %s: %s, %d terms"
          % (a, sl, names['same' if kind is same else 'opp'], r, m))
print("[3] every listed entry agrees on every term of its data field:", ok3)

# [4] castles of height h <-> (h-1)-balanced strings of length w - 1
ok4 = True
for a, h in [('A027383', 3), ('A027557', 4), ('A027559', 5), ('A027560', 6)]:
    r, m = check(a, lambda n: A_zigzag(n + 1, h))
    ok4 &= r
    print("[4] A_zigzag(w, %d) = %s(w - 1): %s, %d terms" % (h, a, r, m))
def balanced(s, k):
    for i in range(len(s)):
        d = 0
        for j in range(i, len(s)):
            d += 1 if s[j] else -1
            if abs(d) > k:
                return False
    return True
ok4b = True
for h in range(2, 8):
    for w in range(1, 14):
        img = [tuple(1 if c[i + 1] > c[i] else 0 for i in range(w - 1)) for c in castles(w, h)]
        bal = {s for s in product((0, 1), repeat=w - 1) if balanced(s, h - 1)}
        ok4b &= len(set(img)) == len(img) and set(img) == bal
print("[4] castle -> step string is a bijection onto the (h-1)-balanced strings of length w - 1, h = 2..7, w = 1..13:", ok4b)
ok4c = all(A_zigzag(w, 2) == 2 for w in range(2, 60)) and A_zigzag(1, 2) == 1
F = [0, 1]
while len(F) < 80:
    F.append(F[-1] + F[-2])
ok4d = all(A_zigzag(w, 3) == (3 * 2 ** ((w - 1) // 2) - 2 if w % 2 else 2 ** ((w + 2) // 2) - 2) for w in range(1, 60))
ok4e = all(A_zigzag(w, 4) == 2 * F[w + 2] - 2 ** ((w + 1) // 2) - 2 ** (w // 2) for w in range(1, 60))
print("[4] h = 2: 2 for w >= 2:", ok4c, "; h = 3: 3*2^((w-1)/2) - 2 (w odd), 2^((w+2)/2) - 2 (w even):", ok4d,
      "; h = 4: 2F_{w+2} - 2^floor((w+1)/2) - 2^floor(w/2):", ok4e, "(w < 60)")
print("[4] A_zigzag(w, h), w = 1..12:")
for h in range(2, 7):
    print("    h = %d:" % h, [A_zigzag(w, h) for w in range(1, 13)])

# [5] blocks = (c_1 + c_w + w - 1)/2, and the even-block and odd-block counts
ok5 = all(2 * blocks(c) == c[0] + c[-1] + len(c) - 1 for h in range(1, 8) for w in range(1, 13) for c in skylines(w, h))
print("[5] blocks(c) = (c_1 + c_w + w - 1)/2 on every zig-zag strip, h <= 7, w <= 12:", ok5)
def parity_counts(w, h):
    """(even-block, odd-block) zig-zag strips of width w on heights 1..h, from the block formula."""
    e = o = 0
    for c1 in range(1, h + 1):
        v = [1 if c == c1 else 0 for c in range(1, h + 1)]
        for _ in range(w - 1):
            v = [(v[i - 1] if i > 0 else 0) + (v[i + 1] if i < h - 1 else 0) for i in range(h)]
        for cw in range(1, h + 1):
            if v[cw - 1]:
                if ((c1 + cw + w - 1) // 2) % 2 == 0:
                    e += v[cw - 1]
                else:
                    o += v[cw - 1]
    return e, o
def Ae_Ao(w, h):
    e1, o1 = parity_counts(w, h); e0, o0 = parity_counts(w, h - 1) if h > 1 else (0, 0)
    return e1 - e0, o1 - o0
ok5b = all(Ae_Ao(w, h) == (sum(blocks(c) % 2 == 0 for c in castles(w, h)), sum(blocks(c) % 2 for c in castles(w, h)))
           for h in range(2, 8) for w in range(1, 13))
print("[5] even-block and odd-block counts from the formula agree with direct enumeration, h = 2..7, w <= 12:", ok5b)
for h in range(2, 7):
    print("    h = %d, w = 1..16, A^e:" % h, [Ae_Ao(w, h)[0] for w in range(1, 17)])
    print("    h = %d, w = 1..16, A^o:" % h, [Ae_Ao(w, h)[1] for w in range(1, 17)])

# [6] growth by width: A_zigzag(w + 2, h) / A_zigzag(w, h) -> 4cos^2(pi/(h+1))
for h in range(2, 10):
    w = 4000
    r = math.sqrt(A_zigzag(w + 2, h) / A_zigzag(w, h))
    print("[6] h = %d: sqrt(A_zigzag(%d, h)/A_zigzag(%d, h)) = %.12f, 2cos(pi/(h+1)) = %.12f" % (h, w + 2, w, r, 2 * math.cos(math.pi / (h + 1))))
print("[6] h = 4: 2cos(pi/5) = phi:", abs(2 * math.cos(math.pi / 5) - (1 + math.sqrt(5)) / 2) < 1e-15)
