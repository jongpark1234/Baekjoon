while True:
    a, b = map(int, input().split())
    if a == b == 0:
        break
    result = a - b
    print('0 0' if result == 1 else f'{result // 2} 0' if result % 2 == 0 else f'{(result - 3) // 2} 1')
