result = 0
a, b, m, n = map(int, input().split())
pond = [list(map(int, input().split())) for _ in range(m)]
if a > b: a, b = b, a
PirateChest = m * n
for i in range(m):
    depth = [1000000007 for _ in range(n)]
    stack = []
    l = [0 for _ in range(n)]
    r = [0 for _ in range(n)]
    for j in range(n):
        depth[j] = pond[i][j]
    for j in range(i, m):
        if i + b <= j:
            break
        h = j - i + 1
        for k in range(n):
            depth[k] = min(depth[k], pond[j][k])
        for k in range(n):
            if not stack or depth[stack[-1]] < depth[k]:
                l[k] = k
                stack.append(k)
            while stack and depth[stack[-1]] >= depth[k]:
                idx = stack.pop()
                r[idx] = k
            if not stack:
                l[k] = 0
                stack.append(k)
            else:
                l[k] = stack[-1] + 1
                stack.append(k)
        while stack:
            idx = stack.pop()
            r[idx] = n
        for k in range(n):
            w = min([b, a][h > a], r[k] - l[k])
            s = w * h
            level = depth[k] * PirateChest
            result = max(result, s * (level // (PirateChest - s) - [1, 0][bool(level % (PirateChest - s))]))
print(result)
