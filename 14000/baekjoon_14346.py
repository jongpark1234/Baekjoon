def binarySearch(x, y, l, r):
    ret = float('inf')
    while abs(r - l) / 2 > 1.1920929e-7:
        mid = (l + r) / 2
        temp = calc(-10, x, mid)
        ret = temp[0]
        if temp[1] < y:
            l = mid
        else:
            r = mid
    return ret
def calc(x, y, pos):
    ret = 0
    for _ in range(2000):
        if y > 13 or y < -13:
            return [float('inf'), y]
        ret += (yFunction(x, y) + 1) * (pos ** 2 + 1) ** 0.5 / 100
        x += 0.01
        y += pos / 100
        pos += EularLagrangeEquation(x, y, pos) / 100
    return [ret, y]
def yFunction(x, y):
    ret = 0
    for i in islands:
        d = x ** 2 + (y - i) ** 2
        if d < 1.1920929e-7:
            return float('inf')
        ret += d ** -1
    return ret
def EularLagrangeEquation(x, y, pos):
    temp = pos ** 2 + 1
    ret = 1
    p1 = p2 = 0
    for i in islands:
        d = x ** 2 + (y - i) ** 2
        ret += d ** -1
        p1 += (y - i) / d ** 2
        p2 += (x + (y - i) * pos) / d ** 2
    return temp * (pos * p2 - temp * p1) * 2 / ret
for i in range(int(input())):
    n, a, b = map(float, input().split())
    islands = list(map(float, input().split()))
    slopes = sorted([-2, 2] + [(i - a) / 10 for i in islands])
    result = float('inf')
    for j in range(len(slopes) - 1):
        temp = binarySearch(a, b, slopes[j], slopes[j + 1])
        if result > temp:
            result = temp
    print(f'Case #{i + 1}: {round(result, 2)}')
