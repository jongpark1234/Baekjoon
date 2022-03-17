from math import gcd
while True:
    try:
        s = input()
        front, back = s.split('.')
        cir = ''
        if '(' in back:
            back, cir = back.split('(')[0], back.split('(')[1].replace(')', '')
            mole = int(front + back + cir) - int(front + back)
            deno = int('9' * len(cir) + '0' * len(back))
        else:
            deno = int(10 ** len(back))
            mole = deno * int(front) + int(back)
        GCD = gcd(mole, deno)
        mole //= GCD
        deno //= GCD
        print(f'{s} = {mole} / {deno}')
    except EOFError:
        break
