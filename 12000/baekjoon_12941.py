VALUE = 1000
def solve(n):
    if n <= VALUE:
        return grundy[n]
    if n in memoization:
        return memoization[n]
    if n & 1:
        return 0
    if solve(n >> 1) == 1:
        memoization[n] = 2
        return 2
    memoization[n] = 1
    return 1
ret = 0
memoization = {}
grundy = [0]
for i in range(1, VALUE + 1):
    grundy.append(min({0, 1, 2} - {grundy[i - 1], grundy[i >> 1] if ~i & 1 else None}))
n, k = map(int,input().split())
for i in map(int, input().split()):
    ret ^= solve(i) if k & 1 else (i if i < 3 else i + 1 & 1)
print('Kevin' if ret else 'Nicky')
