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
        return 'YES'
    else:
        return 'NO'
n, m = map(int, stdin.readline().split())
parent = [i for i in range(n + 1)]
result = []
for i in range(m):
    n, a, b = map(int, stdin.readline().split())
    if n:
        print(isParent(parent, a, b))
    else: 
        unionParent(parent, a, b)
