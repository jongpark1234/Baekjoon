MOD = 1000000009
def resize(arr, t):
    if t <= len(arr):
        return arr[:t]
    else:
        return arr + [0 for _ in range(t - len(arr))]
def power(x, y):
    r = 1
    x %= MOD
    while y:
        if y & 1:
            r = (r * x) % MOD
        y >>= 1
        x = x ** 2 % MOD
    return r
def multiply(v, w, rec):
    m = len(v)
    t = [0 for _ in range(m * 2)]
    for i in range(m):
        for j in range(m):
            t[i + j] += v[i] * w[j] % MOD
            if t[i + j] >= MOD:
                t[i + j] -= MOD
    for i in range(m, 2 * m)[::-1]:
        for j in range(1, m + 1):
            t[i - j] += t[i] * rec[j - 1] % MOD
            if t[i - j] >= MOD:
                t[i - j] -= MOD
    t = resize(t, m)
    return t
def berlekamp_massey(x):
    ls, cur = [], []
    for i in range(len(x)):
        t = 0
        for j in range(len(cur)):
            t += x[i - j - 1] * cur[j]
            t %= MOD
        if (t - x[i]) % MOD == 0:
            continue
        if not cur:
            cur = resize(cur, i + 1)
            lf = i
            ld = (t - x[i]) % MOD
            continue
        k = -(x[i] - t) * power(ld, MOD - 2) % MOD
        c = [0 for _ in range(i - lf - 1)]
        c.append(k)
        for j in ls:
            c.append(-j * k % MOD)
        if len(c) < len(cur):
            c = resize(c, len(cur))
        for j in range(len(cur)):
            c[j] = (c[j] + cur[j]) % MOD
        if i - lf + len(ls) >= len(cur):
            ls, lf, ld = cur, i, (t - x[i]) % MOD
        cur = c[:]
    for i in range(len(cur)):
        cur[i] = (cur[i] % MOD + MOD) % MOD
    return cur
def get_nth(rec, numlist, n):
    m = len(rec)
    s = [1] + [0 for _ in range(m - 1)]
    t = [0, 1] + [0 for _ in range(m - 2)] if m != 1 else [rec[0]] + [0 for _ in range(m - 1)]
    while n:
        if n & 1:
            s = multiply(s, t, rec)
        t = multiply(t, t, rec)
        n >>= 1
    result = 0
    for i in range(m):
        result += s[i] * numlist[i] % MOD
    return result % MOD
def guess_nth_term(x, n):
    return x[n] if n < len(x) else 0 if not (v := berlekamp_massey(x)) else get_nth(v, x, n)
dp = [[2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576, 2097152, 4194304, 8388608, 16777216, 33554432, 67108864, 134217728, 268435456, 536870912, 73741815, 147483630, 294967260, 589934520, 179869031, 359738062, 719476124, 438952239, 877904478, 755808947, 511617885, 23235761, 46471522, 92943044, 185886088, 371772176, 743544352, 487088695, 974177390, 948354771, 896709533], [4, 16, 36, 81, 225, 625, 1600, 4096, 10816, 28561, 74529, 194481, 509796, 1336336, 3496900, 9150625, 23961025, 62742241, 164249856, 429981696, 125736695, 947295503, 716041218, 200652461, 886200432, 458408758, 488281642, 5232020, 529362765, 586008745, 223562643, 76425889, 19069136, 2388928, 953136135, 800450530, 539745896, 966886539, 121283871, 9235872, 533782787, 607200726, 645372102, 671380047, 668750842, 292390808, 950920440, 345351007, 557653218, 15148755], [8, 36, 94, 278, 1062, 3650, 11856, 39444, 135704, 456980, 1534668, 5166204, 17480600, 58888528, 198548648, 669291696, 258436230, 613387281, 676312919, 575341762, 991128221, 557546496, 284542480, 209398972, 232230803, 303596263, 939962513, 351290213, 415931359, 328520111, 887554940, 303667674, 351233655, 747600119, 130781946, 702928593, 155509746, 538853820, 548779965, 726903524, 370846848, 989333901, 795920339, 432839282, 815115627, 902444432, 3195020, 783730971, 232305131, 894592622], [16, 81, 278, 1365, 7164, 33858, 161307, 791722, 3859473, 18702843, 90938441, 442661923, 152542080, 466805482, 911253057, 627500238, 355979736, 651184968, 444168477, 637675570, 340713937, 193363675, 666524059, 932645942, 897647645, 834763352, 662912921, 725854997, 840822360, 61565774, 135123018, 995036230, 730107533, 462094335, 710509782, 525321589, 949550086, 8069878, 739604600, 955573146, 817055186, 27292242, 254984760, 388463753, 467535957, 483265312, 352974171, 592298092, 268922749, 66458109]]
for _ in range(int(input())):
    result = []
    m, n = map(int, input().split())
    for i in range(50):
        result.append(dp[m - 1][i])
    print(guess_nth_term(result, n - 1))
