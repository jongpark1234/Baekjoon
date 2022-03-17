numlist = list(map(int, input().split()))
s = list(map(str, input()))
numlist.sort()
for i in range(3):
    print(numlist[ord(s[i]) - 65], end=' ')
