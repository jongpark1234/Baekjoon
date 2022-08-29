MAX = 10000001
MOD = 1000000007
philist = [0, 1] + [0 for _ in range(MAX - 2)]
dpdict = {}
def phiSum(n):
    if n < MAX and philist[n] != 0:
        return philist[n]
    elif n >= MAX and n in dpdict.keys():
        return dpdict[n]
    ret, i, k = n ** 2 % MOD, 1, 2
    while k ** 2 <= n:
        ret -= phiSum(n // k) - MOD
        ret %= MOD
        k += 1
    while k * i <= n:
        ret -= (n // i - n // (i + 1)) * phiSum(i) - MOD
        ret %= MOD
        i += 1
    if n < MAX:
        philist[n] = ret
    else:
        dpdict[n] = ret
    return ret
def fibonacciSum1(l, r):
    return fibonacciSum2(r) if l == 0 else (fibonacciSum2(r) - fibonacciSum2(l - 1) + MOD) % MOD
def fibonacciSum2(n):
    n += 2
    matrix1, matrix2, matrix3 = [[1, 0], [0, 1]], [[0, 1], [1, 1]], [[0, 0], [0, 0]]
    while n:
        if n & 1:
            for i in range(2):
                for j in range(2):
                    matrix3[i][j] = 0
                    for k in range(2):
                        matrix3[i][j] += matrix1[i][k] * matrix2[k][j] % MOD
                        matrix3[i][j] %= MOD
            temp = [i[:] for i in matrix1]
            matrix1 = [i[:] for i in matrix3]
            matrix3 = [i[:] for i in temp]
        for i in range(2):
            for j in range(2):
                matrix3[i][j] = 0
                for k in range(2):
                    matrix3[i][j] += matrix2[i][k] * matrix2[k][j] % MOD
                    matrix3[i][j] %= MOD
        temp = [i[:] for i in matrix2]
        matrix2 = [i[:] for i in matrix3]
        matrix3 = [i[:] for i in temp]
        n >>= 1
    return (matrix1[0][1] - 1 + MOD) % MOD
n = int(input())
result, i, k = 0, 1, 1
while i ** 2 <= n:
    result += phiSum(n // i) * fibonacciSum1(i, i) % MOD
    result %= MOD
    i += 1
while i * k <= n:
    result += phiSum(k) * fibonacciSum1(n // (k + 1) + 1, n // k) % MOD
    result %= MOD
    k += 1
print(result)
