from sys import stdin
from math import sin, cos, sqrt, pi
def norm(*n):
    return sqrt(sum(pow(i, 2) for i in n))
while (n:=int(stdin.readline())) != 0:
    pos = [0, 0]
    dirlist = []
    queue = [[0, 0]]
    for _ in range(n):
        point, r = stdin.readline().rstrip().split()
        dirlist.append([['N', 'NbE', 'NNE', 'NEbN', 'NE', 'NEbE', 'ENE', 'EbN', 'E', 'EbS', 'ESE', 'SEbE', 'SE', 'SEbS', 'SSE', 'SbE', 'S', 'SbW', 'SSW', 'SWbS', 'SW', 'SWbW', 'WSW', 'WbS', 'W', 'WbN', 'WNW', 'NWbW', 'NW', 'NWbN', 'NNW', 'NbW'].index(point) * pi / 16 * -1, int(r)])
    for i in dirlist:
        pos = [pos[0] - sin(i[0]) * i[1], pos[1] + cos(i[0]) * i[1]]
        queue.append(pos)
    angle = float(stdin.readline()) * pi / 180 * -1
    pos = [cos(angle) * pos[0] - sin(angle) * pos[1], sin(angle) * pos[0] + cos(angle) * pos[1]]
    destination = [norm(i[0] - pos[0], i[1] - pos[1]) for i in queue]
    for i in range(len(queue) - 1):
        if abs(pow(norm(*queue[i]), 2) - pow(norm(*queue[i + 1]), 2) + pos[0] * 2 * (queue[i + 1][0] - queue[i][0]) + pos[1] * 2 * (queue[i + 1][1] - queue[i][1])) < pow(queue[i][0] - queue[i + 1][0], 2) + pow(queue[i][1] - queue[i + 1][1], 2):
            destination.append(abs(pos[0] * queue[i][1] + queue[i][0] * queue[i + 1][1] + queue[i + 1][0] * pos[1] + queue[i][0] * -pos[1] + queue[i][1] * -queue[i + 1][0] + queue[i + 1][1] * -pos[0]) / norm(queue[i][0] - queue[i + 1][0], queue[i][1] - queue[i + 1][1]))
    print(f'{round(min(destination), 2):.2f}')
