m, n = map(int, input().split())
pawn = [0] + list(map(int, input().split())) + [0]
p = t = ret = value = 0
d_pawn = [0 for _ in range(n + 2)]
pawn[-1] = m - 1
if pawn[n] == m - 1:
    ret = 0
    for i in range(1, n + 1)[::-1]:
        if pawn[i] - pawn[i - 1] != 1:
            break
        ret += 1
    ret += 1
    print(ret)
    exit(0)
for i in range(1, n + 1)[::-1]:
    if pawn[i + 1] - pawn[i] != 1:
        d_pawn[t] = p
        t += 1
        p = 0
        if pawn[i + 1] - pawn[i] > 2:
            t += 2 - ((pawn[i + 1] - pawn[i]) & 1)
    p += 1
d_pawn[t] = p
for i in range(1, t + 1):
    if i % 2 == 1:
        value ^= d_pawn[i]
for i in range(1, t + 1):
    if i % 2 == 0:
        if d_pawn[i - 1] ^ value > d_pawn[i - 1] and d_pawn[i - 1] ^ value <= d_pawn[i] + d_pawn[i - 1]:
            ret += 1
    else:
        if d_pawn[i] ^ value < d_pawn[i]:
            ret += 1
print(ret)
