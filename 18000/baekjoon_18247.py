for _ in range(int(input())):
    n, m = map(int, input().split())
    print(m * 11 + 4 if n > 11 and m > 3 else -1)
