while True:
    result = 0
    a, b, c, d = map(int, input().split())
    if a == b == c == d == 0:
        break
    while not a == b == c == d:
        result += 1
        a, b, c, d = abs(a - b), abs(b - c), abs(c - d), abs(d - a)
    print(result)
