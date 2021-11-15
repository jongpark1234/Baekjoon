namelist = [list(input().split()) for _ in range(int(input()))]
print(sorted(namelist, key = lambda x : (-int(x[1]), x[0]))[0][0])
