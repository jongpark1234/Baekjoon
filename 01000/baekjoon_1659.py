NUM, INF = 500000, float('inf')
n, m = map(int, input().split())
s = list(map(int, input().split()))
t = list(map(int, input().split()))
pfs = [0 for _ in range(n + m + 1)]
pft = [0 for _ in range(n + m + 1)]
combined = [0 for _ in range(n + m + 1)]
last = [0 for _ in range(NUM * 2 + 1)]
cnt = [NUM] + [0 for _ in range(n + m)]
idx = 1
idxPair = [0, 0]
while idxPair[0] < n and idxPair[1] < m:
    pfs[idx] = pfs[idx - 1]
    pft[idx] = pft[idx - 1]
    cnt[idx] = cnt[idx - 1]
    if s[idxPair[0]] < t[idxPair[1]]:
        pfs[idx] += s[idxPair[0]]
        combined[idx] = s[idxPair[0]]
        cnt[idx] += 1
        idxPair[0] += 1
    else:
        pft[idx] += t[idxPair[1]]
        combined[idx] = t[idxPair[1]]
        cnt[idx] -= 1
        idxPair[1] += 1
    idx += 1
while idxPair[0] < n:
    pfs[idx] = pfs[idx - 1] + s[idxPair[0]]
    pft[idx] = pft[idx - 1]
    combined[idx] = s[idxPair[0]]
    cnt[idx] = cnt[idx - 1] + 1
    idx += 1
    idxPair[0] += 1
while idxPair[1] < m:
    pfs[idx] = pfs[idx - 1]
    pft[idx] = pft[idx - 1] + t[idxPair[1]]
    combined[idx] = t[idxPair[1]]
    cnt[idx] = cnt[idx - 1] - 1
    idx += 1
    idxPair[1] += 1
result = [0 for _ in range(idx)]
idxPair = [0, 0]
for i in range(1, idx):
    result[i] = INF
    value = last[cnt[i]]
    if cnt[i] == cnt[i - 1] + 1:
        idxPair[0] += 1
    else:
        idxPair[1] += 1
    if value > 0:
        result[i] = result[value] + abs((pfs[i] - pfs[value]) - (pft[i] - pft[value]))
    elif cnt[i] == NUM:
        result[i] = abs(pfs[i] - pft[i])
    temp = INF
    if cnt[i] == cnt[i - 1] + 1:
        if idxPair[1] != 0:
            temp = min(temp, abs(combined[i] - t[idxPair[1] - 1]))
        if idxPair[1] != m:
            temp = min(temp, abs(combined[i] - t[idxPair[1]]))
    else:
        if idxPair[0] != 0:
            temp = min(temp, abs(combined[i] - s[idxPair[0] - 1]))
        if idxPair[0] != n:
            temp = min(temp, abs(combined[i] - s[idxPair[0]]))
    result[i] = min(result[i], result[i - 1] + temp)
    last[cnt[i]] = i
print(result[-1])
