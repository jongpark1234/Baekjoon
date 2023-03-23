from collections import deque
x = int(input())
queue = deque([[x, [x]]])
while queue:
    now, path = queue.popleft()
    if now == 1:
        print(len(path) - 1)
        print(*path)
        break
    if now % 3 == 0:
        queue.append((now // 3, path + [now // 3]))
    if now % 2 == 0:
        queue.append((now // 2, path + [now // 2]))
    queue.append((now - 1, path + [now - 1]))
