result = 0
n = int(input())
for i in range(1, n + 1):
    temp = cur = i
    while temp < n:
        cur += 1
        temp += cur
    if temp == n:
        result += 1
print(result)
