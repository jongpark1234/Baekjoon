from sys import stdin
from collections import deque
good_friend = 0
n, k = map(int, stdin.readline().split())
namelist = [len(stdin.readline().rstrip()) for _ in range(n)]
slist = [deque() for i in range(21)]
for i, v in enumerate(namelist):
    while slist[v] and i - slist[v][0] > k:
        slist[v].popleft()
    if slist[v]:
        good_friend += len(slist[v])
    slist[v].append(i)
print(good_friend)
