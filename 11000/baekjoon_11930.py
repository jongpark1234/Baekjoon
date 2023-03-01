from sys import stdin
pos, pointlist, k = [0, 0, 0], [], 0.1
n = int(input())
for _ in range(n):
    x, y, z = map(float, stdin.readline().split())
    pos[0] += x
    pos[1] += y
    pos[2] += z
    pointlist.append([x, y, z])
for i in range(3):
    pos[i] /= n
for _ in range(30000):
    result = temp = 0
    for i in range(n):
        a, b, c = pointlist[i]
        dis = pow(pos[0] - a, 2) + pow(pos[1] - b, 2) + pow(pos[2] - c, 2)
        if dis > result:
            temp, result = i, dis
    for i in range(3):
        pos[i] += (pointlist[temp][i] - pos[i]) * k
    k *= 0.999
print('%0.2f' % result ** 0.5)
