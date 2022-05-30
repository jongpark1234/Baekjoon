from sys import stdin
from collections import deque
def search(cur):
    ret = [0 for _ in range(len(cur))]
    queue = deque([])
    for i in range(len(cur)):
        if ret[i]:
            continue
        ret[i] = 1
        queue.append(i)
        while queue:
            for j in cur[(p := queue.popleft())]:
                if ret[j]:
                    continue
                ret[j] = 3 - ret[p]
                queue.append(j)
    return ret
n = int(input())
graph = [[] for _ in range(n * 2 + 1)]
for _ in range(n):
    a, b = map(int, stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(1, n * 2 + 1, 2):
    graph[i].append(i + 1)
    graph[i + 1].append(i)
result = search(graph)
print(''.join('?XY'[result[i]] for i in range(1, n * 2 + 1)))
