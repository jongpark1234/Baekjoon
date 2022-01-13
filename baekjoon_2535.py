from sys import stdin
cnt = 0
stu = []
team = {}
for i in range(int(stdin.readline())):
    Input = list(map(int, stdin.readline().split()))
    team[Input[0]] = 0
    stu.append([*Input])
stu.sort(key = lambda x: -x[2])
for i in sorted(stu, key = lambda x: -x[2]):
    team[i[0]] += 1
    if team[i[0]] > 2:
        continue
    print(i[0], i[1])
    cnt += 1
    if cnt == 3:
        break
