from math import sqrt, hypot
for _ in range(int(input())):
    a, b, c, d = map(int, input().split())
    if a < b:
        a, b = b, a
    if c < d:
        c, d = d, c
    if a > c and b > d:
        print('Escape is possible.')
        continue
    if d >= b:
        print('Box cannot be dropped.')
        continue
    x, y = hypot(a, b), hypot(c, d)
    if y < b:
        print('Escape is possible.')
        continue
    if y > x:
        print('Box cannot be dropped.')
        continue
    print('Escape is possible.' if d < hypot((b - sqrt(y ** 2 - a ** 2)) / 2, (a - sqrt(y ** 2 - b ** 2)) / 2) else 'Box cannot be dropped.')
