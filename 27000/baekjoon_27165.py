n = int(input())
a = list(map(int, input().split()))
x = int(input())
one = a.count(1)
if one >= 3:
    print('NO')
elif one == 2:
    idx = a.index(1)
    try:
        if a[idx + x] == 1:
            print('YES')
            print(idx, idx + x)
        else:
            print('NO')
    except:
        print('NO')
elif one == 1:
    idx = a.index(1)
    if idx - x >= 0:
        if a[idx - x] >= 3:
            print('YES')
            print(idx - x, idx)
            exit(0)
    if idx + x <= n:
        if a[idx + x] >= 1:
            print('YES')
            print(idx, idx + x)
            exit(0)
    print('NO')
else:
    for i in range(n - x + 1):
        if a[i] not in [0, 2]:
            if a[i + x] >= 1:
                print('YES')
                print(i, i + x)
                break
    else:
        print('NO')
