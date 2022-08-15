d = k = s = h = 0
input()
for i in input():
    if i == 'D':
        d += 1
    elif i == 'K':
        k += d
    elif i == 'S':
        s += k
    elif i == 'H':
        h += s
print(h)
