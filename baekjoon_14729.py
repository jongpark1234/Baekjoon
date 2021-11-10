from sys import stdin
students = sorted([float(stdin.readline()) for i in range(int(stdin.readline()))])
for i in range(7):
    print('{:.3f}'.format(students[i]))
