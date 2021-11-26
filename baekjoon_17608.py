sticks = [int(input()) for i in range(int(input()))]
high = 0
cnt = 0
for i in sticks[::-1]:
    if i > high:
        cnt += 1
        high = i
print(cnt)
