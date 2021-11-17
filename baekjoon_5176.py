for _ in range(int(input())):
    seatlist = []
    cnt = 0
    p, m = map(int, input().split())
    for i in range(p):
        seat = int(input())
        if seat in seatlist:
            cnt += 1
        else:
            seatlist.append(seat)
    print(cnt)
