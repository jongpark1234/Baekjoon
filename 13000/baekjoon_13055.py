from decimal import Decimal, Context, setcontext, MAX_PREC, MAX_EMAX
def multiply(a, b, digit = 0):
    setcontext(Context(prec=MAX_PREC, Emax=MAX_EMAX))
    if digit == 0:
        digit = len(str(min(len(a), len(b)) * max(a) * max(b)))
    f = f'0{digit}d'
    a_dec = Decimal(''.join(format(x, f) for x in a))
    b_dec = Decimal(''.join(format(x, f) for x in b))
    c_dec = a_dec * b_dec
    total_digit = digit * (len(a) + len(b) - 1)
    c = format(c_dec, f'0{total_digit}f')
    return [int(c[i:i + digit]) for i in range(0, total_digit, digit)]
s = input()
n = len(s)
a = list(map(lambda x: x == 'A', s))
b = list(map(lambda x: x == 'B', s))[::-1]
print(*multiply(a, b)[n:n * 2 - 1])
