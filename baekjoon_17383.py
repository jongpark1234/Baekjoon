# pypy3
N = int(input())
t = sorted(list(map(int, input().split())))
l, r = 1, 1000000000
result = 1000000000
def F(n):
    a, b = 0, 0
    value = []
    for i in range(N):
        m = t[i] // n
        if m * n == t[i]:
            value.append(m)
        else:
            value.append(m + 1)
    for i in range(N):
        if value[i] == 1:
            a += 1
        elif b == 0:
            b = value[i] - 1
        else:
            b += value[i] - 2
    return a >= b
while l <= r:
    mid = (l + r) // 2
    if F(mid):
        result = min(result, mid)
        r = mid - 1
    else:
        l = mid + 1
print(result)
