def j(v, i):
    return v % (10 ** i) // (10 ** (i - 1))
while True:
	a, b = map(int, input().split())
	t, c = 0, 0
	if a == b == 0:
		break
	for i in range(1, len(str(max(a, b))) + 1):
		ta, tb = j(a, i), j(b, i)
		if (ta + tb + t >= 10):
			c += 1
			t = 1
		else:
			s = 0
	print(c)
