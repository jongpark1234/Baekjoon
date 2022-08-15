n = int(input())
numlist = list(map(int, input().split()))
print(len(numlist) - len(set(numlist)))
