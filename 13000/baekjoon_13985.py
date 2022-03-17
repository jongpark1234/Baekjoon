s = input()
numlist = []
for i in range(len(s)):
    if s[i].isdecimal():
        numlist.append(int(s[i]))
temp = numlist[-1]
numlist.pop()
add = sum(numlist)
if add - temp: print('NO')
else: print('YES')
