from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 7)
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]
def allie(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
        strength[a] += strength[b]
    else:
        parent[a] = b
        strength[b] += strength[a]
def fight(a, b):
    a = find(a)
    b = find(b)
    if strength[a] > strength[b]:
        strength[a] -= strength[b]
        parent[b] = a
    elif strength[b] > strength[a]:
        strength[b] -= strength[a]
        parent[a] = b
    else:
        parent[a] = 0
        parent[b] = 0
n, m = map(int, stdin.readline().split())
parent = [i for i in range(n + 1)]
strength = [0 for _ in range(n + 1)]
for i in range(1, n + 1):
    strength[i] = int(stdin.readline())
for i in range(m):
    o, p, q = map(int, stdin.readline().split())
    if o == 1:
        allie(p, q)
    else:
        fight(p, q)
countries = set()
result = []
for i in range(1, n + 1):
    country = find(i)
    if country != 0:
        countries.add(find(i))
for i in countries:
    result.append(strength[i])
print(len(countries))
print(*sorted(result))
