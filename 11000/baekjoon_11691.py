SIZE = 1000001
MOD = 1000000007
result = 0
v = []
bit = [[] for _ in range(128)]
mobius = [0 for _ in range(SIZE)]
dp = [0 for _ in range(SIZE)]
def dec(n: int) -> None:
    v.clear()
    while n != 1:
        if not v or v[-1] != mobius[n]:
            v.append(mobius[n])
        n //= mobius[n]
def calc(n: int) -> int:
    ret = n * (n + 1) >> 1
    size = len(v)
    for i in range(1, 1 << size):
        temp, length = 1, len(bit[i])
        for j in range(length):
            temp *= v[bit[i][j]]
        u = n // temp
        T = temp * (u * (u + 1) >> 1)
        ret += T * (-1 if length & 1 else 1)
    return ret * n
for i in range(2, SIZE):
    if not mobius[i]:
        for j in range(i, SIZE, i):
            mobius[j] = i
for i in range(1, 128):
    for j in range(7):
        if i & (1 << j):
            bit[i].append(j)
n = int(input())
for i in range(2, n + 1):
    dec(i)
    dp[i] = (dp[i - 1] + calc(i)) % MOD
for i in range(1, n + 1):
    result = (result + dp[n // i] * i) % MOD
print(result)
