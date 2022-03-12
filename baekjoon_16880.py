from sys import stdin
ret = 0
for _ in range(int(stdin.readline())):
    x, y, c = stdin.readline().rstrip().split()
    x = int(x); y = int(y)
    if y > x:
        x, y = y, x
    if c == 'R':
        ret ^= x ^ y
    elif c == 'B':
        ret ^= min(x, y)
    elif c == 'K':
        if y % 2 == 0:
            ret ^= 0 if x % 2 == 0 else 1
        else:
            ret ^= 3 if x % 2 == 0 else 2
    elif c == 'N':
        if x == y:
            ret ^= 1 if x % 3 == 2 else 0
        elif x == y + 1:
            ret ^= 0 if x % 3 == 0 else 1
        else:
            ret ^= y % 3
    elif c == 'P':
        ret ^= ((x // 3) ^ (y // 3)) * 3 + (x + y) % 3
print('koosaga' if ret else 'cubelover')
