y, m, d = map(int, input().split('-'))
for i in range(int(input())):
    d += 1
    if d > 30:
        m += 1
        d = 1
    if m > 12:
        y += 1
        m = 1
print(f'{y}-{m:02d}-{d:02d}')
