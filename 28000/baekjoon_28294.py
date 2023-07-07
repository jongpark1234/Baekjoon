MOD = 1_000_000_007
n, a = map(int, input().split())
print((MOD + pow(n, a + 1, MOD) + pow(n - 1, a - 1, MOD) - pow(n - 1, a + 1, MOD)) % MOD * (n - 1) % MOD)
