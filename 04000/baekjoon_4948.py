# pypy3
from sys import stdin
def isprime(num):
    for i in range(2, int(num ** 0.5) + 1):
        if not num % i:
            return False
    return True
while True:
    n = int(stdin.readline())
    if n == 0: break
    cnt = 0
    for i in range(n + 1, n * 2 + 1):
        if isprime(i):
            cnt += 1
    print(cnt)
