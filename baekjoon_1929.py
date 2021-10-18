from math import *
m, n = map(int, input().split())
primes = []
def isprime(num):
    if num == 1:
        return False
    else:
        for i in range(2, int(sqrt(num) + 1)):
            if num % i == 0:
                return False
        return True
for i in range(m, n + 1):
    if isprime(i):
        print(i)
