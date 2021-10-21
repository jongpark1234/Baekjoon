import sys
strlist = []
while True:
    s = sys.stdin.readline().rstrip()
    if s == 'END':
        break
    strlist.append(s)
for i in range(len(strlist)):
    temp = list(strlist[i])
    temp.reverse()
    for j in range(len(temp)):
        print(temp[j], end='')
    print()
