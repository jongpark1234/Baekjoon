result = 0
for _ in range(int(input())):
    n = int(input())
    result += (n // 10) ** (n % 10)
print(result)
