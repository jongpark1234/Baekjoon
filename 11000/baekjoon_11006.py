for _ in range(int(input())):
    n, m = map(int, input().split())
    oneleg = m * 2 - n
    print(oneleg, m - oneleg)
