n, m ,k = map(int, input().split())
students = -1
while n + m >= k and n >= 0 and m >= 0:
    n -= 2
    m -= 1
    students += 1
print(students)
