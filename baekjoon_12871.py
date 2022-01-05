from math import gcd
def lcm(x, y):
    return x * y // gcd(x, y)
s = input()
t = input()
LCM = lcm(len(s), len(t))
if s * (LCM // len(s)) == t * (LCM // len(t)):
    print(1)
else:
    print(0)
