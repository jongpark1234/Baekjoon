from sys import *
from math import *
def lcm(a, b):
    return a * b // gcd(a, b)
t = int(stdin.readline())
for i in range(t):
    x, y = map(int, stdin.readline().split())
    print(lcm(x, y))