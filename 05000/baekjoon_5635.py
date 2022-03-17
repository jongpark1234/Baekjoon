infolist = sorted([list(input().split()) for i in range(int(input()))], key = lambda x: (int(x[3]), int(x[2]), int(x[1])))
print(infolist[-1][0], infolist[0][0], sep='\n')
