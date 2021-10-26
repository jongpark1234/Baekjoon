import sys
glist = []
wordlist = []
groupword = 0
n = int(sys.stdin.readline())
for i in range(n):
    wordlist.append(sys.stdin.readline().rstrip())
for i in range(n):
    error = False
    glist.clear()
    for j in range(len(wordlist[i])):
        if (wordlist[i][j] in glist) and (wordlist[i][j] != glist[len(glist) - 1]):
            error = True
            break
        elif (wordlist[i][j] in glist) and (wordlist[i][j] == glist[len(glist) - 1]):
            pass
        else:
            glist.append(wordlist[i][j])
    if error == False:
        groupword += 1
print(groupword)
