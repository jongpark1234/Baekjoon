s = input()
save = []
alist = []
for i in range(26):
    alist.append(-1)
for j in range(len(s)):
    temp = ord(s[j]) - 97
    if save.count(s[j]) == 0:
        alist[temp] = j
        save.append(s[j])
for k in range(len(alist)):
    print(alist[k], end=" ")