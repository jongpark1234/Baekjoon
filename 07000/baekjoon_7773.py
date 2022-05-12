x, y, d = map(int, input().split())
print('Impossible' if x ** 2 + y ** 2 > d ** 2 else 'Single staircase' if x ** 2 + y ** 2 == d ** 2 else ' '.join(map(str, [x * ((((x ** 2 + y ** 2) ** 0.5) + d) / 2) / ((x ** 2 + y ** 2) ** 0.5), y * ((((x ** 2 + y ** 2) ** 0.5) + d) / 2) / ((x ** 2 + y ** 2) ** 0.5), d - ((((x ** 2 + y ** 2) ** 0.5) + d) / 2)])))
