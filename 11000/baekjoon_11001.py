def dnc(left, right, a, b):
    global result
    if left > right:
        return
    mid = (left + right) // 2
    num = max(a, mid - d)
    for i in range(num, min(mid, b) + 1):
        if w(num, mid) < w(i, mid):
            num = i
    result = max(result, w(num, mid))
    dnc(left, mid - 1, a, num)
    dnc(mid + 1, right, num, b)
result = 0
w = lambda x, y: (y - x) * t[y] + v[x]
n, d = map(int, input().split())
t = [0] + list(map(int, input().split()))
v = [0] + list(map(int, input().split()))
dnc(1, n, 1, n)
print(result)
