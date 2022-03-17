index = 0
maxnum = 0
result = ''
strlist = []
for i in range(5):
    s = input()
    strlist.append(s)
    maxnum = max(maxnum, len(s))
for i in range(maxnum):
    for j in range(5):
        if len(strlist[j]) > i:
            result += strlist[j][i]
print(result)
