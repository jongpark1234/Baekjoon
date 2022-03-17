from sys import *
from collections import deque
n = int(stdin.readline())
deque = deque([i for i in range(1, n + 1)])
while len(deque) > 1:
    deque.popleft()
    temp = deque.popleft()
    deque.append(temp)
print(deque[0])
