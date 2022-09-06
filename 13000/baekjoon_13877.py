for _ in range(int(input())):
    k, n = input().split()
    o, n, h = 0 if '9' in n or '8' in n else int(n, 8), int(n), int(n, 16)
    print(k, o, n, h)
