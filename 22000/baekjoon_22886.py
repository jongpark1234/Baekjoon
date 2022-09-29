for tc in range(int(input())):
    x, y, s = input().split()
    x = int(x); y = int(y)
    costs = ((0, x), (y, 0))
    dp = [[float('inf') for _ in range(2)] for _ in range(len(s))]
    for i in range(len(s)):
        for j in range(2):
            if (j == 0 and s[i] == 'J') or (j == 1 and s[i] == 'C'):
                continue
            dp[i][j] = min(dp[i - 1][0] + costs[0][j], dp[i - 1][1] + costs[1][j]) if i else 0
    print(f'Case #{tc + 1}: {min(dp[-1])}')
