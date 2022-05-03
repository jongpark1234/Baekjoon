from sys import setrecursionlimit
setrecursionlimit(10 ** 6)
a = []
def f(n, m, i, j, k):
    if n == 0:
        return False
    if m == 0:
        return True
    if n <= 1 and i <= j:
        return False
    if n > 1:
        x = i
        y = a[k][n - 1]
        if x + y > j:
            if not f(m, n - 1, j, x + y, not k):
                return True
    if i > j:
        if not f(m - 1, n, a[not k][m - 1], i, not k):
            return True
    return False
tc = 1
while True:
    try:
        a = []
        n, m = map(int, input().split())
        for _ in range(2):
            a.append(sorted([0] + list(map(int, input().split()))))
        print(f'Case {tc}:', end = ' ')
        print(['Buyout Limited', 'Takeover Incorporated'][f(n, m, a[0][n], a[1][m], False)])
        tc += 1
    except EOFError:
        break
