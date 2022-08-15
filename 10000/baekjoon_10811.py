n, m = map(int, input().split())
numlist = list(range(1, n + 1))
for _ in range(m):
    idx = 0
    i, j = map(int, input().split())
    i -= 1
    temp = numlist[i:j][::-1]
    for l in range(i, j):
        numlist[l] = temp[idx]
        idx += 1
print(*numlist)
