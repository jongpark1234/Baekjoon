from sys import *
s = stdin.readline()
alist = []
for i in range(26):
    alist.append(-1)
for j in range(len(s)):
    print(ord(s[j]) - 97)
    # alist[ord(s[j]) - 97] = j

print(alist)
