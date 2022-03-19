a, b = map(lambda x: x / 100, map(float, input().split()))
l = 1
Mw = 1
Mev = 0
if b > 0:
    while True:
        Pev = 0
        flag = False
        w = Mw
        while True:
            factor = (1 - b) / b
            x = factor ** l
            y = factor ** (w + l)
            p_l = (x - y) / (1 - y)
            p_w = (1 - x) / (1 - y)
            Cev = p_w * w - p_l * l * (1 - a)
            if Cev > Mev:
                Mev = Cev
                Mw = w
                flag = True
            if Cev < Pev:
                break
            Pev = Cev
            w += 1
        if flag:
            l += 1
        else:
            break
print(Mev)
