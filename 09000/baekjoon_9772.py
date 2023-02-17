while True:
    x, y = map(float, input().split())
    print('Q1' if x > 0 and y > 0 else 'Q2' if x < 0 and y > 0 else 'Q3' if x < 0 and y < 0 else 'Q4' if x > 0 and y < 0 else 'AXIS')
    if x == y == 0:
        break
