price = sum(map(int, input().split()))
c = int(input()) * 2
if price >= c:
    print(price - c)
else:
    print(price)
