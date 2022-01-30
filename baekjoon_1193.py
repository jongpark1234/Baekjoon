# pypy3
fra = [1, 1]
turn = 1
Max = 1
idx = 1
x = int(input())
while True:
    if idx == x:
        break
    if fra[turn] == Max:
        Max += 1
        fra[turn] += 1
        turn = not turn
    else:
        fra[turn] += 1
        fra[not turn] -= 1
    idx += 1
print('/'.join(map(str, fra)))
