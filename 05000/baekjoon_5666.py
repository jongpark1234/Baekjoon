while True:
    try:
        h, p = map(int, input().split())
        print(f'{round(h / p, 2):.2f}')
    except EOFError:
        break
