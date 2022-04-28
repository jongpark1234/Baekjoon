def extendedGCD(a, b):
    if b == 0:
        return a, 1, 0
    GCD, x, y = extendedGCD(b, a % b)
    return GCD, y, x - (a // b) * y
def Problem(a, b, s):
    if a == b == 0:
        return s == 0
    if a == 0:
        return s % b == 0
    if b == 0:
        return s % a == 0
    GCD, x, y = extendedGCD(a, b)
    if s % GCD != 0:
        return False
    x *= s // GCD
    y *= s // GCD
    for i in range(-GCD * x // b + 1, GCD * y // a + 1):
        if extendedGCD(x + i * b // GCD, y - i * a // GCD)[0] == 1:
            return True
    return False
print('YES' if Problem(*map(int, input().split())) else 'NO')
