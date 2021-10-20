import sys
alist = []
n = int(input())
for _ in range(n):
    word = sys.stdin.readline().rstrip()
    if word in alist:
        pass
    else:
        alist.append(word)
alist.sort(key=lambda x : (len(x), x))
for i in range(len(alist)):
    print(alist[i])
