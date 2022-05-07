from sys import stdin
MAX = 50001
dp = [1] + [0 for _ in range(MAX - 1)]
a = [0 for _ in range(MAX)]
b = [0 for _ in range(MAX)]
def layout(num, w, n):
    idx = 0
    for i in range(1, n + 1):
        dp[i] = 0
        a[i] = (x[i] + 1) + a[i - 1]
        b[i] = (x[i] + num) + b[i - 1]
    for i in range(1, n + 1):
        while a[i] - a[idx] > w + 1:
            idx += 1
        while idx < i - 1 and dp[idx] == 0:
            idx += 1
        if idx < i - 1 and dp[idx] and (b[i] - b[idx] >= w + num):
            dp[i] = 1
    if dp[n]:
        return True
    for i in range(n):
        if a[n] - a[i] <= w + 1 and dp[i]:
            return True
    return False
while True:
    w, n = map(int, stdin.readline().split())
    if w == n == 0:
        break
    x = [0] + list(map(int, stdin.readline().split()))
    left, right = 1, MAX
    while left != right:
        mid = (left + right) // 2
        if layout(mid, w, n):
            right = mid
        else:
            left = mid + 1
    print(left)
