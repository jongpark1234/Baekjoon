n = int(input())
if n % 2 == 0:
    first, second= n // 2, n // 2
else:
    first = n // 2 + 1
    second = n - first
for i in range(n):
    print('* ' * first)
    print(' *' * second)
