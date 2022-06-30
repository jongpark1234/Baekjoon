MOD = 1000000007
jc, b = [1], [1]
for i in range(1, 102):
    jc.append(jc[i - 1] * i % MOD)
for i in range(1, 10001):
    b.append(b[i - 1] * 2 % MOD)
n = int(input())
if n == 1:
    print(1, 0, 0, sep = '\n')
elif n == 2:
    print(2, 1, 0, sep = '\n')
elif n == 3:
    print(12, 6, 6, sep = '\n')
else:
    print(jc[n] * b[(n - 2) * (n - 1) // 2] % MOD, jc[n + 1] * b[(n + 1) * (n - 4) // 2] % MOD, jc[n] * n % MOD * b[(n + 1) * (n - 4) // 2] % MOD, sep = '\n')
