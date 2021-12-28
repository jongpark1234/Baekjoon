alist = [0] * 26
word = input().upper()
for i in word:
    alist[ord(i) - 65] += 1
print('?' if alist.count(max(alist)) > 1 else chr(alist.index(max(alist)) + 65))
