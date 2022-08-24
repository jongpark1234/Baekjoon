n, f = map(lambda x: int(x) if x.isnumeric() else x, input().split())
x = [0] + list(map(int, input().split()))    
if (f == 'Alice' and n & 1) or (f == 'Bob' and n & 1 ^ 1):
    result = x[-1]
    for i in range(1, n - (n + 1 >> 1) + 1):
        result = min(result, x[i + (n + 1 >> 1)] - x[i])
    print(result)
else:
    l, r = 0, x[-1]
    while l <= r:
        m = l + r >> 1
        j = temp = 1
        for i in range(n):
            if x[i + 1] - x[j] > m:
                temp += 1
                j = i + 1
        if temp > n + 1 >> 1:
            l = m + 1
        else:
            r = m - 1
    print(l)
