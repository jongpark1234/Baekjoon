result = 0
n = int(input())
a0 = int(input())
for _ in range(n):
    a = int(input())
    result += min(abs(a - a0), 360 - a0 + a, a0 + 360 - a)
    a0 = a
print(result)
