def multiply(x, y, m):
    return x * y % m
def power(x, y, p):
    r = 1
    x %= p
    while y:
        if y & 1:
            r = (r * x) % p
        y >>= 1
        x = x ** 2 % p
    return r
def tonelli_shanks(n, p):
    if n == 0:
        return 0
    if power(n, (p - 1) // 2, p) != 1:
        return -1
    q = p - 1
    s = 0
    while not (q & 1):
        s += 1
        q >>= 1
    for i in range(2, p):
        if power(i, (p - 1) // 2, p) != 1:
            z = i
            break
    m = s % p
    c = power(z, q, p)
    t = power(n, q, p)
    r = power(n, (q + 1) // 2, p)
    while True:
        if t == 0:
            return 0
        if t == 1:
            return r
        i
        temp = multiply(t, t, p)
        for j in range(1, m):
            if temp == 1:
                i = j
                break
            temp = multiply(temp, temp, p)
        b = power(c, power(2, m - i - 1, p - 1), p)
        m = i % p
        c = multiply(b, b, p)
        t = multiply(t, c, p)
        r = multiply(r, b, p)
for i in range(int(input())):
    p, a0, a1 = map(int, input().split())
    if p == 2:
        if a0 == a1 == 0:
            print('0 0')
        elif a0 == 0 and a1 == 1:
            print('0 1')
        elif a0 == 1 and a1 == 0:
            print('1 1')
        else:
            print(-1)
        continue
    k = ((a1 + p) // 2) if a1 & 1 else a1 // 2
    n = (k ** 2 - a0 + p) % p
    ans = tonelli_shanks(n, p)
    if ans == -1:
        print(-1)
        continue
    result_1 = (k + ans) % p
    result_2 = (a1 - result_1 + p) % p
    print(*sorted([result_1, result_2]))
