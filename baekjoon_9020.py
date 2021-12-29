primes = {i for i in range(2, 10001) if i == 2 or i % 2 == 1}
for odd in range(3, 101, 2):
    primes -= {i for i in range(2 * odd, 10001, odd) if i in primes}
for _ in range(int(input())):
    n = int(input())
    halfnum = n // 2
    for i in range(halfnum, 1, -1):
        if n - i in primes and i in primes:
            print(i, n - i)
            break
