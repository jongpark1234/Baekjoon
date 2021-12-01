from sys import stdin
n, m = map(int, stdin.readline().split())
numlist = list(map(int, stdin.readline().split()))
sums = [0]
temp = 0
for i in numlist:
    temp += i
    sums.append(temp)
for _ in range(m):
    i, j = map(int, stdin.readline().split())
    print(sums[j] - sums[i - 1])
