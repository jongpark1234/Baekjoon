dp = [1, 2, 4]
for i in range(7):
    dp.append(sum(dp[-3:]))
for _ in range(int(input())):
    print(dp[int(input()) - 1])
