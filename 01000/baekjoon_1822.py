input().split()
a = {}; b = {}
dset = []
count = 0
for i in map(int, input().split()):
    a[i] = 1
for i in map(int, input().split()):
    b[i] = 1
for i in a:
    if i not in b:
        count += 1
        dset.append(i)
print(count)
if count:
    print(' '.join(map(str, sorted(dset))))
