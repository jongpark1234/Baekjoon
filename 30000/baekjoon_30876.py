xlist, ylist = [], []
for _ in range(int(input())):
    x, y = map(int, input().split())
    xlist.append(x)
    ylist.append(y)
print(xlist[ylist.index(min(ylist))], min(ylist))
