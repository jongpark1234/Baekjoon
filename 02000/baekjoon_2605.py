n = int(input())
numlist = list(map(int, input().split()))
result = []
for i in range(n):
    result.insert(numlist[i], i + 1)
print(*result[::-1])
