n = int(input())
numlist = list(map(int, input().split()))
temp = sum(numlist)
result = 0
for i in numlist:
    temp -= i
    result += i * temp
print(result)
