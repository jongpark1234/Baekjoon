def dp(h, m, p):
    n = len(p)
    if p[n - 1] > p[n - 2]:
        return 0
    ret = 0
    numlist = [0 for _ in range(n)]
    for i in range(1 << n):
        b = i & 1
        numlist[0] = i & 1
        s = 0
        g = table[numlist[0]][h][p[0]]
        for j in range(1, n):
            numlist[j] = (i >> j) & 1
            b += numlist[j]
            if p[j - 1] == p[j] and numlist[j - 1] < numlist[j]:
                break
            s = [0, s + 1][p[j - 1] == p[j] and numlist[j - 1] == numlist[j]]
            g = g * (table[numlist[j]][h][p[j]] + s) // (s + 1)
        else:
            if b <= n - m:
                ret += g
        continue
    return ret
result = 0
n = int(input())
table = [[[0 for _ in range(n + 1)] for _ in range(n // 2 + 1)] for _ in range(2)]
table[0][0][0] = 1
for i in range(1, n // 2 + 1):
    table[1][i][0] = 1
    for j in range(1, n + 1):
        for k in range(i - 1, j):
            for l in range(min(k, j - k - 1) + 1):
                table[0][i][j] += dp(i - 1, 1, [k, l, j - 1 - k - l])
        table[1][i][j] = table[1][i - 1][j] + table[0][i - 1][j]
for i in range(1, n + 1):
    h = i // 2
    if i & 1 == 0:
        for j in range(h, n):
            result += dp(h, 2, [j, n - j])
    else:
        for j in range(h, n):
            for k in range(h, min(j, n - j - 1) + 1):
                for l in range(min(k, n - j - k - 1) + 1):
                    result += dp(h, 2, [j, k, l, n - j - k - l - 1])
print(result)
