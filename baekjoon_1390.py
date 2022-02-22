# pypy3
n = int(input())
dp = [[[0 for _ in range(305)] for _ in range(305)] for _ in range(305)]
dp[0][0][0] = 1
for x in range(n + 1):
    for y in range(n + 1):
        for z in range(n + 1):
            dp[x][y][z] %= 1000000
            if x == y: dp[x + 2][y + 2][z] += dp[x][y][z]
            if y == z: dp[x][y + 2][z + 2] += dp[x][y][z]
            if y == z + 1: dp[x][y + 2][z + 2] += dp[x][y][z]
            if x == y + 1: dp[x + 2][y + 2][z] += dp[x][y][z]
            if x == y and z == y + 1: dp[x + 1][y + 2][z + 1] += dp[x][y][z]
            if z == y + 1: dp[x][y + 2][z + 2] += dp[x][y][z]
            if y == x + 1: dp[x + 2][y + 2][z] += dp[x][y][z]
            if y == z and x == y + 1: dp[x + 1][y + 2][z + 1] += dp[x][y][z]
            if y == z + 1: dp[x][y + 1][z + 3] += dp[x][y][z]
            if x == y + 1: dp[x + 1][y + 3][z] += dp[x][y][z]
            if x == y and y == z: dp[x + 1][y + 2][z + 1] += dp[x][y][z]
            if z == y + 1: dp[x][y + 3][z + 1] += dp[x][y][z]
            if y == x + 1: dp[x + 3][y + 1][z] += dp[x][y][z]
            if x == z and y + 1 == x: dp[x + 1][y + 2][z + 1] += dp[x][y][z]
            if z + 2 == y: dp[x][y + 1][z + 3] += dp[x][y][z]
            if y + 2 == x: dp[x + 1][y + 3][z] += dp[x][y][z]
            if x + 1 == y and y == z: dp[x + 2][y + 1][z + 1] += dp[x][y][z]
            if x == y: dp[x + 3][y + 1][z] += dp[x][y][z]
            if y == z: dp[x][y + 3][z + 1] += dp[x][y][z]
            if x == y and y == z: dp[x + 1][y + 1][z + 2] += dp[x][y][z]
            if x + 2 == y: dp[x + 3][y + 1][z] += dp[x][y][z]
            if y + 2 == z: dp[x][y + 3][z + 1] += dp[x][y][z]
            if x == y and z + 1 == y: dp[x + 1][y + 1][z + 2] += dp[x][y][z]
            if y == z: dp[x][y + 1][z + 3] += dp[x][y][z]
            if x == y: dp[x + 1][y + 3][z] += dp[x][y][z]
            if x == y and y == z: dp[x + 2][y + 1][z + 1] += dp[x][y][z]
print(dp[n][n][n])