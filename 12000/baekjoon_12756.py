from math import ceil
a1, a2 = map(int, input().split())
b1, b2 = map(int, input().split())
a, b = ceil(a2 / b1), ceil(b2 / a1)
print('DRAW' if a == b else 'PLAYER A' if a > b else 'PLAYER B')
