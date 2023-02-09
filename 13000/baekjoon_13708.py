from sys import stdin
pos, pointlist, k = [0, 0], [], 0.1
n = int(input())
for _ in range(n):
    x, y = map(float, stdin.readline().split())
    pos[0] += x
    pos[1] += y
    pointlist.append([x, y])
for i in range(2):
    pos[i] /= n
for _ in range(30000):
    result = temp = 0
    for i in range(n):
        dis = pow(pos[0] - pointlist[i][0], 2) + pow(pos[1] - pointlist[i][1], 2)
        if dis > result:
            temp, result = i, dis
    for i in range(2):
        pos[i] += (pointlist[temp][i] - pos[i]) * k
    k *= 0.999
print('%0.2f' % (result ** 0.5 * 2))
