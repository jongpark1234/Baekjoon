from sys import stdin
students = []
for i in range(int(input())):
    students.append(stdin.readline().rstrip().split())
students.sort(key = lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))
for i in range(len(students)):
    print(students[i][0])
