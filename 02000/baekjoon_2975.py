while True:
    a, w, b = input().split()
    if f'{a}{w}{b}' == '0W0':
        break
    a, b = int(a), int(b)
    result = a - b if w == 'W' else a + b
    print(result if result > -201 else 'Not allowed')
