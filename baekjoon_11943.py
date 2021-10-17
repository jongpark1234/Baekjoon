a, b = map(int, input().split())
c, d = map(int, input().split())
if (a + d <= b + c):
    print(a + d)
else:
    print(b + c)
