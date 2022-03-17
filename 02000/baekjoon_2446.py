n = int(input())
space = - 1
star = n * 2
for i in range(n):
    space += 1
    print(' ' * space, end='')
    print('*' * (star - 1))
    star -= 2
for j in range(n - 1):
    space -= 1
    star += 2
    print(' ' * space, end='')
    print('*' * (star + 1))
