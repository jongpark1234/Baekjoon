from collections import deque
result = 1
n = int(input())
h = deque(map(int, input().split()))
temp = h.popleft()
while h:
    if temp <= h[0]:
        result += 1
    temp = h.popleft()
print(result)
