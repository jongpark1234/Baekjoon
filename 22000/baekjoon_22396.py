from math import ceil
while True:
    r0, w0, c, r = map(int, input().split())
    if r0 == w0 == c == r == 0:
        break
    print(0 if w0 * c <= r0 else ceil((w0 * c - r0) / r))
