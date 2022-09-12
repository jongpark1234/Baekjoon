from heapq import *
n, k = map(int, input().split())
pq = []
costlist = []
basic = result = 0
for i in range(n):
    m, *cost = list(map(int, input().split()))
    cost = sorted(cost) + [float('inf') for _ in range(10 - m)]
    basic += cost[0]
    costlist.append(list(map(lambda x: x - cost[0], cost)))
costlist.sort()
heappush(pq, [0, 0, 0])
for _ in range(k):
    cost, loc, idx = heappop(pq)
    result += basic + cost
    if idx < 9 and costlist[loc][idx + 1] != float('inf'):
        heappush(pq, [cost + costlist[loc][idx + 1] - costlist[loc][idx], loc, idx + 1])
    if loc + 1 < len(costlist):
        if idx:
            heappush(pq, [cost + costlist[loc + 1][1] - costlist[loc + 1][0], loc + 1, 1])
            if idx == 1:
                heappush(pq, [cost + costlist[loc + 1][1] - costlist[loc + 1][0] - costlist[loc][1] + costlist[loc][0], loc + 1, 1])
print(result)
