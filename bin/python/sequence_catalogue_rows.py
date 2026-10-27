# First terms of rows of config/castle-sequences.tsv, each recomputed from the row's castle definition
# (enumeration, transfer matrix or dynamic program) and checked against every listed term of the OEIS
# data field at the stated offset; the tables A080934, A080936 and A271940 entry by entry; and the
# split P(k, 5) = (-1)^k A_5(k) + B_5(k) into polynomials against A112742.
# Data: config/castle-sequences.tsv; page: wiki/pages/castle-sequence-catalogue.md.
from fractions import Fraction
from functools import lru_cache
from itertools import product

OEIS = {  # (offset, data field), read 2026-10-27
    'A283667': (0, [1, 3, 13, 64, 334, 1802, 9933, 55575, 314362, 1793126, 10295625, 59430043, 344559826,
                    2005026610, 11703965955, 68503652100, 401892122682, 2362629703214, 13914547415998,
                    82081163986020, 484893156220356, 2868234297838092, 16986185485228431, 100703275233924096]),
    'A004149': (0, [1, 1, 1, 1, 2, 4, 8, 16, 33, 69, 146, 312, 673, 1463, 3202, 7050, 15605, 34705, 77511,
                    173779, 390966, 882376, 1997211, 4532593, 10311720, 23512376, 53724350, 122995968,
                    282096693, 648097855, 1491322824, 3436755328, 7931085771]),
    'A080934': (0, [1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 2, 1, 0, 1, 1, 2, 4, 1, 0, 1, 1, 2, 5, 8, 1, 0, 1, 1,
                    2, 5, 13, 16, 1, 0, 1, 1, 2, 5, 14, 34, 32, 1, 0, 1, 1, 2, 5, 14, 41, 89, 64, 1, 0, 1, 1,
                    2, 5, 14, 42, 122, 233, 128, 1, 0, 1, 1, 2, 5, 14, 42, 131, 365, 610, 256, 1, 0, 1, 1, 2,
                    5, 14, 42, 132, 417, 1094, 1597, 512, 1, 0]),
    'A080936': (1, [1, 1, 1, 1, 3, 1, 1, 7, 5, 1, 1, 15, 18, 7, 1, 1, 31, 57, 33, 9, 1, 1, 63, 169, 132, 52,
                    11, 1, 1, 127, 482, 484, 247, 75, 13, 1, 1, 255, 1341, 1684, 1053, 410, 102, 15, 1, 1,
                    511, 3669, 5661, 4199, 1975, 629, 133, 17, 1, 1, 1023, 9922, 18579, 16017, 8778, 3366,
                    912, 168, 19, 1]),
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
    'A000447': (0, [0, 1, 10, 35, 84, 165, 286, 455, 680, 969, 1330, 1771, 2300, 2925, 3654, 4495, 5456, 6545,
                    7770, 9139, 10660, 12341, 14190, 16215, 18424, 20825, 23426, 26235, 29260, 32509, 35990,
                    39711, 43680, 47905, 52394, 57155, 62196, 67525, 73150, 79079, 85320, 91881, 98770,
                    105995, 113564, 121485]),
    'A009545': (0, [0, 1, 2, 2, 0, -4, -8, -8, 0, 16, 32, 32, 0, -64, -128, -128, 0, 256, 512, 512, 0, -1024,
                    -2048, -2048, 0, 4096, 8192, 8192, 0, -16384, -32768, -32768, 0, 65536, 131072, 131072, 0,
                    -262144, -524288, -524288, 0, 1048576, 2097152, 2097152, 0, -4194304, -8388608, -8388608,
                    0, 16777216, 33554432]),
    'A063496': (1, [1, 19, 85, 231, 489, 891, 1469, 2255, 3281, 4579, 6181, 8119, 10425, 13131, 16269, 19871,
                    23969, 28595, 33781, 39559, 45961, 53019, 60765, 69231, 78449, 88451, 99269, 110935,
                    123481, 136939, 151341, 166719, 183105, 200531, 219029, 238631, 259369, 281275, 304381]),
    'A112742': (0, [0, 0, 4, 24, 80, 200, 420, 784, 1344, 2160, 3300, 4840, 6864, 9464, 12740, 16800, 21760,
                    27744, 34884, 43320, 53200, 64680, 77924, 93104, 110400, 130000, 152100, 176904, 204624,
                    235480, 269700, 307520, 349184, 394944, 445060, 499800, 559440]),
    'A199833': (1, [4, 40, 140, 336, 660, 1144, 1820, 2720, 3876, 5320, 7084, 9200, 11700, 14616, 17980,
                    21824, 26180, 31080, 36556, 42640, 49364, 56760, 64860, 73696, 83300, 93704, 104940,
                    117040, 130036, 143960, 158844, 174720, 191620, 209576, 228620, 248784]),
    'A352116': (1, [1, 4, 19, 40, 85, 140, 231, 336, 489, 660, 891, 1144, 1469, 1820, 2255, 2720, 3281, 3876,
                    4579, 5320, 6181, 7084, 8119, 9200, 10425, 11700, 13131, 14616, 16269, 17980, 19871,
                    21824, 23969, 26180, 28595, 31080, 33781, 36556, 39559, 42640, 45961, 49364, 53019, 56760,
                    60765]),
    'A014105': (0, [0, 3, 10, 21, 36, 55, 78, 105, 136, 171, 210, 253, 300, 351, 406, 465, 528, 595, 666, 741,
                    820, 903, 990, 1081, 1176, 1275, 1378, 1485, 1596, 1711, 1830, 1953, 2080, 2211, 2346,
                    2485, 2628, 2775, 2926, 3081, 3240, 3403, 3570, 3741, 3916, 4095, 4278]),
    'A000384': (0, [0, 1, 6, 15, 28, 45, 66, 91, 120, 153, 190, 231, 276, 325, 378, 435, 496, 561, 630, 703,
                    780, 861, 946, 1035, 1128, 1225, 1326, 1431, 1540, 1653, 1770, 1891, 2016, 2145, 2278,
                    2415, 2556, 2701, 2850, 3003, 3160, 3321, 3486, 3655, 3828, 4005, 4186, 4371, 4560]),
    'A038505': (0, [0, 0, 1, 3, 6, 10, 16, 28, 56, 120, 256, 528, 1056, 2080, 4096, 8128, 16256, 32640, 65536,
                    131328, 262656, 524800, 1048576, 2096128, 4192256, 8386560, 16777216, 33558528, 67117056,
                    134225920, 268435456, 536854528, 1073709056]),
    'A038503': (0, [1, 1, 1, 1, 2, 6, 16, 36, 72, 136, 256, 496, 992, 2016, 4096, 8256, 16512, 32896, 65536,
                    130816, 261632, 523776, 1048576, 2098176, 4196352, 8390656, 16777216, 33550336, 67100672,
                    134209536, 268435456, 536887296, 1073774592, 2147516416, 4294967296, 8589869056,
                    17179738112]),
    'A077860': (0, [1, 3, 5, 5, 1, -7, -15, -15, 1, 33, 65, 65, 1, -127, -255, -255, 1, 513, 1025, 1025, 1,
                    -2047, -4095, -4095, 1, 8193, 16385, 16385, 1, -32767, -65535, -65535, 1, 131073, 262145,
                    262145, 1, -524287, -1048575, -1048575, 1, 2097153, 4194305, 4194305, 1, -8388607,
                    -16777215, -16777215]),
    'A005408': (0, [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47,
                    49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91,
                    93, 95, 97, 99, 101, 103, 105, 107, 109, 111, 113, 115, 117, 119, 121, 123, 125, 127, 129,
                    131]),
    'A005891': (0, [1, 6, 16, 31, 51, 76, 106, 141, 181, 226, 276, 331, 391, 456, 526, 601, 681, 766, 856,
                    951, 1051, 1156, 1266, 1381, 1501, 1626, 1756, 1891, 2031, 2176, 2326, 2481, 2641, 2806,
                    2976, 3151, 3331, 3516, 3706, 3901, 4101, 4306, 4516, 4731, 4951, 5176, 5406]),
    'A063490': (1, [1, 10, 40, 105, 219, 396, 650, 995, 1445, 2014, 2716, 3565, 4575, 5760, 7134, 8711, 10505,
                    12530, 14800, 17329, 20131, 23220, 26610, 30315, 34349, 38726, 43460, 48565, 54055, 59944,
                    66246, 72975, 80145, 87770, 95864, 104441, 113515, 123100, 133210, 143859, 155061]),
    'A160747': (0, [1, 15, 85, 295, 771, 1681, 3235, 5685, 9325, 14491, 21561, 30955, 43135, 58605, 77911,
                    101641, 130425, 164935, 205885, 254031, 310171, 375145, 449835, 535165, 632101, 741651,
                    864865, 1002835, 1156695, 1327621, 1516831, 1725585, 1955185, 2206975]),
    'A001045': (0, [0, 1, 1, 3, 5, 11, 21, 43, 85, 171, 341, 683, 1365, 2731, 5461, 10923, 21845, 43691,
                    87381, 174763, 349525, 699051, 1398101, 2796203, 5592405, 11184811, 22369621, 44739243,
                    89478485, 178956971, 357913941, 715827883, 1431655765, 2863311531, 5726623061, 11453246123]),
    'A006130': (0, [1, 1, 4, 7, 19, 40, 97, 217, 508, 1159, 2683, 6160, 14209, 32689, 75316, 173383, 399331,
                    919480, 2117473, 4875913, 11228332, 25856071, 59541067, 137109280, 315732481, 727060321,
                    1674257764, 3855438727, 8878212019, 20444528200, 47079164257, 108412748857, 249650241628]),
    'A006131': (0, [1, 1, 5, 9, 29, 65, 181, 441, 1165, 2929, 7589, 19305, 49661, 126881, 325525, 833049,
                    2135149, 5467345, 14007941, 35877321, 91909085, 235418369, 603054709, 1544728185,
                    3956947021, 10135859761, 25963647845, 66507086889, 170361678269]),
    'A000071': (1, [0, 0, 1, 2, 4, 7, 12, 20, 33, 54, 88, 143, 232, 376, 609, 986, 1596, 2583, 4180, 6764,
                    10945, 17710, 28656, 46367, 75024, 121392, 196417, 317810, 514228, 832039, 1346268,
                    2178308, 3524577, 5702886, 9227464, 14930351, 24157816, 39088168, 63245985, 102334154]),
    'A077855': (0, [1, 3, 6, 11, 20, 36, 64, 113, 199, 350, 615, 1080, 1896, 3328, 5841, 10251, 17990, 31571,
                    55404, 97228, 170624, 299425, 525455, 922110, 1618191, 2839728, 4983376, 8745216,
                    15346785, 26931731, 47261894, 82938843, 145547524, 255418100, 448227520, 786584465]),
    'A130578': (1, [0, 0, 1, 3, 6, 10, 16, 26, 43, 71, 116, 188, 304, 492, 797, 1291, 2090, 3382, 5472, 8854,
                    14327, 23183, 37512, 60696, 98208, 158904, 257113, 416019, 673134, 1089154, 1762288,
                    2851442, 4613731, 7465175, 12078908, 19544084]),
    'A271940': (2, [1, 2, 5, 13, 34, 1, 89, 8, 233, 42, 610, 183, 1, 1597, 717, 13, 4181, 2622, 102, 10946,
                    9134, 624, 1, 28657, 30691, 3275, 19, 75025, 100284, 15473, 205, 196418, 320466, 67684,
                    1650, 1, 514229, 1005630, 279106, 11020, 26, 1346269, 3108324, 1098402, 64553, 366,
                    3524578, 9485551, 4161750, 342867, 3716, 1]),
    'A001523': (0, [1, 1, 2, 4, 8, 15, 27, 47, 79, 130, 209, 330, 512, 784, 1183, 1765, 2604, 3804, 5504,
                    7898, 11240, 15880, 22277, 31048, 43003, 59220, 81098, 110484, 149769, 202070, 271404,
                    362974, 483439, 641368, 847681, 1116325, 1464999, 1916184, 2498258, 3247088, 4207764]),
    'A011782': (0, [1, 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536,
                    131072, 262144, 524288, 1048576, 2097152, 4194304, 8388608, 16777216, 33554432, 67108864,
                    134217728, 268435456, 536870912, 1073741824, 2147483648, 4294967296, 8589934592]),
    'A115981': (0, [0, 0, 0, 0, 0, 1, 5, 17, 49, 126, 303, 694, 1536, 3312, 7009, 14619, 30164, 61732, 125568,
                    254246, 513048, 1032696, 2074875, 4163256, 8345605, 16717996, 33473334, 66998380,
                    134067959, 268233386, 536599508, 1073378850, 2147000209]),
    'A332578': (0, [1, 1, 2, 4, 7, 13, 21, 36, 57, 91, 140, 217, 323, 485, 711, 1039, 1494, 2144, 3032, 4279,
                    5970, 8299, 11438, 15708, 21403, 29065, 39218, 52725, 70497, 93941, 124562, 164639,
                    216664, 284240, 371456, 484004, 628419, 813669, 1050144, 1351757, 1734873, 2221018,
                    2835613]),
    'A332669': (0, [0, 0, 0, 0, 1, 3, 11, 28, 71, 165, 372, 807, 1725, 3611, 7481, 15345, 31274, 63392,
                    128040, 257865, 518318, 1040277, 2085714, 4178596, 8367205, 16748151, 33515214, 67056139,
                    134147231, 268341515, 536746350, 1073577185, 2147266984, 4294683056, 8589563136,
                    17179385180]),
}


