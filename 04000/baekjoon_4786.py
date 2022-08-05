while True:
    n, k, t = map(int, input().split())
    if n == k == t == 0:
        break
    a = [0] + list(map(int, input().split())) + [0 for _ in range(10000 - t)]
    if a[1] > n or a[1] > k:
        print(-1)
        continue
    v, m = a[1], 0
    for i in range(1, t + 1):
        if i + 2 > t:
            m += min(n, k) - v
            k, v = n, 0
            if i == t:
                print(m)
            continue
        if a[i + 1] > min(n, k) + n - v:
            print(-1)
            break
        elif a[i + 1] <= n:
            d = min(n, k) - v
            k += n - v - d
            n += d
            v = a[i + 1]
        else:
            temp = a[i + 1] - n
            d1, d2 = min(n, k) - v - temp, min(max(0, k - n), temp)
            k += n - v - temp - d1
            v = n + d2
            n += d1 + d2
