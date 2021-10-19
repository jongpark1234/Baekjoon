from sys import *
strlist = []
while True:
    strlist.append(stdin.readline().rstrip())
    if strlist[len(strlist) - 1] == '0':
        break
who = stdin.readline().rstrip()
where = stdin.readline().rstrip()
what = stdin.readline().rstrip()
for i in range(len(strlist) - 1):
    s = strlist[i]
    s = s.replace('WHO', who)
    s = s.replace('WHERE', where)
    s = s.replace('WHAT', what)
    print(s)
