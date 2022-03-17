n = int(input())
numlist = list(map(int, input().split()))
numlist.sort()
maxnum, minnum = numlist[len(numlist) - 1], numlist[0]
print(minnum, maxnum)
