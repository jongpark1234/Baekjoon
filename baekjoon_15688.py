import sys
n = int(sys.stdin.readline())
numlist = []
for _ in range(n):
    numlist.append(int(sys.stdin.readline()))
numlist.sort()
for i in range(n):
    print(numlist[i])
    