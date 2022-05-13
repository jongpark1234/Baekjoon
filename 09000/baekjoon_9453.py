num = 0
am = an = 12345
a, b, c, d = map(int, input().split())
for m in range(a + 1, 10817):
    for n in range(d + 1, 10817):
        if m * b == n * c and (m * a & 1 == 0 and n * d & 1 == 0) and (m >= c and n >= b) and m + n < am + an:
            am, an = m, n
m, n = am, an
print(m, n)
for i in range(1, m + 1):
    for j in range(i + 1, i + (a // 2) + 1):
        print(i, (j - 1) % m + 1)
if a & 1:
    for i in range(1, m // 2 + 1):
        print(i, m // 2 + i)
for i in range(1, n + 1):
    for j in range(i + 1, i + (d // 2) + 1):
        print(m + i, m + (j - 1) % n + 1)
if d & 1:
    for i in range(1, n // 2 + 1):
        print(m + i, m + n // 2 + i)
for i in range(1, m + 1):
    for j in range(1, b + 1):
        num += 1
        if num > n:
            num = 1
        print(i, m + num)
