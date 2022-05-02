dp = [[0, 0] for _ in range(101010)]
host = [0]
protocol = [0]
def sample(n, credibility, host, protocol):
    for i in range(n):
        dp[i][0] = credibility[i]
    for i in range(1, n)[::-1]:
        if protocol[i] == 0:
            dp[host[i]][0] += dp[i][1]
            dp[host[i]][1] += max(dp[i][0], dp[i][1])
        elif protocol[i] == 1:
            dp[host[i]][0] = max(dp[host[i]][0] + max(dp[i][0], dp[i][1]), dp[host[i]][1] + dp[i][0])
            dp[host[i]][1] += dp[i][1]
        else:
            dp[host[i]][0] = max(dp[host[i]][0] + dp[i][1], dp[host[i]][1] + dp[i][0])
            dp[host[i]][1] += dp[i][1]
    return max(dp[0][0], dp[0][1])
n = int(input())
credibility = list(map(int, input().split()))
information = list(map(int, input().split()))
for i in range(len(information)):
    if i & 1:
        protocol.append(information[i])
    else:
        host.append(information[i])
print(sample(n, credibility, host, protocol))
