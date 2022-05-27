while True:
    d, rh, rv = map(float, input().split())
    if d == rh == rv == 0:
        break
    w = 16 * d / (337 ** 0.5)
    h = 9 * w / 16
    print(f'Horizontal DPI: {rh / w:.2f}\nVertical DPI: {rv / h:.2f}')
