for i in range(int(input())):
    m = 0
    Input = list(map(int, input().split()))
    for j in range(5):
        m = m * [20, 18][j == 3] + Input[j]
    result = int(input()) - m - 584054
    print(f'Data Set {i + 1}:')
    print('It\'s a hoax!' if result < 0 else 'Panic!' if result == 0 else result, end = '\n\n')
