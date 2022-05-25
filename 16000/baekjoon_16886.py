dp = [0 for _ in range(100001)]
check = [[] for _ in range(100001)]
def calc(p):
    ret = 0
    for i in range(p[0], p[1] + 1):
        ret ^= dp[i]
    return ret
i = 2
while (i * (i + 1)) // 2 <= 100000:
    l, r = 0, i
    while True:
        v = (r * (r + 1)) // 2 - (l * (l + 1)) // 2
        if v > 100000:
            break
        check[v].append([l + 1, r])
        l += 1
        r += 1
    i += 1
for i in range(3, 100001):
    grundy = [False for _ in range(500)]
    for j in check[i]:
        grundy[calc(j)] = True
    j = 0
    while True:
        if not grundy[j]:
            dp[i] = j
            break
        j += 1
n = int(input())
if dp[n] == 0:
    print(-1)
else:
    for i in check[n]:
        if calc(i) == 0:
            print(i[1] - i[0] + 1)
            break
