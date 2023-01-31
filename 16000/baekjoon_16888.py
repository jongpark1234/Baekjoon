SIZE = 1000000
dp = [False, True, False] + [False for _ in range(SIZE - 2)]
for i in range(1, int(SIZE ** 0.5) + 1):
    dp[i * i] = True
for i in range(2, SIZE + 1):
    if not dp[i]:
        for j in range(1, int((SIZE - i) ** 0.5) + 1):
            dp[i + j * j] = True
for i in map(int, [*open(0)][1:]):
    print('koosaga' if dp[i] else 'cubelover')
