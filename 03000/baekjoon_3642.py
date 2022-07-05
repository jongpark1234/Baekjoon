from decimal import *
from math import ceil, sqrt
getcontext().prec = 99
def getDistance(d, q):
    v = max(q, Decimal(0))
    v1 = (Decimal(1000) - v) * Decimal(2)
    v2 = v * v1 + v1 ** Decimal(2) / Decimal(4)
    ret = (Decimal(sqrt(v ** Decimal(2) + d)) - v) * Decimal(2) if v2 > d else v1 + (d - v2) / Decimal(1000)
    return ret - q if q < Decimal(0) else ret
def getQ(n, distance):
    temp = Decimal(sqrt(n * Decimal(4)))
    if temp > Decimal(2000):
        temp = n / Decimal(1000) + Decimal(1000)
    if temp < distance:
        return temp - distance
    ret = n / distance - distance / Decimal(4)
    return Decimal(1000) - sqrt(distance * Decimal(1000) - n) if ret + distance / Decimal(2) > Decimal(1000) else ret
def traveling(temp, t, Max, Min, idx):
    global result
    if idx == l:
        if t + (distance := getDistance(xdest - temp, Max)) < result:
            result = t + distance
    else:
        d = x[idx][0] - temp
        tmin, tmax = t + getDistance(d, Max), t + getDistance(d, Min)
        cycling = x[idx][1] + x[idx][2]
        j = int(tmin / cycling)
        while cycling * j <= tmax and cycling * j <= result:
            s, e = cycling * j + x[idx][1], (j + 1) * cycling
            if e <= tmax:
                v = min((v := max(getQ(d, e - t), Decimal(0))) + getDistance(d, v) / Decimal(2), Decimal(1000))
                if v > speed[idx][j + 1]:
                    speed[idx][j + 1] = v
            if s <= tmax:
                traveling(temp, t, getQ(d, s - t) if s > tmin else Max, getQ(d, e - t) if e < tmax else Min, idx + 1)
            j += 1
while True:
    try:
        xdest, l = map(Decimal, input().split())
        result = temp = Decimal(0)
        l = int(l)
        x = [list(map(Decimal, input().split())) for _ in range(l)]
        speed = [[Decimal(-1) for _ in range(1024)] for _ in range(10)]
        for i in range(l):
            result += getDistance(x[i][0] - temp, Decimal(0)) + x[i][1]
            temp = x[i][0]
        result += getDistance(xdest - temp, Decimal(0))
        traveling(Decimal(0), Decimal(0), Decimal(0), -result, 0)
        for i in range(l):
            cycling = x[i][1] + x[i][2]
            for j in range(ceil(result / cycling)):
                if speed[i][j] >= Decimal(0):
                    traveling(x[i][0], cycling * Decimal(j), speed[i][j], -result, i + 1)
        print(round(result, 3))
    except:
        break
