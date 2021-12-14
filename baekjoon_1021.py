from collections import deque
n, m = map(int, input().split())
numlist = list(map(int, input().split()))
queue = deque([i for i in range(1, n + 1)])
cnt = 0
for i in range(m):
    length = len(queue)
    idx = queue.index(numlist[i])
    if idx < length - idx:
        while True:
            if queue[0] == numlist[i]:
                queue.popleft()
                break
            queue.append(queue.popleft())
            cnt += 1
    else:
        while True:
            if queue[0] == numlist[i]:
                queue.popleft()
                break
            queue.appendleft(queue.pop())
            cnt += 1
print(cnt)
