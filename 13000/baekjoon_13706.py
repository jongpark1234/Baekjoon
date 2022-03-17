from math import *
import sys
n = int(sys.stdin.readline())
start, end = 1, n
while True:
    mid = (start + end) // 2
    if mid ** 2 == n:
        print(mid)
        break
    elif mid ** 2 > n:
        end = mid - 1
    elif mid ** 2 < n:
        start = mid + 1
