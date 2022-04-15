from math import gcd
VALUE = 1e18
def R(a,b):
    if b == 1:
        return a
    if a >= b:
        return R(abs(a // b), b)
    else:
        return R(b, a)
def C(g, h, o):
    a = g
    k = 1
    while a > k:
        k *= h
    if o:
        k *= h
    a = (k * 2 // a - 1) * g
    if a == g:
        g = 0
    return [h * a + g, a]
for _ in range(int(input())):
    g, h = map(int, input().split())
    value1 = C(g, h, False)
    value2 = C(g, h, True)
    n1 = n2 = 0
    if value1[0] > VALUE:
        n1 += 1
    if value1[0] > VALUE:
        n2 += 1
    if gcd(value1[0], value1[1]) != g or R(value1[0], value1[1]) != h:
        n1 += 1
    if gcd(value2[0], value2[1]) != g or R(value2[0], value2[1]) != h:
        n2 += 1
    if n1 == 0:
        print(value1[0], value1[1])
    elif n2 == 0:
        print(value2[0], value2[1])
