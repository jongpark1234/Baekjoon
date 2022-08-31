n = int(input())
stair = [int(input()) for _ in range(n)]
if n < 3:
    print(sum(stair))
else:
    dp = [stair[0], stair[0] + stair[1], max(stair[0], stair[1]) + stair[2]]
    for i in range(3, n):
        dp.append(max(dp[i - 2], dp[i - 3] + stair[i - 1]) + stair[i])
    print(dp[-1])
