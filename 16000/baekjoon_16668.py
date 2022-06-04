MAX = 401
f = [1] + [0 for _ in range(MAX - 1)]
dp = [[0 for _ in range(MAX)] for _ in range(MAX)]
dp[0][0] = 1
t, p = map(int, input().split())
for i in range(1, MAX):
    f[i] = f[i - 1] * i % p
for i in range(1, MAX):
    for j in range(MAX):
        for k in range(1, j + 1):
            dp[i][j] += dp[i - 1][j - k] * f[k] % p
        dp[i][j] %= p
order = f[:]
result = f[:]
for i in range(1, MAX):
    for j in range(3, i):
        result[i] += p - result[j] * dp[j][i] % p
    for j in range(1, i):
        order[i] += p - order[j] * f[i - j] % p
        if i > 2:
            result[i] += p - (order[j] * f[i - j] * 2) % p
    result[i] %= p
    order[i] %= p
for _ in range(t):
    print(result[int(input())])
