MOD = 998244353
SIZE = 200000
def calc(n: int, m: int) -> int:
    return 0 if n < m or m < 0 else factorial[n] * invFactorial[m] % MOD * invFactorial[n - m] % MOD
def solve(x: int, numlist: list, idx: int) -> None:
    temp = (((numlist[x] != (n << 1)) * calc(numlist[x] - x, n - x) * ilist[numlist[x]]) + numlist2[numlist[x] + 1]) % MOD
    for i in range(x + 1):
        if numlist[i] < numlist[i + 1]:
            temp = (temp + (numlist1[numlist[i + 1] - i - 1] - numlist1[numlist[i] - i] + MOD) * ilist[i]) % MOD
    result[idx] = (temp << 1) % MOD
factorial = [1] + [0 for _ in range(200002)]
invFactorial = [0 for _ in range(200002)]
ilist = [1] + [0 for _ in range(200002)]
numlist1 = [0 for _ in range(200002)]
numlist2 = [0 for _ in range(200002)]
result = [0 for _ in range(200002)]
v = [[] for _ in range(100001)]
q = [[] for _ in range(100001)]
n, m = map(int, input().split())
for i in range(1, SIZE + 1):
    factorial[i] = factorial[i - 1] * i % MOD
invFactorial[SIZE] = pow(factorial[SIZE], MOD - 2, MOD)
for i in range(SIZE, 0, -1):
    invFactorial[i - 1] = invFactorial[i] * i % MOD
for i in range(1, SIZE + 1):
    ilist[i] = ((MOD + 1) >> 1) * ilist[i - 1] % MOD
for i in range(1, m + 1):
    Input = list(map(int, input().split()))
    q[Input[0]] += [i]
    v[i] += [0]
    for j in Input[1:]:
        v[i] += [j]
    v[i] += [n << 1]
for i in range(1, (n << 1) + 1):
    numlist1[i] = (calc(i - 1, n - 1) * ilist[i] + numlist1[i - 1]) % MOD
for i in range(2, n + 1):
    if q[i]:
        for j in range((n << 1) - 1, 0, -1):
            numlist2[j] = (calc(j - i - 1, n - i - 1) * ilist[j] + numlist2[j + 1]) % MOD
        for j in q[i]:
            solve(i, v[j], j)
print('\n'.join(map(str, result[1:m + 1])))
