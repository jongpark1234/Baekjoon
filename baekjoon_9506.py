while True:
    divisor = []
    n = int(input())
    if n == -1:
        break
    for i in range(1, n):
        if n % i == 0:
            divisor.append(i)
    if sum(divisor) == n:
        print(f'{n} = {divisor[0]}', end=' ')
        for i in range(1, len(divisor)):
            print('+', divisor[i], end=' ')
        print()
    else:
        print(f'{n} is NOT perfect.')
