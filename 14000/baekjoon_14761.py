x, y, n = map(int, input().split())
for i in range(1, n + 1):
    if i % x == 0:
        print('Fizz', end='')
    if i % y == 0:
        print('Buzz', end='')
    if i % x and i % y:
        print(i, end='')
    print()
