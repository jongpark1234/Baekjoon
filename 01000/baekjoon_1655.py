from sys import stdin
from heapq import heappush, heappop
heap1 = []
heap2 = []
for _ in range(int(stdin.readline())):
    num = int(stdin.readline())
    heappush(heap1, (-num, num)) if len(heap1) == len(heap2) else heappush(heap2, (num, num))
    if heap2 and heap1[0][1] > heap2[0][0]:
        Min = heappop(heap2)[0]
        Max = heappop(heap1)[1]
        heappush(heap1, (-Min, Min))
        heappush(heap2, (Max, Max))
    print(heap1[0][1])
