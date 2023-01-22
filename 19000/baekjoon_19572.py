d1, d2, d3 = map(int, input().split())
temp = (d1 + d2 - d3) / 2
a, b, c = temp, d1 - temp, d2 - temp
print(-1 if a <= 0 or b <= 0 or c <= 0 else f'1\n{a} {b} {c}')
