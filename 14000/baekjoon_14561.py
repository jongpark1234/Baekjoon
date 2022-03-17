t = int(input())
for i in range(t):
    a, n = map(int, input().split())
    slist = []
    while True:
        if a == 0:
            break
        s = a % n
        slist.append(s)
        a //= n
    palin = True        
    for j in range(len(slist)):
        if slist[j] != slist[-1 * (j + 1)]:
            palin = False
            break
    print(int(palin))
