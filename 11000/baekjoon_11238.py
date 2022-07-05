from math import gcd
MOD = 1000000007
for _ in range(int(input())):
    result = [1, 0]
    matrix = [[1, 1], [1, 0]]
    GCD = gcd(*map(int, input().split()))
    while GCD:
        if GCD & 1:
            result[0], result[1] = (matrix[0][0] * result[0] + matrix[0][1] * result[1]) % MOD, (matrix[1][0] * result[0] + matrix[1][1] * result[1]) % MOD
        matrix[0][0], matrix[0][1], matrix[1][0], matrix[1][1] = (matrix[0][0] * matrix[0][0] + matrix[0][1] * matrix[1][0]) % MOD, (matrix[0][0] * matrix[0][1] + matrix[0][1] * matrix[1][1]) % MOD, (matrix[1][0] * matrix[0][0] + matrix[1][1] * matrix[1][0]) % MOD, (matrix[1][0] * matrix[0][1] + matrix[1][1] * matrix[1][1]) % MOD
        GCD >>= 1
    print(result[1])
