for i in range(int(input())):
    n, m, b = map(int, input().split())
    d = [[0 for _ in range(b + 1)] for _ in range(n + 1)]
    for j in range(n):
        Input = list(map(float, input().split()))
        for k in range(m + 1):
            for l in range(b - k + 1):
                d[j + 1][k + l] = max(d[j + 1][k + l], Input[k] + d[j][l])
    print(f'Data Set {i + 1}:\n{d[n][b]:.2f}\n')
