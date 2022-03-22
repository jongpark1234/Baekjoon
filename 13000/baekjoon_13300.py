from math import ceil
cnt = 0
school = [[0 for _ in range(6)] for _ in range(2)]
a, b = map(int, input().split())
for i in range(a):
    x, y = map(int, input().split())
    school[x][y - 1] += 1
for i in range(2):
    for j in range(6):
        cnt += ceil(school[i][j] / b)
print(cnt)
