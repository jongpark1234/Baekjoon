for i in range(int(input())):
    g = s = 0
    Input = list(map(int, input().split()))
    for j in range(6):
        g += [1, 2, 3, 3, 4, 10][j] * Input[j]
    Input = list(map(int, input().split()))
    for j in range(7):
        s += [1, 2, 2, 2, 3, 5, 10][j] * Input[j]
    print(f'Battle {i + 1}:',  'Good triumphs over Evil' if g > s else 'Evil eradicates all trace of Good' if g < s else 'No victor on this battle field')
