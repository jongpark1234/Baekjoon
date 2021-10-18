k = int(input()) 
s = list(input())
temp = s[::k]
for i in range(len(temp)):
    print(temp[i], end="")