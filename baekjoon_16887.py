ret = 0
n = int(input())
for i in list(map(int, input().split())):
    if 3 >= i >= 1:
        ret ^= 0
    elif 15 >= i >= 4:
        ret ^= 1
    elif 81 >= i >= 16:
        ret ^= 2
    elif 6723 >= i >= 82:
        ret ^= 0
    elif 50625 >= i >= 6724:
        ret ^= 3
    elif 2562991875 >= i >= 50626:
        ret ^= 1
    else:
        ret ^= 2
print('koosaga' if ret else 'cubelover')
