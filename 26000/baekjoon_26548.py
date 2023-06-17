from decimal import Decimal
from math import sqrt
def f(pm: Decimal) -> Decimal:
    return round((-b + (b ** 2 - Decimal(4) * a * c) ** Decimal(0.5) * pm) / (Decimal(2) * a), 3)
for _ in range(int(input())):
    a, b, c = map(Decimal, input().split())
    print(f'{f(Decimal(1))}, {f(Decimal(-1))}')
