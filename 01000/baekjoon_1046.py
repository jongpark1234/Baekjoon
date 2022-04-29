count = x = y = result = 0
p, slopeList = [], []
def search(x, y, pos, angle):
    pos = pos[:]
    if x == -1 or x == w or y == -1 or y == h or box[y][x] == '#':
        p.append(pos)
        return
    x1 = x + 1 if angle[0] > 0 else x - 1
    x2 = x + 1 if angle[0] > 0 else x
    y1 = y + 1 if angle[0] * angle[1] > 0 else y - 1
    y2 = y + 1 if angle[0] * angle[1] > 0 else y
    y_nx = pos[1] + (angle[1]) * (x2 - pos[0])
    x_ny = pos[0] + ((y2 - pos[1]) / (angle[1]))
    if y + 1e-7 < y_nx and y_nx < y + 1 - 1e-7 and (x_ny < x - 1e-7 or x_ny > x + 1 + 1e-7):
        pos = [x2, y_nx]
        search(x1, y, pos, angle)
    elif x + 1e-7 < x_ny and x_ny < x + 1 - 1e-7 and (y - 1e-7 > y_nx or y_nx > y + 1 + 1e-7):
        pos = [x_ny, y2]
        search(x, y1, pos, angle)
    else:
        pos = [x2, y2]
        if angle[1] > 0 and (x1 == -1 or x1 == w or box[y][x1] == '#'):
            p.append(pos)
        if angle[1] < 0 and (y1 == -1 or y1 == h or box[y1][x] == '#'):
            p.append(pos)
        search(x1, y1, pos, angle)
        if angle[1] > 0 and (y1 == -1 or y1 == h or box[y1][x] == '#'):
            p.append(pos)
        if angle[1] < 0 and (x1 == -1 or x1 == w or box[y][x1] == '#'):
            p.append(pos)
h, w = map(int, input().split())
box = [input() for _ in range(h)]
for i in range(h):
    for j in range(w):
        if box[i][j] == '*':
            x = j
            y = i
            Light = [j + 0.5, i + 0.5]
        elif box[i][j] == '#':
            count += 1
for i in range(2):
    for j in range(2):
        slope = [0, 0]
        j = w * j
        i = h * i
        slope = [1 if j - Light[0] > 0 else -1, (i - Light[1]) / (j - Light[0])]
        slopeList.append(slope)
for i in range(h + 1):
    for j in range(w + 1):
        slope = [1 if j - Light[0] > 0 else -1, (i - Light[1]) / (j - Light[0])]
        if slope not in slopeList:
            slopeList.append(slope)
for i in sorted(slopeList):
    search(x, y, Light, i)
for i in range(len(p)):
    j = (i + 1) % len(p)
    result += abs((Light[0] * p[i][1] + p[i][0] * p[j][1] + p[j][0] * Light[1]) - (p[i][0] * Light[1] + p[j][0] * p[i][1] + Light[0] * p[j][1])) / 2
print(f'{w * h - result - count:.13f}')
