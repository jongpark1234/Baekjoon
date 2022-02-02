idx = 1
kayak = []
rank = [0] * 9
r, c = map(int, input().split())
for i in range(r):
    kayak.append(input()[1:-1][::-1])
for i in range(c - 2):
    found = False
    for j in kayak:
        if j[i] != '.':
            if rank[int(j[i]) - 1] == 0:
                rank[int(j[i]) - 1] = idx
                found = True
    if found:
        idx += 1
print('\n'.join(map(str, rank)))
