ascore = 0
bscore = 0
for i in range(3):
    if i == 0:
        ascore += int(input()) * 3
    elif i == 1:
        ascore += int(input()) * 2
    else:
        ascore += int(input())
for i in range(3):
    if i == 0:
        bscore += int(input()) * 3
    elif i == 1:
        bscore += int(input()) * 2
    else:
        bscore += int(input())
if ascore > bscore:
    print('A')
elif ascore < bscore:
    print('B')
else:
    print('T')
