dist = [[0 for _ in range(101)] for _ in range(101)]
numlist1, numlist2, s1, s2, f1, f2, now, nx, ny, result = [], [], [], [], [], [], [], [], [], [0]
def solve(x):
    if s1[x]:
        return False
    s1[x] = True
    for y in range(len(numlist2)):
        if dist[numlist1[x]][numlist2[y]] > d ** 2:
            if f2[y] == -1 or solve(f2[y]):
                f1[x] = y
                f2[y] = x
                return True
    return False
def marking(y):
    if s2[y]:
        return
    s2[y] = True
    now.append(numlist2[y])
    x = f2[y]
    if x == -1:
        return
    s1[x] = True
    for x2 in range(len(numlist1)):
        if dist[numlist1[x2]][numlist2[y]] > d ** 2:
            marking(f1[x2])
n, d = map(int, input().split())
for i in range(n):
    x, y = map(int, input().split())
    nx += [x]
    ny += [y]
for i in range(n):
    for j in range(n):
        dist[i][j] = (nx[i] - nx[j]) * (nx[i] - nx[j]) + (ny[i] - ny[j]) * (ny[i] - ny[j])
for i in range(n):
    for j in range(i + 1, n):
        if dist[i][j] <= d ** 2:
            numlist1, numlist2 = [], []
            for k in range(n):
                if k not in [i, j] and dist[i][k] <= dist[i][j] and dist[j][k] <= dist[i][j]:
                    if (nx[j] - nx[i]) * (ny[k] - ny[i]) - (ny[j] - ny[i]) * (nx[k] - nx[i]) <= 0:
                        numlist1.append(k)
                    else:
                        numlist2.append(k)
            f1 = [-1 for _ in range(len(numlist1))]
            f2 = [-1 for _ in range(len(numlist2))]
            for k in range(len(numlist1)):
                s1 = [0 for _ in range(len(numlist1))]
                solve(k)
            now = [i, j]
            s1 = [0 for _ in range(len(numlist1))]
            s2 = [0 for _ in range(len(numlist2))]
            for x in range(len(numlist1)):
                if not s1[x] and f1[x] != -1:
                    for y in range(len(numlist2)):
                        if f2[y] == -1 and dist[numlist1[x]][numlist2[y]] > d ** 2:
                            marking(f1[x])
            for x in range(len(numlist1)):
                if not s1[x]:
                    now.append(numlist1[x])
                    if f1[x] != -1:
                        s2[f1[x]] = True
            for y in range(len(numlist2)):
                if not s2[y]:
                    now.append(numlist2[y])
            if len(now) > len(result):
                result = now
print(len(result))
print(*map(lambda x: int(x) + 1, result))
