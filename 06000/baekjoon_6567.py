from math import gcd
while True:
    n, k = map(int, input().split())
    if n == k == 0:
        break
    print((sum(pow(n, gcd(k, i)) for i in range(1, k + 1)) + ((k >> 1) * (pow(n, k >> 1) + pow(n, (k >> 1) + 1)) if ~k & 1 else k * pow(n, k + 1 >> 1))) // (k << 1))
