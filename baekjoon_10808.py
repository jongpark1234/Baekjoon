alist = [0 for i in range(26)]
s = input()
for i in range(len(s)):
    alist[ord(s[i]) - 97] += 1
for i in range(26):
    print(alist[i], end=' ')
