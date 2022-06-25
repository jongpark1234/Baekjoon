n, t = map(int, input().split())
numlist = sorted([tuple(map(int, input().split())) for _ in range(n)])
plist1 = sorted([i[1] for i in numlist])
plist2 = [plist1[i] for i in range(n)]
blist = [0 for _ in range(n)]
idx = [n for _ in range(n)]
for i in range(n)[::-1]:
    for j in range(n):
        if numlist[i][1] <= plist1[j]:
            plist2[j] -= t
            while idx[j] > i + 1 and plist2[j] < numlist[idx[j] - 1][0]:
                idx[j] -= 1
            if idx[j] < n:
                plist2[j] = min(plist2[j], numlist[idx[j]][0] - blist[idx[j]])
            if plist2[j] < numlist[i][0]:
                print('no'); exit()
            if plist2[j] < numlist[i][0] + t:
                blist[i] = max(blist[i], numlist[i][0] + t - plist2[j])
    for j in range(i + 1, n):
        blist[i] = max(blist[i], blist[j] - (numlist[j][0] - numlist[i][0]))
    for j in range(i + 1, n):
        if numlist[j][0] - blist[j] < numlist[i][0]:
            blist[j] = max(blist[j], blist[i] + (numlist[j][0] - numlist[i][0]))
print('yes')
