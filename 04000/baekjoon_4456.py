while (n := int(input())):
    result = False
    poslist = list(map(int, input().split()))
    m = [[] for _ in range(n + 1)]
    for i in range(n << 1):
        for j in range(i + 1, n << 1):
            if poslist[i] == poslist[j]:
                if i & 1 == j & 1:
                    result = True
                    break
        else:
            continue
        break
    if result:
        print('escaped')
        continue
    for i in range(n << 1):
        for j in range(i + 1, n << 1):
            if poslist[i] == poslist[j]:
                temp = poslist[i + 1:j]
                idx = 1
                for k in range(i + 1, j):
                    poslist[k] = temp[-idx]
                    idx += 1
    for i in range(n << 1):
        m[poslist[i]].append(i)
    for i in range(0, 2 ** (n + 1), 2):
        flag = True
        for j in range(1, n + 1):
            for k in range(1, n + 1):
                if m[j][0] < m[k][0]:
                    if m[k][0] < m[j][1]:
                        if m[j][1] < m[k][1]:
                            if (i >> j) & 1 == (i >> k) & 1:
                                flag = False
                                break
            else:
                continue
            break
        if flag:
            print('caught')
            break
    else:
        print('escaped')
