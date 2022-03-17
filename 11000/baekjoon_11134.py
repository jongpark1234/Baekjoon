for i in range(int(input())):
    n, c = map(int, input().split())
    if n / c == n // c:
        print(n // c)
    else:
        print(n // c + 1)
