def calc(a, o, b):
    a, b = int(a), int(b)
    if o == '/':
        if a * b < 0:
            return abs(a) // abs(b) * -1
        else:
            return a // b
    return eval(f'{a}{o}{b}')
k1, o1, k2, o2, k3 = input().split()
print(*sorted([calc(calc(k1, o1, k2), o2, k3), calc(k1, o1, calc(k2, o2, k3))]))
