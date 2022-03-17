from sys import stdin, maxsize
from heapq import heappush, heappop
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
cnt = 1
inf = maxsize
def dijkstra():
    q = []
    heappush(q, (graph[0][0], 0, 0))
    distance[0][0] = 0
    while q:
        cost1, x1, y1 = heappop(q)
        if x1 == n - 1 and y1 == n - 1:
            print(f'Problem {count}: {distance[x1][y1]}')
        for i in range(4):
            x2 = x1 + dx[i]
            y2 = y1 + dy[i]
            if 0 <= x2 < n and 0 <= y2 < n:
                cost2 = cost1 + graph[x2][y2]
                if cost2 < distance[x2][y2]:
                    distance[x2][y2] = cost2
                    heappush(q, (cost2, x2, y2))
count = 1
while True:
    n = int(stdin.readline())
    if n == 0:
        break
    graph = [list(map(int, stdin.readline().split())) for _ in range(n)]
    distance = [[inf] * n for _ in range(n)]
    dijkstra()
    count += 1
