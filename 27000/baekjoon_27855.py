h1, b1 = map(int, input().split())
h2, b2 = map(int, input().split())
one, two = h1 * 3 + b1, h2 * 3 + b2
print('NO SCORE' if one == two else f'{(two > one) + 1} {abs(two - one)}')
