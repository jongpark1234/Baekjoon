n, m = map(int, input().split())
numlist = list(range(1, n + 1))
for _ in range(m):
    idx = 0
    i, j, k = map(int, input().split())
    temp = numlist[k - 1:j] + numlist[i - 1:k - 1]
    for l in range(i - 1, j):
        numlist[l] = temp[idx]
        idx += 1
print(*numlist)
