from math import gcd
n, m = map(int, input().split(':'))
while True:
    GCD = gcd(n, m)
    if GCD == 1:
        break
    n //= GCD
    m //= GCD
print(n, m, sep=':')
