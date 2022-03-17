n = int(input())
space = False
for i in range(n):
    print(' ' * int(space), end='')
    print('* ' * n)
    space = not space
