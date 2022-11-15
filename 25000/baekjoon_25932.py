for _ in range(int(input())):
    numlist = list(map(int, input().split()))
    print(*numlist)
    if 17 in numlist:
        print('both' if 18 in numlist else 'zack')
    else:
        print('mack' if 18 in numlist else 'none')
    print()
