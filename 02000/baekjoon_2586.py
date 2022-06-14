result = 0
a = [[0, 0]]
v = [[] for _ in range(400001)]
p, f = map(int, input().split())
for i in map(int, input().split()):
    a.append([i, 0])
for i in map(int, input().split()):
    a.append([i, 1])
a.sort()
idx = p + f
for i in range(1, p + f + 1):
    if a[i][1] == 0:
        v[idx].append(a[i])
        idx += 1
    else:
        idx -= 1
        v[idx].append(a[i])
for i in range(400001):
    if v[i]:
        temp = 0
        for j in range(1, len(v[i]), 2):
            temp += abs(v[i][j][0] - v[i][j - 1][0])
        if ~len(v[i]) & 1:
            result += temp
            continue
        value = temp
        for j in range(2, len(v[i]), 2)[::-1]:
            temp += abs(v[i][j][0] - v[i][j - 1][0]) - abs(v[i][j - 1][0] - v[i][j - 2][0])
            value = min(value, temp)
        result += value
print(result)
