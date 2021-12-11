import decimal
decimal.getcontext().prec = 1000
for i in range(int(input())):
    num = decimal.Decimal(input() + '.0000000000')
    powd = decimal.Decimal('1') / decimal.Decimal('3')
    num = round(decimal.Decimal(num ** powd), 500)
    num = decimal.Decimal(num).quantize(decimal.Decimal('.0000000001'), rounding=decimal.ROUND_DOWN)
    print(num)