def blocks(c, base=0):
    """Block count of a skyline (castle, base 0) or tower: the total ascent from the ground."""
    return sum(max(0, b - a) for a, b in zip((base,) + tuple(c), c))


def castles(w, h):
    return (c for c in product(range(1, h + 1), repeat=w) if max(c) == h)


def compositions(n):
    if n == 0:
        yield ()
        return
    for f in range(1, n + 1):
        for rest in compositions(n - f):
            yield (f,) + rest


def weakly_unimodal(c):
    i = c.index(max(c))
    return all(c[j] <= c[j + 1] for j in range(i)) and all(c[j] >= c[j + 1] for j in range(i, len(c) - 1))


def vee(c):
    i = c.index(min(c))
    return all(c[j] >= c[j + 1] for j in range(i)) and all(c[j] <= c[j + 1] for j in range(i, len(c) - 1))


def signed_tower(k, L):
    """P(k, L): the sum of (-1)^blocks over the towers of height at most k on a base of length L."""
    v = {c: (-1) ** c for c in range(k + 1)}          # one column of height c starts c blocks
    for _ in range(L - 1):
        v = {b: sum(s * (-1) ** max(0, b - a) for a, s in v.items()) for b in range(k + 1)}
    return sum(v.values()) if L else 1


def towers_by_blocks(L, b):
    """T^(L, b): the towers of any height on a base of length L with b blocks (height <= b)."""
    return sum(1 for c in product(range(b + 1), repeat=L) if blocks(c) == b)


