x, k = map(int, input().split())
if k * 7 <= x:
    print(k * 7000)
elif k * 3.5 <= x:
    print(k * 3500)
elif k * 1.75 <= x:
    print(k * 1750)
else:
    print(0)
