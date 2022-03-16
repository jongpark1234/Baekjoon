# pypy3
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
d = [0 for _ in range(m + 1)]
result = 0
def dfs(s):
    if visited[s] == True:
        return False
    visited[s] = True
    for i in graph[s]:
        if d[i] == 0 or dfs(d[i]):
            d[i] = s
            return True
    return 0
for i in range(1, n + 1):
    a = list(map(int, input().split()))
    for j in a[1:]:
        graph[i].append(j)
for j in range(2):
    for i in range(1, n + 1):
        visited = [False for _ in range(n + 1)]
        if dfs(i):
            result += 1
print(result)
