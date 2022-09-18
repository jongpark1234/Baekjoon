from sys import stdin
MOD = 1000000007
factorial = [1, 1]
for i in range(1, 4000001):
    factorial.append(factorial[i] * (i + 1) % MOD)
for _ in range(int(input())):
    n, k = map(int, stdin.readline().split())
    print(factorial[n] * pow(factorial[k] * factorial[n - k] % MOD, MOD - 2, MOD) % MOD)
