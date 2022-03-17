from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 7)
def findParent(parent, x):
    if parent[x] != x:
        parent[x] = findParent(parent, parent[x])
    return parent[x]
def unionParent(parent, a, b):
    a = findParent(parent, a)
    b = findParent(parent, b)
    if a < b:
        parent[b] = a
    elif a > b:
        parent[a] = b
    else:
        return
def isParent(parent, a, b):
    a = findParent(parent, a)
    b = findParent(parent, b)
    if a == b:
        return True
    else:
        return False
n = int(stdin.readline())
m = int(stdin.readline())
parent = [i for i in range(n + 1)]
for i in range(n):
    a = list(map(int, stdin.readline().split()))
    for j in range(n):
        if a[j] == 1:
            unionParent(parent, i + 1, j + 1)
plan = list(map(int, stdin.readline().split()))
for i in range(m - 1):
    if not isParent(parent, plan[i], plan[i + 1]):
        print('NO')
        exit(0)
print('YES')
