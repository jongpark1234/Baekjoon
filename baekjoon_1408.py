h1, m1, s1 = map(int, input().split(':'))
h2, m2, s2 = map(int, input().split(':'))
dis = h2 * 3600 + m2 * 60 + s2 - (h1 * 3600 + m1 * 60 + s1)
if dis < 0:
    dis += 86400
h = dis // 3600
m = dis % 3600 // 60
s = dis % 60
print('{:02d}:{:02d}:{:02d}'.format(h, m, s))
