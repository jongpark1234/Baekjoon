MAX = 2501
graph, nlist, nc = [], [], []
def slicing1(v, ret = 0):
    for i in sorted(v):
        for j in graph[i]:
            if j not in v:
                ret += 1
    return ret
def slicing2(v, ret = 0):
    for i in sorted(v):
        for j in graph[i]:
            if checked[j] != 1:
                ret += 1
    return ret
def dfs(x, y, sub, numlist, Set):
    global nlist
    if len(Set) > b:
        return False
    if slicing2(Set) <= c:
        nlist = Set
        return True
    if sub >= b + c:
        return False
    if len(graph[x]) == y:
        while numlist and checked[numlist[-1]] == -1:
            numlist.pop()
        if not numlist:
            return False
        v = numlist.pop()
        return dfs(v, 0, sub, numlist, Set)
    if checked[graph[x][y]]:
        return dfs(x, y + 1, sub, numlist, Set)
    checked[graph[x][y]] = 1
    if dfs(x, y + 1, sub + 1, numlist + [graph[x][y]], Set + [graph[x][y]]):
        return True
    checked[graph[x][y]] = -1
    if dfs(x, y + 1, sub + 1, numlist, Set):
        return True
    checked[graph[x][y]] = 0
    return False
n, b, c = map(int, input().split())
for i in range(n):
    Input = list(map(int, input().split()))
    if Input[0] > b + c:
        print('NO')
        exit()
    graph.append(sorted(Input[1:]))
for i in range(n):
    for j in graph[i]:
        if i not in graph[j]:
            print('NO')
            exit()
for i in range(n):
    checked, nlist = [0 for _ in range(MAX)], []
    checked[i] = 1
    if not dfs(i, 0, 1, [], [i]):
        print('NO')
        exit()
    nc.append(sorted(nlist))
for i in range(n):
    for j in range(i):
        A, B = [], []
        for k in nc[i]:
            if not k in nc[j]:
                A.append(k)
        if len(A) == len(nc[i]):
            continue
        for k in nc[j]:
            if not k in nc[i]:
                B.append(k)
        if slicing1(A) <= c:
            nc[i] = A
        else:
            nc[j] = B
result = [nc[i] for i in range(n) if nc[i]]
print('YES')
print(len(result))
for i in result:
    print(len(i), *i)
