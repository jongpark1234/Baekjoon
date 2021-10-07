n = int(input())
numlist = list(map(int, input().split()))
max = 0
min = 1000001

for i in range(n):
    if (numlist[i] > max):
        max = numlist[i]

for j in range(n):
    if (numlist[i] < min):
        min = numlist[i]

print(min, max)
