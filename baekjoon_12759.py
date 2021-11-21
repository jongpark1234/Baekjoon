Map = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
player = False if int(input()) == 1 else True
draw = True
for _ in range(9):
    player = not player
    x, y = map(int, input().split())
    Map[x - 1][y - 1] = player
    if Map[0][0] == Map[0][1] == Map[0][2] or Map[1][0] == Map[1][1] == Map[1][2] or Map[2][0] == Map[2][1] == Map[2][2] or Map[0][0] == Map[1][0] == Map[2][0] or Map[0][1] == Map[1][1] == Map[2][1] or Map[0][2] == Map[1][2] == Map[2][2] or Map[0][0] == Map[1][1] == Map[2][2] or Map[0][2] == Map[1][1] == Map[2][0]:
        print(1 if player else 2)
        draw = False
        break
if draw: print(0)
