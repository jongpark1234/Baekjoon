for _ in range(int(input())):
    result = [[0 for _ in range(100)] for _ in range(100)]
    s, c = map(int, input().split())
    Input = list(map(int, input().split()))
    for i in range(s):
        result[0][i] = Input[i]
    for i in range(s - 1):
        for j in range(1, s):
            result[i + 1][j] = result[i][j] - result[i][j - 1]
    for i in range(c):
        for j in range(s - 1)[::-1]:
            result[j][s - 1] += result[j + 1][s - 1]
        print(result[0][s - 1], end = ' ')
    print()
