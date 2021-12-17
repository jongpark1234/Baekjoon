n, l = map(int, input().split())
x = -1
for i in range(l, 101):
    t = n - (i * (i - 1)) / 2
    if t % i == 0 and t // i >= 0:
        x = int(t // i)
        length = i
        break
if x == -1:
    print(-1)
else:
    for i in range(x, x + length):
        print(i, end=' ')
