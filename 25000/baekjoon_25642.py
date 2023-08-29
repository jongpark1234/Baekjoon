turn = 0
a, b = map(int, input().split())
while True:
    if turn:
        a += b
    else:
        b += a
    if max(a, b) > 4:
        print('yj' if turn else 'yt')
        break
    turn ^= 1
