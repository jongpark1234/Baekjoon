MOD = 1000000007
def resize(arr, t):
    if t <= len(arr):
        return arr[:t]
    else:
        return arr + [0 for _ in range(t - len(arr))]
def multiply(v, w, rec):
    m = len(v)
    t = [0 for _ in range(m << 1)]
    for i in range(m):
        for j in range(m):
            t[i + j] += v[i] * w[j] % MOD
            if t[i + j] >= MOD:
                t[i + j] -= MOD
    for i in range(m * 2 - 1, m - 1, -1):
        for j in range(1, m + 1):
            t[i - j] += t[i] * rec[j - 1] % MOD
            if t[i - j] >= MOD:
                t[i - j] -= MOD
    return resize(t, m)
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
    ret = 0
    m = len(rec)
    s = [1] + [0 for _ in range(m - 1)]
    t = [0, 1] + [0 for _ in range(m - 2)] if m != 1 else [rec[0]] + [0 for _ in range(m - 1)]
    while n:
        if n & 1:
            s = multiply(s, t, rec)
        t = multiply(t, t, rec)
        n >>= 1
    for i in range(m):
        ret += s[i] * numlist[i] % MOD
    return ret % MOD
def guess_nth_term(x, n):
    return x[n] if n < len(x) else 0 if not (v := berlekamp_massey(x)) else get_nth(v, x, n)
dp = [[0 for _ in range(1000)] for _ in range(2000)]
n, m = map(int, input().split())
a = list(map(int, input().split()))
dp[0][0] = a[0]
for i in range(1, m):
    dp[0][i] = (dp[0][i - 1] + a[i]) % MOD
for i in range(1, m << 1):
    dp[i][0] = (dp[i - 1][0] * a[0]) % MOD
for i in range(1, m):
    for j in range(1, m << 1):
        dp[j][i] = (dp[j - 1][i] * a[i] + dp[j][i - 1]) % MOD
print(guess_nth_term([dp[i][m - 1] for i in range(m << 1)], n - 1))
