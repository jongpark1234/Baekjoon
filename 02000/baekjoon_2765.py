from math import acos
tc = 0
while True:
    tc += 1
    a, b, c = map(float, input().split())
    if b == 0:
        break
    distance = a * b * acos(-1) / 63360
    print(f'Trip #{tc}: {round(distance, 2):.2f} {round(distance / c * 3600, 2):.2f}')
