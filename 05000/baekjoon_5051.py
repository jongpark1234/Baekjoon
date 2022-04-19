P = 469762049
def FFT(L, inverted = False):
    j = 0
    n = len(L)
    for i in range(1, n):
        bit = n >> 1
        while j >= bit:
            j -= bit
            bit >>= 1
        j += bit
        if i < j:
            L[i], L[j] = L[j], L[i]
    Len = 2
    while Len <= n:
        u = pow(3, P // Len, P)
        if inverted:
            u = pow(u, P - 2, P)
        for i in range(0, n, Len):
            w = 1
            for k in range(i, i + Len // 2):
                value = L[k + Len // 2] * w
                L[k + Len // 2] = (L[k] - value) % P
                L[k] = (L[k] + value) % P
                w = w * u % P
        Len *= 2
    if inverted:
        inverted_n = P - (P - 1) // n
        for i in range(n):
            L[i] = L[i] * inverted_n % P
def Multiply(num):
    n = 2
    while n < len(num):
        n *= 2
    n *= 2
    num += [0 for _ in range(n - len(num))]
    FFT(num)
    value = [i * i % P for i in num]
    FFT(value, inverted = True)
    return value
result = 0
n = int(input())
L = [0 for _ in range(n)]
for i in range(1, n):
    L[i * i % n] += 1
LL = Multiply(L[:])
for i in range(n):
    result += L[i] * LL[i] + L[i] * LL[i + n]
for i in range(n):
    result += L[i] * L[i * 2 % n]
print(result // 2)
