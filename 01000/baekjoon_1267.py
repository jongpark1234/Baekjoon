from math import ceil
n = int(input())
y = m = 0
for i in map(int, input().split()):
    y += ceil((i + 1) / 30) * 10
    m += ceil((i + 1) / 60) * 15
print('Y' if y < m else 'M' if y > m else 'Y M', min(y, m))
