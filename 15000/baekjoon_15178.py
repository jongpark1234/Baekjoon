for _ in range(int(input())):
    a, b, c = map(int, input().split())
    print(a, b, c, 'Seems OK' if a + b + c == 180 else 'Check')
