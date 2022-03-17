import sys
numlist = []
n = int(sys.stdin.readline())
for i in range(n):
    numlist.append(int(sys.stdin.readline()))
numlist.sort()
for j in range(n):
    print(numlist[j])
