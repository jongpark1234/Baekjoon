from math import ceil
for _ in range(int(input())):
    h, w, n = map(int, input().split())
    floor = n % h
    if n % h == 0:
        floor = h
    print(str(floor) + '{:02d}'.format(ceil(n / h)))
