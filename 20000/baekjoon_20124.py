from sys import stdin
namelist = [list(stdin.readline().split()) for _ in range(int(stdin.readline()))]
print(sorted(namelist, key = lambda x : (-int(x[1]), x[0]))[0][0])
