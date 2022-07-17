MOD = 998244353
INV = 796898467
n, k, x = map(int, input().split())
invlist, p = [0, 1], []
for i in range(2, x + 1):
    invlist.append(MOD - (MOD // i) * invlist[MOD % i] % MOD)
for i in map(float, input().split()):
    p.append(round(i * 10000) * INV % MOD)
q = [pow(p[0], n, MOD)]
invertedP = pow(p[0], MOD - 2, MOD)
for i in range(x):
    temp, j = 0, 1
    while j <= k and j <= i + 1:
        temp = (temp + ((n + 1) * j % MOD - i + MOD - 1) * p[j] % MOD * q[i - j + 1]) % MOD
        j += 1
    q.append(temp * invertedP % MOD * invlist[i + 1] % MOD)
result, temp = 0, 1
for i in range(x):
    result = (result + q[i] * i) % MOD
    temp -= q[i]
    temp += (temp >> 31) & MOD
print((result + temp * x) % MOD)
