d = p = 0
for i in [*open(0)][1:]:
    if i == 'D\n':
        d += 1
    else:
        p += 1   
    if abs(d - p) > 1:
        break
print(f'{d}:{p}')
