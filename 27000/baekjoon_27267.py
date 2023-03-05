a, b, c, d = map(int, input().split())
m, p = a * b, c * d
print('M' if m > p else 'P' if m < p else 'E')
