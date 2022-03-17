from sys import stdin
x1, y1, x2, y2 = map(int, stdin.readline().split())
x3, y3, x4, y4 = map(int, stdin.readline().split())
def cross(x1, y1, x2, y2, x3, y3):
    temp = (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)
    if temp > 0:
        return 1
    elif temp < 0:
        return -1
    else:
        return 0
result = 0
if cross(x1, y1, x2, y2, x3, y3) * cross(x1, y1, x2, y2, x4, y4) < 0 and cross(x3, y3, x4, y4, x1, y1) * cross(x3, y3, x4, y4, x2, y2) < 0:
    result = 1
print(result)
