n = int(input())
while n != 1:
    print(n, end = ' ')
    n = n * 3 + 1 if n & 1 else n >> 1
print(n)
