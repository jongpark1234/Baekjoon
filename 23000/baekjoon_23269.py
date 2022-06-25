def dp(a, b, c):
    s = 0
    length = len(a)
    Max, Cur = [-1 for _ in range(c * 2 + 1)], [0 for _ in range(c + 1)]
    for i in range(length):
        if a[i] > b - s:
            Max[s - b + c] = i
            break
        s += a[i]
    for i in range(i, length):
        if Max[c] > -1:
            return [b]
        x = a[i]
        for j in range(c + 1)[::-1]:
            Max[j + x] = max(Max[j + x], Max[j])
        for j in range(c, c * 2 + 1)[::-1]:
            k = Cur[j - c]
            while k < Max[j]:
                Max[j - a[k]] = max(Max[j - a[k]], k)
                k += 1
            Cur[j - c] = k
    return [i + b - c for i in range(c * 2 + 1) if Max[i] > -1]
n, x = map(int, input().split())
t = sorted(list(map(int, input().split())))
Max = max(t)
while t and t[-1] > x:
    t.pop()
if len(t) > 4:
    numlist = [x + 1 - i for i in t[4:]]
    Sum = sum(numlist)
    result = x + 1 + min(max(i, Sum - i) for i in dp(numlist, Sum // 2, max(numlist)))
elif len(t) > 2:
    result = x + 1
else:
    result = Max
print(max(result, Max))
