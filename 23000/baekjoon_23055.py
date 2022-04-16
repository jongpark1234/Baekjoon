n = int(input())
if n == 1:
    print('*')
    exit()
print('*' * n)
for i in range(n // 2 - 1):
    print('*' + ' ' * i + '*' + ' ' * (n - 4 - (i * 2)) + '*' + ' ' * i + '*')
if n % 2:
    print('*' + ' ' * (n // 2 - 1) + '*' + ' ' * (n // 2 - 1) + '*')
for i in range(n // 2 - 1)[::-1]:
    print('*' + ' ' * i + '*' + ' ' * (n - 4 - (i * 2)) + '*' + ' ' * i + '*')
print('*' * n)
