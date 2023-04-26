fibonacci = [0, 1]
for i in range(2, 81):
    fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])
dp = [0, 4, 6, 10]
for i in range(4, 81):
    dp.append(fibonacci[i] * 3 + fibonacci[i - 1] * 2 + fibonacci[i - 2] * 2 + fibonacci[i - 3])
print(dp[int(input())])
