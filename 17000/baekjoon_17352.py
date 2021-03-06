from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 7)
n = int(stdin.readline())
parent = [i for i in range(n + 1)]
result = []
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
for i in range(n - 2):
    a, b = map(int, stdin.readline().split())
    unionParent(parent, a, b)
for i in range(1, n + 1):
    result.append(findParent(parent, i))
for i in range(1, len(result)):
    if result[i - 1] != result[i]:
        if result.count(result[i - 1]) > result.count(result[i]):
            print(result[i - 1], result[i])
            break
        else:
            print(result[i], result[i - 1])
            break
