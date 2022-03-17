a, b = map(int, input().split())
if a == b == 0:
    print('Not a moose')
elif a == b:
    print(f'Even {a * 2}')
else:
    print(f'Odd {max(a, b) * 2}')
