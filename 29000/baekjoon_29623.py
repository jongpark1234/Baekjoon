from decimal import Decimal
for _ in range(int(input())):
    a, b, c, d = map(Decimal, input().split())
    l, r = a + b.sqrt(), c + d.sqrt()
    print('Less' if l < r else 'Greater' if l > r else 'Equal')
