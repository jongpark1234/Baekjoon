min, max = map(int, input().split())
result = max - min + 1
sieve = [False] * result
for i in range(2, int(max ** 0.5) + 1):
    square = i ** 2
    for j in range(((min - 1) // square + 1) * square, max + 1, square):
        if not sieve[j - min]:
            sieve[j - min] = True
            result -= 1
print(result)
