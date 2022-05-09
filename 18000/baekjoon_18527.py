n, t = map(int, input().split())
result = t - n + 1 - (Sum := sum(x := [int(input()) - 1 for _ in range(n)]))
for i in range(1, n):
    Sum -= x[i - 1]
    result *= t - Sum + 1
    result %= 998244353
print(result)
