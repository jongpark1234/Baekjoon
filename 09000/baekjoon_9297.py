for i in range(int(input())):
    n, d = map(int, input().split())
    I, n = divmod(n, d)
    print(f'Case {i + 1}:', end=' ')
    if I == 0 and n == 0:
        print(0)
    elif I == 0:
        print(f'{n}/{d}')
    elif n == 0:
        print(I)
    else:
        print(f'{I} {n}/{d}')
