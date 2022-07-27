def swap1(numlist: list, x: int, y: int) -> None:
    for i in range(1, n + 1):
        numlist[x][i], numlist[y][i] = numlist[y][i], numlist[x][i]
def swap2(numlist: list, x: int, y: int) -> None:
    for i in range(1, n + 1):
        numlist[i][x], numlist[i][y] = numlist[i][y], numlist[i][x]
def add1(numlist: list, x: int, y: int, z: int) -> None:
    for i in range(1, n + 1):
        numlist[y][i] = (numlist[y][i] + numlist[x][i] * z) % MOD
def add2(numlist: list, x: int, y: int, z: int) -> None:
    for i in range(1, n + 1):
        numlist[i][y] = (numlist[i][y] + numlist[i][x] * z) % MOD
MOD = 2
result = [[0 for _ in range(501)] for _ in range(501)]
result[0][0] = 1
n = int(input())
matrix1 = [[0 for _ in range(501)] for _ in range(501)]
matrix2 = [[0 for _ in range(501)] for _ in range(501)]
for i in range(1, n + 1):
    Input = list(map(int, input()))
    for j in range(1, n + 1):
        matrix1[i][j] = Input[j - 1]
for i in range(1, n + 1):
    Input = list(map(int, input()))
    for j in range(1, n + 1):
        matrix2[i][j] = Input[j - 1]
w, num = 1, 0
for i in range(1, n + 1):
    while not matrix1[i][i]:
        j = i
        while not matrix1[i][j] and j <= n:
            j += 1
        if j <= n:
            for l in [matrix2, matrix1]:
                swap2(l, i, j)
            w *= -1
            w += (w >> 31) & MOD
            break
        num += 1
        if num > n:
            break
        for j in range(1, n + 1):
            matrix2[i][j], matrix1[i][j] = 0, matrix2[i][j]
        for j in range(1, i):
            if matrix1[i][j]:
                for l in [matrix2, matrix1]:
                    add1(l, j, i,MOD - matrix1[i][j])
    if num > n:
        break
    inv = pow(matrix1[i][i], matrix1[i][i])
    w = w * matrix1[i][i] % MOD
    for j in range(1, n + 1):
        matrix2[i][j] = matrix2[i][j] * inv % MOD
        matrix1[i][j] = matrix1[i][j] * inv % MOD
    for j in range(1, n + 1):
        if i ^ j and matrix1[j][i]:
            add1(matrix2, i, j, MOD - matrix1[j][i])
            add1(matrix1, i, j, MOD - matrix1[j][i])
for i in range(1, n + 1):
    for j in range(1, n + 1):
        matrix2[i][j] *= -1
        matrix2[i][j] += (matrix2[i][j] >> 31) & MOD
for i in range(1, n):
    j = i + 1
    while not matrix2[j][i] and j <= n:
        j += 1
    if j > n:
        continue
    for k in range(1, n + 1):
        matrix2[i + 1][k], matrix2[j][k] = matrix2[j][k], matrix2[i + 1][k]
    for k in range(1, n + 1):
        matrix2[k][i + 1], matrix2[k][j] = matrix2[k][j], matrix2[k][i + 1]
    inv = pow(matrix2[i + 1][i], matrix2[i + 1][i])
    for j in range(i + 2, n + 1):
        if matrix2[j][i]:
            t = inv * matrix2[j][i] % MOD
            for k in range(i, n + 1):
                matrix2[j][k] -= t * matrix2[i + 1][k] % MOD
                matrix2[j][k] += (matrix2[j][k] >> 31) & MOD
            for k in range(1, n + 1):
                matrix2[k][i + 1] = (matrix2[k][i + 1] + t * matrix2[k][j]) % MOD
for i in range(1, n + 1):
    ac = 1
    for j in range(1, i + 1):
        result[i][j] = result[i - 1][j - 1]
    for j in range(i + 1):
        result[i][j] -= matrix2[i][i] * result[i - 1][j] % MOD
        result[i][j] += (result[i][j] >> 31) & MOD
    for j in range(i - 1, 0, -1):
        ac = ac * matrix2[j + 1][j] % MOD
        temp = (MOD - ac) * matrix2[j][i] % MOD
        for k in range(j + 1):
            result[i][k] = (result[i][k] + temp * result[j - 1][k]) % MOD
print('\n'.join(map(str, [result[n][min(n + 1, num + i)] * w % MOD for i in range(n + 1)])))
