import decimal
from sys import stdin
def multiply(a, b, digit = 0):
    decimal.setcontext(decimal.Context(prec=decimal.MAX_PREC, Emax=decimal.MAX_EMAX))
    if digit == 0:
        digit = len(str(min(len(a), len(b)) * max(a) * max(b)))
    f = f'0{digit}d'
    a_dec = decimal.Decimal(''.join(format(x, f) for x in a))
    b_dec = decimal.Decimal(''.join(format(x, f) for x in b))
    c_dec = a_dec * b_dec
    total_digit = digit * (len(a) + len(b) - 1)
    c = format(c_dec, f'0{total_digit}f')
    return [int(c[i:i + digit]) for i in range(0, total_digit, digit)]
k = [int(stdin.readline()) for _ in range(int(stdin.readline()))]
d = [int(stdin.readline()) for _ in range(int(stdin.readline()))]
Max = max(d)
f = [1] + [0] * Max
for k_i in k:
    if k_i <= Max:
        f[k_i] = 1
f_square = multiply(f, f)
print(sum(1 for i in d if f_square[i] > 0))
