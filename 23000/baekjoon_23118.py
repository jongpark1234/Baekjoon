from sys import stdin
from math import gcd
def solve(plist: list, cur: list) -> list:
    idx = len(plist) - 1
    if plist[idx][1] + cur[1] <= plist[idx][0]:
        tmp = gcd(plist[idx][1], cur[1])
        plist.pop()
        return solve(plist[:], [cur[0], tmp])
    if plist[idx][1] >= cur[1]:
        Len = plist[idx][0] - plist[idx - 1][0]
        Len %= cur[1]
        plist.pop()
        return solve(solve(plist[:], [plist[idx - 1][0] + Len, Len]) if Len else plist[:], cur[:])
    else:
        temp, flag = plist[idx][0] - cur[1], False
        if temp < 0:
            return plist + [cur]
        elif temp == 0:
            flag = True
        else:
            for i in range(idx, 0, -1):
                if temp > plist[i - 1][0]:
                    if (temp - plist[i - 1][0]) % plist[i][1] == 0:
                        flag = True
                        break
                    ret, hl = plist[:i], plist[i][1]
                    if temp - plist[i - 1][0] > hl:
                        ret = solve(ret[:], [(temp - plist[i - 1][0]) // hl * hl + plist[i - 1][0], hl])
                    ret = solve(solve(ret[:], [temp, (temp - plist[i - 1][0]) % hl]), [(temp - plist[i - 1][0]) // hl * hl + plist[i - 1][0] + hl, hl - (temp - plist[i - 1][0]) % hl])
                    if temp + hl < plist[i][0]:
                        ret = solve(ret[:], [plist[i][0], hl])
                    for j in range(i, idx):
                        ret = solve(ret[:], plist[j + 1][:])
                    return solve(ret[:], cur[:])
        if flag:
            if cur[1] % plist[idx][1] == 0:
                cur[1] = plist[idx][1]
            return plist + [cur]
while True:
    result, pair = 0, [[0, 0], [1, 1]]
    n, l = map(int, stdin.readline().split())
    if n == l == 0:
        break
    a = [0] + sorted(set(list(map(int, stdin.readline().split())) + [1]))
    n = len(a[1:])
    for i in range(2, n + 1):
        pair = solve(pair[:], [a[i], a[i] - a[i - 1]])
    for i in range(1, len(pair)):
        result += (pair[i][0] - pair[i - 1][0]) // pair[i][1]
    print(result)
