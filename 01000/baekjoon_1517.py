def merge(s, e):
    global result
    m = s + e >> 1
    x, y, z = s, m + 1, 0
    while x <= m and y <= e:
        if a[x] <= a[y]:
            b[z] = a[x]
            x += 1; z += 1
        else:
            b[z] = a[y]
            result += m - x + 1
            y += 1; z += 1
    while x <= m:
        b[z] = a[x]
        x += 1; z += 1
    while y <= e:
        b[z] = a[y]
        y += 1; z += 1
    for x in range(s, e + 1):
        a[x] = b[x - s]
def dnc(s, e):
    if s >= e:
        return
    m = s + e >> 1
    dnc(s, m)
    dnc(m + 1, e)
    merge(s, e)
result = 0
n = int(input())
a = list(map(int, input().split()))
b = [0 for _ in range(n)]
dnc(0, n - 1)
print(result)
