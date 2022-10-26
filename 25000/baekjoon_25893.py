for _ in range(int(input())):
    a, b, c = map(int, input().split())
    print(a, b, c)
    print(['zilch', 'double', 'double-double', 'triple-double'][sum([a >= 10, b >= 10, c >= 10])])
    print()
