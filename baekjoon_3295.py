# pypy3
def dfs(s):
    visited[s] = True
    for i in graph[s]:
        if (b[i] == -1) or (not visited[b[i]] and dfs(b[i])):
            b[i] = s
            return True
    return False
for _ in range(int(input())):
    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
    b = [-1 for _ in range(n)]
    result = 0
    for i in range(n):
        visited = [False for _ in range(n)]
        result += dfs(i)
    print(result)
