time = int(input())
a, b, c = 0, 0, 0
if time >= 300:
    a = time // 300
    time %= 300
if time >= 60:
    b = time // 60
    time %= 60
if time >= 10:
    c = time // 10
    time %= 10
if time == 0:
    print(a, b, c)
else:
    print(-1)