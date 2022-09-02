x = int(input())
if x == 1:
    print(0, 0)
    exit(0)
result = (x, 1)
for i in range(2, min(x + 1, 200)):
    l, r = i, x
    while r >= l + 1:
        temp = 1
        m = l + r >> 1
        for j in range(1, i + 1):
            temp = temp * (m - i + j) // j
            if temp > x:
                r = m
                break
        else:
            if temp == x:
                result = min(result, (m, i))
                break
            elif temp < x:
                l = m + 1
            else:
                r = m
print(*result)
