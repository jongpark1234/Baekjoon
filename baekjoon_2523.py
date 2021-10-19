n = int(input())
star = 0
for i in range(n):
    star += 1
    print('*' * star, end='')
    print()
for i in range(n - 1):
    star -= 1
    print('*' * star, end='')
    print()
