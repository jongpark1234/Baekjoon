from collections import deque
MAX = 100001
graph = [[] for _ in range(MAX)]
win = [[False for _ in range(MAX)] for _ in range(2)]
draw = [[False for _ in range(MAX)] for _ in range(2)]
n, m = map(int, input().split())
for i in range(m):
    s, e = map(int, input().split())
    graph[e].append(s)
numarr = [0 for _ in range(MAX)]
for i in range(1, n + 1):
    for j in graph[i]:
        numarr[j] += 1
queue = deque([])
for i in range(1, n + 1):
    if numarr[i] == 0:
        queue.append([0, i])
        win[0][i] = True
while queue:
    x = queue.popleft()
    if not x[0]:
        for j in graph[x[1]]:
            if not win[1][j]:
                win[1][j] = True
                queue.append([1, j])
    else:
        for j in graph[x[1]]:
            numarr[j] -= 1
            if not numarr[j] and not win[0][j]:
                win[0][j] = True
                queue.append([0, j])
numarr = [0 for _ in range(MAX)]
for i in range(1, n + 1):
    for j in graph[i]:
        numarr[j] += 1
    draw[0][i] = draw[1][i] = True
queue = deque([])
for i in range(1, n + 1):
    if numarr[i] == 0:
        queue.append([0, i])
        queue.append([1, i])
        draw[0][i] = draw[1][i] = False
while queue:
    x = queue.popleft()
    if not x[0]:
        for j in graph[x[1]]:
            if draw[1][j]:
                draw[1][j] = False
                queue.append([1, j])
    else:
        for j in graph[x[1]]:
            numarr[j] -= 1
            if not numarr[j] and draw[0][j]:
                draw[0][j] = False
                queue.append([0, j])
print(''.join(['D' if draw[0][i] else 'L' if win[0][i] else 'W' for i in range(1, n + 1)]))
print(''.join(['W' if win[1][i] else 'D' if draw[1][i] else 'L' for i in range(1, n + 1)]))
