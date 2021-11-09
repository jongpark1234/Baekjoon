complain = 0
numlist = sorted([int(input()) for i in range(int(input()))])
for i in range(len(numlist)):
    complain += abs(numlist[i] - (i + 1))
print(complain)