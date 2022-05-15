def power(x, y):
    r = 1
    x %= MOD
    while y:
        if y & 1:
            r = (r * x) % MOD
        y >>= 1
        x = x ** 2 % MOD
    return r
for _ in range(int(input())):
    a = list('0' + input())
    n = len(a)
    a.append('0')
    a += ['0' for _ in range(n * 2)]
    for i in range(n + 1, n * 2):
        a[i] = a[n * 2 - i]
    MOD = n * 2
    k = power(2, n + 10)
    result = 0
    for i in range(1, n + 1):
        temp = int(a[(i + k) % MOD]) ^ int(a[(i - k + MOD) % MOD])
        if temp:
            result = 1
            break
    print('LIVES' if result else 'DIES')
