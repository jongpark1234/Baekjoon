for _ in range(int(input())):
    alist = []; blist = []
    a, b = input().split()
    for i in a:
        alist.append(i)
    for i in b:
        blist.append(i)
    alist.sort()
    blist.sort()
    print('Possible' if alist == blist else 'Impossible')
