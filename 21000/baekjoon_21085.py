def dfs(u, n):
    global visited, match
    for i in range(1, n + 1):
        if visited[i] or not graph[u][i]:
            continue
        visited[i] = True
        if not match[i] or dfs(match[i], n):
            match[i] = u
            return True
    return False
def check(n):
    global visited, match
    match = [0 for _ in range(201)]
    for i in range(1, n + 1):
        visited = [False for _ in range(201)]
        if not dfs(i, n):
            return 0
    return 1
visited = [False for _ in range(201)]
result, dresult = [], [62]
n = int(input())
for i in range(min(200, n)):
    graph = [[False for _ in range(201)] for _ in range(201)]
    for y in range(1, i + 1):
        for x in range(1, i + 1):
            if (n - y + 1) % x == 0:
                graph[y][x] = True
    result.append(check(i))
if n == 0:
    print(2)
    print(1, 1)
elif n < 402:
    for i in range(len(result), n + 1):
        result.append(result[n - i])
    print(2)
    print(len(result), *result)
else:
    print(64)
    for i in range(1, 61):
        print(2, 0 if i == 1 else i, 0 if i == 1 else i)
    print(len(result), *result)
    result.reverse()
    print(len(result), *result)
    temp = n + 1 - len(result) * 2
    for i in range(61):
        if temp >> i & 1:
            dresult.append(i + 1 if i else 0)
    dresult.append(63)
    print(len(dresult), *dresult)
