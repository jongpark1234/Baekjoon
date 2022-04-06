for _ in range(int(input())):
    cnt = 0
    n = input()
    while n != '6174':
        cnt += 1
        temp = ''.join(sorted(n.zfill(4)))
        n = str(int(temp[::-1]) - int(temp))
    print(cnt)
