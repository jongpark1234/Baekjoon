from collections import deque
queue = deque([(int(input()), 0)])
while queue:
    now, idx = queue.popleft()
    if now == 1:
        break
    if now % 3 == 0:
        queue.append((now // 3, idx + 1))
    if now % 2 == 0:
        queue.append((now // 2, idx + 1))
    queue.append((now - 1, idx + 1))
print(idx)
