from math import acos
def calc(n1, n2):
    if n1[0] == n2[0]:
        return 0
    a = (n2[1] - n1[1]) / (n2[0] - n1[0])
    b = n1[1] - a * n1[0]
    return (((a ** 2 / 3) * n2[0] * n2[0] * n2[0] + a * b * n2[0] * n2[0] + b ** 2 * n2[0]) - ((a ** 2 / 3) * n1[0] * n1[0] * n1[0] + a * b * n1[0] * n1[0] + b ** 2 * n1[0])) * acos(-1)
x1, y1, x2, y2, x3, y3 = map(int, input().split())
v = sorted([[x1, y1], [x2, y2], [x3, y3]], key=lambda x: x[0])
result1 = calc(v[0], v[2]) - calc(v[0], v[1]) - calc(v[1], v[2])
for i in range(3):
    v[i][0], v[i][1] = v[i][1], v[i][0]
v.sort(key=lambda x: x[0])
result2 = calc(v[0], v[2]) - calc(v[0], v[1]) - calc(v[1], v[2])
print(abs(result1), abs(result2))
