for i in range(int(input())):
    result = []
    h, w = map(int, input().split())
    x = [input() for _ in range(h)]
    print(f'Data Set {i + 1}:')
    for j in range(w):
        flag = False
        c = 0
        for k in range(h):
            if x[k][j] == 'X':
                flag = True
                break
            elif x[k][j] == 'H':
                c += 3
            elif x[k][j] == 'S':
                c += 1
        result.append(str(c) if flag else 'N')
    print(' '.join(result) + '\n')
