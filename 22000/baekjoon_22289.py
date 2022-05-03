p = 469762049
def FFT(L, invert = False):
    j = 0
    n=len(L)
    for i in range(1, n):
        bit = n >> 1
        while j >= bit:
            j -= bit
            bit >>= 1
        j += bit
        if i < j:
            L[i], L[j] = L[j], L[i]
    m = 2
    while m <= n:
        u = pow(3, p // m, p)
        if invert:
            u = pow(u, p - 2, p)
        for i in range(0, n, m):
            w = 1
            for k in range(i, i + m // 2):
                tmp = L[k + m // 2] * w
                L[k + m // 2] = (L[k] - tmp) % p
                L[k] += tmp
                L[k] %= p
                w *= u
                w %= p
        m *= 2
    if invert:
        invertedN = p-(p - 1) // n
        for i in range(n):
            L[i] = (L[i] * invertedN) % p
def multiply(a, b):
    n = 2
    while n < max(len(a), len(b)):
        n *= 2
    n *= 2
    a += [0 for _ in range(n - len(a))]
    b += [0 for _ in range(n - len(b))]
    FFT(a)
    FFT(b)
    result = [(i * j) % p for i, j in zip(a, b)]
    FFT(result, invert = True)
    return result
a, b = input().split()
n = len(a) + len(b) - 1
a = list(map(int, list(a)))
b = list(map(int, list(b)))
if a[0] == 0 or b[0] == 0:
    print(0)
    exit()
ab = multiply(a, b)[:n]
result = [0 for _ in range(n + 1)]
for i in range(1, n + 1)[::-1]:
    result[i] += ab[i - 1] % 10
    result[i - 1] += ab[i - 1] // 10
    result[i - 1] += result[i] // 10
    result[i] %= 10
f = True
for i in result:
    if f and i == 0:
        continue
    else:
        f = False
    print(i, end = '')
