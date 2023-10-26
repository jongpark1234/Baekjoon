result = 0
n, k, x, y = map(int, input().split())
for _ in range(n):
    xi, yi = map(int, input().split())
    if pow(xi - x, 2) + pow(yi - y, 2) > pow(k, 2):
        result += 1
print(result)
