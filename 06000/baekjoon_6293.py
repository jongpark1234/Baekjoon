MAX = 10
n = int(input())
s = list(input())
e = True
result = idx = 0
idxlist = [0 for _ in range(n + 1)]
dp1 = [[float('inf') for _ in range(MAX)] for _ in range(n)]
dp2 = [[[float('inf') for _ in range(MAX)] for _ in range(MAX)] for _ in range(n)]
for i in range(n):
    if s[i] != 'e':
        s[idx], idxlist[idx] = s[i], e
        idx += 1
        e = False
    else:
        result += (idx != 0) + 1
        e = True
s[idx], s[idx + 1] = 'e', 0
s[idx + 1] = dp1[0][ord(s[0]) - 97] = 0
for i in range(idx):
    char = ord(s[i]) - 97
    for j in range(MAX):
        x = dp1[i][j]
        if x == float('inf'):
            continue
        if j != char:
            if not idxlist[i]:
                dp1[i + 1][j] = min(dp1[i + 1][j], x)
            for k in range(MAX):
                dp2[i + 1][j][k] = min(dp2[i + 1][j][k], x + 3)
        else:
            for k in range(MAX):
                dp1[i + 1][k] = min(dp1[i + 1][k], x + 2)
                for l in range(MAX):
                    dp2[i + 1][k][l] = min(dp2[i + 1][k][l], x + 5)
    for j in range(MAX):
        for k in range(MAX):
            x = dp2[i][j][k]
            if x == float('inf'):
                continue
            if j != char and k != char:
                dp2[i + 1][j][k] = min(dp2[i + 1][j][k], x + 1)
            elif j != char and k == char:
                for l in range(MAX):
                    dp2[i + 1][j][l] = min(dp2[i + 1][j][l], x + 3)
            elif j == char and k != char:
                dp1[i + 1][k] = min(dp1[i + 1][k], x)
                for l in range(MAX):
                    dp2[i + 1][l][k] = min(dp2[i + 1][l][k], x + 3)
            else:
                for l in range(MAX):
                    dp1[i + 1][l] = min(dp1[i + 1][l], x + 2)
                    for m in range(MAX):
                        dp2[i + 1][m][l] = min(dp2[i + 1][m][l], x + 5)
print(result + dp1[idx][4] - 2)
