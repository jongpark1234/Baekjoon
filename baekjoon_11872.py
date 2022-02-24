ret = 0
n = int(input())
for i in list(map(int, input().split())):
    if i % 4 == 0:
        i -= 1
    elif i % 4 == 3:
        i += 1
    ret ^= i
print('koosaga' if ret else 'cubelover')
