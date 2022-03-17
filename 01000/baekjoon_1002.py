import sys
import math
t = int(sys.stdin.readline())
for _ in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())
    distance = math.sqrt(pow(abs(x1 - x2), 2) + pow(abs(y1 - y2), 2))
    outrdis, inrdis = r1 + r2, abs(r1 - r2)
    if distance == 0 and r1 == r2:
        print(-1)
    elif inrdis == distance or outrdis == distance:
        print(1)
    elif inrdis < distance < outrdis:
        print(2)
    else:
        print(0)
