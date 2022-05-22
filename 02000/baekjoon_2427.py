dp = [0 for _ in range(150001)]
n, p, v = map(int, input().split())
dp[0] = 1
result = 150001
for i in range(result):
    if not dp[i]:
        continue
    j = 2
    while i + j * p + v < result:
        dp[i + j * p + v] = max(dp[i + j * p + v], dp[i] * j)
        if dp[i] * j >= n:
            result = i + j * p + v
            break
        j += 1
print(result)
