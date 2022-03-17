from sys import stdin
from math import sqrt
def isprime(num):
    if num == 1:
        return False
    else:
        for i in range(2, int(sqrt(num) + 1)):
            if num % i == 0:
                return False
        return True
while True:
    n = int(stdin.readline())
    if n == 0:
        break
    for i in range(3, n):
        if isprime(i) and (isprime(n - i)):
            print(f'{n} = {i} + {n - i}')
            break
