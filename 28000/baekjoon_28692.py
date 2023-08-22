from sys import stdin
n = int(input())
xlist, ylist = [], []
for _ in range(n):
    x, y = map(int, stdin.readline().split())
    xlist.append(x)
    ylist.append(y)
Sx, Sy = sum(xlist), sum(ylist)
Sxx, Sxy = sum(map(lambda x: x ** 2, xlist)), sum(xlist[i] * ylist[i] for i in range(n))
if Sx ** 2 != n * Sxx:
    a2 = (n * Sxy - Sx * Sy) / (n * Sxx - Sx ** 2)
    b2 = (Sy - a2 * Sx) / n
    print(f'{a2} {b2}' if Sx ** 2 != n * Sxx else 'EZPZ')
else:
    print('EZPZ')
