n, k = map(int, input().split())
k -= 1
p = list(map(float, input().split()))
numlist1, numlist2 = [[[[0, 0], [0, 0]] for _ in range(n)] for _ in range(n)], [[[0, 0] for _ in range(n)] for _ in range(n)]
numlist2[k][k][0] = 1
for i in range(n - 1):
    numlist1[i][i][0][1] = numlist1[i][i][1][1] = p[i]
    numlist1[i][i][1][0] = numlist1[i][i][0][0] = 1 - p[i]
for i in range(2, n):
    for j in range(n - i):
        numlist1[j][i + j - 1][0][0] = (1 - p[j]) / ((1 - p[j]) + p[j] * numlist1[j + 1][i + j - 1][0][1])
        numlist1[j][i + j - 1][0][1] = p[j] * numlist1[j + 1][i + j - 1][0][1] / ((1 - p[j]) + p[j] * numlist1[j + 1][i + j - 1][0][1])
        numlist1[j][i + j - 1][1][1] = p[i + j - 1] / (p[i + j - 1] + (1 - p[i + j - 1]) * numlist1[j][i + j - 2][1][0])
        numlist1[j][i + j - 1][1][0] = (1 - p[i + j - 1]) * numlist1[j][i + j - 2][1][0] / (p[i + j - 1] + (1 - p[i + j - 1]) * numlist1[j][i + j - 2][1][0])
for i in range(2, n):
    for j in range(n - i):
        numlist2[j][i + j - 1][0] = numlist2[j + 1][i + j - 1][0] * numlist1[j + 1][i + j - 1][0][0] + numlist2[j + 1][i + j - 1][1] * numlist1[j + 1][i + j - 1][1][0]
        numlist2[j][i + j - 1][1] = numlist2[j][i + j - 2][0] * numlist1[j][i + j - 1 - 1][0][1] + numlist2[j][i + j - 2][1] * numlist1[j][i + j - 2][1][1]
print(numlist2[0][n - 2][0] + numlist2[0][n - 2][1])
