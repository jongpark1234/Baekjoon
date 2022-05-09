from decimal import *
getcontext().prec = 99
def rooting(x):
    return a * x ** 3 + b * x ** 2 + c * x + d
def binarySearch(l, r):
    while r - l > 1e-21:
        x = (l + r) / 2
        if rooting(x) * rooting(l) > 0:
            l = x
        else:
            r = x
    return l
for _ in range(int(input())):
    s = []
    a, b, c, d = map(Decimal, input().split())
    formula = b * b + a * c * -3
    l, r = Decimal(-2000000), Decimal(2000001)
    if formula < 0:
        result = [binarySearch(l, r)]
    else:
        formula = sorted([(-b - formula ** Decimal('0.5')) / (a * 3), (-b + formula ** Decimal('0.5')) / (a * 3)])
        lhs, rhs = round(rooting(formula[0]), 20), round(rooting(formula[1]), 20)
        if round(rooting(formula[0]) * rooting(formula[1]), 20) > 0:
            result = [binarySearch(l, r)]
        elif lhs == rhs == 0:
            result = [formula[0]]
        elif lhs == 0:
            result = [formula[0], binarySearch(formula[1], r)]
        elif rhs == 0:
            result = [binarySearch(l, formula[0]), formula[1]]
        else:
            result = [binarySearch(l, formula[0]), binarySearch(formula[0], formula[1]), binarySearch(formula[1], r)]
    for i in result:
        print(f'{i:.9f}', end = ' ')
    print()
