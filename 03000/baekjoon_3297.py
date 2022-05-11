result = 0
x, y = [0], [0]
dp = [[0 for _ in range(101)] for _ in range(101)]
def ccw(p, q, r):
    return True if q == r else (x[q] - x[p]) * (y[r] - y[q]) - (y[q] - y[p]) * (x[r] - x[q]) > 0
def search(a, b):
    result = -1000000000
    if b == 0:
        return 1
    if dp[a][b]:
        return dp[a][b]
    for i in range(n + 1):
        if b == i:
            continue
        if ccw(a, b, i) and ccw(b, i, 0):
            result = max(result, search(b, i))
    result += 1
    dp[a][b] = result
    return result
n = int(input())
for i in range(n):
    Input = list(map(int, input().split()))
    x.append(Input[0])
    y.append(Input[1])
for i in range(1, n + 1):
    result = max(result, search(0, i))
print(result)
