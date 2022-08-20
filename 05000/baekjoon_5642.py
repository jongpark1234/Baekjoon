from sys import stdin
def init():
    global grundy
    for i in range(1, len(grundy)):
        grundy[i][0] = i
    for i in range(1, len(grundy[0])):
        grundy[0][i] = i
    Max = max(len(grundy), len(grundy[0]))
    for i in range(1, len(grundy)):
        for j in range(1, len(grundy[i])):
            cnt = 0
            visited = [False for _ in range(Max + 1)]
            k = 1
            while i - k >= 0:
                visited[grundy[i - k][j]] = True
                k += 1
            k = 1
            while j - k >= 0:
                visited[grundy[i][j - k]] = True
                k += 1
            k = 1
            while i - k >= 0 and j - k >= 0:
                visited[grundy[i - k][j - k]] = True
                k += 1
            while cnt < len(visited) and visited[cnt]:
                cnt += 1
            grundy[i][j] = cnt
            Max = max(Max, grundy[i][j])
def calc(row, col):
    global cycle
    global grundy
    if row > col:
        row, col = col, row
    if col < len(grundy[row]):
        return grundy[row][col]
    stage = (col - (len(grundy[row]) - 1) + cycle[row] - 1) // cycle[row]
    col2 = col - stage * cycle[row]
    return grundy[row][col2] + cycle[row] * stage
grundy = [[0 for _ in range(3800)] for _ in range(25)]
cycle = [1, 3, 3, 6, 12, 24, 12, 24, 24, 24, 24, 48, 48, 96, 96, 96, 192, 192, 384, 384, 384, 768, 768, 768, 768]
init()
for _ in range(int(stdin.readline())):
    ret = 0
    Input1 = []
    while len(Input1) < 3:
        Input1 += list(map(int, input().split()))
    Input2 = []
    while len(Input2) < Input1[2] * 2:
        Input2 += list(map(int, input().split()))
    for i in range(0, len(Input2), 2):
        ret ^= calc(Input2[i] - 1, Input2[i + 1] - 1)
    print('YES' if ret else 'NO')
