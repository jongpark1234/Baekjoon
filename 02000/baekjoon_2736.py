from math import sin, cos
n, ha, hb = map(float, input().split())
temp = 0.017453292519943295
for _ in range(int(n)):
    alpha, beta, gamma, delta = map(float, input().split())
    v1 = 100 * (cos(temp * alpha) * cos(temp * gamma)) + (hb - ha) * sin(temp * alpha)
    v2 = 100 * (cos(temp * beta) * cos(temp * delta)) + (hb - ha) * sin(temp * beta)
    v3 = (cos(temp * alpha) * cos(temp * gamma)) * (cos(temp * alpha) * cos(temp * gamma)) + (cos(temp * alpha) * sin(temp * gamma)) * (cos(temp * alpha) * sin(temp * gamma)) + sin(temp * alpha) * sin(temp * alpha)
    v4 = (cos(temp * alpha) * cos(temp * gamma)) * (cos(temp * beta) * cos(temp * delta)) + (cos(temp * alpha) * sin(temp * gamma)) * (cos(temp * beta) * sin(temp * delta)) + sin(temp * alpha) * sin(temp * beta)
    v5 = (cos(temp * beta) * cos(temp * delta)) * (cos(temp * beta) * cos(temp * delta)) + (cos(temp * beta) * sin(temp * delta)) * (cos(temp * beta) * sin(temp * delta)) + sin(temp * beta) * sin(temp * beta)
    v6 = -v3 * v5 + v4 * v4
    ta = (-v1 * v5 + v2 * v4) / v6
    tb = (v2 * v3 - v1 * v4) / v6
    result = (ha + sin(temp * alpha) * ((-v1 * v5 + v2 * v4) / v6) + hb + sin(temp * beta) * ((v2 * v3 - v1 * v4) / v6)) / 2
    print(round(result))
