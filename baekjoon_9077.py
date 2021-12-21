from sys import stdin
Map = [[-1 for _ in range(10001)] for _ in range(10001)]
for t in range(int(stdin.readline())):
    n = int(stdin.readline())
    mine = []
    for _ in range(n):
        pos = list(map(int, stdin.readline().split()))
        mine.append(pos)
        Map[pos[0]][pos[1]] = t
    Max = 0
    for i in range(n):
        ek = min(mine[i][0] + 10, 10000)
        k = max(mine[i][0] - 10, 0)
        while k <= ek:
            s = 0
            ex = min(k + 10, 10000)
            ey = min(mine[i][1] + 10, 10000)
            for x in range(k, ex + 1):
                for y in range(mine[i][1], ey + 1):
                    if Map[x][y] == t:
                        s += 1
            Max = max(Max, s)
            s = 0
            ex = min(k + 10, 10000)
            ey = min(mine[i][1] - 10, 10000)
            for x in range(k, ex + 1):
                for y in range(ey, mine[i][1] + 1):
                    if Map[x][y] == t:
                        s += 1
            Max = max(Max, s)
            k += 1
    print(Max)
