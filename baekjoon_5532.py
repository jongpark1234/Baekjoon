import sys
import math
l = int(sys.stdin.readline())
a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())
d = int(sys.stdin.readline())
ac = math.ceil(a / c)
bd = math.ceil(b / d)
if (ac > bd):
    print(l - ac)
else:
    print(l - bd)
