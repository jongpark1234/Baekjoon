result = 0
n = int(input())
while n:
    if n & 1:
        result += 1
    n >>= 1
print(result)
