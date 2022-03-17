dp = [0 for _ in range(1001)]
dp[0] = 0; dp[1] = 0; dp[2] = 1
n = int(input())
for i in range(3, n + 1):
    check = [False for _ in range(16)]
    for j in range(i - 2):
        temp = dp[j] ^ dp[i - 2 - j]
        check[temp] = True
    for j in range(16):
        if not check[j]:
            dp[i] = j
            break
print(1 if dp[n] else 2)
