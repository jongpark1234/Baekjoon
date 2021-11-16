n = int(input())
numlist = sorted(list(map(int, input().split())))
x = int(input())
l, r = 0, n - 1
cnt = 0
while l < r:
    temp = numlist[l] + numlist[r]
    if temp == x:
        cnt += 1
    if temp < x:
        l += 1
        continue
    r -= 1
print(cnt)
