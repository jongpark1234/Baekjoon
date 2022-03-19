a = 0
n_x = 0
n_y = 0
i_x = 0
i_y = 0
n = int(input())
x = [0 for _ in range(n)]
y = [0 for _ in range(n)]
for i in range(n):
    x[i], y[i] = map(int, input().split())
for i in range(1, n - 1):
    a += ((x[i] - x[0]) * (y[i + 1] - y[0]) - (x[i + 1] - x[0]) * (y[i] - y[0])) / 2
for i in range(n):
    n_x += ((x[(i + 1) % n] ** 3 + x[(i + 1) % n] ** 2 * x[i] + x[(i + 1) % n] * x[i] ** 2 + x[i] ** 3) * (y[(i + 1) % n] - y[i])) / 12
    n_y += ((y[(i + 1) % n] ** 3 + y[(i + 1) % n] ** 2 * y[i] + y[(i + 1) % n] * y[i] ** 2 + y[i] ** 3) * (x[(i + 1) % n] - x[i])) / -12
    i_x += ((x[(i + 1) % n] ** 2 + x[(i + 1) % n] * x[i] + x[i] ** 2) * (y[(i + 1) % n] - y[i])) / 6
    i_y += ((y[(i + 1) % n] ** 2 + y[(i + 1) % n] * y[i] + y[i] ** 2) * (x[(i + 1) % n] - x[i])) / -6
print((a * n_x + a * n_y - i_x ** 2 - i_y ** 2) * 2 / a ** 2)
