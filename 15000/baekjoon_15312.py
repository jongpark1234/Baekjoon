from collections import deque
stroke = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]
a = input()
b = input()
slist = deque([])
for i in range(len(a)):
    slist.append(stroke[ord(a[i]) - 65])
    slist.append(stroke[ord(b[i]) - 65])
while len(slist) != 2:
    for i in range(len(slist) - 1):
        slist.append(int(str(slist[0] + slist[1])[-1]))
        slist.popleft()
    slist.popleft()
print(''.join(map(str, slist)))
