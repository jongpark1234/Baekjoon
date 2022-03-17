a, b = map(int, input().split())
temp = 0
numlist = []
for i in range(1, 1001):
    for j in range(i):
        numlist.append(i)
for i in range(a - 1, b):
    temp += numlist[i]
print(temp)
