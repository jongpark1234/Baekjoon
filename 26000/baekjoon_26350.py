for _ in range(int(input())):
    d, *numlist = list(map(int, input().split()))
    print(f'Denominations:', *numlist)
    for i in range(1, d):
        if numlist[i - 1] * 2 > numlist[i]:
            print('Bad', end=' ')
            break
    else:
        print('Good', end=' ')
    print('coin denominations!\n')
