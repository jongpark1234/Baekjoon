ret = 0
n = int(input())
for i in list(map(int, input().split())):
    if 2 >= i >= 1:
        ret ^= 1
    elif 5 >= i >= 3:
        ret ^= 2
    elif 9 >= i >= 6:
        ret ^= 3
    elif 14 >= i >= 10:
        ret ^= 4
    elif 20 >= i >= 15:
        ret ^= 5
    elif 27 >= i >= 21:
        ret ^= 6
    elif 35 >= i >= 28:
        ret ^= 7
    elif 44 >= i >= 36:
        ret ^= 8
    elif 54 >= i >= 45:
        ret ^= 9
    else:
        ret ^= 10
print('koosaga' if ret else 'cubelover')
