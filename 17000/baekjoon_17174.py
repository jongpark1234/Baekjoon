result = 0
n, m = map(int, input().split())
while n >= m:
    result += n
    n //= m
print(result + n)
