while True:
    cnt = 0
    n = input().split()
    if len(n) == 1:
        break
    for i in n[1:]:
        cnt += i.lower().count(n[0])
    print(n[0], cnt)
