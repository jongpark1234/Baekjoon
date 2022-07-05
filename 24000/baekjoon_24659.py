n = int(input())
result = 0
visited = [0 for _ in range(100001)]
p = [0] + list(map(int, input().split()))
a = [0] + list(map(int, input().split()))
b = [0] + list(map(int, input().split()))
for i in range(1, n + 1):
    if p[i] == i or visited[i]:
        continue
    visited[i] = True
    dp1, dp2 = [[a[i], a[i] + b[i]], [a[i] + b[i], b[i]]], [[0, 0], [0, 0]]
    x = p[i]
    while x != i:
        visited[x] = True
        for j in range(2):
            dp2[j][0] = min(dp1[j][0] + a[x], dp1[j][1] + b[x] + a[x])
            dp2[j][1] = min(dp1[j][0] + b[x], dp1[j][1] + b[x])
            dp1[j] = [dp2[j][0], dp2[j][1]]
        x = p[x]
    result += min(min(dp1[0][0], dp1[1][1]), dp1[1][0])
print(result)
