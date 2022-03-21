from sys import stdin
for i in range(int(stdin.readline())):
    n = int(stdin.readline())
    a, b = map(int, stdin.readline().split())
    for _ in range(n):
        a, b = map(int, stdin.readline().split())
    print(f'Material Management {i + 1}')
    print('Classification ---- End!')
