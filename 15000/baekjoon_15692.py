result = 0
n, d, r = map(int, input().split())
numlist = [[0 for _ in range(1001)] for _ in range(1001)]
numlist[0][0] = 1
for i in range(1, 1001):
    numlist[i][0] = 1
    numlist[i][i] = 1
for i in range(2, 1001):
    for j in range(1, i):
        numlist[i][j] = numlist[i - 1][j - 1] + numlist[i - 1][j]
gem = numlist[n + d - 1][d]
for i in range(1, d + 1):
	calc = [0 for _ in range(501)]
	for j in range(1, min(n, d // i) + 1):
		idx = min(n, d // i) - j + 1
		temp = numlist[n][idx] * numlist[n + d - i * idx - 1][n - 1]
		for k in range(idx + 1, min(n, d // i) + 1):
			temp -= numlist[k][idx] * calc[k]
		calc[idx] = temp
		result += min(r, idx) * calc[idx]
print(result / gem + r)
