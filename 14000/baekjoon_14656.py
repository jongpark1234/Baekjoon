cnt = 0
input()
slist = list(map(int, input().split()))
for i in range(len(slist)):
    if i + 1 != slist[i]:
        cnt += 1
print(cnt)
