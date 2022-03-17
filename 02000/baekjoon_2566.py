from sys import stdin
maxnum = -1
for i in range(1, 10):
    s = list(map(int, stdin.readline().rstrip().split()))
    if max(s) > maxnum:
        maxnum = max(s)
        xpos = i
        ypos = s.index(max(s)) + 1
print(maxnum)
print(xpos, ypos)
