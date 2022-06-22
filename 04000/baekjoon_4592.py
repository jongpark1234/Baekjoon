while len(numlist := list(map(int, input().split()))) > 1:
    temp = ''
    for i in numlist[1:]:
        if temp != i:
            print(i, end=' ')
            temp = i
    print('$')
