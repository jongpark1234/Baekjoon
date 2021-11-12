from sys import stdin
meetlist = sorted([tuple(map(int, stdin.readline().split())) for i in range(int(stdin.readline()))], key = lambda x : (x[1], x[0]))
result = 0; endtime = 0
for i, j in meetlist:
    if i >= endtime:
        result += 1
        endtime = j
print(result)
