picture = []
for i in range(5):
    n = input()
    picture.append(n)
for i in range(5):
    for j in range(len(n)):
        if picture[2][j] == 'm':
            if i == 0:
                print('o', end='')
            elif i == 1:
                print('w', end='')
            elif i == 2:
                print('l', end='')
            elif i == 3:
                print('n', end='')
            else:
                print('.', end='')
        elif picture[2][j] == 'l':
            if i == 0:
                print('.', end='')
            elif i == 1:
                print('o', end='')
            elif i == 2:
                print('m', end='')
            elif i == 3:
                print('l', end='')
            else:
                print('n', end='')
        else:
            if i == 0:
                print('.', end='')
            elif i == 1:
                print('.', end='')
            elif i == 2:
                print('o', end='')
            elif i == 3:
                print('L', end='')
            else:
                print('n', end='')
    print()
