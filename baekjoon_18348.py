from math import gcd
sieve = [0] * 1835008
primes = [0] * 103000
pp, p, q = 0, -1, -1
s, n = input().split()
n = int(n)
if s[0] == 'o':
    if n >= 6:
        print('4 2', end = ' ')
        for i in range(8, n + 1, 2):
            print(i, end = ' ')
        print('6 3 1', end = ' ')
        for i in range(7, n + 1, 2):
            print(i, end = ' ')
        print('5')
    elif n == 5:
        print('4 2 3 1 5')
    else:
        for i in range(2, n + 1, 2):
            print(i, end = ' ')
        for i in range(1, n + 1, 2):
            print(i, end = ' ')
    exit(0)
elif n < 8:
    if n == 2:
        print('1 2')
    elif n == 3:
        print('1 2 3')
    elif n == 4:
        print('1 2 3 4')
    elif n == 5:
        print('1 2 5 3 4')
    elif n == 6:
        print('1 4 3 2 5 6')
    elif n == 7:
        print('1 2 3 4 7 6 5')
    exit(0)
for i in range(2, (n << 1) + 1):
    if sieve[i]:
        continue
    if i < n:
        primes[pp] = i
        pp += 1
    for j in range(i * 2, (n << 1) + 1, i):
        sieve[j] = 1
if n & 1:
    m = n - 1
    x = 1
    for i in range(1, m + 1):
        if not sieve[n + i]:
            x = i
            break
else:
    m = n
    x = 1
for i in range(1, pp):
    if sieve[primes[i] + m]:
        continue
    for j in range(1, i):
        if sieve[primes[j] + m]:
            continue
        if gcd(primes[i] - primes[j], m) == 2:
            p = primes[i]
            q = primes[j]
            break
    if p >= 0:
        break
for i in range(1, m + 1):
    print(x, end = ' ')
    if i & 1:
        x = (q - x + m - 1) % m + 1
    else:
        x = (p - x + m - 1) % m + 1
if n & 1:
    print(n)
