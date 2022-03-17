import sys
input = sys.stdin.readline
n, k = map(int, input().split())
numlist = []
for i in range(n):
    numlist.append(list(map(int, input().split())))
numlist.sort(key=lambda x: (-x[1], -x[2], -x[3]))
for i in range(n):
    if numlist[i][0] == k:
        index = i
for i in range(n):
    if numlist[index][1:] == numlist[i][1:]:
        print(i + 1)
        break
