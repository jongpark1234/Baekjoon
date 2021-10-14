import sys
import math
a, b, v = map(int, sys.stdin.readline().split())
print(math.ceil((v - b) / (a - b)))
