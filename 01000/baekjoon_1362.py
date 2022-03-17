case = 0
while True:
    die = False
    case += 1
    o, w = map(int, input().split())
    if o == w == 0:
        break
    while True:
        cmd, num = input().split()
        if f'{cmd} {num}' == '# 0':
            break
        if cmd == 'E':
            w -= int(num)
        else:
            w += int(num)
        if w < 1:
            die = True
    print(case, end = ' ')
    if die:
        print('RIP')
    elif o // 2 < w < o * 2:
        print(':-)')
    else:
        print(':-(')
