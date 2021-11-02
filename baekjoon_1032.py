from sys import stdin
n = int(stdin.readline())
strlist, s = [], ''
for _ in range(n):
    strlist.append(input())
for i in range(len(strlist[0])):
    same = True
    for j in range(len(strlist) - 1):
        if strlist[j][i] != strlist[j + 1][i]:
            same = False
            break
    if same:
        s += strlist[0][i]
    else:
        s += '?'
print(s)
