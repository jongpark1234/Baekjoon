from sys import stdin
n, m, b = map(int, stdin.readline().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, stdin.readline().split())))
Min = min(map(min, graph))
Max = max(map(max, graph))
leastTime = 1000000000
for i in range(Min, Max + 1):
    pluscount = 0
    minuscount = 0
    for j in range(n):
        for k in range(m):
            h = graph[j][k] - i
            if h > 0:
                minuscount += h
            elif h < 0:
                pluscount -= h
    if minuscount + b >= pluscount:
        time = minuscount * 2 + pluscount
        if leastTime >= time:
            leastTime = time
            result = i
print(leastTime, result)
