from sys import stdin
def power(x, y, p):
    r = 1
    while y:
        if y & 1:
            r = (r * x) % p
        y //= 2
        x = (x * x) % p
    return r
def millerRabin(n, a):
    r = 0
    d = n - 1
    while d % 2 == 0:
        r += 1
        d //= 2
    x = power(a, d, n)
    if x == 1 or x == n - 1:
        return True
    for _ in range(r - 1):
        x = power(x, 2, n)
        if x == n - 1:
            return True
    return False
count = 0
for _ in range(int(stdin.readline())):
    isprime = 0
    s = int(stdin.readline())
    for i in [2, 3, 5, 7, 11]:
        if millerRabin(2 * s + 1, i):
            isprime += 1
        else:
            break
    if isprime == 5:
        count += 1
print(count)
