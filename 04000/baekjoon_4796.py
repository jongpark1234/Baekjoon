tc = 0
while True:
    tc += 1
    l, p, v = map(int, input().split())
    if l == p == v == 0:
        break
    print(f'Case {tc}: {((v // p) * l) + min(v % p, l)}')
