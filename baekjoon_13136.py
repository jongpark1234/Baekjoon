import math
r, c, n = map(int, input().split())
cctv1 = math.ceil(r / n)
cctv2 = math.ceil(c / n)
cctv = cctv1 * cctv2
print(cctv)