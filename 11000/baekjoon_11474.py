n, m = map(int, input().split())
available = [0 for _ in range(n)]
unavailable = []
radius = [[] for _ in range(n)]
visited = [False for _ in range(m)]
pos = [-1 for _ in range(n)]
result = [0 for _ in range(n * 2)]
tri = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(m)]
for i in range(m):
    available[tri[i][1]] += 1
    radius[tri[i][0]].append(i)
    radius[tri[i][2]].append(i)
for i in range(n):
    if available[i] == 0:
        unavailable.append(i)
for i in range(n):
    for j in radius[unavailable[i]]:
        if visited[j]:
            continue
        visited[j] = True
        available[tri[j][1]] -= 1
        if available[tri[j][1]] == 0:
            unavailable.append(tri[j][1])
l = r = n
for i in range(n)[::-1]:
    cnt1 = cnt2 = 0
    for j in radius[unavailable[i]]:
        z = tri[j][0] ^ tri[j][2] ^ unavailable[i]
        y = tri[j][1]
        if pos[y] < 0 or pos[z] < 0:
            continue
        cnt1 += 1
        if pos[y] < pos[z]:
            cnt2 += 1
    if cnt2 * 2 >= cnt1:
        l -= 1
        result[l] = unavailable[i]
        pos[unavailable[i]] = l
    else:
        result[r] = unavailable[i]
        pos[unavailable[i]] = r
        r += 1
print(*map(lambda x: x + 1, result[l:r]))
