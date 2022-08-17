for _ in range(int(input())):
    d, n, s, p = map(int, input().split())
    s, p = s * n, d + p * n
    print('does not matter' if s == p else 'do not parallelize' if s < p else 'parallelize')
