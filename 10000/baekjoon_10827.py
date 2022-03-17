import decimal
decimal.getcontext().prec = 1101
r, n = input().split()
print('{0:f}'.format(decimal.Decimal(r) ** int(n)))
