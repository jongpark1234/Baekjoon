k, n, m = map(int, input().split())
temp = k * n - m
if temp < 0:
    temp = 0
print(temp)