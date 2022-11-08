for _ in range(int(input())):
    b, p = map(float, input().split())
    print(*[60 * (b + i) / p for i in range(-1, 2)])