def tree_skylines(w, h):
    """Skylines in {1..h}^w with no two neighboring columns both of height >= 2 (no 2 x 2 square)."""
    v = [1] * h
    for _ in range(w - 1):
        v = [sum(v) if b == 1 else v[0] for b in range(1, h + 1)]
    return sum(v)


def zstrips(w, h, keep):
    v = [1 if keep(c) else 0 for c in range(1, h + 1)]
    for _ in range(w - 1):
        v = [(v[i - 1] if i else 0) + (v[i + 1] if i < h - 1 else 0) for i in range(h)]
    return sum(v)


def semiperimeter_castles(s_max, allowed=None, need=None):
    """{s: count} of castles with semi-perimeter s = w + blocks <= s_max, columns in `allowed`,
    reaching `need` if given; also returns {s: [castles]} for small s."""
    out = {}
    def rec(c, b):
        s = len(c) + b
        if c and (need is None or need in c):
            out.setdefault(s, []).append(c)
        for x in (allowed or range(1, s_max)):
            nb = b + max(0, x - (c[-1] if c else 0))
            if len(c) + 1 + nb <= s_max:
                rec(c + (x,), nb)
    rec((), 0)
    return out


def peaks(c):
    """Deutsch-Elizalde peaks: maximal runs of equal columns higher than both neighbors (ground 0)."""
    runs, i = [], 0
    while i < len(c):
        j = i
        while j + 1 < len(c) and c[j + 1] == c[i]:
            j += 1
        runs.append((c[i], i, j)); i = j + 1
    ext = [(0, -1, -1)] + runs + [(0, len(c), len(c))]
    return sum(1 for t in range(1, len(ext) - 1) if ext[t][0] > ext[t - 1][0] and ext[t][0] > ext[t + 1][0])


