n = int(input())
space = 1
print('*' * n + ' ' * (n * 2 - 3) + '*' * n)
for i in reversed(range(n - 2)):
    print(' ' * space + '*' + ' ' * (n - 2) + '*' + ' ' * (i * 2 + 1) + '*' + ' ' * (n - 2) + '*')
    space += 1
print(' ' * space + '*' + ' ' * (n - 2) + '*' + ' ' * (n - 2) + '*')
for i in range(n - 2):
    space -= 1
    print(' ' * space + '*' + ' ' * (n - 2) + '*' + ' ' * (i * 2 + 1) + '*' + ' ' * (n - 2) + '*')
print('*' * n + ' ' * (n * 2 - 3) + '*' * n)