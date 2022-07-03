n = int(input())
if n % 4 > 1:
    print('NO')
else:
    print('YES')
    if n == 1:
        print(0)
    elif n == 5:
        print(2, 4, 1, 3, 0)
    else:
        print(*([n // 4 * 2 - 1] + [n // 4 * 4 - i + 1 for i in range(1, n // 4 + 1)] + [n // 4 * 3 - i for i in range(1, n // 4 + 1)] + [n // 4 * 2 - i - 1 for i in range(1, n // 4 - 1)] + [n // 4 * 3] + [n // 4 - i for i in range(n // 4 + 1)] if n % 4 else [n // 4 * 2] + [n // 4 * 4 - i for i in range(1, n // 4)] + [n // 4 * 3 - i for i in range(1, n // 4)] + [n // 4 * 2 - i for i in range(1, n // 4 + 1)] + [n // 4 * 3] + [n // 4 - i for i in range(1, n // 4 + 1)]))
