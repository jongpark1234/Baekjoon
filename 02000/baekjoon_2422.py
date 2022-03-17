from sys import stdin
n, m = map(int, stdin.readline().split())
comb = [[False for _ in range(n)] for _ in range(n)]
for i in range(m):
    a, b = map(int, stdin.readline().split())
    comb[a - 1][b - 1] = True
    comb[b - 1][a - 1] = True
cnt = 0
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if not comb[i][j] and not comb[i][k] and not comb[j][k]:
                cnt += 1
print(cnt)
