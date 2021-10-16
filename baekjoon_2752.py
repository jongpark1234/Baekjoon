numlist = list(map(int, input().split()))
numlist.sort()
for i in range(len(numlist)):
    print(numlist[i], end=" ")