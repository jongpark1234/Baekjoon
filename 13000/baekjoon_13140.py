n = int(input())
for h in range(1, 10):
    for e in range(10):
        if h == e:
            continue
        for l in range(10):
            if l in [h, e]:
                continue
            for o in range(10):
                if o in [h, e, l]:
                    continue
                for w in range(1, 10):
                    if w in [h, e, l, o]:
                        continue
                    for r in range(10):
                        if r in [h, e, l, o, w]:
                            continue
                        for d in range(10):
                            if d in [h, e, l, o, w, r]:
                                continue
                            hello = int(f'{h}{e}{l}{l}{o}')
                            world = int(f'{w}{o}{r}{l}{d}')
                            if hello + world == n:
                                print(f'  {hello}')
                                print(f'+ {world}')
                                print('-------')
                                print(str(n).rjust(7, ' '))
                                break
                        else:
                            continue
                        break
                    else:
                        continue
                    break
                else:
                    continue
                break
            else:
                continue
            break
        else:
            continue
        break
    else:
        continue
    break
else:
    print('No Answer')
