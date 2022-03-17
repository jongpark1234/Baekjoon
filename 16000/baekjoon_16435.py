n, l = map(int, input().split())
h = sorted(list(map(int, input().split())))
for i in h:
    if l >= i:
        l += 1
    else:
        break
print(l)
