from math import *
a, i = map(int, input().split())
for m in range(10001):
    if ceil(m / a) == i:
        break
print(m)
