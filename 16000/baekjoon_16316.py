for i, j in zip(range(1, int(input()) + 1), input().split()):
    if j.isnumeric() and i != int(j):
        print('something is fishy')
        break
else:
    print('makes sense')
