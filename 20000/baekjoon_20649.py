east = []
north = []
xlist = []
ylist = []
n = int(input())
for i in range(n):
    facing, x, y = input().split()
    if facing == 'E':
        east.append(i)
    else:
        north.append(i)
    xlist.append(int(x))
    ylist.append(int(y))
east.sort(key = lambda x: ylist[x])
north.sort(key = lambda x: xlist[x])
stop = [False for _ in range(n)]
stopCount = [0 for _ in range(n)]
for i in east:
    for j in north:
        if not stop[i] and not stop[j] and xlist[j] > xlist[i] and ylist[i] > ylist[j]:
            if xlist[j] - xlist[i] > ylist[i] - ylist[j]:
                stop[i] = True
                stopCount[j] += stopCount[i] + 1
            elif ylist[i] - ylist[j] > xlist[j] - xlist[i]:
                stop[j] = True
                stopCount[i] += stopCount[j] + 1
print('\n'.join(map(str, stopCount)))
