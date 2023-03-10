from collections import deque
MAX = 100000
result = 0
visited = [-1 for _ in range(MAX + 1)]
n, k = map(int, input().split())
queue = deque([(n, 0)])
while queue:
    now, idx = queue.popleft()
    if visited[now] != -1 and visited[now] < idx:
        continue
    visited[now] = idx
    if now == k:
        if visited[k] == -1 or idx < visited[k]:
            result = 1
        else:
            result += 1
        continue
    for i in [now - 1, now + 1, now << 1]:
        if 0 <= i <= MAX:
            queue.append((i, idx + 1))
print(visited[k], result)
