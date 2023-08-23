result = -float('inf')
n, m = map(int, input().split())
numSquare = [list(map(int, input())) for _ in range(n)]
for i in range(n):
    for j in range(m):
        for k in range(min(n - i, m - j)):
            if numSquare[i][j] == numSquare[i + k][j] == numSquare[i][j + k] == numSquare[i + k][j + k]:
                result = max(result, k + 1)
print(result ** 2)
