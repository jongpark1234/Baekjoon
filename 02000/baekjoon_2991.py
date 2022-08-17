a, b, c, d = map(int, input().split())
for i in map(int, input().split()):
    print((i % (a + b) <= a and i % (a + b) > 0) + (i % (c + d) <= c and i % (c + d) > 0))
