for k in range(int(input())):
    e, a = map(int, input().split())
    print(f'Data Set {k + 1}:')
    if e <= a:
        print('no drought\n')
    else:
        temp = 0
        while e > a:
            a *= 5
            temp += 1
        print('mega ' * (temp - 1) + 'drought\n')
