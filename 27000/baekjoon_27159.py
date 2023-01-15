result = 0
n = int(input())
numlist = list(map(int, input().split()))
for i in range(n):
    if numlist[i] - numlist[i - 1] != 1:
        result += numlist[i]
print(result)
