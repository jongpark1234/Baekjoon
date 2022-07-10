from collections import deque
def mod(x):
    return x if x < MOD else x - MOD
def bfs(x, y):
    global d
    d = [[-1 for _ in range(101)] for _ in range(101)]
    d[x][y] = 0
    q = deque([[x, y]])
    while q:
        a, b = q.popleft()
        for i in range(4):
            t1, t2 = a + dx[i], b + dy[i]
            if 1 <= t1 <= total1 and 1 <= t2 <= total2 and not banned[t1][t2] and d[t1][t2] == -1:
                d[t1][t2] = d[a][b] + 1
                q.append([t1, t2])
MOD = 1000000007
arr = [0 for _ in range(1000001)]
idx1, idx2, s1, s2, numarr1, numarr2 = arr[:], arr[:], arr[:], arr[:], arr[:], arr[:]
numlist1, numlist2 = [0], [0]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
total1 = total2 = 0
banned = [[0 for _ in range(100)] for _ in range(100)]
d = [[-1 for _ in range(101)] for _ in range(101)]
result = 0
h, w = map(int, input().split())
n = int(input())
for _ in range(n):
    x, y = map(lambda x: int(x) + 1, input().split())
    numlist1.append(x)
    numlist2.append(y)
    s1[x] += 1
    s2[y] += 1
for i in range(1, h + 1):
    s1[i] += s1[i - 1]
    if i >= 2 and s1[i] == s1[i - 2]:
        idx1[i] = idx1[i - 1]
        result = mod(result + mod((i - 1) * w % MOD + MOD - s1[i - 1]) * mod((h - i + 1) * w % MOD + MOD - (n - s1[i - 1])) % MOD)
    else:
        total1 += 1
        idx1[i] = total1
    numarr1[idx1[i]] += 1
for i in range(1, w + 1):
    s2[i] += s2[i - 1]
    if i >= 2 and s2[i] == s2[i - 2]:
        idx2[i] = idx2[i - 1]
        result = mod(result + mod((i - 1) * h % MOD + MOD - s2[i - 1]) * mod((w - i + 1) * h % MOD + MOD - (n - s2[i - 1])) % MOD)
    else:
        total2 += 1
        idx2[i] = total2
    numarr2[idx2[i]] += 1
for i in range(1, n + 1):
    banned[idx1[numlist1[i]]][idx2[numlist2[i]]] = 1
for i in range(1, total1 + 1):
    for j in range(1, total2 + 1):
        if not banned[i][j]:
            temp = 0
            bfs(i, j)
            for k in range(i, total1 + 1):
                for l in range(j + 1 if k == i else 1, total2 + 1):
                    if not banned[k][l]:
                        temp = mod(temp + numarr1[k] * numarr2[l] % MOD * d[k][l] % MOD)
            result = mod(result + numarr1[i] * numarr2[j] % MOD * temp % MOD)
print(result)
