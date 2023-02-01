from math import gcd
n = int(input())
dp = [0 for _ in range(n + 1)]
c = [0] + list(map(int, input().split()))
p = [0] + list(map(int, input().split()))
for i in range(1, n + 1):
    p[i] += p[i - 1]
numlist = [[dp[1] - p[1] + c[1], c[1]]]
for i in range(2, n + 1):
    j = k = 0
    templist = []
    dp[i] = float('inf')
    for j in range(len(numlist)):
        numlist[j][1] = gcd(numlist[j][1], c[i])
    while j < len(numlist):
        while k < len(numlist) and numlist[j][1] == numlist[k][1]:
            numlist[j][0] = min(numlist[j][0], numlist[k][0])
            k += 1
        templist.append(numlist[j])
        j = k
    for Min, Gcd in templist:
        dp[i] = min(dp[i], Min + p[i - 1] + c[i] - Gcd * 2)
    numlist = templist + [[dp[i] - p[i] + c[i], c[i]]]
print(dp[-1])
