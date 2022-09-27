from sys import stdin
SIZE1 = 100
SIZE2 = 240
ACC1 = 300
ACC2 = 500
def solve(R: list, G: list, B: list) -> int:
    h1 = w1 = h2 = w2 = white = green = flag = 0
    ch = [0 for _ in range(500)]
    cw = [0 for _ in range(500)]
    for i in range(h):
        for j in range(w - 1):
            temp = abs(R[i][j] - R[i][j + 1]) + abs(G[i][j] - G[i][j + 1]) + abs(B[i][j] - B[i][j + 1])
            if temp > (SIZE1 >> 1):
                h1 += 1
                ch[i] += 1
            if temp > SIZE1:
                h2 += 1
    for i in range(h - 1):
        for j in range(w):
            temp = abs(R[i][j] - R[i + 1][j]) + abs(G[i][j] - G[i + 1][j]) + abs(B[i][j] - B[i + 1][j])
            if temp > (SIZE1 >> 1):
                w1 += 1
                cw[j] += 1
            if temp > SIZE1:
                w2 += 1
    for i in range(h):
        for j in range(w):
            if ((G[i][j] * 7) > (R[i][j] << 3)) and ((G[i][j] * 7) > (B[i][j] << 3)):
                green += 1
            if (R[i][j] > SIZE2) and (G[i][j] > SIZE2) and (B[i][j] > SIZE2):
                white += 1
    for i in range(h):
        if ch[i] * h * ACC1 > h1 * ACC2:
            flag = 1
            break
    else:
        for i in range(w):
            if cw[i] * w * ACC1 > w1 * ACC2:
                flag = 1
                break
    if h2 + w2 < ACC1 * 10:
        return 4
    if (h1 + w1) * 10 > (h2 + w2) * 21:
        return 2
    if flag:
        return 1
    return 3
h, w = map(int, input().split())
print(solve(*[[list(map(int, stdin.readline().split())) for _ in range(h)] for _ in range(3)]))
