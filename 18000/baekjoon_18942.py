def dnc(k: int, l: int, r: int, opl: int, opr: int) -> None:
    if l > r:
        return
    mid, pos = l + r >> 1, -1
    for i in range(opl, min(opr + 1, mid - 1)):
        t = f[k - 1][i] + w[i + 1][mid - 1] + p
        if t > f[k][mid]:
            f[k][mid], pos = t, i
    dnc(k, l, mid - 1, opl, pos)
    dnc(k, mid + 1, r, pos, opr)
n, k, p = map(int, input().split())
a = [0] + list(map(int, input().split()))
c = [0] + list(map(int, input().split()))
f = [[-float('inf') for _ in range(2001)] for _ in range(2001)]
w = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
f[0][0] = 0
for i in range(1, n + 1):
    for j in range(i, n + 1):
        w[i][j] = w[i][j - 1] + a[j] * c[j - i + 1]
result = -float('inf')
for i in range(1, n + 1):
    dnc(i, i + 1, n + 1, i - 1, n - 1)
    for j in range(i, n + 2):
        f[i][j] = max(f[i - 1][j - 1], f[i][j])
    if n + 1 - i <= k:
        result = max(result, f[i][n + 1])
print(max(result, 0))
