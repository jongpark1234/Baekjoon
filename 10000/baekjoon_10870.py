n = int(input())
numlist = [0, 1]
for i in range(2, n + 1):
    numlist.append(numlist[i - 2] + numlist[i - 1])
print(numlist[n])
