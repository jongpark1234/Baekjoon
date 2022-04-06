def point():
    return p[0] == q[2] or p[1] == q[3] or p[3] == q[1] or p[2] == q[0]
def line():
    return posp[0] == posq[2] or posp[1] == posq[3] or posp[2] == posq[0] or posp[3] == posq[1]
def null():
    return posp[0] > posq[2] or posp[1] > posq[3] or posp[2] < posq[0] or posp[3] < posq[1]
x1, y1, x2, y2 = map(int, input().split())
p = [(x1, y2), (x2, y2), (x2, y1), (x1, y1)]
posp = [x1, y1, x2, y2]
x1, y1, x2, y2 = map(int, input().split())
q = [(x1, y2), (x2, y2), (x2, y1), (x1, y1)]
posq = [x1, y1, x2, y2]
if null():
    print('NULL')
elif point():
    print('POINT')
elif line():
    print('LINE')
else:
    print('FACE')
