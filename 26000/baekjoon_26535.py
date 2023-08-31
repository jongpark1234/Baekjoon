n = 1
denotes = int(input())
while denotes > n ** 2:
    n += 1
print('x' * (n + 2))
print('\n'.join('x' + '.' * n + 'x' for _ in range(n)))
print('x' * (n + 2))
