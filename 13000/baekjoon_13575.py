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
result = [1]
n, k = map(int, input().split())
a = list(map(int, input().split()))
gem = [False for _ in range(max(a) + 1)]
for i in a:
    gem[i] = True
for i in bin(k)[::-1]:
    if i == '1':
        result = [False if g == False else True for g in multiply(result, gem)]
    gem = [False if g == False else True for g in multiply(gem, gem)]
print(' '.join(str(i) for i, x in enumerate(result) if x == True))
