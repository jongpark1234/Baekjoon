a = [0]
k = [0]
w, h, n = map(int, input().split())
x = [w]
r = h / w
a.append(0.5)
for i in range(1, n + 1):
    k.append((1 - r * r) / a[i] / 4)
    a.append(0.5 - a[i] * k[i] * k[i])
result = (a[n + 1] - 0.5 + (r + 1) ** 2 / 4) * w ** 2
for i in range(n + 1)[::-1]:
    x.insert(0, x[0] * k[i])
print(f'{result:.6f}')
i = 1
while i <= n and i < 11:
    print(f'{x[i]:.6f}')
    i += 1
