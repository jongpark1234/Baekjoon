from random import shuffle
def dfs(u, p):
    print(u, end = ' ')
    for i in numlist[u]:
        if i ^ p:
            dfs(i, u)
n = int(input())
v = [[False for _ in range(401)] for _ in range(401)]
numarr = [i for i in range(1, n + 1)]
numlist = [[] for _ in range(401)]
for _ in range(25000):
    shuffle(numarr)
    print('?', *numarr)
    x = int(input())
    if x == n - 1:
        print('!', *numarr)
        exit(0)
    if x:
        continue
    for i in range(n - 1):
        v[numarr[i]][numarr[i + 1]] = v[numarr[i + 1]][numarr[i]] = True
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if (i ^ j) and not v[i][j]:
            numlist[i].append(j)
for i in range(1, n + 1):
    if len(numlist[i]) == 1:
        print('!', end=' ')
        dfs(i, 0)
        exit(0)
