n = int(input())
for _ in range(2):
    for _ in range(n):
        print('@' * n + ' ' * n * 3 + '@' * n)
    for _ in range(n):
        print('@' * n * 5)
for _ in range(n):
    print('@' * n + ' ' * n * 3 + '@' * n)
