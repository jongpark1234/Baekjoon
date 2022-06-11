def find(x):
    if x == numlist[x]:
        return x
    numlist[x] = find(numlist[x])
    return numlist[x]
def union(x, y):
    x = find(x)
    y = find(y)
    numlist[y] = x
MAX = 250001
result = 0
numlist = [0 for _ in range(MAX)]
plist = [[0, 0] for _ in range(MAX)]
arrlist = [[] for _ in range(MAX)]
v = []
n = int(input())
for i in range(n):
    q1, q2 = map(int, input().split())
    v.append([q1, i + 1])
    v.append([q2, i + 1])
    numlist[i + 1] = i + 1
    result += q1 + q2
    plist[i + 1] = [q1, q2]
v.sort()
for i in range(1, len(v)):
    if v[i - 1][0] == v[i][0] and find(v[i - 1][1]) != find(v[i][1]):
        union(v[i - 1][1], v[i][1])
for i in range(1, n + 1):
    arrlist[find(i)].append(i)
for i in range(1, n + 1):
    c = []
    if not arrlist[i]:
        continue
    for j in arrlist[i]:
        c.append(plist[j][0])
        c.append(plist[j][1])
    c = sorted(list(set(c)))
    for j in range(len(arrlist[i])):
        result -= c[j]
print(result)
