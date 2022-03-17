from sys import stdin
dic = {}
for _ in range(int(stdin.readline())):
    temp = int(stdin.readline())
    if temp in dic:
        dic[temp] += 1
    else:
        dic[temp] = 1
print(sorted(dic.items(), key=lambda x: (-x[1], x[0]))[0][0])
