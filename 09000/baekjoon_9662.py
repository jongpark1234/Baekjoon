m = int(input())
k = int(input())
stones = list(map(int, input().split()))
mask = (1 << 22) - 1
result = -1
Dict = {}
r = []
idx = 0
while True:
    if idx > m:
        break
    mask <<= 1
    result += 1
    for j in stones:
        if mask & (1 << j) == 0:
            mask += 1
            result -= 1
            break
    mask &= (1 << 22) - 1
    if mask in Dict.keys():
        length = (idx - Dict[mask])
        cnt = (m - idx) // length
        idx += cnt * length
        result += cnt * (result - r[Dict[mask]])
    Dict[mask] = idx
    r.append(result)
    idx += 1
print(result)
