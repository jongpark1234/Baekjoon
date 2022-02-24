ret = 0
n = int(input())
for i in list(map(int, input().split())):
    if i % 2 == 0:
        i = (i // 2) - 1
    else:
        i = (i + 1) // 2
    ret ^= i
print('koosaga' if ret else 'cubelover')
