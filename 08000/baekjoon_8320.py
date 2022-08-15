result = 0
n = int(input())
for i in range(1, int(n ** 0.5) + 1):
    for j in range(i, n // i + 1):
        result += 1
print(result)
