from sys import stdin
complain = 0
numlist = sorted([int(stdin.readline()) for i in range(int(stdin.readline()))])
for i in range(len(numlist)):
    complain += abs(numlist[i] - (i + 1))
print(complain)
