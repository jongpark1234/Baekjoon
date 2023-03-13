turn = 0
n, x = map(int, input().split())
t = list(map(int, input().split()))
while True:
    if t[turn] < x:
        print(turn + 1)
        break
    turn = (turn + 1) % n
    x += 1
