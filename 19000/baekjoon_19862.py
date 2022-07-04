from sys import setrecursionlimit
from random import randrange
setrecursionlimit(10 ** 6)
cl = 0
cntDict = {}
depth = [0 for _ in range(250001)]
numlist1 = [0 for _ in range(250001)]
numlist2 = [0 for _ in range(250001)]
pairlist = [[] for _ in range(250001)]
visited = [False for _ in range(250001)]
def dfs(i, previous):
    global cl
    visited[i] = True
    depth[i] = depth[previous] + 1
    for j, k in pairlist[i]:
        if not visited[j]:
            dfs(j, i)
            numlist2[k] = numlist1[j]
            numlist1[i] ^= numlist1[j]
        elif depth[j] < depth[i] - 1:
            numlist2[k] = randrange(98734587345987345987345)
            numlist1[i] ^= numlist2[k]
            numlist1[j] ^= numlist2[k]
            if (depth[i] ^ depth[j] ^ 1) & 1:
                cl ^= numlist2[k]
n, m = map(int, input().split())
for i in range(m):
    u, v = map(int, input().split())
    pairlist[u].append([v, i])
    pairlist[v].append([u, i])
dfs(1, 0)
if cl == 0:
    print(1)
else:
    result = 0
    for i in range(m):
        if numlist2[i] == cl:
            result += 1
    if result:
        print(result)
    else:
        for i in range(m):
            try:
                result += cntDict[cl ^ numlist2[i]]
            except:
                pass
            try:
                cntDict[numlist2[i]] += 1
            except:
                cntDict[numlist2[i]] = 1
        print(result)
