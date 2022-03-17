n = int(input())
star = -1
space = n
for i in range(n):
    star += 2
    space -= 1
    print(' ' * space, end='')
    print('*' * star)
for i in range(n - 1):
    star -= 2
    space += 1
    print(' ' * space, end='')
    print('*' * star)
