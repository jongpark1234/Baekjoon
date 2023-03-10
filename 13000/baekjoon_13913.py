from collections import deque
MAX = 100000
visited = [-1 for _ in range(MAX + 1)]
n, k = map(int, input().split())
queue = deque([(n, 0)])
while queue:
    now, idx = queue.popleft()
    if now == k:
        print(idx)
        path = []
        while now != n:
            path.append(now)
            now = visited[now]
        print(now, *path[::-1])
        break
    for i in [now - 1, now + 1, now << 1]:
        if 0 <= i <= MAX:
            if visited[i] == -1:
                visited[i] = now
                queue.append((i, idx + 1))
