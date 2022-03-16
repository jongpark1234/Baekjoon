# pypy3
def Counting(n, m):
    cnt = 0
    for i in range(1, n + 1):
        cnt += min(m // i, n)
    return cnt
n = int(input())
k = int(input())
l, r = 0, n * n
while l + 1 < r:
    mid = l + r >> 1
    if Counting(n, mid) < k:
        l = mid
    else:
        r = mid
print(r)
