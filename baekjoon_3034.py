n, w, h = map(int, input().split())
for _ in range(n):
    if int(input()) > int((w ** 2 + h ** 2) ** 0.5):
        print('NE')
    else:
        print('DA')
