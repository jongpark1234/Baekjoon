for _ in range(int(input())):
    n, result = 1, 0
    l, v1, v2, t, s = map(int, input().split())
    lf = (v2 - v1 + t - 1) // t
    mnv = v2 - lf * t
    while n > 0 and lf > n:
        result += 1
        maxv = l // (s * result)
        temp = min(lf, (maxv - mnv + t) // t)
        n -= lf - temp
        n += n
        lf = temp
    print(['impossible', result][n > 0])
