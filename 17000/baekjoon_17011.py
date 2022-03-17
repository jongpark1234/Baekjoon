for _ in range(int(input())):
    cnt = 0
    now = ''
    for i in input():
        if i != now:
            if now != '':
                print(cnt, now, end=' ')
            now = i
            cnt = 1
        else:
            cnt += 1
    print(cnt, now)
