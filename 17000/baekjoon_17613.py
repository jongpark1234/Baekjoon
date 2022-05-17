def dnc(x, y):
    if y < 2:
        return y
    n = 30
    while y < (1 << n) - 1:
        n -= 1
    line = (1 << n) - 1
    if x > line - 1:
        return dnc(x - line, y - line) + n
    else:
        w = n
        for i in range(max(0, n - line + x - 1), n - 1)[::-1]:
            w += i
        return max(dnc(0, y - line) + n, w)
for _ in range(int(input())):
    print(dnc(*map(int, input().split())))
