strlist = sorted([input() for i in range(int(input()))], key = lambda x : len(x))
count = len(strlist)
for i in range(len(strlist) - 1):
    for j in range(i + 1, len(strlist)):
        if strlist[i] == strlist[j][:len(strlist[i])]:
            count -= 1
            break
print(count)
