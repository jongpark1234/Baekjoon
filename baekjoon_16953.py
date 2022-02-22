a, b = map(int, input().split())
cnt = 1
while True:
    if a == b:
        break
    elif (b % 2 and b % 10 != 1) or (a > b):
        cnt = -1
        break
    else:
        if b % 10 == 1:
            b //= 10
            cnt += 1
        else:
            b //= 2
            cnt += 1
print(cnt)
