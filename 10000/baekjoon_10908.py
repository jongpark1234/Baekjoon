def power(x, y):
    r = 1
    while y:
        if y & 1:
            r = r * x % 1000000007
        x = x ** 2 % 1000000007
        y >>= 1
    return r
def EBS(s, t):
    x = ([0, 0], [0, 0])
    for i in range(2):
        for j in range(2):
            r = 0
            for k in range(2):
                r += s[i][k] * t[k][j] % 1000000014000000049
            x[i][j] = r % 1000000014000000049
    return x
def Phibonacci(n):
    if n <= 1:
        return abs(n)
    n -= 2
    x = ([1, 1], [1, 0])
    r = ([1, 1], [1, 0])
    while n:
        if n & 1:
            r = EBS(r, x)
        x = EBS(x, x)
        n >>= 1
    return r[0][0]
n, k = map(int, input().split())
f_nk = Phibonacci(n * k)
f_k = Phibonacci(k)
if f_k % 1000000007 == 0:
    f_k //= 1000000007
    f_nk //= 1000000007
A = f_nk * power(f_k, 1000000005) % 1000000007
B = (Phibonacci(n * k - 1) - Phibonacci(k - 1) * A) % 1000000007
print(A, B)
