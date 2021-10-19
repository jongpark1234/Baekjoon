n = int(input())
space = n
star = 0
for i in range(n):
    space -= 1
    star += 1
    print(' ' * space, end='')
    print('*' * star)
for i in range(n - 1):
    space += 1
    star -= 1
    print(' ' * space, end='')
    print('*' * star)
