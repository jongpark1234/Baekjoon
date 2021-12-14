from heapq import heappush, heappop
from sys import stdin
q = []
for i in range(int(stdin.readline())):
    x = int(stdin.readline().rstrip())
    if x == 0:
        if not len(q):
            print(0)
        else:
            print(-1 * heappop(q))
    else:
        heappush(q, -x)
