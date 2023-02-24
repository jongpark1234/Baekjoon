for _ in range(int(input())):
    p, t = map(int, input().split())
    print(p - t // 7 + t // 4)
