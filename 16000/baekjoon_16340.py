MAX = 2000
result = 0
grundy = [0 for _ in range(MAX + 1)]
for i in range(1, MAX + 1):
    mex = [0 for _ in range(MAX >> 1)]
    for j in range(1, i):
        q, r = divmod(i, j)
        mex[grundy[j] ^ grundy[r] if q & 1 else grundy[r]] = 1
    grundy[i] = mex.index(0)
n = int(input())
for i in map(int, input().split()):
    result ^= grundy[i]
print('First' if result else 'Second')
