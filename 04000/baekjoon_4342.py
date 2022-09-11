def gcd(a, b):
    a, b = sorted([a, b])
    if b % a == 0:
        return True
    if b - a < a:
        return not gcd(b - a, a)
    return True
while True:
    a, b = map(int, input().split())
    if a == b == 0:
        break
    print('A' if gcd(a, b) else 'B', 'wins')
