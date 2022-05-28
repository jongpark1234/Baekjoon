i = 1
while True:
	a, b, c = map(int, input().split())
	if a == b == c == 0:
		break
	print(f'Triangle #{i}')
	i += 1
	if a == -1:
		print('Impossible.' if c ** 2 - b ** 2 <= 0 else f'a = {(c ** 2 - b ** 2) ** 0.5:.3f}')
	elif b == -1:
		print('Impossible.' if c ** 2 - a ** 2 <= 0 else f'b = {(c ** 2 - a ** 2) ** 0.5:.3f}')
	else:
		print(f'c = {(a ** 2 + b ** 2) ** 0.5:.3f}')
	print()
