def euc(a, b):
    if b == 0:
        return a, 1, 0
    g, x, y = euc(b, a % b)
    return g, y, x - (a // b) * y
def Problem(a, b, s):
    if a == b == 0:
        return s == 0
    if a == 0:
        return s % b == 0
    if b == 0:
        return s % a == 0
    g, x, y = euc(a, b)
    if s % g != 0:
        return 0
    x *= s // g
    y *= s // g
    for i in range(-g * x // b + 1, g * y // a + 1):
        if euc(x + i * b // g, y - i * a // g)[0] == 1:
            return 1
    return 0
a, b, s = map(int, input().split())
print('YES' if Problem(a, b, s) else 'NO')
