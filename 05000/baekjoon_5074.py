while True:
    t1, t2 = input().split()
    h1, m1, h2, m2 = map(int, t1.split(':') + t2.split(':'))
    if h1 == m1 == h2 == m2 == 0:
        break
    h, m = divmod(m1 + m2, 60)
    d, h = divmod(h + h1 + h2, 24)
    print(f'{h:02d}:{m:02d}{f" +{d}" if d else ""}')
