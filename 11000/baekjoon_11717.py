def hashing(H, c):
    return (H * 131 + ord(c)) % 1000000007
def Search(h1, w1, h2, w2):
    if h1 > h2 or w1 > w2:
        return False
    b = 0
    for i in range(h1, h2 + 1):
        for j in range(w1, w2 + 1):
            b = hashing(b, board[i][j])
        b = hashing(b, '0')
    try:
        return dp[b]
    except KeyError:
        pass
    getGrundy = [False for _ in range(100)]
    for i in range(h1, h2 + 1):
        for j in range(w1, w2 + 1):
            if board[i][j] == 'X':
                continue
            grundy = 0
            grundy ^= Search(h1, w1, i - 1, j - 1)
            grundy ^= Search(h1, j + 1, i - 1, w2)
            grundy ^= Search(i + 1, w1, h2, j - 1)
            grundy ^= Search(i + 1, j + 1, h2, w2)
            getGrundy[grundy] = True
    for i in range(100):
        if not getGrundy[i]:
            dp[b] = i
            return dp[b]
dp = {}
board = [['0' for _ in range(21)] for _ in range(21)]
h, w = map(int, input().split())
for i in range(1, h + 1):
    Input = input()
    for j in range(1, w + 1):
        board[i][j] = Input[j - 1]
print('First' if Search(1, 1, h, w) else 'Second')
