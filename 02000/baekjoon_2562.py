numlist = []
for i in range(9):
    n = int(input())
    numlist.append(n)
    maxnum = max(numlist)
print(maxnum, (numlist.index(maxnum) + 1),sep="\n")
