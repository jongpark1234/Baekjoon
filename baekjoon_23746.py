string = ''
alphadict = {}
for i in range(int(input())):
    a, b = input().split()
    alphadict[b] = a
compressed = input()
s, e = map(int, input().split())
for i in compressed:
    string += alphadict[i]
print(string[s - 1:e])
