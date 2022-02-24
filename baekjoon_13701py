import sys
import os
nlist = bytearray(4914304)
us = os.fdopen(sys.stdin.fileno(), 'rb', 1000000)
while True:
    n = 0
    while True:
        ch = us.read(1)
        if b'0' <= ch <= b'9':
            n = 10 * n + int(ch)
        elif ch == b' ':
            break
        else:
            x, y = n % 8, n // 8
            if not nlist[y] & (1 << x):
                print(n, end = '')
            exit()
    x, y = n % 8, n // 8
    if not nlist[y] & (1 << x):
        print(n, end = ' ')
    nlist[y] |= (1 << x)
