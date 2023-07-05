from math import ceil
numlist = [i + 1 for i in range(int(input()))]
while len(numlist) > 1:
    for i in range(ceil(len(numlist) / 2)):
        del numlist[i]
print(*numlist)
