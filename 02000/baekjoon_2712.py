for _ in range(int(input())):
    num, unit = input().split()
    num = float(num)
    if unit == 'kg':
        print('{:.4f}'.format(round(num * 2.2046, 4)), 'lb')
    elif unit == 'lb':
        print('{:.4f}'.format(round(num * 0.4536, 4)), 'kg')
    elif unit == 'l':
        print('{:.4f}'.format(round(num * 0.2642, 4)), 'g')
    elif unit == 'g':
        print('{:.4f}'.format(round(num * 3.7854, 4)), 'l')
