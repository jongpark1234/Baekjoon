y1, m1, d1 = map(int, input().split())
y2, m2, d2 = map(int, input().split())
old1, old2, old3 = 0, 1, 0
if (m1 < m2 or (m1 == m2 and d1 <= d2)): old1 += y2 - y1
else: old1 += y2 - y1 - 1
old2 += y2 - y1
old3 += y2 - y1
print(old1, old2, old3, sep='\n')
