from math import *
def color(x):
    if ceil(x / 8) % 2 == 0:
        if x % 2 == 0:
            return 'black'
        else:
            return 'white'
    else:
        if x % 2 == 0:
            return 'white'
        else:
            return 'black'
t = int(input())
for i in range(t):
    a, b = input().split()
    a = int((int(a[1]) - 1) * 8 + ord(a[0]) - 64)
    b = int(b)
    if color(a) == color(b):
        print('YES')
    else:
        print('NO')
