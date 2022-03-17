from sys import stdin
num = 1000000007
dp = [1, 1, 0, 0, 2] + [0] * 9999996
for i in range(5, 10000001):
    dp[i] = (num * 10 + ((i + 1) * dp[i - 1]) % num - ((i - 2) * dp[i - 2]) % num - ((i - 5) * dp[i - 3]) % num + ((i - 3) * dp[i - 4]) % num) % num
for _ in range(int(stdin.readline())):
    print(dp[int(stdin.readline())])
