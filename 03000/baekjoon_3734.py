from math import isqrt
n, k = map(int, input().split())
for x in range(-100000, 100001):
    i = x ** 2 + n * k * 4
    if i < 0:
        continue
    if i == isqrt(i) ** 2:
        j = isqrt(i)
        if (j - x) % (k << 1) == 0:
            p = (j - x) // (k << 1)
            q = n // p
            if p <= q:
                print(f'{p} * {q}')
                break
