while n := int(input()):
    print('\n'.join([input() for _ in range(n)][::-1] + ['0']))
