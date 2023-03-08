n, m = map(int, input().split())
numlist = [0 for _ in range(n)]
for _ in range(m):
    i, j, k = map(int, input().split())
    for idx in range(i - 1, j):
        numlist[idx] = k
print(*numlist)
