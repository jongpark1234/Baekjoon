while True:
    a, b, c, d = map(int, input().split())
    if 0 == a == b == c == d:
        break
    print(c - b, d - a)
