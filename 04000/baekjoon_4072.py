while True:
    s = input().split()
    if s == ['#']:
        break
    print(*map(lambda x: x[::-1], s))
