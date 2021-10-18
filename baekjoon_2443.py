n = int(input())
space = - 1
star = n * 2
for i in range(n):
    space += 1
    print(' ' * int(space), end='')
    print('*' * int(star - 1))
    star -= 2
