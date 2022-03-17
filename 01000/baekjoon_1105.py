l, r = input().split()
eight = 0
if len(l) != len(r) or l[0] != r[0]:
    print(0)
else:
    if l[0] == '8':
        eight += 1
    for i in range(1, len(l)):
        if l[i] != r[i]:
            break
        else:
            if l[i] == '8':
                eight += 1
    print(eight)
