dp = [[0 for _ in range(8001)] for _ in range(801)]
p = [[0 for _ in range(8001)] for _ in range(801)]
def cost(x, y):
    return (r[y] - r[x - 1]) * (y - x + 1)
def dnc(t, l, r, left, right):
    if l > r:
        return
    mid = (l + r) // 2
    dp[t][mid] = -1
    p[t][mid] = -1
    for i in range(left, right + 1):
        temp = dp[t - 1][i] + cost(i + 1, mid)
        if dp[t][mid] == -1 or dp[t][mid] > temp:
            dp[t][mid] = temp
            p[t][mid] = i
    dnc(t, l, mid - 1, left, p[t][mid])
    dnc(t, mid + 1, r, p[t][mid], right)
l, g = map(int, input().split())
c, r = [0] + list(map(int, input().split())), [0]
for i in range(1, l + 1):
    r.append(r[i - 1] + c[i])
for i in range(l + 1):
    dp[1][i] = cost(1, i)
    p[1][i] = 0
for i in range(2, g + 1):
    dnc(i, 0, l, 0, l)
print(dp[g][l])
