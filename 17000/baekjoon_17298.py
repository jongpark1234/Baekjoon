from sys import stdin
from collections import deque
n = int(stdin.readline())
a = list(map(int, stdin.readline().split()))
result = [-1] * n
stack = deque()
for i in range(n):
    while stack and (stack[-1][0] < a[i]):
        temp, idx = stack.pop()
        result[idx] = a[i]
    stack.append([a[i], i])
print(*result)
