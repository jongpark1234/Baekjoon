def processing(n, o):
    if n == 3:
        print(f'{2} to {-1}')
        print(f'{5} to {2}')
        print(f'{3} to {-3}')
    elif n == 4:
        print(f'{o + 6} to {o - 1}')
        print(f'{o + 3} to {o + 6}')
        print(f'{o} to {o + 3}')
        print(f'{o + 7} to {o}')
    elif n == 5:
        print(f'{o + 8} to {o - 1}')
        print(f'{o + 3} to {o + 8}')
        print(f'{o + 6} to {o + 3}')
        print(f'{o} to {o + 6}')
        print(f'{o + 9} to {o}')
    elif n == 6:
        print(f'{o + 10} to {o - 1}')
        print(f'{o + 7} to {o + 10}')
        print(f'{o + 2} to {o + 7}')
        print(f'{o + 6} to {o + 2}')
        print(f'{o} to {o + 6}')
        print(f'{o + 11} to {o}')
    elif n == 7:
        print(f'{o + 8} to {o - 1}')
        print(f'{o + 5} to {o + 8}')
        print(f'{o + 12} to {o + 5}')
        print(f'{o + 3} to {o + 12}')
        print(f'{o + 9} to {o + 3}')
        print(f'{o} to {o + 9}')
        print(f'{o + 13} to {o}')
    else:
        print(f'{n * 2 + o - 2} to {o - 1}')
        print(f'{o + 3} to {n * 2 + o - 2}')
        processing(n - 4, o + 4)
        print(f'{o} to {n * 2 + o - 5}')
        print(f'{n * 2 + o - 1} to {o}')
processing(int(input()), 0)
