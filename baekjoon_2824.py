from math import gcd
from sys import stdin
n = int(stdin.readline())
a = list(map(int, stdin.readline().split()))
A = a[0]
for i in range(1, n):
    A *= a[i]
m = int(stdin.readline())
b = list(map(int, stdin.readline().split()))
B = b[0]
for i in range(1, m):
    B *= b[i]
GCD = str(gcd(A, B))
if len(GCD) > 9:
    print(GCD[-9:])
else:
    print(GCD)
