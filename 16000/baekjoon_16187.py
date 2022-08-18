dp = [0 for _ in range(5001)]
dp[0] = 0; dp[1] = 0; dp[2] = 1
for i in range(3, 5001):
    check = [False for _ in range(16)]
    for j in range(i - 2):
        temp = dp[j] ^ dp[i - 2 - j]
        check[temp] = True
    for j in range(16):
        if not check[j]:
            dp[i] = j
            break
for _ in range(int(input())):
    print('First' if dp[int(input())] else 'Second')
