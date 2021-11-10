from sys import stdin
strlist = []
strdict = {}
numlist = []
result = 0
index = 9
n = int(stdin.readline())
for _ in range(n):
    strlist.append(stdin.readline().rstrip())
for i in range(n):
    for j in range(len(strlist[i])):
        if strlist[i][j] in strdict:
            strdict[strlist[i][j]] += 10 ** (len(strlist[i]) - j - 1)
        else:
            strdict[strlist[i][j]] = 10 ** (len(strlist[i]) - j - 1)
for i in strdict.values():
    numlist.append(i)
for i in sorted(numlist, reverse = True):
    result += index * i; index -= 1
print(result)
