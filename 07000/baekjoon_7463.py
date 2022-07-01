from math import pi
def calc(v):
    return v[0] * x[4] + v[1] * y[4] + v[2]
def line(v, a, b):
    v[0] = y[a] - y[b]
    v[1] = x[b] - x[a]
    v[2] = x[a] * -v[0] + y[a] * -v[1]
def solve():
    line(a1, 1, 0)
    line(a1, 2, 0)
    line(a1, 2, 1)
    line(a1, 3, 0)
    line(a1, 3, 1)
    line(a1, 3, 2)
    line(a1, 4, 0)
    line(a1, 4, 1)
    line(a1, 4, 2)
    line(a1, 4, 3)
    line(a1, 0, 1)
    line(a2, 2, 3)
    line(b1, 0, 2)
    line(b2, 1, 3)
    for i in range(3):
        for j in range(3):
            q[i][j] = (calc(b1) * calc(b2)) * (a1[i] * a2[j] + a1[j] * a2[i]) - (calc(a1) * calc(a2)) * (b1[i] * b2[j] + b1[j] * b2[i])
    return -1 if (ret1 := q[0][0] * q[1][1] - q[0][1] * q[1][0]) <= 0 or (ret2 := (q[0][0] * q[1][1] * q[2][2] - q[0][0] * q[1][2] * q[2][1] + q[1][0] * q[2][1] * q[0][2] - q[1][0] * q[2][2] * q[0][1] + q[2][0] * q[0][1] * q[1][2] - q[2][0] * q[0][2] * q[1][1]) * [1, -1][q[0][0] > 0]) <= 0 else pi * ret2 / (ret1 * ret1 ** 0.5)
a1, a2, b1, b2, q = [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for _ in range(int(input())):
    Input = list(map(int, input().split()))
    x, y = Input[0::2], Input[1::2]
    print('IMPOSSIBLE' if (result := solve()) < 0 else result)
