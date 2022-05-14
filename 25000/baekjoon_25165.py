n, m = map(int, input().split())
Ac, d = map(int, input().split())
Sr, Sc = map(int, input().split())
field = [[0 for _ in range(m)] for _ in range(n)]
field[Sr - 1][Sc - 1] = 1
posX, posY = Ac - 1, 0
while True:
    if d == 0:
        if posX == 0:
            posY += 1
            d = 1
        else:
            posX -= 1
    else:
        if posX == m - 1:
            posY += 1
            d = 0
        else:
            posX += 1
    if posY == n - 1 and posX == m - 1:
        print('YES!')
        break
    if field[posY][posX] == 1:
        print('NO...')
        break
