def d(n: int, m: int) -> int:
    return 0 if m < 0 or n < m else numlist1[n] * numlist2[n - m] % MOD * numlist2[m] % MOD
def calc(i: int, j: int) -> int:
    return 1 if j == 0 else d((j << 1) + i - 1, j) - d((j << 1) + i - 1, j - 1)
MOD = 998244353
numlist1 = [1, 1] + [0 for _ in range(3000000)]
numlist2 = [1, 1] + [0 for _ in range(3000000)]
inverted = [0, 1] + [0 for _ in range(3000000)]
result, acc = 0, 1
n, m, k = map(int, input().split())
for i in range(2, n + (m << 1) + 1):
    numlist1[i] = i * numlist1[i - 1] % MOD
    inverted[i] = MOD - (MOD // i) * inverted[MOD % i] % MOD
    numlist2[i] = inverted[i] * numlist2[i - 1] % MOD
mul = calc(1, k)
mul += (mul >> 31) & MOD
for i in range(min(m // k, n) + 1):
    w = (calc(n - i, m - i * k) + MOD) * d(n, i) % MOD * acc % MOD
    if i & 1:
        result -= w
    else:
        result += w - MOD
    result += (result >> 31) & MOD
    acc = acc * mul % MOD
print(result)
