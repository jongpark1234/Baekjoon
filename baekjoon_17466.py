# pypy3
n, p = map(int, input().split())
result = 1
for i in range(2, n + 1):
    result *= i
    result %= p
print(result % p)
