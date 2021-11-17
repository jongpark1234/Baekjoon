for _ in range(int(input())):
    score = [0, 0]
    for i in range(int(input())):
        p1, p2 = input().split()
        if (p1 == 'R' and p2 == 'S') or (p1 == 'P' and p2 == 'R') or (p1 == 'S' and p2 == 'P'):
            score[0] += 1
        elif (p2 == 'R' and p1 == 'S') or (p2 == 'P' and p1 == 'R') or (p2 == 'S' and p1 == 'P'):
            score[1] += 1
    if score[0] > score[1]:
        print('Player 1')
    elif score[0] < score[1]:
        print('Player 2')
    else:
        print('TIE')
