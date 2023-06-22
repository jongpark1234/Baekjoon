from sys import stdin
from math import hypot
for _ in range(int(input())):
    x1, y1, r1, x2, y2, r2 = map(int, stdin.readline().split())
    distance = hypot(abs(x1 - x2), abs(y1 - y2))
    outrdis, inrdis = r1 + r2, abs(r1 - r2)
    if x1 == y1 == r1 == x2 == y2 == r2 == 0:
        print(1)
    elif distance == 0 and r1 == r2:
        print(-1)
    elif inrdis == distance or outrdis == distance:
        print(1)
    elif inrdis < distance < outrdis:
        print(2)
    else:
        print(0)
