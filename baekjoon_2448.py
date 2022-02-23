def printing(x, y, n):
    if n == 3:
        ans[x][y] = '*'
        ans[x + 1][y - 1] = ans[x + 1][y + 1] = '*'
        for i in range(-2, 3):
            ans[x + 2][y + i] = '*'
    else:
        s = n // 2
        printing(x, y, s)
        printing(x + s, y - s, s)
        printing(x + s, y + s, s)
n = int(input())
ans = [[' '] * 2 * n for _ in range(n)]
printing(0, n - 1, n)
for i in ans:
    print("".join(i))