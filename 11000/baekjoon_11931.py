from sys import stdin
numlist = []
for _ in range(int(stdin.readline())):
    numlist.append(int(stdin.readline()))
numlist.sort(reverse=True)
print('\n'.join(map(str, numlist)))
