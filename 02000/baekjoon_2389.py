from math import hypot
pos, pointlist, k = [0, 0], [], 0.1
for _ in range(n := int(input())):
    x, y = map(float, input().split())
    pos[0] += x
    pos[1] += y
    pointlist.append([x, y])
for i in range(2):
    pos[i] /= n
for _ in range(10000):
    result = temp = 0
    for i in range(n):
        dis = hypot(pos[0] - pointlist[i][0], pos[1] - pointlist[i][1])
        if dis > result:
            temp, result = i, dis
    for i in range(2):
        pos[i] += (pointlist[temp][i] - pos[i]) * k
    k *= 0.999
print(*pos, result)
