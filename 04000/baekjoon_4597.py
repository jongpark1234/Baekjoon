while True:
    s = input()
    if s == '#':
        break
    p, s = s[-1], s[:-1]
    on = s.count('1')
    if p == 'e':
        s += str(on & 1)
    else:
        s += str(on & 1 ^ 1)
    print(s)
