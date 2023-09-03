from sys import stdin
from math import log2, ceil
for _ in range(int(input())):
	cnt = 0
	x, w = map(int, stdin.readline().split())
	while x < w:
		x *= 2
		cnt += 1
	print(cnt)
