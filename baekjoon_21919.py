from math import gcd
primes = []
def isprime(num):
    if num == 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
n = int(input())
for i in list(map(int, input().split())):
    if isprime(i):
        primes.append(i)
if primes:
    num = primes[0]
    for i in range(1, len(primes)):
        num = num * primes[i] // gcd(num, primes[i])
    print(num)
else:
    print(-1)
