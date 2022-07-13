def solve(r, c):
    global n
    if result[r][c] == '.' and n > 0:
        result[r][c] = '#'
        n -= 1
n, r, c = map(int, input().split())
t = min(n + 1 >> 1, min(r, c))
result = [['.' for _ in range(c)] for _ in range(r)]
for i in range(t):
    solve(0, i)
    solve(i, 0)
for i in range(r):
    for j in range(c):
        solve(i, j)
print(t)
for i in result:
    print(''.join(i))
