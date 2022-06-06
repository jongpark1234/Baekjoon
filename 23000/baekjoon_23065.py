from sys import stdin
MAX = 1001
graph = [[] for _ in range(MAX)]
numlist = [False for _ in range(MAX)]
road = [False for _ in range(MAX)]
checked = [False for _ in range(MAX)]
def dfs(x, y):
    ret = [0, x]
    for i in graph[x]:
        if i != y:
            numlist[i] = x
            num = dfs(i, x)
            num[0] += 1
            ret = max([ret, num])
    return ret
n, m = map(int, stdin.readline().split())
for _ in range(m):
    s, e = map(int, stdin.readline().split())
    graph[s].append(e)
    graph[e].append(s)
if m != n - 1:
    print('NO')
elif n == 1:
    print('YES')
    print(1)
    print(1)
elif n == 2:
    print('YES')
    print(2)
    print(1, 1)
else:
    u = dfs(1, -1)[1]
    v = dfs(u, -1)[1]
    idx = v
    while True:
        checked[idx] = True
        road[idx] = True
        for j in graph[idx]:
            checked[j] = True
            for k in graph[j]:
                checked[k] = True
        if idx == u:
            break
        idx = numlist[idx]
    if checked[1:n + 1].count(0):
        print('NO')
        exit(0)
    else:
        result = []
        idx = numlist[v]
        while idx != u:
            result.append(idx)
            for j in graph[idx]:
                if len(graph[j]) == 1 or road[j]:
                    continue
                result.append(j)
                result.append(idx)
            idx = numlist[idx]
        print('YES')
        print(len(result) * 2)
        print(*result, *result[::-1])