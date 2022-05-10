tc = 0
while True:
    n = int(input())
    if n == 0:
        break
    tc += 1
    numlist1 = [[0 for _ in range(n)] for _ in range(n)]
    numlist2 = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        Input = list(map(int, input().split()))
        for j in range(n):
            numlist2[i][j] = Input[j]
            if numlist2[i][j] == 0:
                numlist2[i][j] = 1000000000000
            else:
                numlist1[i][j] = numlist2[i][j]
        numlist2[i][i] = 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                numlist2[j][k] = min(numlist2[j][k], numlist2[j][i] + numlist2[i][k])
    Input = list(map(int, input().split()))
    m = Input[0] - 1
    p = Input[1:]
    idx = result = 0
    while True:
        st = p[idx]
        while idx < m and numlist2[st][p[idx]] + numlist1[p[idx]][p[idx + 1]] == numlist2[st][p[idx + 1]]:
            idx += 1
        if idx != m:
            result += 1
            idx += 1
        if idx == m:
            break
    print(f'Case {tc}: {result}')
