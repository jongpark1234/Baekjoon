import math
t = int(input())
for _ in range(t):
    h, w, n = map(int, input().split())
    floor = n % h
    if n % h == 0:
        floor = h
    print(str(floor) + '{:02d}'.format(math.ceil(n / h)))
