from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 6)
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]
def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    elif a > b:
        parent[a] = b
    else:
        return
def isParent(a, b):
    return +(find(a) == find(b))
for i in range(int(stdin.readline())):
    n = int(stdin.readline())
    k = int(stdin.readline())
    parent = [i for i in range(n + 1)]
    for _ in range(k):
        a, b = map(int, stdin.readline().split())
        union(a, b)
    print(f'Scenario {i + 1}:')
    for _ in range(int(stdin.readline())):
        u, v = map(int, stdin.readline().split())
        print(isParent(u, v))
    print()
