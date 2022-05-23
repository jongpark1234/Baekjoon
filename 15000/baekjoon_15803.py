pos = sorted([list(map(int, input().split())) for _ in range(3)], key=lambda x: (x[0], -x[1]))
if pos[0][0] == pos[1][0] == pos[2][0] or pos[0][1] == pos[1][1] == pos[2][1]:
    print('WHERE IS MY CHICKEN?')
else:
    try:
        print('WHERE IS MY CHICKEN?' if (pos[1][1] - pos[0][1]) / (pos[1][0] - pos[0][0]) == (pos[2][1] - pos[1][1]) / (pos[2][0] - pos[1][0]) else 'WINNER WINNER CHICKEN DINNER!')
    except:
        print('WINNER WINNER CHICKEN DINNER!')
