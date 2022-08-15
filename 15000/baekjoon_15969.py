n = int(input())
numlist = sorted(list(map(int, input().split())))
print(numlist[-1] - numlist[0])
