p = list(map(int, input().split()))
x, y, r = map(int, input().split())
for i in range(4):
    if p[i] == x:
        print(i + 1)
        break
else:
    print(0)
