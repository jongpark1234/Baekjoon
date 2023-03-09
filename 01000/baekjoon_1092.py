result = 0
n = int(input())
cranelist = sorted(map(int, input().split()), reverse=True)
m = int(input())
boxlist = sorted(map(int, input().split()), reverse=True)
if max(boxlist) > max(cranelist):
    print(-1)
    exit()
while boxlist:
    for i in range(len(cranelist)):
        for j in range(len(boxlist)):
            if cranelist[i] >= boxlist[j]:
                del boxlist[j]
                break
    result += 1
print(result)
