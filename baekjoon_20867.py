m, s, g = map(int, input().split())
a, b = map(float, input().split())
l, r = map(int, input().split())
left = l / a + m / g
right = r / b + m / s
if left < right:
    print('friskus')
else:
    print('latmask')
