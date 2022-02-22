# pypy3
from collections import deque
def update(idx, val):
    while idx <= 65539:
        tree[idx] += val
        idx += idx & (-idx)
def find(idx):
    rtn = 0
    while idx > 0:
        rtn += tree[idx]
        idx -= idx & (-idx)
    return rtn
def biSearch():
    L = 1
    R = 65537
    median = (k+1)//2
    while True:
        mid = (L+R)//2
        cnt = find(mid)
        if L == mid:
            if cnt < median:
                return R-1
            return L-1
        if cnt < median:
            L = mid
        else:
            R = mid
ans = 0
tree = [0 for _ in range(65540)]
n, k = map(int, input().split())
dq = deque()
for i in range(n):
    dq.append(int(input()))
    update(dq[-1]+1, 1)
    if len(dq) > k:
        update(dq.popleft()+1, -1)
    if len(dq) == k : ans += biSearch()
print(ans)