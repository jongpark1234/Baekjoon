from math import pi, cos
for i in range(int(input())):
    x, a, sa, sm = map(float, input().split())
    d = 6378.1 / cos(pi * (90 - (a / 2)) / 180)
    result = (x - d) / sa - (d - 6378.1) / sm
    print(f'Data Set {i + 1}:')
    print('Oh no!' if result < 0 else f'{result:.2f}', end = '\n\n')
