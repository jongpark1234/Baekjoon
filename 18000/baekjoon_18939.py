from sys import stdin
for _ in range(int(input())):
    n, m, k = map(int, stdin.readline().split())
    print('Yuto' if max(n, m) < k * 2 or n * m % 2 else 'Platina')
