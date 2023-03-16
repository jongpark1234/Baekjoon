while True:
    a, d, x = map(int, input().split())
    if a == d == x == 0:
        break
    n, m = divmod(x - a, d)
    print(n + 1 if m == 0 and m >= 0 else 'X')
