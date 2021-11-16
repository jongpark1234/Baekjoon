from sys import stdin
n = int(stdin.readline())
numlist = list(map(int, stdin.readline().split()))
sortedlist = sorted(set(numlist))
numdict = {sortedlist[i] : i for i in range(len(sortedlist))}
for i in numlist:
    print(numdict[i], end=' ')
