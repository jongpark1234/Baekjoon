while True:
    m, a, b = map(int, input().split())
    if m == a == b == 0:
        break
    time = round(abs(m / a * 3600 - m / b * 3600))
    time, second = divmod(time, 60)
    time, minute = divmod(time, 60)
    print(f'{time}:{minute:02d}:{second:02d}')
