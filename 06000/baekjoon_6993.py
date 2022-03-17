for _ in range(int(input())):
    w, n = input().split()
    print(f'Shifting {w} by {n} positions gives us: {w[-int(n):] + w[:-int(n)]}')
