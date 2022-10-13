while True:
    h, w = sorted(map(int, input().split()))
    if w == h == 0: break
    print(1 if w == h else w * h if w % h else w // h)
