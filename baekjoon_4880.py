from sys import stdin
while True:
    a, b, c = map(int, stdin.readline().split())
    if a == b == c == 0:
        break
    if b - a == c - b:
        print(f'AP {c + (b - a)}')
    elif b // a == c // b:
        print(f'GP {c * (b // a)}')
