x, y = map(int, input().split())
cnt = 1
while True:
    if y * cnt - x * cnt >= y:
        print(cnt)
        break
    cnt += 1
