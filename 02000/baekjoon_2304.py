import sys
n = int(sys.stdin.readline())
hlist = []
poslist, xposlist, yposlist = [], [], []
temp = 0

for _ in range(n):
    pos = list(map(int, sys.stdin.readline().split()))
    if pos[1] > temp:
        temp = pos[1]
    poslist.append(pos)

poslist.sort(key = lambda x : (x[0], x[1]))

for i in range(n):
    xposlist.append(poslist[i][0])
for i in range(n):
    yposlist.append(poslist[i][1])

mid = xposlist[yposlist.index(max(yposlist))]

h = 0
for i in range(mid):
    if i in xposlist:
        y = yposlist[xposlist.index(i)]
    else: 
        y = 0
    if y > h: 
        h = y
    hlist.append(h)

h = 0
for i in reversed(range(mid, xposlist[-1] + 1)):
    if i in xposlist:
        y = yposlist[xposlist.index(i)]
    else:
        y = 0
    if y > h:
        h = y
    hlist.append(h)
    
print(sum(hlist))
