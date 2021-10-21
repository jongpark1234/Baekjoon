n = int(input())
star = 0
space = n - 1
print(' ' * space + '*')
for i in range(n - 2):
    space -= 1
    print(' ' * space + '*' + ' ' * (i * 2 + 1) + '*')
if (n != 1): print('*' * (n * 2 - 1))
