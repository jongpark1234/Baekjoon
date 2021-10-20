n = int(input())
space = n - 1
star = 1
for i in range(n):
    for j in range(space):
        print(' ', end='')
    for k in range(star):
        print('* ', end='')
    space -= 1
    star += 1
    print()
