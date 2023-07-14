result = 0
n = int(input())
while n != 1:
    result += 1
    n = n * 3 + 1 if n & 1 else n >> 1
print(result)
