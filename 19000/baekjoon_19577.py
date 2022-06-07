MAX = 10000000000
def prime(n):
    if n == 1:
        return 1
    if n % 2 == 0:
        return 2
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return i
    return n
def pair(n):
    c, a, i = 0, 1, 2
    while n - 1:
        if n % i == 0:
            n //= i
            a *= i - 1 if c != i else i
            c = i
            i -= 1
        i = prime(n)
    return a
n = int(input())
x = MAX
for i in range(1, int(n ** 0.5) + 1):
    if n % i == 0:
        if i * pair(i) == n:
            x = min(x, i)
        if n // i * pair(n // i) == n:
            x = min(x, n // i)
print(-1 if x == MAX else x)
