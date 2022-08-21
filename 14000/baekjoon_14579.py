result = 1
a, b = map(int, input().split())
for i in range(a, b + 1):
    result *= sum(j for j in range(1, i + 1))
print(result % 14579)
