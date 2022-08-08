MOD = 998244353
n, k = map(lambda x: int(x) - 1, input().split())
temp, f, result = n + 1, 1, 1
for i in range(2, int(temp ** 0.5) + 1):
    if temp % i == 0:
        temp //= i
        result *= i - 1
        while temp % i == 0:
            temp //= i
            result *= i
if temp > 1:
    result *= temp - 1
for i in range(k):
    result = result * (n - i) % MOD
for i in range(1, k + 1):
    f = f * i % MOD
f = pow(f, MOD - 2, MOD)
print(result * f % MOD)
