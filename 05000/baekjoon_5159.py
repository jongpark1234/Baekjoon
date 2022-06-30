for i in range(int(input())):
    result = [[0 for _ in range(101)] for _ in range(101)]
    n, d, t, c = map(float, input().split())
    n, d, t = int(n), int(d), int(t)
    r = [0] + [list(map(float, input().split())) for _ in range(d)]
    for j in range(t // 2 + 1):
        result[0][j] = c
    for j in range(1, d + 1):
        result[j][0] = c
    for j in range(1, d + 1):
        for k in range(1, t // 2 + 1):
            result[j][k] = result[j - 1][k]
            for l in range(1, j):
                for m in range(n):
                    if result[l][k - 1] * r[j][m] / r[l][m] > result[j][k]:
                        result[j][k] = result[l][k - 1] * r[j][m] / r[l][m]
    print(f'Data Set {i + 1}:\n{round(result[d][t // 2], 2):.2f}\n')
