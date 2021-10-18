n = int(input())
star = 0
space = n * 2
for i in range(n):
    star += 1
    space -= 2
    print('*' * star, end='')
    print(' ' * space, end='')
    print('*' * star)
for i in range(n - 1):
    star -= 1
    space += 2
    print('*' * star, end='')
    print(' ' * space, end='')
    print('*' * star)
