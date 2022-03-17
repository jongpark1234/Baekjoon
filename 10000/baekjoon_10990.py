n = int(input())
space = n - 1
print(' ' * space + '*')
for i in range(n - 1):
    space -= 1
    print(' ' * space + '*' + ' ' * (i * 2 + 1) + '*')
