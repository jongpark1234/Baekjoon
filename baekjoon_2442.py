n = int(input())
space = n
star = -1
for i in range(n):
    space -= 1
    star += 2
    for j in range(space):
        print(' ', end='')
    for k in range(star):
        print('*', end='')
    print()