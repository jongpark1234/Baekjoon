from collections import deque
flag = 1
numlist = deque([i + 1 for i in range(int(input()))])
while numlist:
    t = numlist.popleft()
    print(t, end=' ') if flag else numlist.append(t)
    flag ^= 1
