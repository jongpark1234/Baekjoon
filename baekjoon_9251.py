s1 = input()
s2 = input()
dp = [0] * 1000
for i in range(len(s1)):
    maxdp = 0
    for j in range(len(s2)):
        if maxdp < dp[j]:
            maxdp = dp[j]
        elif s1[i] == s2[j]:
            dp[j] = maxdp + 1
print(max(dp))
