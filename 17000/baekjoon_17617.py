n = int(input())
r, m = map(int, input().split())
x = sorted(list(map(int, input().split())))
value = result = 0
for i in range(n):
    x.append(x[i] + m)
for i in range(1, n * 2):
    value += x[i] - x[i - 1] - 2 * r
    result = max(result, value)
    value = max(value, 0)
print((result + 1) // 2)
