n, k = map(int, input().split())
bottle = 0
if n <= k:
    print(0)
else:
    while True:
        cnt = 0
        temp = n
        while temp:
            if temp % 2:
                cnt += 1
            temp //= 2
        if cnt <= k:
            break 
        n += 1
        bottle += 1
    print(bottle)
