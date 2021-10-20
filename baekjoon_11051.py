import sys
from math import *
n,k = map(int, sys.stdin.readline().split())
answer = factorial(n) // (factorial(k) * factorial(n-k))
print(answer % 10007)
