cnt = 0
while True:
    cnt += 1
    n0 = int(input())
    if n0 == 0:
        break
    n1 = 3 * n0
    if n1 % 2:
        print(f'{cnt}. odd', end=' ')
        n2 = (n1 + 1) // 2
        n3 = 3 * n2
        n4 = n3 // 9
    else:
        print(f'{cnt}. even', end=' ')
        n2 = n1 // 2
        n3 = 3 * n2
        n4 = n3 // 9
    print(n4)