def dyck_paths(n, hmax=None, hexact=None):
    """Dyck paths of semilength n with height at most hmax, or exactly hexact."""
    @lru_cache(None)
    def f(i, y, top, cap):
        if y < 0 or y > cap:
            return 0
        if i == 2 * n:
            return 1 if y == 0 and (hexact is None or top == hexact) else 0
        return f(i + 1, y + 1, max(top, y + 1), cap) + f(i + 1, y - 1, top, cap)
    return f(0, 0, 0, hmax if hmax is not None else (hexact if hexact is not None else n))


def cornerless_motzkin(n):
    """Motzkin paths of length n with no UD and no DU (the tower words of length n)."""
    @lru_cache(None)
    def f(i, y, last):
        if y < 0:
            return 0
        if i == n:
            return 1 if y == 0 else 0
        t = f(i + 1, y, 'R')
        if last != 'D':
            t += f(i + 1, y + 1, 'U')
        if last != 'U':
            t += f(i + 1, y - 1, 'D')
        return t
    return f(0, 0, None)


def anchored_smooth(w, h):
    """1-smooth castles of width w and height h with first column at height 1."""
    def strips(hh):
        v = [1 if c == 1 else 0 for c in range(1, hh + 1)]
        for _ in range(w - 1):
            v = [sum(v[j] for j in (i - 1, i, i + 1) if 0 <= j < hh) for i in range(hh)]
        return sum(v)
    return strips(h) - (strips(h - 1) if h > 1 else 0)


