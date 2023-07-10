n, w, h = map(int, input().split())
r = (w ** 2 + h ** 2) ** 0.5
for i in range(n):
    print('YES' if int(input()) <= r else 'NO')
