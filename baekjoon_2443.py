n = int(input())
space = 0
star = n * 2 - 1
for i in range(n):
    print(' ' * int(space), end='')
    print('*' * int(star))
    space += 1
    star -= 2
