while True:
    side = sorted(list(map(int, input().split())))
    if sum(side) == 0:
        break
    elif side[2] >= side[1] + side[0]:
        print('Invalid')
    elif side[0] == side[1] == side[2]:
        print('Equilateral')
    elif side[0] == side[1] or side[1] == side[2] or side[0] == side[2]:
        print('Isosceles')
    else:
        print('Scalene')
