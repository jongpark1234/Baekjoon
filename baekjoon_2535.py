from sys import stdin
dic = {}
students = []
for i in range(int(stdin.readline())):
    s = list(map(int, stdin.readline().split()))
    students.append(s)
    dic[s[0]] = 0
students.sort(key = lambda x: -x[2])
for i in range(3):
    dic[students[i][0]] += 1
    if dic[students[i][0]] == 3:
        i += 1
    print(students[i][0], students[i][1])
