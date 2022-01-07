price = [350.34, 230.90, 190.55, 125.30, 180.90]
for _ in range(int(input())):
    money = 0
    part = list(map(int, input().split()))
    for i in range(5):
        money += price[i] * part[i]
    print(f'${money:.2f}')
