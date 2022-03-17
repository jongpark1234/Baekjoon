from math import gcd
n = int(input())
a = list(map(int, input().split()))
mole, deno = 1, a[0]
for i in range(1, n):
    mole = mole * a[i] + deno
    deno *= a[i]
GCD = gcd(mole, deno)
mole //= GCD
deno //= GCD
print(f'{deno}/{mole}')
