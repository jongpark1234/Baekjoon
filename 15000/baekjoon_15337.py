numlist = [0 for _ in range(100001)]
sum1 = [0 for _ in range(100001)]
sum2 = [0 for _ in range(100001)]
a = []
n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    numlist[x] += 1
    numlist[y] -= 1
    sum1[y] += 1
    sum2[x] += 1
    a.append([x, y])
result1, result2 = 0, 1000000007
for i in range(1, 100001):
    numlist[i] += numlist[i - 1]
    result1 = max(result1, numlist[i])
for i in range(100000):
    sum1[i + 1] += sum1[i]
for i in range(100000)[::-1]:
    sum2[i] += sum2[i + 1]
for i in range(n):
    result2 = min(result2, sum1[a[i][0]] + sum2[a[i][1]])
print(n - result2, result1)
