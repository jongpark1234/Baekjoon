re1, re2 = [11, 15, 19, 29, 33], [1, 2, 6, 10, 16, 22, 26, 30, 36, 40, 44]
n, m = map(int, input().split())
if n > 44 and m > 44:
    print('hs' if (n - 45) % 34 in re1 and (m - 45) % 34 in re1 else 'sh')
    exit(0)
if n < 45 and m < 45:
    print('hs' if n in re2 and m in re2 else 'sh')
    exit(0)
if n > m:
    n, m = m, n
print('hs' if n in re2 and (m - 45) % 34 in re1 else 'sh')
