numlist = list(map(int, input().split()))
if sum(numlist) >= 100:
    print('OK')
else:
    if numlist.index(min(numlist)) == 0:
        print('Soongsil')
    elif numlist.index(min(numlist)) == 1:
        print('Korea')
    else:
        print('Hanyang')
