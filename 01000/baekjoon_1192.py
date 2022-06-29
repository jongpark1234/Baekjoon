n = int(input())
gloves = [list(map(int, input().split())) for _ in range(2)]
temp, numlist = [], []
for i in range(1 << n):
    cnt = [0, 0]
    for j in range(n):
        cnt[(i >> j) & 1] += gloves[(i >> j) & 1][j]
    temp.append(cnt)
temp.sort(reverse = True)
for i in temp:
    if not numlist or numlist[-1][1] < i[1]:
        numlist.append(i)
result = [float('inf'), float('inf')]
for i in range(1, len(numlist)):
    l = numlist[i][0] + 1
    r = numlist[i - 1][1] + 1
    result = min(result, [l + r, r])
print(result[0] - result[1], result[1], sep = '\n')
