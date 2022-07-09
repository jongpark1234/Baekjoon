h1, m1, s1 = map(int, input().split(':'))
h2, m2, s2 = map(int, input().split(':'))
time1, time2 = h1 * 3600 + m1 * 60 + s1, h2 * 3600 + m2 * 60 + s2
if time1 >= time2:
    time2 += 86400
result = time2 - time1
h, result = divmod(result, 3600)
m, result = divmod(result, 60)
print(f'{h:02d}:{m:02d}:{result:02d}')
