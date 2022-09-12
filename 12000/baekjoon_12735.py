MOD = 1000000007
MAX = 500
result = 0
inv = [0]
dp1 = [1] + [0 for _ in range(MAX)]
dp2 = [[0 for _ in range(MAX + 1)] for _ in range(MAX + 1)]
s, e = [0 for _ in range(MAX + 1)], [0 for _ in range(MAX + 1)]
values = [0 for _ in range(MAX + 1)]
v = []
n = int(input())
for i in range(1, n + 1):
    s[i], e[i] = map(int, input().split())
    e[i] += 1
    v += [s[i], e[i]]
v = sorted(set(v))
for i in range(1, 1001):
    inv.append(pow(i, MOD - 2, MOD))
for i in range(1, len(v)):
    cnd = []
    st, ed = v[i - 1:i + 1]
    values[0] = 1
    for j in range(1, n + 1):
        values[j] = (values[j - 1] + dp1[j]) % MOD
        if s[j] <= st and ed <= e[j]:
            cnd.append(j)
    for i in range(1, min(len(cnd), ed - st) + 1):
        for j in range(i - 1, len(cnd)):
            if i == 1:
                dp2[i][j] = values[cnd[j] - 1] * (ed - st)
                if j:
                    dp2[i][j] += dp2[i][j - 1]
                dp2[i][j] %= MOD
            else:
                dp2[i][j] = ((dp2[i - 1][j - 1] * inv[i] % MOD) * (ed - st - i + 1) + dp2[i][j - 1]) % MOD
    for i in range(1, min(len(cnd), ed - st) + 1):
        for j in range(i - 1, len(cnd)):
            cnt = (dp2[i][j] - (dp2[i][j - 1] if j else 0) + MOD) % MOD
            dp1[cnd[j]] = (dp1[cnd[j]] + cnt) % MOD
for i in range(1, n + 1):
    result += dp1[i]
print(result % MOD)
