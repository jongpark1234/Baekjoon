from collections import deque
MAX = 100000
visited = [False for _ in range(MAX + 1)]
n, k = map(int, input().split())
queue = deque([(n, 0)])
while queue:
    now, idx = queue.popleft()
    if now == k:
        print(idx)
        break
    for i in [now - 1, now + 1, now << 1]:
        if 0 <= i <= MAX:
            if not visited[i]:
                visited[i] = True
                queue.append((i, idx + 1))
