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
m, k = map(int, input().split())
ei = [0 for _ in range(k + 1)]
bags = [0, 1]
for i in range(2, k + 1):
    for j in range(i, k + 1, i):
        if not ei[j]:
            ei[j] = i
for i in range(2, k + 1):
    if ei[i] == i:
        bags.append(-1)
    else:
        if ei[i // ei[i]] == ei[i]:
            bags.append(0)
        else:
            bags.append(-bags[i // ei[i]])
for i in range(1, k + 1):
    result += (MOD + bags[i]) * (power((k // i) * 2 + 1, m) - 1)
    result %= MOD
print(result + 1)
