def calc(x):
    x += (x >> 31) & MOD
    return x
MOD = 998244353
result = 0
arr = [0 for _ in range(5001)]
numlist1, numlist2 = arr[:], arr[:]
c = [arr[:] for _ in range(5001)]
n = int(input())
a = [0] + sorted(list(map(int, input().split())))
a.append(a[-1])
for i in range(5001):
    c[i][0] = 1
    for j in range(c[i][0], i + 1):
        c[i][j] = calc(c[i - 1][j - 1] + c[i - 1][j] - MOD)
for i in range(a[1] + 1):
    numlist2[i] = c[a[1]][i]
for i in range(1, n + 1):
    result, numlist1[a[i]] = calc(result + numlist2[1] - MOD), 0
    for j in range(a[i]):
        numlist1[j] = (numlist2[j + 1] * c[j + 1][2] << 1) % MOD
    for j in range(a[i] + 1):
        numlist1[j] = calc(numlist1[j] + numlist2[j] - MOD)
    for j in range(a[i + 1] + 1):
        numlist2[j] = 0
    for j in range(a[i] + 1):
        for k in range(a[i + 1] - a[i] + 1):
            numlist2[j + k] = (numlist2[j + k] + numlist1[j] * c[a[i + 1] - a[i]][k]) % MOD
for i in range(n):
    result = calc(result - a[i + 1])
print(result * (MOD + 1 >> 1) % MOD)
