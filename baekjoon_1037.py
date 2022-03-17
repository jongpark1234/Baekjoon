n = int(input())
numlist = list(map(int, input().split()))
numlist.sort()
print(numlist[0] * numlist[-1])
