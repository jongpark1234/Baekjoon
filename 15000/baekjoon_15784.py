n, a, b = map(int, input().split())
x = [list(map(int, input().split())) for _ in range(n)]
temp = x[a - 1][b - 1]
print('ANGRY' if any(x[a - 1][i] > temp for i in range(n) if i != b - 1) or any(x[i][b - 1] > temp for i in range(n) if i != a - 1) else 'HAPPY')
