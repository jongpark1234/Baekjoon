for i in range(1, int(input()) + 1):
    length = sorted(list(map(int, input().split())))
    print(f'Scenario #{i}:')
    print('yes\n' if length[0] ** 2 + length[1] ** 2 == length[2] ** 2 else 'no\n')
