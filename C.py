def Find(n, m, a, b):
    try:
        if board[n][m] in MBTI[0]:
            n += a
            m += b
            if n < 0 or m < 0:
                return 0
            if board[n][m] in MBTI[1]:
                n += a
                m += b
                if n < 0 or m < 0:
                    return 0
                if board[n][m] in MBTI[2]:
                    n += a
                    m += b
                    if n < 0 or m < 0:
                        return 0
                    if board[n][m] in MBTI[3]:
                        return 1
        return 0
    except IndexError:
        return 0
cnt = 0
n, m = map(int, input().split())
board = [input() for _ in range(n)]
MBTI = ['EI', 'NS', 'TF', 'PJ']
for i in range(n):
    for j in range(m):
        cnt += Find(i, j, 0, 1) # 동쪽
        cnt += Find(i, j, -1, 1) # 북동쪽
        cnt += Find(i, j, -1, 0) # 북쪽
        cnt += Find(i, j, -1, -1) # 북서쪽
        cnt += Find(i, j, 0, -1) # 서쪽
        cnt += Find(i, j, 1, -1) # 남서쪽
        cnt += Find(i, j, 1, 0) # 남쪽
        cnt += Find(i, j, 1, 1) # 남동쪽
print(cnt)
