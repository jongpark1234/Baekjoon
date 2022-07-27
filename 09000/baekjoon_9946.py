tc = 0
while True:
    tc += 1
    if (a := input()) == (b := input()) == 'END':
        break
    print(f'Case {tc}:', 'same' if sorted(list(a)) == sorted(list(b)) else 'different')
