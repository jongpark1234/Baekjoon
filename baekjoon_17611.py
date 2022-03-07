ans = 0
vertices = []
n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    vertices.append([x + 500000, y + 500000])
x_count = [0] * 1000001
y_count = [0] * 1000001
for i in range(n):
    x, y = vertices[i][0], vertices[i][1]
    x_next, y_next = vertices[(i + 1) % n][0], vertices[(i + 1) % n][1]
    if x == x_next:
        y_max = max(y, y_next)
        y_min = min(y, y_next)
        y_count[y_min] += 1
        y_count[y_max] -= 1
    else:
        x_max = max(x, x_next)
        x_min = min(x, x_next)
        x_count[x_min] += 1
        x_count[x_max] -= 1
for i in range(1, 1000001):
    x_count[i] += x_count[i - 1]
    y_count[i] += y_count[i - 1]
for i in range(1, 1000001):
    ans = max(max(x_count[i], y_count[i]), ans)
print(ans)
