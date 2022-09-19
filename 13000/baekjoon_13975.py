from heapq import *
for _ in range(int(input())):
    result = 0
    n = int(input())
    pq = sorted(map(int, input().split()))
    for i in range(n - 1):
        temp = heappop(pq) + heappop(pq)
        result += temp
        heappush(pq, temp)
    print(result)
