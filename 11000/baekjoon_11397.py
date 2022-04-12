SIZE1 = 1010
SIZE2 = 1000
SIZE3 = 1000000000
def calc(n, fibonamial, p):
    value = 0
    if p == 2:
        value += n // fibonamial
        fibonamial *= p
        while n // fibonamial:
            if fibonamial == 6:
                value += n // fibonamial * 2
            else:
                value += n // fibonamial
            fibonamial *= p
    else:
        while n // fibonamial:
            value += n // fibonamial
            fibonamial *= p
    return value
def factorial(n):
    value = [0 for _ in range(SIZE1)]
    while n % 2 == 0:
        n //= 2
        value[2] += 1
    for i in range(3, int(n ** 0.5) + 1, 2):
        while n % i == 0:
            n //= i
            value[i] += 1
        if n == 1:
            break
    if n != 1:
        value[n] += 1
    return value
def eratosthenes():
    for i in range(3, int(SIZE2 ** 0.5) + 1, 2):
        if sieve[i] or i % 2 == 0:
            continue
        for j in range(i ** 2, SIZE2, i):
            sieve[j] = False
    for i in range(3, SIZE2, 2):
        if sieve[i]:
            primes.append(i)
    for i in primes:
        n1, n2, cnt = 0, 1, 1
        while True:
            s = n1 + n2
            n1, n2 = n2, s
            cnt += 1
            if s % i == 0:
                break
        fibonamial.append(cnt)
def solve():
    value = SIZE3
    c = factorial(i)   
    for j in range(2, i + 1):
        if c[j] == 0:
            continue
        value = min(value, calc(n, fibonamial[primes.index(j)], j) // c[j])
    return value
n, p = map(int, input().split())
sieve = [True for _ in range(SIZE1)]
primes = [2]
fibonamial = []
eratosthenes()
for i in range(2, p + 1):
    print(solve())
