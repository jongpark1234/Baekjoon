n, s, q = map(int, input().split())
result = 0
for i in range(n):
    if (pow(i, q, n) + q * i) % n == s:
        result = (result + i) % q
print(result)
