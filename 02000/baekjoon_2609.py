from math import *
def lcm(a, b):
    return a * b // gcd(n, m)
n, m = map(int, input().split())
print(gcd(n, m))
print(lcm(n, m))
