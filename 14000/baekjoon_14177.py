# pypy3
q = [[0 for _ in range(4001)] for _ in range(4001)]
result1 = [[0 for _ in range(4001)] for _ in range(4001)]
result2 = [[0 for _ in range(4001)] for _ in range(4001)]
result = [[0 for _ in range(4001)] for _ in range(4001)]
def dnc(n, start, end, left, right):
    if start > end:
        return
    mid = (start + end) // 2
    result[n][mid] = float('inf')
    for i in range(left, min(right, mid - 1) + 1):
        if result[n][mid] > result[n - 1][i] + result2[i + 1][mid]:
            result[n][mid] = result[n - 1][i] + result2[i + 1][mid]
            q[n][mid] = i
    dnc(n, start, mid - 1, left, q[n][mid])
    dnc(n, mid + 1, end, q[n][mid], right)
n, k = map(int, input().split())
u = [[0 for _ in range(n + 1)]]
for i in range(n):
    u.append([0] + list(map(int, input().split())))
for i in range(1, n + 1):
    result1[i][1] = u[i][1]
    for j in range(2, n + 1):
        result1[i][j] = result1[i][j - 1] + u[i][j]
for i in range(1, n + 1):
    result2[i][i] = 0
    for j in range(i + 1, n + 1):
        result2[i][j] = result2[i][j - 1] + (result1[j][j] - result1[j][i - 1])
for i in range(1, n + 1):
    result[1][i] = result2[1][i]
for i in range(2, k + 1):
    dnc(i, i, n, i - 1, n - 1)
print(result[k][n])
