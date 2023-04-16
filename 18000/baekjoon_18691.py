for _ in range(int(input())):
    g, c, e = map(int, input().split())
    print(max(e - c, 0) * [1, 3, 5][g - 1])
