from itertools import combinations
result = 0
piles = []
Dict = {}
n = int(input())
for i in range(n):
    p = input()
    temp = w = 0
    t = 1099511627776
    for j in range(len(p)):
        if w or (j != 0 and p[j] != p[j - 1]):
            w = 1
            t //= 2
        temp += t if p[j] == 'W' else -t
    piles.append([temp, len(p)])
fL, bL = piles[:n // 2], piles[n // 2:]
for i in range(len(fL) + 1):
    for j in combinations(fL, i):
        p, b = 0, 0
        for k in j:
            p += k[0]
            b += k[1]
        try:
            if Dict[p] < b:
                Dict[p] = b
        except KeyError:
            Dict[p] = b
for i in range(len(bL) + 1):
    for j in combinations(bL, i):
        p, b = 0, 0
        for k in j:
            p += k[0]
            b += k[1]
        try:
            result = max(result, Dict[-p] + b)
        except KeyError:
            pass
print(result)
