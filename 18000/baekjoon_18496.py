from math import gcd
d, k = map(int, input().split())
D, K = d, k
while (GCD := gcd(d, K)) != 1:
    K //= GCD
    D *= GCD
print(D * (2 if d % 4 == 2 and k % 2 == 0 and k >= 4 else 1))
