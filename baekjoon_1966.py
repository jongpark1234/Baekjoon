from collections import deque
import sys
t = int(sys.stdin.readline())
queue = deque([])
for i in range(t):
    queue.clear()
    n, m = map(int, sys.stdin.readline().split())
    index, th = m, 0
    queue.extend(list(map(int, sys.stdin.readline().split())))
    while True:
        if queue[0] == max(queue):
            th += 1
            if index == 0:
                break
            else:
                index -= 1
            queue.popleft()
        else:
            temp = queue[0]
            queue.popleft()
            queue.append(temp)
            if index == 0:
                index = len(queue) - 1
            else:
                index -= 1
    print(th)
