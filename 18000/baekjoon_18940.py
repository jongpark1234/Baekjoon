from sys import stdin
for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    print('Platina' if n in [0, 14, 34] or n % 34 in [4, 8, 20, 24, 28] else 'Yuto')
