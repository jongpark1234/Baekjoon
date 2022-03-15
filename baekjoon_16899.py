ret = 0
def grundy(n):
    n -= 1
    if n % 4 == 0:
        return 1
    elif n % 4 == 1:
        return 3 + (n // 4) * 4
    elif n % 4 == 2:
        return 0
    else:
        return 4 + (n // 4) * 4
for i in range(int(input())):
    x, m = map(int, input().split())
    if x - 1 == 0:
        ret ^= grundy(m)
    else:
        ret ^= grundy(x + m - 1) ^ grundy(x - 1)
print('koosaga' if ret else 'cubelover')
