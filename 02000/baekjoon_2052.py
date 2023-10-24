from decimal import *
getcontext().prec = 200
print('{:f}'.format((Decimal('1') / Decimal('2') ** Decimal(input()))))
