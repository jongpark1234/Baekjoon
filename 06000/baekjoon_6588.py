from sys import stdin
from math import isqrt
MAX = 1000000
sieve = [False, False] + [True for _ in range(MAX - 1)]
for i in range(2, isqrt(MAX) + 1):
    if sieve[i]:
        for j in range(i * 2, MAX, i):
            sieve[j] = False
while True:
    n = int(stdin.readline())
    if n == 0:
        break
    for i in range(3, MAX + 1, 2):
        if sieve[i] and sieve[n - i]:
            print(f'{n} = {i} + {n - i}')
            break
    else:
        print('Goldbach\'s conjecture is wrong.')
