pillow = 0
r, c = map(int, input().split())
Rg, Cg, Rp, Cp = map(int, input().split())
for i in [input() for _ in range(r)]:
    pillow += i.count('P')
print(int(not Rp * Cp == pillow))
