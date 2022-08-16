while True:
    result = 0
    n = float(input())
    if n == 0:
        break
    for i in range(5):
        result += n ** i
    print(f'{round(result, 2):.2f}')
