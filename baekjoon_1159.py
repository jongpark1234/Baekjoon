from sys import stdin
alist = [0] * 26
predaja = True
playerlist = [stdin.readline().rstrip()[0] for i in range(int(stdin.readline()))]
for i in playerlist:
    alist[ord(i) - 97] += 1
for i in range(len(alist)):
    if alist[i] >= 5:
        predaja = False
        print(chr(i + 97), end='')
if predaja:
    print('PREDAJA')
