from math import sqrt
def F(a, b, c, n = False):
    dn = [0, 0, 1, 1] if n else [0, 1, 1, 0]
    ret = (b[dn[0]] - a[dn[0]]) * (c[dn[1]] - a[dn[1]]) - (b[dn[2]] - a[dn[2]]) * (c[dn[3]] - a[dn[3]])
    return -1 if ret < -1e-10 else ret > 1e-10
def getPair(a, b, n):
    dx = b[0] - a[0]
    dy = b[1] - a[1]
    d1 = sqrt(dx ** 2 + dy ** 2)
    dx /= d1
    dy /= d1
    cost = n ** 2 / d1
    c = [b[0] - dx * cost, b[1] - dy * cost]
    d2 = sqrt(n ** 2 - cost ** 2)
    return [[c[0] + dy * d2, c[1] - dx * d2], [c[0] - dy * d2, c[1] + dx * d2]]
def side(O, From, To, now):
    return F(O, To, now) < 1 if F(O, From, now) < 0 else (F(O, To, now) > 0) + 2
def possible(a, b, d):
    global iscrowded, now
    if (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 > d ** 2:
        pair = getPair(a, b, d)
        if iscrowded:
            now, iscrowded = pair, False
        else:
            if F(a, now[0], now[1]) == 0:
                if F(a, pair[0], pair[1]):
                    return side(a, pair[0], pair[1], now[0]) == 2
                else:
                    return F(a, now[0], pair[0], True) > 0
            s = [side(a, now[0], now[1], pair[i]) for i in range(2)]
            if s[0] < 2:
                if s[1] < 2:
                    return False
                else:
                    if s[1] == 2:
                        now[1] = pair[1]
            else:
                if s[0] == 3:
                    return False
                else:
                    now[0] = pair[0]
                    if s[1] == 2:
                        now[1] = pair[1]
    return True
iscrowded, now, result = False, [], [1]
n, d = map(int, input().split())
p = [tuple(map(int, input().split())) for _ in range(n)]
table = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    iscrowded = True
    for j in range(i + 1, n):
        if not possible(p[i], p[j], d):
            break
        if iscrowded or side(p[i], now[0], now[1], p[j]) == 2:
            table[i][j] += 1
for i in range(n)[::-1]:
    iscrowded = True
    for j in range(i)[::-1]:
        if not possible(p[i], p[j], d):
            break
        if iscrowded or side(p[i], now[0], now[1], p[j]) == 2:
            table[j][i] += 1
for i in range(1, n):
    result += [i + 1]
    for j in range(i):
        if table[j][i] == 2:
            result[i] = min(result[i], result[j] + 1)
print(result[-1])