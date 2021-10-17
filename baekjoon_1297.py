import math
d, h, w = map(int, input().split())
r = d / math.sqrt((h * h) + (w * w))
print(int(r * h), int(r * w))
