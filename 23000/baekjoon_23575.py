result = []
numlist = list(map(int, input().split()))
numlist = [[numlist[i], i + 1] for i in range(3)]
while True:
    numlist.sort()
    if numlist[0][0] == 0:
        break
    x, y = divmod(numlist[1][0], numlist[0][0])
    flag = y <= numlist[0][0] >> 1
    x += flag ^ 1
    while x > flag ^ 1:
        if x & 1:
            result.append((numlist[1][1], numlist[0][1]))
            numlist[1][0] -= numlist[0][0]
            numlist[0][0] <<= 1
        else:
            result.append((numlist[2][1], numlist[0][1]))
            numlist[2][0] -= numlist[0][0]
            numlist[0][0] <<= 1
        x >>= 1
    if flag ^ 1:
        result.append((numlist[0][1], numlist[1][1]))
        numlist[0][0] -= numlist[1][0]
        numlist[1][0] <<= 1
print(len(result))
for i in result:
    print(*i)
