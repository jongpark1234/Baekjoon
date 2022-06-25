def shifting(numlist, idx, temp):
    numlist[idx][0] = temp
    for i in range(logN):
        numlist[idx][i + 1] = min(numlist[idx][i], numlist[max(idx - (1 << i), 0)][i])
def before(numlist, idx, temp):
    for i in range(logN + 1)[::-1]:
        if idx < 0:
            break
        if numlist[idx][i] >= temp:
            idx -= 1 << i
    return max(idx, -1)
def numbering(num):
    ret = 0
    while (2 << ret) < num:
        ret += 1
    return ret
n = int(input())
a = list(map(int, input().split()))
logN = numbering(n + 1)
psumA = [0]
for i in range(n):
    psumA.append(psumA[i] + a[i])
result = 1e18
over = [[0 for _ in range(logN + 1)] for _ in range(n + 1)]
under = [[0 for _ in range(logN + 1)] for _ in range(n + 1)]
blist = [[0 for _ in range(logN + 1)] for _ in range(n + 1)]
numlist = [0]
for i in range(1, n + 1):
    numlist.append(max(psumA[i] - 1, 0))
    if not a[i - 1]:
        numlist[i] = min(numlist[i], numlist[i - 1])
    r = before(over, i - 1, psumA[i] - i + 1)
    if r > -1:
        l = before(under, r - 1, i - psumA[i])
        temp = numbering(r - l)
        numlist[i] = min(numlist[i], psumA[i] * 2 - i - 1 + min(blist[r][temp], blist[l + (1 << temp)][temp]))
    result = min(result, numlist[i] + max(psumA[n] - psumA[i] - 1, 0))
    shifting(over, i, psumA[i] - i)
    shifting(under, i, i - psumA[i])
    shifting(blist, i, numlist[i] - psumA[i] * 2 + i)
print(result)
