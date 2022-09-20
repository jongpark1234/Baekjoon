from sys import stdin
from heapq import *
def greater(v) -> list:
    if type(v) == list:
        return list(map(lambda x: -x, v))
    elif type(v) == int:
        return -v
    else:
        return v
for _ in range(int(stdin.readline())):
    visited = [False for _ in range(1000001)]
    maxpq, minpq = [], []
    for i in range(int(stdin.readline())):
        o, n = stdin.readline().split()
        n = int(n)
        if o == 'I':
            heappush(maxpq, greater([n, i]))
            heappush(minpq, [n, i])
            visited[i] = True
        else:
            if n == 1:
                while maxpq and not visited[greater(maxpq[0][1])]:
                    heappop(maxpq)
                if maxpq:
                    visited[greater(heappop(maxpq)[1])] = False
            else:
                while minpq and not visited[minpq[0][1]]:
                    heappop(minpq)
                if minpq:
                    visited[heappop(minpq)[1]] = False
    while maxpq and not visited[greater(maxpq[0][1])]:
        heappop(maxpq)
    while minpq and not visited[minpq[0][1]]:
        heappop(minpq)
    if maxpq and minpq:
        print(greater(maxpq[0][0]), minpq[0][0])
    else:
        print('EMPTY')
