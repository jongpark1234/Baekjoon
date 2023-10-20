def f(x):
    return x * 2 - x % 2
for _ in range(int(input())):
    x, y = map(int, input().split())
    if x == y:
        print(f(x))
    elif x == y + 2:
        print(f(x - 2) + 2)
    else:
        print('No Number')