def check(a, f, idx, rng):
    """Every listed term a(idx(x)) for x in rng equals f(x); returns (ok, number of terms compared)."""
    off, data = OEIS[a]
    n = 0
    for x in rng:
        i = idx(x) - off
        if 0 <= i < len(data):
            if data[i] != f(x):
                return False, n
            n += 1
    return True, n


def fmt(xs):
    return '`' + ', '.join(str(x) for x in xs) + '`'


def compute():
    """{row id: (anum, check result, terms text)} for every row this script fills."""
    R = {}
    def put(rid, a, f, idx, rng, shown):
        ok, n = check(a, f, idx, rng)
        R[rid] = (a, ok, n, fmt([f(x) for x in shown]))
    put('smooth1-14', 'A283667', lambda h: anchored_smooth(2 * h - 1, h), lambda h: h - 1, range(1, 9), range(1, 8))
    put('motzkin-14', 'A004149', cornerless_motzkin, lambda n: n + 1, range(0, 25), range(0, 14))
    put('motzkin-15', 'A080934', lambda m: dyck_paths(m, hmax=2), None, (), range(0, 9))   # checked below as a table
    put('motzkin-16', 'A080936', lambda m: dyck_paths(m, hexact=2), None, (), range(2, 9))
    for rid, a, par, side in [('zigzag-31', 'A153334', 'same', lambda n: n), ('zigzag-32', 'A153335', 'opp', lambda n: n),
                              ('zigzag-33', 'A153336', 'even', lambda n: 2 * n), ('zigzag-34', 'A153337', 'odd', lambda n: 2 * n - 1),
                              ('zigzag-35', 'A153338', 'even', lambda n: 2 * n - 1)]:
        def f(n, par=par, side=side):
            s = side(n)
            keep = {'same': lambda c: c % 2 == s % 2, 'opp': lambda c: c % 2 != s % 2,
                    'even': lambda c: c % 2 == 0, 'odd': lambda c: c % 2 == 1}[par]
            return zstrips(s, s, keep)
        put(rid, a, f, lambda n: n, range(1, 21), range(1, 9))
    put('ptower-13', 'A199833', lambda m: abs(signed_tower(2 * m + 1, 4)), lambda m: m + 1, range(0, 30), range(0, 9))
    put('ptower-11', 'A063496', lambda m: signed_tower(2 * m, 4), lambda m: m + 1, range(0, 30), range(0, 9))
    put('ptower-14', 'A352116', lambda k: abs(signed_tower(k, 4)), lambda k: k + 1, range(0, 40), range(0, 12))
    put('ptower-10', 'A009545', lambda w: sum((-1) ** blocks(c) for c in castles(w, 2) if c[-1] == 2), lambda w: w, range(1, 15), range(1, 13))
    put('castles-wh-9', 'A014105', lambda m: sum(1 for c in castles(3, 2 * m + 1) if blocks(c) % 2 == 0), lambda m: m, range(0, 11), range(0, 10))
    put('castles-wh-10', 'A000384', lambda m: sum(1 for c in castles(3, 2 * m) if blocks(c) % 2 == 1), lambda m: m, range(1, 11), range(1, 10))
    put('castles-wh-20', 'A038505', lambda w: sum(1 for c in castles(w, 2) if blocks(c) % 2 == 0), lambda w: w + 1, range(1, 15), range(1, 11))
    put('castles-wh-21', 'A038503', lambda w: sum(1 for c in castles(w, 2) if blocks(c) % 2 == 1) + 1, lambda w: w + 1, range(1, 15), ())
    R['castles-wh-21'] = R['castles-wh-21'][:3] + (fmt([sum(1 for c in castles(w, 2) if blocks(c) % 2 == 1) for w in range(1, 11)]),)
    put('castles-wh-22', 'A077860', lambda w: sum((-1) ** blocks(c) for c in castles(w, 2)), lambda w: w - 1, range(1, 15), range(1, 11))
    put('towers-blocks-4', 'A005408', lambda b: towers_by_blocks(2, b), lambda b: b, range(0, 9), range(0, 8))
    put('towers-blocks-5', 'A005891', lambda b: towers_by_blocks(3, b), lambda b: b, range(0, 9), range(0, 8))
    put('towers-blocks-6', 'A063490', lambda b: towers_by_blocks(4, b), lambda b: b + 1, range(0, 8), range(0, 8))
    put('towers-blocks-7', 'A160747', lambda b: towers_by_blocks(5, b), lambda b: b, range(0, 7), range(0, 7))
    put('tree-width-1', 'A001045', lambda w: tree_skylines(w, 3), lambda w: w + 2, range(1, 25), range(1, 9))
    put('tree-width-2', 'A006130', lambda w: tree_skylines(w, 4), lambda w: w + 1, range(1, 25), range(1, 9))
    put('tree-width-3', 'A006131', lambda w: tree_skylines(w, 5), lambda w: w + 1, range(1, 25), range(1, 9))
    put('tree-width-4', 'A000071', lambda w: sum(1 for c in castles(w, 2) if all(not (x == y == 2) for x, y in zip(c, c[1:]))),
        lambda w: w + 2, range(1, 15), range(1, 11))
    sp2 = semiperimeter_castles(18, allowed=(1, 2), need=2)
    put('semiper-11', 'A077855', lambda s: len(sp2.get(s, [])), lambda s: s - 3, range(3, 19), range(3, 15))
    sp3 = semiperimeter_castles(18, allowed=(1, 3), need=3)
    put('semiper-12', 'A130578', lambda s: len(sp3.get(s, [])), lambda s: s - 1, range(2, 19), range(4, 16))
    put('classical-4', 'A001523', lambda n: sum(1 for c in compositions(n) if weakly_unimodal(c)), lambda n: n, range(1, 16), range(1, 13))
    put('classical-5', 'A011782', lambda n: sum(1 for _ in compositions(n)), lambda n: n, range(1, 16), range(1, 13))
    put('classical-6', 'A115981', lambda n: sum(1 for c in compositions(n) if not weakly_unimodal(c)), lambda n: n, range(1, 16), range(1, 13))
    put('classical-7', 'A332578', lambda n: sum(1 for c in compositions(n) if vee(c)), lambda n: n, range(1, 16), range(1, 13))
    put('classical-8', 'A332669', lambda n: sum(1 for c in compositions(n) if not vee(c)), lambda n: n, range(1, 16), range(1, 13))
    return R


