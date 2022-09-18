MOD = 1000000007
n, k = map(int, input().split())
if 1 in [k, n - k]:
    print(n)
elif k in [0, n]:
    print(1)
else:
    a = b = 1
    for i in range(n, n - k, -1):
        a = a * i % MOD
    for i in range(1, k + 1):
        b = b * i % MOD
    print(((a % MOD) * pow(b, MOD - 2, MOD) % MOD) % MOD)
