a, b, c, x, y = map(int, input().split())
if a + b < c * 2:
    print(a * x + b * y)
else:
    money = min(x, y) * c * 2
    if x >= y:
        index = x - y
        money += min(a * index, c * index * 2)
    else:
        index = y - x
        money += min(b * index, c * index * 2)
    print(money)
