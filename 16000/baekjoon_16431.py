Br, Bc = map(int, input().split())
Dr, Dc = map(int, input().split())
Jr, Jc = map(int, input().split())
B = max(abs(Jr - Br), abs(Jc - Bc))
D = abs(Jr - Dr) + abs(Jc - Dc)
if B == D:
    print('tie')
elif B < D:
    print('bessie')
else:
    print('daisy')
