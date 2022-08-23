from sys import stdin
from collections import deque
n = int(input())
alpha = 'a' + input()
graph = [[] for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]
result = ''
for _ in range(n - 1):
    u, v = map(int, stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)
queue = deque([1])
while queue:
    result += alpha[queue[0]]
    temp = deque([])
    word = 'a'
    while queue:
        v = queue.popleft()
        visited[v] = True
        for i in graph[v]:
            if visited[i]:
                continue
            if alpha[i] > word:
                while temp:
                    temp.popleft()
                word = alpha[i]
            if alpha[i] >= word:
                temp.append(i)
    queue = temp
print(result)
