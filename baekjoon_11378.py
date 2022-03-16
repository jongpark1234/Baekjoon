# pypy3
n, m, k = map(int, input().split())
graph = [[] for _ in range(n + 1)]
d = [0 for _ in range(m + 1)]
result = 0
def dfs(s):
    if visited[s]:
        return False
    visited[s] = True
    for i in graph[s]:
        if d[i] == 0 or dfs(d[i]):
            d[i] = s
            return True
    return False
for i in range(1, n + 1):
    nlist = list(map(int, input().split()))
    for j in nlist[1:]:
        graph[i].append(j)
for i in range(1, n + 1):
    visited = [False for _ in range(n + 1)]
    result += dfs(i)
for i in range(1, n + 1):
    while k:
        visited = [False for _ in range(n + 1)]
        if dfs(i):
            k -= 1
            result += 1
        else:
            break
print(result)
