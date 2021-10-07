n = int(input())
numlist = list(map(int, input().split()))
max = 0
min = 1000001
for i in range(len(numlist)):
    if (numlist[i] > max):
        max = numlist[i]
for j in range(len(numlist)):
    if (numlist[j] < min):
        min = numlist[j]

print(min, max)
