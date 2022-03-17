# pypy3
from sys import stdin
primes = {i for i in range(2, 1000001) if i == 2 or i % 2 == 1}
for odd in range(3, 10001, 2):
    primes -= {i for i in range(2 * odd, 1000001, odd) if i in primes}
for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    count = 0
    for i in range(2, n // 2 + 1):
        if n - i in primes and i in primes:
            count += 1
    print(count)
