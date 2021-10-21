import sys
k = int(sys.stdin.readline())
numlist = []
for i in range(k):
    num = int(sys.stdin.readline())
    if num == 0:
        del numlist[-1]
    else:
        numlist.append(num)
print(sum(numlist))
