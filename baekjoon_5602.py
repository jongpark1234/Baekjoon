n, m = map(int, input().split())
student = []
count = []
for i in range(n):
    student.append(list(map(int, input().split())))
for i in range(m):
    num = 0
    for j in range(n):
        if student[j][i]:
            num += 1
    count.append((num, i + 1))
count.sort(key = lambda x: (-x[0], x[1]))
for i in count:
    print(i[1], end=' ')
