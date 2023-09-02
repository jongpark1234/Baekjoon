from sys import stdin
for i in range(int(input())):
    a, b, c = sorted(map(int, stdin.readline().split()))
    print(f'Case #{i + 1}: {"YES" if a ** 2 + b ** 2 == c ** 2 else "NO"}')
