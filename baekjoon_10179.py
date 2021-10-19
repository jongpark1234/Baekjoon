n = int(input())
for i in range(n):
    cash = float(input())
    print('${:.2f}'.format(round(cash * (4 / 5), 2)))
