from math import gcd
for i in range(int(input())):
    a, b = map(int, input().split())
    print(a * b // gcd(a, b), gcd(a, b))
