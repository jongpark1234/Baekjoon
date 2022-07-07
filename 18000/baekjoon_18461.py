MOD = 998244353
def dfs(d, s, up):
    global result
    if not s:
        numlist2, temp = [0 for _ in range(n + 2)], faced[n]
        for i in numlist1[1:d]:
            numlist2[i] += 1
        for i in range(1, n + 1)[::-1]:
            numlist2[i] += numlist2[i + 1]
        for i in range(1, d):
            for j in range(1, numlist1[i] + 1):
                temp = temp * inverted[numlist1[i] + numlist2[j] - i - j + 1] % MOD
        result = (result + temp ** 2) % MOD
    for i in range(1, min(s, up) + 1):
        numlist1[d] = i
        dfs(d + 1, s - i, i)
result = 0
inverted, faced = [0], [1]
n = int(input())
for i in range(1, n + 1):
    inverted.append(1 if i == 1 else (MOD - MOD // i) * inverted[MOD % i] % MOD)
    faced.append(faced[i - 1] * i % MOD)
for i in range(1, (n >> 1) + 1):
    numlist1 = [0, i, i] + [0 for _ in range(n + 2)]
    dfs(3, n - (i << 1), i)
print(result)
