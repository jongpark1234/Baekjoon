from sys import stdin
for _ in range(int(stdin.readline())):
    s = []
    a, b, c, d = map(int, stdin.readline().split())
    for i in range(-2000000, 2000001):
        if a * i ** 3 + b * i ** 2 + c * i + d == 0:
            s.append(i)
            break
    b += a * s[0]
    c += b * s[0]
    x = b * b - 4 * a * c
    if b * b - 4 * a * c >= 0:
        s.append((-b + x ** 0.5) / (a * 2))
        s.append((-b - x ** 0.5) / (a * 2))
    for i in set(sorted(s)):
        print(f'{i:.4f}', end = ' ')
    print()