def tables():
    """The rows read from OEIS tables: A080934, A080936, A271940, and the A112742 split."""
    out = {}
    # A080934, read by antidiagonals d = n + k, entries T(n, d - n) for n = 0..d
    off, data = OEIS['A080934']
    T, i, d = {}, 0, 0
    while i < len(data):
        for n in range(d + 1):
            if i < len(data):
                T[(n, d - n)] = data[i]; i += 1
        d += 1
    out['A080934'] = all(dyck_paths(n, hmax=k) == v for (n, k), v in T.items()), len(T)
    # A080936, rows n >= 1, k = 1..n
    off, data = OEIS['A080936']
    T, i, n = {}, 0, 1
    while i < len(data):
        for k in range(1, n + 1):
            if i < len(data):
                T[(n, k)] = data[i]; i += 1
        n += 1
    out['A080936'] = all(dyck_paths(n, hexact=k) == v for (n, k), v in T.items()), len(T)
    # A271940, rows n >= 2 (semi-perimeter), k >= 1 peaks, each row up to its last nonzero entry
    sp = semiperimeter_castles(14)
    rows = {s: {} for s in range(2, 15)}
    for s in rows:
        for c in sp.get(s, []):
            rows[s][peaks(c)] = rows[s].get(peaks(c), 0) + 1
    flat = [rows[s].get(k, 0) for s in range(2, 15) for k in range(1, max(rows[s]) + 1)]
    off, data = OEIS['A271940']
    out['A271940'] = flat == data[:len(flat)], len(flat)
    out['A271940 rows'] = '; '.join(', '.join(str(rows[s][k]) for k in sorted(rows[s])) for s in range(2, 10))
    # A112742: P(k, 5) = (-1)^k A_5(k) + B_5(k) with A_5, B_5 polynomials; interpolate the even and odd k separately
    P = [signed_tower(k, 5) for k in range(0, 30)]
    def interp(pts):
        def f(x):
            tot = Fraction(0)
            for i, (xi, yi) in enumerate(pts):
                term = Fraction(yi)
                for j, (xj, _) in enumerate(pts):
                    if j != i:
                        term *= Fraction(x - xj, xi - xj)
                tot += term
            return tot
        return f
    E = interp([(k, P[k]) for k in range(0, 20, 2)][:6]); O = interp([(k, P[k]) for k in range(1, 20, 2)][:6])
    poly_ok = all(E(k) == P[k] for k in range(0, 30, 2)) and all(O(k) == P[k] for k in range(1, 30, 2))
    A5 = [(E(k) - O(k)) / 2 for k in range(0, 12)]
    off, data = OEIS['A112742']
    out['A112742'] = poly_ok and all(A5[k] == data[k + 1 - off] for k in range(0, 12)), 12
    out['A112742 terms'] = fmt([int(x) for x in A5[:9]])
    return out


if __name__ == '__main__':
    R = compute()
    for rid, (a, ok, n, terms) in R.items():
        print('[1] %-16s %s  agrees on %2d terms: %s   %s' % (rid, a, n, ok, terms))
    t = tables()
    print('[2] A080934 square array (antidiagonals) = Dyck paths of semilength n and height <= k, every listed entry: %s (%d entries)' % t['A080934'])
    print('[2] A080936 triangle = Dyck paths of semilength n and height k, every listed entry: %s (%d entries)' % t['A080936'])
    print('[2] A271940 = castles by semi-perimeter s and Deutsch-Elizalde peaks, rows s = 2..14: %s (%d entries)' % t['A271940'])
    print('[2] A271940 rows s = 2..9:', t['A271940 rows'])
    print('[3] P(k, 5) = (-1)^k A_5(k) + B_5(k) with polynomial A_5, B_5 (k < 30), and A_5(k) = A112742(k + 1): %s; A_5 = %s' % (t['A112742'][0], t['A112742 terms']))
    print('[4] all checks pass:', all(v[1] for k, v in R.items() if k not in ('motzkin-15', 'motzkin-16')) and t['A080934'][0] and t['A080936'][0] and t['A271940'][0] and t['A112742'][0])
