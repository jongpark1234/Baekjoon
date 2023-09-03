from sys import stdin
for _ in range(int(input())):
	cnt = 0
	x, w = map(int, stdin.readline().split())
	while x < w:
		x *= 2
		cnt += 1
	print(cnt)
