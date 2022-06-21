MOD = 7340033
def resize(arr, t):
    if t <= len(arr):
        return arr[:t]
    else:
        return arr + [0 for _ in range(t - len(arr))]
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
        k = -(x[i] - t) * pow(ld, MOD - 2, MOD) % MOD
        c = [0 for _ in range(i - lf - 1)] + [k]
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
print(guess_nth_term([1, 2, 4, 4, 6, 10, 12, 14, 22, 26, 30, 44, 56, 70, 98, 130, 162, 216, 292, 358, 470, 628, 792, 1050, 1384, 1788, 2334, 3072, 3974, 5162, 6784, 8786, 11420, 14992, 19484, 25388, 33160, 43262, 56252, 73392, 95798, 124496, 162556, 212048, 275976, 360154, 469694, 611844, 797628, 1040344, 1355550, 1766402, 2304368, 3002354, 3913802, 5103798, 6651808, 1330929, 3964467, 56364, 4526934, 3020079, 3283660, 5845937, 4089463, 6249217, 6173168, 5434618, 6035817, 3277472, 599541, 2502130, 101659, 1046904, 615205, 4310505, 7073937, 1528843, 1573423, 628109, 3338517, 7141678, 6639170, 7199721, 2508559, 6983719, 3226808, 1362909, 4057445, 5216401, 4789473, 7148607, 3490252, 3859839, 3919928, 4410603, 1774464, 5030371, 3213868, 3673656, 2253480, 162153, 6967672, 6212357, 1488891, 5272969, 2288129, 3900589, 6122846, 6177603, 475903, 151346, 4687899, 1154734, 4168110, 1744680, 1925769, 3198859, 1886183, 702652, 4959058, 6769965, 4832688, 6752128, 5192022, 872961, 2974929, 4528640, 4768052, 929662, 5895668, 7181370, 6213930, 7284455, 594448, 3091509, 5305389, 2707419, 3941867, 1121753, 845827, 3309438, 595600, 781040, 946746, 13034, 2718932, 7085679, 3266476, 5093050], int(input())))
