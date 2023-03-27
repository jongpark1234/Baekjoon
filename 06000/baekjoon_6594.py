x = 10 ** 50
for tc, i in enumerate([*open(0)]):
    lt, rt = map(eval, i.rstrip().split('='))
    nx = lt // x - rt // x
    y = rt % x - lt % x
    print(f'Equation #{tc + 1}')
    if nx == 0 and y != 0:
        print('No solution.')
    elif nx == 0 and y == 0:
        print('Infinitely many solutions.')
    else:
        print(f'x = {y / nx:.6f}')
    print()
