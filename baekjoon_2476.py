n = int(input())
price = []
for i in range(n):
    a, b, c = map(int, input().split())
    if a == b == c:
        price.append(10000 + a * 1000)
    elif a == b or a == c:
        price.append(1000 + a * 100)
    elif b == c:
        price.append(1000 + b * 100)
    else:
        price.append(max(a, b, c) * 100)
print(max(price))
