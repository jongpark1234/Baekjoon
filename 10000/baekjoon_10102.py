v = int(input())
sumlist = [0, 0]
a = list(map(str, input()))
for i in range(v):
    sumlist[ord(a[i]) - 65] += 1
if sumlist[0] - sumlist[1] == 0:
    print('Tie')
else:
    print(chr(sumlist.index(max(sumlist)) + 65))
