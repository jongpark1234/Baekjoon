import sys
n = int(sys.stdin.readline())
mlist = []
for i in range(n):
    age, name = map(str, sys.stdin.readline().rstrip().split())
    age = int(age)
    mlist.append((age, name))
mlist.sort(key=lambda x: (x[0]))
for i in mlist:
    print(i[0], i[1])
