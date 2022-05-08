from sys import stdin
def dp(left, right, s, e):
    if left > right:
        return 0
    m = (left + right) // 2
    result = -2000000000000000000
    val = s
    for i in range(s, e + 1):
        x = b[i][0] - a[m][0]
        y = b[i][1] - a[m][1]
        if (x >= 0 or y >= 0) and result <= x * y:
            result = x * y
            val = i
    return max(result, dp(left, m - 1, s, val), dp(m + 1, right, val, e))
a, b = [], []
m, n = map(int, stdin.readline().split())
pd = sorted([list(map(int, stdin.readline().split())) for _ in range(m)])
qe = sorted([list(map(int, stdin.readline().split())) for _ in range(n)])
for i in pd:
    if len(a) != 0:
        if a[-1][1] <= i[1]:
            continue
    a.append(i)
for i in qe:
    while len(b) != 0 and b[-1][1] <= i[1]:
        b.pop()
    b.append(i)
print(max(0, dp(0, len(a) - 1, 0, len(b) - 1)))
