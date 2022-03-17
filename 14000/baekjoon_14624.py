n = int(input())
if n % 2 == 0:
    print('I LOVE CBNU')
else:
    space = int(n / 2)
    print('*' * n)
    print(' ' * space + '*')
    for i in range(1, int(n / 2) + 1):
        space -= 1
        print(' ' * space + '*' + ' ' * ((i - 1) * 2 + 1) + '*')
