scales = list(map(int, input().split()))
tf = True
if scales[0] == 1:
    for i in range(7):
        if scales[i] + 1 != scales[i + 1]:
            tf = False
            break
    if tf: print('ascending')
    else: print('mixed')
elif scales[0] == 8:
    for i in range(7):
        if scales[i] - 1 != scales[i + 1]:
            tf = False
            break
    if tf: print('descending')
    else: print('mixed')
else: print('mixed')
