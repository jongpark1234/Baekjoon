Av, As, Ae = map(int, input().split())
Bv, Bs, Be = map(int, input().split())
Cv, Cs, Ce = map(int, input().split())
time = Av * Bv * Cv
while min(As, Bs, Cs) < time:
    if max(As, Bs, Cs) <= min(Ae, Be, Ce):
        print(max(As, Bs, Cs))
        exit()
    if Ae <= Be and Ae <= Ce:
        As += Av
        Ae += Av
    elif Be <= Ae and Be <= Ce:
        Bs += Bv
        Be += Bv
    else:
        Cs += Cv
        Ce += Cv
print(-1)
    