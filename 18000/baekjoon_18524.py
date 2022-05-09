MOD = 998244353
def power(x, y):
    r = 1
    x %= MOD
    while y:
        if y & 1:
            r = (r * x) % MOD
        y >>= 1
        x = x ** 2 % MOD
    return r
result = 0
m, n = map(int, input().split())
low = [0 for _ in range(n + 1)]
bags = [0, 1]
for i in range(2, n + 1):
    for j in range(i, n + 1, i):
        if not low[j]:
            low[j] = i
for i in range(2, n + 1):
    if low[i] == i:
        bags.append(-1)
    else:
        if low[i // low[i]] == low[i]:
            bags.append(0)
        else:
            bags.append(-bags[i // low[i]])
for i in range(1, n + 1):
    result += (MOD + bags[i]) * (power((n // i) * 2 + 1, m) - 1)
    result %= MOD
print(result + 1)
