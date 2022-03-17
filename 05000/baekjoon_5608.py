from sys import stdin
res = ''
keydict = {}
for _ in range(int(stdin.readline())):
    a, b = stdin.readline().rstrip().split()
    keydict[a] = b
for _ in range(int(stdin.readline())):
    s = stdin.readline().rstrip()
    if s in keydict.keys():
        res += keydict[s]
    else:
        res += s
print(res)
