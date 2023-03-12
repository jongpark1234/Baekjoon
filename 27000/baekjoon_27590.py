MAX = 5000
ds, ys = map(int, input().split())
dm, ym = map(int, input().split())
solar = [False for _ in range(MAX + 1)]
for i in range(ys - ds, MAX + 1, ys):
    solar[i] = True
for i in range(ym - dm, MAX + 1, ym):
    if solar[i]:
        print(i)
        break
