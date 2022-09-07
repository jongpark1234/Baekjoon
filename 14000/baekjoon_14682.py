n, k = input(), int(input())
result = int(n)
for i in range(1, k + 1):
    result += int(n + '0' * i)
print(result)
