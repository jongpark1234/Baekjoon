notZero = True
result = pos = 0
MAX = 10 ** 8
n, m = map(int, input().split())
x = [int(input()) for _ in range(n)]
l = [[[0, 0] for _ in range(n + 1)] for _ in range(n + 1)]
r = [[[0, 0] for _ in range(n + 1)] for _ in range(n + 1)]
for i in range(n):
    if x[i] == 0:
        notZero = False
        break
else:
    x += [0]
    n += 1 
x.sort()
for i in range(n):
    if not x[i]:
        pos = i
        break
for i in range(1, n):
    for j in range(n):
        for k in range(j, n):
            l[j][k][i & 1] = r[j][k][i & 1] = MAX
            if j >= 1:
                l[j][k][i & 1] = min(l[j][k][i & 1], l[j - 1][k][(i + 1) % 2] + i * (x[j] - x[j - 1]))
                r[j][k][i & 1] = min(r[j][k][i & 1], l[j - 1][k][(i + 1) % 2] + i * (x[k] - x[j - 1]))
            if k < n - 1:
                l[j][k][i & 1] = min(l[j][k][i & 1], r[j][k + 1][(i + 1) % 2] + i * (x[k + 1] - x[j]))
                r[j][k][i & 1] = min(r[j][k][i & 1], r[j][k + 1][(i + 1) % 2] + i * (x[k + 1] - x[k]))
    result = max(result, m * i - l[pos][pos][i & 1])
print(result + [m, 0][notZero])
