temp = [[0 for _ in range(100)] for _ in range(100)]
def get1(r, s, m, n):
    ret = get2(r, s, n)
    if r == 0:
        ret += get2(r, (s + n // 2) % n, n)
    else:
        ret += get2(r - 1, s, n)
    if r == m - 1:
        ret += get2(r, (s + n // 2) % n, n)
    else:
        ret += get2(r + 1, s, n)
    return ret
def get2(r, s, n):
    ret = table[r][s]
    if s > 0:
        ret += table[r][s - 1]
    else:
        ret += table[r][n - 1]
    if s < n - 1:
        ret += table[r][s + 1]
    else:
        ret += table[r][0]
    return ret
tc = 0
while True:
    m, n = map(int, input().split())
    if m == n == 0:
        break
    tc += 1
    table = [[False for _ in range(n)] for _ in range(m)]
    k = int(input())
    inputCnt = 0
    while inputCnt < k * 2:
        Input = list(map(int, input().split()))
        inputCnt += len(Input)
        for i in range(0, len(Input), 2):
            table[Input[i]][Input[i + 1]] = True
    g = int(input())
    for _ in range(1, g + 1):
        for i in range(m):
            for j in range(n):
                count = get1(i, j, m, n)
                if table[i][j]:
                    temp[i][j] = count == 3 or count == 4
                else:
                    temp[i][j] = count == 3
        for i in range(m):
            for j in range(n):
                table[i][j] = temp[i][j]
    result = 0
    a = -1
    for i in range(m):
        for j in range(n):
            if table[i][j]:
                result += 1
                if a == -1:
                    a = i
                    b = j
                c = i
                d = j
    print(f'Case {tc}:', end = ' ')
    if a != -1:
        print(result, a, b, c, d)
    else:
        print(result, -1, -1, -1, -1)
