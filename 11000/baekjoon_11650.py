import sys
n = int(sys.stdin.readline())
poslist = []
for i in range(n):
    xpos, ypos = map(int, sys.stdin.readline().split())
    poslist.append((xpos, ypos))
poslist.sort()
for i in poslist:
    print(i[0], i[1])
